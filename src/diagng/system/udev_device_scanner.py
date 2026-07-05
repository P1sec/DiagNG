#!/usr/bin/env python3
from typing import List, Optional, Tuple, Dict
from pyudev import Context, Monitor, Device
from pyudev.glib import MonitorObserver
from collections import defaultdict
from logging import info, debug
from threading import Thread
from json import dumps

from diagng.gobject.udev_device import UDevDevice
from diagng.gobject.serial_port import SerialPort

from gi.repository import GLib, Gio, GObject


class DeviceScanner(GObject.Object):
    state_update_pending: bool = False
    timer_source: int = None

    usb_tree_gobjs: GLib.Variant
    spi_tree_gobjs: GLib.Variant
    spi_gobjs: GLib.Variant

    usb_device_tree = GObject.Property(type=Gio.ListStore)
    spi_device_tree = GObject.Property(type=Gio.ListStore)
    spi_devices = GObject.Property(type=Gio.ListStore)

    main_app: 'MainApplication'
    json_state: Optional[List[dict]] = None

    def __init__(self, main_app: 'MainApplication'):
        super().__init__()

        self.main_app = main_app

        self.usb_device_tree = Gio.ListStore.new(UDevDevice)
        self.spi_device_tree = Gio.ListStore.new(UDevDevice)
        self.spi_devices = Gio.ListStore.new(SerialPort)

        self.state_update_pending = False

        context = Context()
        monitor = Monitor.from_netlink(context)
        observer = MonitorObserver(monitor)
        observer.connect('device-event', self.on_device_event)
        monitor.start()

        self.queue_state_update()
        # Cf. https://pyudev.readthedocs.io/en/latest/api/pyudev.glib.html#module-pyudev.glib

    def on_device_event(self, observer, device):
        if device.action != 'change':
            info(
                'Received udev event "%s" on device "%s"'
                % (device.action, device)
            )
        self.queue_state_update()
        self.timer_source = GLib.timeout_add_seconds(
            2, self.queue_state_update, True
        )

    def queue_state_update(self, late_retry: bool = False):
        if late_retry and self.timer_source:
            GLib.source_remove(self.timer_source)
            self.timer_source = None
        if not self.state_update_pending:
            self.state_update_pending = True

            self.thread = Thread(target=self.update_json_state)
            self.thread.daemon = True
            self.thread.start()
        elif not self.timer_source:
            self.timer_source = GLib.timeout_add_seconds(
                2, self.queue_state_update, True
            )
        return GLib.SOURCE_REMOVE

    def update_json_state(self, *args):
        try:
            self.json_state, usb_device_tree, spi_device_tree, spi_devices = (
                self.get_udev_device_tree()
            )

            def run_in_main_thread():

                try:
                    with self.usb_device_tree.freeze_notify():
                        self.usb_device_tree.remove_all()
                        for pos in range(usb_device_tree.get_n_items()):
                            self.usb_device_tree.append(
                                usb_device_tree.get_item(pos)
                            )

                    with self.spi_device_tree.freeze_notify():
                        self.spi_device_tree.remove_all()
                        for pos in range(spi_device_tree.get_n_items()):
                            self.spi_device_tree.append(
                                spi_device_tree.get_item(pos)
                            )

                    with self.spi_devices.freeze_notify():
                        self.spi_devices.remove_all()
                        for pos in range(spi_devices.get_n_items()):
                            self.spi_devices.append(spi_devices.get_item(pos))

                    self.usb_tree_gobjs = GLib.Variant.new_array(
                        GLib.VariantType.new('a{sv}'),
                        [
                            self.usb_device_tree.get_item(
                                position
                            ).to_gvariant()
                            for position in range(
                                self.usb_device_tree.get_n_items()
                            )
                        ],
                    )

                    self.spi_tree_gobjs = GLib.Variant.new_array(
                        GLib.VariantType.new('a{sv}'),
                        [
                            self.spi_device_tree.get_item(
                                position
                            ).to_gvariant()
                            for position in range(
                                self.spi_device_tree.get_n_items()
                            )
                        ],
                    )

                    self.spi_gobjs = GLib.Variant.new_array(
                        GLib.VariantType.new('a{sv}'),
                        [
                            self.spi_devices.get_item(position).to_gvariant()
                            for position in range(
                                self.spi_devices.get_n_items()
                            )
                        ],
                    )

                    debug(
                        'Got udev status data'  # dumps(self.json_state, indent=4)
                    )
                    self.main_app.udev_debug_data = dumps(
                        self.json_state, indent=4
                    )

                    dbus_connection = self.main_app.get_dbus_connection()
                    if dbus_connection:
                        dbus_connection.emit_signal(
                            None,
                            self.main_app.get_dbus_object_path(),
                            'com.p1security.diagmetad',
                            'MMInfoUpdated',
                            GLib.Variant.new_tuple(
                                self.usb_tree_gobjs,
                                self.spi_tree_gobjs,
                                self.spi_gobjs,
                                GLib.Variant.new_string(
                                    dumps(self.json_state, indent=4)
                                ),
                            ),
                        )

                finally:
                    self.state_update_pending = False

            GLib.idle_add(run_in_main_thread)

        except Exception:
            self.state_update_pending = False
            raise

    def get_udev_device_tree(
        self,
    ) -> Tuple[List[dict], Gio.ListStore, Gio.ListStore, Gio.ListStore]:
        """
        Output syntax:
        [ // Root (parentless) devices only at this level <-- This is returned by the function
            {
                "subsystem": "{{ device.subsystem }}" e.g "usb",
                "name": "{{ device.sys_name }}",
                "path": "{{ device.sys_path }}",
                "vendor": "{{ ID_VENDOR_FROM_DATABASE }}" or null,
                "model": "{{ ID_MODEL_FROM_DATABASE }}" or null,
                "usb_interface": "{{ INTERFACE }}" or null,
                "usb_vid_pid": "{{ ID_USB_VENDOR_ID }}:{{ ID_USB_MODEL_ID }}" or null,
                "usb_vid": "{{ ID_USB_VENDOR_ID }}" or null,
                "usb_pid": "{{ ID_USB_MODEL_ID }}" or null,
                "usb_revision": "{{ ID_USB_REVISION }}" or null,
                "driver": "{{ DRIVER }}" or null,
                "is_usb_related": true or false, // SUBSYSTEM=usb* anywhere in ancestors or descents
                "is_spi_related": true or false, // name=/dev/tty{USB,HS}* anywhere in ancestors or descents
                "mac": "{{ ':'.join(ID_NET_NAME_MAC[-12 + i * 2:-12 + (i+1) * 2] for i in range(6)).lower() }}"
                    or null,
                "raw_props": {
                    "X": "Y",
                }
                children: [
                    ..<.
                ]
            }
        ]
        """

        # Sample commands:
        # udevadm info -e (all devices)
        # udevadm info /sys/devices/pci0000:00/0000:00:1c.2/0000:04:00.0/net/wlp4s0 <-- udev properties
        # udevadm info -a /sys/devices/pci0000:00/0000:00:1c.2/0000:04:00.0/net/wlp4s0 <-- sysfs attributes

        # See https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device
        # See https://pyudev.readthedocs.io/en/latest/guide.html#enumerating-devices
        # See http://wiki.dmz.intl.p1sec.io/index.php/Udev_filters
        # See http://wiki.dmz.intl.p1sec.io/index.php/Python_snippets/pyudev.glib

        root_devices: List[dict] = []
        path_to_device: Dict[str, dict] = defaultdict(dict)

        for device in Context().list_devices():
            possible_mac_addr = device.properties.get('ID_NET_NAME_MAC')
            if possible_mac_addr:
                possible_mac_addr = ':'.join(
                    possible_mac_addr[
                        -12 + i * 2 : (-12 + (i + 1) * 2) or None
                    ]
                    for i in range(6)
                ).lower()

            model = device.properties.get(
                'ID_MODEL_FROM_DATABASE'
            ) or device.properties.get('ID_MODEL')
            if (
                model
                and 'xHCI' in model
                and device.properties.get('ID_MODEL')
                and 'xHCI' not in device.properties.get('ID_MODEL')
            ):
                model = device.properties.get('ID_MODEL')

            device_name = device.properties.get('DEVNAME')
            if not device_name or (
                device_name and device.sys_name not in device_name
            ):
                device_name = device.sys_name

            path_to_device[device.sys_path].update(
                {
                    'subsystem': device.subsystem,
                    'name': device_name,
                    'kernel_name': device.sys_name,
                    'path': device.sys_path,
                    'vendor': device.properties.get('ID_VENDOR_FROM_DATABASE')
                    or device.properties.get('ID_VENDOR'),
                    'model': model,
                    'usb_interface': device.properties.get('INTERFACE'),
                    'usb_vid_pid': f'{device.properties["ID_USB_VENDOR_ID"]}:{device.properties["ID_USB_MODEL_ID"]}'
                    if (
                        device.properties.get('ID_USB_VENDOR_ID')
                        and device.properties.get('ID_USB_MODEL_ID')
                    )
                    else None,
                    'usb_vid': device.properties.get('ID_USB_VENDOR_ID'),
                    'usb_pid': device.properties.get('ID_USB_MODEL_ID'),
                    'usb_revision': device.properties.get('ID_USB_REVISION'),
                    'driver': device.properties.get('DRIVER'),
                    'mac': possible_mac_addr,
                    'raw_props': dict(device.properties),
                    'children': [
                        path_to_device[child.sys_path]
                        for child in device.children
                        if child.parent == device
                    ]
                    or None,
                }
            )

            if device_name and (
                device_name.startswith('/dev/ttyHS')
                or device_name.startswith('/dev/ttyUSB')
            ):
                self.set_contaminating_flag(
                    'is_spi_related', path_to_device, device
                )

            else:
                path_to_device[device.sys_path].setdefault(
                    'is_spi_related', False
                )

            if device.subsystem.startswith('usb'):
                self.set_contaminating_flag(
                    'is_usb_related', path_to_device, device
                )

            else:
                path_to_device[device.sys_path].setdefault(
                    'is_usb_related', False
                )

            if not device.parent:
                root_devices.append(path_to_device[device.sys_path])

        # Ditch the non USB-related part of the device
        # tree, we don't need it as of today

        # Ouput two distinct GObject trees: SPI-over-USB
        # devices and all USB-related devices

        def visit(
            items_in: List[dict],
            parent_item_in: Optional[dict],
            udev_gobjs_out: Gio.ListStore,
            udev_gobjs_out_spi_only: Optional[Gio.ListStore],
            spi_gobjs_out: Gio.ListStore,
        ):
            items_out = []
            for item_in in items_in:
                if not item_in['is_usb_related']:
                    continue
                if parent_item_in:
                    for key_to_copy in [
                        'usb_interface',
                        'usb_vid_pid',
                        'usb_vid',
                        'usb_pid',
                        'usb_revision',
                    ]:
                        if parent_item_in.get(key_to_copy) and not item_in.get(
                            key_to_copy
                        ):
                            item_in[key_to_copy] = parent_item_in[key_to_copy]
                udev_gobj_out = UDevDevice()
                name_parts: list[str] = [
                    item_in.get('subsystem') or '??',
                    item_in.get('name') or '??',
                    item_in.get('vendor') or '??',
                    item_in.get('model') or '??',
                ]
                for key in ('driver', 'path', 'usb_interface', 'usb_vid_pid'):
                    value = item_in.get(key)
                    if value:
                        name_parts.append('%s=%s' % (key, value))
                full_name = GLib.markup_escape_text(
                    ' - '.join(filter(None, name_parts))
                )
                udev_gobj_out.text_summary = full_name
                if udev_gobjs_out_spi_only is not None and item_in.get(
                    'is_spi_related'
                ):
                    udev_gobj_out_spi = UDevDevice()  # Won't have the same children, only the SPI-related ones
                    udev_gobj_out_spi.text_summary = udev_gobj_out.text_summary

                    if item_in.get('subsystem') == 'tty':
                        spi_gobj_out = SerialPort()
                        spi_gobj_out.tty_device_path = item_in.get('name')
                        spi_gobj_out.kernel_name = item_in.get('kernel_name')
                        spi_gobj_out.sysfs_device_path = item_in.get('path')
                        spi_gobj_out.usb_interface = item_in.get(
                            'usb_interface'
                        )
                        spi_gobj_out.usb_vid_pid = item_in.get('usb_vid_pid')
                        spi_gobj_out.usb_vendor = item_in.get('vendor')
                        spi_gobj_out.usb_product = item_in.get('model')
                        spi_gobjs_out.append(spi_gobj_out)
                else:
                    udev_gobj_out_spi = None
                if item_in.get('children'):
                    item_in['children'] = visit(
                        item_in['children'],
                        item_in,
                        udev_gobj_out.children,
                        (
                            udev_gobj_out_spi.children
                            if udev_gobj_out_spi is not None
                            else None
                        ),
                        spi_gobjs_out,
                    )
                if udev_gobj_out.children.get_n_items():
                    udev_gobj_out.is_empty = False
                if (
                    udev_gobj_out_spi is not None
                    and udev_gobj_out_spi.children.get_n_items()
                ):
                    udev_gobj_out_spi.is_empty = False
                items_out.append(item_in)
                udev_gobjs_out.append(udev_gobj_out)
                if udev_gobj_out_spi is not None:
                    udev_gobjs_out_spi_only.append(udev_gobj_out_spi)
            return items_out

        udev_usb_gobjs = Gio.ListStore.new(UDevDevice)
        udev_spi_gobjs = Gio.ListStore.new(UDevDevice)
        spi_gobjs = Gio.ListStore.new(SerialPort)
        usb_devices = visit(
            root_devices, None, udev_usb_gobjs, udev_spi_gobjs, spi_gobjs
        )

        return (usb_devices, udev_usb_gobjs, udev_spi_gobjs, spi_gobjs)

    def set_contaminating_flag(
        self, flag_name: str, path_to_device: Dict[str, dict], device: Device
    ):
        path_to_device[device.sys_path][flag_name] = True

        # All parents are also ModemManager related if this child is
        parent_obj = device.parent
        while parent_obj:
            parent = path_to_device[parent_obj.sys_path]
            if parent.get(flag_name):
                break  # Avoid circular graph traversing
            parent[flag_name] = True
            parent_obj = parent_obj.parent

        # As well as its children
        def visit_child(child_obj):
            child = path_to_device[child_obj.sys_path]
            if child.get(flag_name):
                return  # Avoid circular graph traversing
            child[flag_name] = True
            for next_child in child_obj.children:
                visit_child(next_child)

        for child in device.children:
            visit_child(child)
