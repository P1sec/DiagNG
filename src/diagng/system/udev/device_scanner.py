#!/usr/bin/env python3
from typing import List, Optional, Tuple, Dict
from pyudev import Context, Monitor, Device
from pyudev.glib import MonitorObserver
from collections import defaultdict
from logging import info, debug
from threading import Thread
from json import dumps

from diagng.gobject.udev_device import UDevDevice

import gi

gi.require_version('Json', '1.0')
from gi.repository import GLib, Gio, Json


class DeviceScanner:
    state_update_pending: bool = False
    timer_source: int = None

    rpc_wrapper: 'ServiceApplication'
    json_state: Optional[List[dict]] = None

    def __init__(self, rpc_wrapper: 'ServiceApplication'):
        self.rpc_wrapper = rpc_wrapper

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
            self.json_state, usb_gobjs, spi_gobjs = self.get_udev_device_tree()

            if self.rpc_wrapper:
                debug(
                    'DEBUG: Got udev status data: '
                    + dumps(self.json_state, indent=4)
                )
                self.rpc_wrapper.broadcast_message(
                    'sync_usb_devices',
                    GLib.Variant.new_array(
                        GLib.VariantType.new('a{sv}'),
                        [
                            usb_gobjs.get_item(position).to_gvariant()
                            for position in range(usb_gobjs.get_n_items())
                        ],
                    ),
                )
                self.rpc_wrapper.broadcast_message(
                    'sync_spi_devices',
                    GLib.Variant.new_array(
                        GLib.VariantType.new('a{sv}'),
                        [
                            spi_gobjs.get_item(position).to_gvariant()
                            for position in range(spi_gobjs.get_n_items())
                        ],
                    ),
                )
                self.rpc_wrapper.broadcast_message(
                    'sync_udev_debug_info',
                    Json.gvariant_deserialize(
                        Json.from_string(dumps(self.json_state)), None
                    ),
                )

        finally:
            self.state_update_pending = False

    def get_udev_device_tree(
        self,
    ) -> Tuple[List[dict], Gio.ListStore, Gio.ListStore]:
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
                    ...
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
            gobjs_out: Gio.ListStore,
            gobjs_out_spi_only: Optional[Gio.ListStore],
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
                gobj_out = UDevDevice()
                name_parts: list[str] = [
                    item_in.get('subsystem') or '??',
                    item_in.get('name') or '??',
                    item_in.get('vendor') or '??',
                    item_in.get('model') or '??',
                ]
                for key in ('driver', 'path', 'usb_interface', 'usb_product'):
                    value = item_in.get(key)
                    if value:
                        name_parts.append('%s=%s' % (key, value))
                full_name = GLib.markup_escape_text(
                    ' - '.join(filter(None, name_parts))
                )
                gobj_out.text_summary = full_name
                if (
                    gobjs_out_spi_only is not None
                    and item_in['is_spi_related']
                ):
                    gobj_out_spi = UDevDevice()  # Won't have the same children, only the SPI-related ones
                    gobj_out_spi.text_summary = gobj_out.text_summary
                else:
                    gobj_out_spi = None
                if item_in.get('children'):
                    item_in['children'] = visit(
                        item_in['children'],
                        item_in,
                        gobj_out.children,
                        gobj_out_spi.children
                        if gobj_out_spi is not None
                        else None,
                    )
                if gobj_out.children.get_n_items():
                    gobj_out.is_empty = False
                if (
                    gobj_out_spi is not None
                    and gobj_out_spi.children.get_n_items()
                ):
                    gobj_out_spi.is_empty = False
                items_out.append(item_in)
                gobjs_out.append(gobj_out)
                if gobj_out_spi is not None:
                    gobjs_out_spi_only.append(gobj_out_spi)
            return items_out

        usb_gobjs = Gio.ListStore.new(UDevDevice)
        spi_gobjs = Gio.ListStore.new(UDevDevice)
        usb_devices = visit(root_devices, None, usb_gobjs, spi_gobjs)

        return (usb_devices, usb_gobjs, spi_gobjs)

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
