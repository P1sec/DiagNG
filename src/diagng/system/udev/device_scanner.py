#!/usr/bin/env python3
from typing import List, Optional, Dict
from collections import defaultdict
from logging import info, debug
from threading import Thread
from json import dumps

from pyudev import Context, Monitor, Device
from pyudev.glib import MonitorObserver

import gi

gi.require_version('Json', '1.0')
from gi.repository import GLib, Json


class DeviceScanner:
    state_update_pending: bool = False

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

    def queue_state_update(self):
        if not self.state_update_pending:
            self.state_update_pending = True

            self.thread = Thread(target=self.update_json_state)
            self.thread.daemon = True
            self.thread.start()

    def update_json_state(self, *args):
        self.json_state = self.get_udev_device_tree()

        if self.rpc_wrapper:
            debug(
                'DEBUG: Got udev status data: '
                + dumps(self.json_state, indent=4)
            )
            self.rpc_wrapper.broadcast_message(
                'sync_udev_info',
                Json.gvariant_deserialize(
                    Json.from_string(dumps(self.json_state)), None
                ),
            )
            """
            self.ws_server.broadcast_message(
                {"type": "SYNC_UDEV_STATUS", "devices": self.json_state}
            )
            """

        self.state_update_pending = False

    def get_udev_device_tree(self) -> List[dict]:
        """
        Output syntax:
        {
            'type': 'SYNC_UDEV_STATUS',
            'devices': [ // Root (parentless) devices only at this level <-- Only this list is returned by the function
                {
                    "subsystem": "{{ device.subsystem }}" e.g "usb",
                    "name": "{{ device.sys_name }}",
                    "path": "{{ device.sys_path }}",
                    "vendor": "{{ ID_VENDOR_FROM_DATABASE }}" or null,
                    "model": "{{ ID_MODEL_FROM_DATABASE }}" or null,
                    "usb_interface": "{{ INTERFACE }}" or null,
                    "usb_product": "{{ PRODUCT }}" or null,
                    "driver": "{{ DRIVER }}" or null,
                    "is_usb_related": true or false, // SUBSYSTEM=usb anywhere in ancestors or descents
                    "is_mm_related": true or false, // ID_MM_CANDIDATE anywhere in ancestors or descents
                    "is_mm_usable": true or false, // ID_MM_CANDIDATE set
                    "is_mm_blacklisted": false or true, // ID_MM_DEVICE_IGNORE or ID_MM_PORT_IGNORE set
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
        }
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
                    'usb_product': device.properties.get('PRODUCT'),
                    'driver': device.properties.get('DRIVER'),
                    'is_mm_blacklisted': bool(
                        int(device.properties.get('ID_MM_PORT_IGNORE') or '0')
                    )
                    or bool(
                        int(
                            device.properties.get('ID_MM_DEVICE_IGNORE') or '0'
                        )
                    ),
                    'is_mm_usable': bool(
                        int(device.properties.get('ID_MM_CANDIDATE') or '0')
                    ),
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

            if device.properties.get('ID_MM_CANDIDATE'):
                self.set_contaminating_flag(
                    'is_mm_related', path_to_device, device
                )

            else:
                path_to_device[device.sys_path].setdefault(
                    'is_mm_related', False
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

        def visit(items: list[dict]) -> list[dict]:
            filtered_items: list[dict] = []
            for item in items:
                if not item['is_usb_related']:
                    continue
                filtered_items.append(item)
                if item['children']:
                    item['children'] = visit(item['children'])
            return filtered_items

        usb_devices = visit(root_devices)

        return usb_devices

    def set_contaminating_flag(
        self, flag_name: str, path_to_device: Dict[str, dict], device: Device
    ):
        path_to_device[device.sys_path][flag_name] = True

        # All parents are also ModemManager related if this child is
        next_parent = device.parent
        while next_parent:
            if path_to_device[next_parent.sys_path].get(flag_name):
                break  # Avoid circular graph traversing
            path_to_device[next_parent.sys_path][flag_name] = True
            next_parent = next_parent.parent

        # As well as its children
        def visit_child(child):
            if path_to_device[child.sys_path].get(flag_name):
                return  # Avoid circular graph traversing
            path_to_device[child.sys_path][flag_name] = True
            for next_child in child.children:
                visit_child(child)

        for child in device.children:
            visit_child(child)
