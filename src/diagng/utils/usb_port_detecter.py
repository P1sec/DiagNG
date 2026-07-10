#!/usr/bin/env python3
from collections import defaultdict
from gi.repository import Gio

from diagng.gobject.usb_interface import USBInterface
from diagng.gobject.mm_modem import ModemManagerModem
from diagng.gobject.mm_port import ModemManagerPort
from diagng.acquisition.qualcomm import usb_input
from diagng.gobject.usb_device import USBDevice

# WIP 2026-06-25: Import logic here from usb_modem_pyusb_devfinder.py
# @ qcsuper.

"""
Cf. docs in "qcsuper/src/main.py":

input_mode.add_argument(
    '--usb-modem',
    metavar='TTY_DEV',
    help='Use an USB modem exposing a DIAG pseudo-serial port through USB.\n'
    + 'Possible syntaxes:\n'
    + '  - "auto": Use the first device interface in the system found where the\n'
    + '    following criteria is matched, by order of preference:\n'
    + '    - bInterfaceClass=255/bInterfaceSubClass=255/bInterfaceProtocol=48/bNumEndpoints=2\n'
    + '    - bInterfaceClass=255/bInterfaceSubClass=255/bInterfaceProtocol=255/bNumEndpoints=2\n'
    + '  - usbserial or hso device name (Linux/macOS): "/dev/tty{USB,HS,other}{0-9}"\n'
    + '  - COM port identifier (Windows): "COM{0-9}"\n'
    + '  - "vid:pid[:cfg:intf]" (vendor ID/product ID/optional bConfigurationValue/optional\n'
    + '    bInterfaceNumber) format in hexa: e.g. "05c6:9091" or "05c6:9091:1:0 (vid and pid\n'
    + '    are four zero-padded hex digits, cfg and intf are canonical values from the USB\n'
    + '    descriptor, or guessed using the criteria specified for "auto" above if not specified)\n'
    + '  - "bus:addr[:cfg:intf]" (USB bus/device address/optional bConfigurationValue/optional\n'
    + '    bInterfaceNumber) format in decimal: e.g "001:003" or "001:003:0:3" (bus and addr are\n'
    + '    three zero-padded digits, cfg and intf are canonical values from the USB descriptor)',
)
"""

# Should be able to provide content to generate Adw.ExpanderRow
# items for raw USB ports, eventually.


def visit_udev_tree(
    usb_dev: USBDevice,
    out_obj: USBInterface,
    node: dict[str, object],
    dev_path_to_mm_obj: dict[str, tuple[ModemManagerModem, ModemManagerPort]],
    target_usb_name: str,
    found_interface=True,
):
    if node.get('name') == target_usb_name:
        found_interface = True

    if found_interface:
        if node.get('vendor_alt') and not usb_dev.alt_vendor_name:
            usb_dev.alt_vendor_name = node.get('vendor_alt')
            usb_dev.alt_model_name = node.get('model_alt')
        if node.get('vendor'):
            usb_dev.vendor_name = node.get('vendor')
            usb_dev.model_name = node.get('model')
        if found_interface and node.get('subsystem') == 'tty':
            out_obj.udev_tty_device_path = node.get('name')
            out_obj.udev_tty_kernel_name = node.get('kernel_name')

            if out_obj.udev_tty_device_path in dev_path_to_mm_obj:
                usb_dev.mm_obj, out_obj.mm_obj = dev_path_to_mm_obj[
                    out_obj.udev_tty_device_path
                ]

    if node.get('children'):
        for child in node['children']:
            visit_udev_tree(
                usb_dev,
                out_obj,
                child,
                dev_path_to_mm_obj,
                target_usb_name,
                found_interface,
            )


def detect_diag_usb_ports(
    udev_device_tree: list[dict],
    nusb_device_tree: list[dict],
    gobjs_out: Gio.ListStore[USBDevice],
    modems: Gio.ListStore[ModemManagerModem],
):
    full_device_id_to_usb_device: dict[str, USBDevice] = defaultdict(USBDevice)

    dev_path_to_mm_obj: dict[
        str, tuple[ModemManagerModem, ModemManagerPort]
    ] = {}

    for pos in range(modems.get_n_items()):
        modem = modems.get_item(pos)

        for pos in range(modem.ports.get_n_items()):
            port = modem.ports.get_item(pos)

            dev_path_to_mm_obj[port.device_path] = (modem, port)

    with gobjs_out.freeze_notify():
        gobjs_out.remove_all()

        if nusb_device_tree and nusb_device_tree.get('device_tree'):
            for bus in nusb_device_tree['device_tree']:
                for device in bus['devices']:
                    vid_pid = device['vendor_id'] + ':' + device['product_id']
                    full_device_id = '%s-%s' % (
                        device['bus_string'].lstrip('0'),
                        '.'.join(
                            str(port_num) for port_num in device['port_chain']
                        ),
                    )

                    usb_dev = full_device_id_to_usb_device[full_device_id]
                    usb_dev.bus_id = device['bus_string']
                    usb_dev.port_chain = device['port_chain']
                    usb_dev.full_device_id = full_device_id
                    usb_dev.vid_pid = vid_pid
                    if not usb_dev.interfaces:
                        usb_dev.interfaces = Gio.ListStore.new(USBInterface)

                    if device.get('vendor_name'):
                        usb_dev.vendor_name = (
                            device['vendor_name'].replace(',', ' ').strip()
                        )
                    if device.get('product_name'):
                        usb_dev.model_name = (
                            device['product_name'].replace(',', ' ').strip()
                        )

                    for configuration in device['configurations']:
                        conf_num = configuration['b_configuration_number']
                        conf_name = configuration['i_configuration']

                        for interface in configuration['interfaces']:
                            intf_num = interface['b_interface_number']
                            intf_name = interface['i_interface']

                            intf_class = interface['class']
                            intf_subclass = interface['subclass']
                            intf_protocol = interface['protocol']

                            text_interface = '%d/%d/%d' % (
                                intf_class,
                                intf_subclass,
                                intf_protocol,
                            )

                            if text_interface not in (
                                '255/255/48',
                                '255/255/255',
                            ):
                                continue

                            for alt_setting in interface['alt_settings']:
                                alt_setting_num = alt_setting['b_alt_setting']
                                num_endpoints = len(alt_setting['endpoints'])

                                if num_endpoints != 2:
                                    continue

                                out_obj = USBInterface()
                                out_obj.has_alt_settings = (
                                    len(interface['alt_settings']) > 1
                                )
                                out_obj.full_intf_id = '%s:%d.%d' % (
                                    usb_dev.full_device_id,
                                    conf_num,
                                    intf_num,
                                )
                                out_obj.connected = (
                                    out_obj.full_intf_id
                                    in usb_input._connected_ports
                                )
                                out_obj.conf_name = conf_name
                                out_obj.intf_name = intf_name
                                out_obj.conf_num = conf_num
                                out_obj.intf_num = intf_num
                                out_obj.alt_setting_num = alt_setting_num
                                out_obj.usb_class = intf_class
                                out_obj.usb_subclass = intf_subclass
                                out_obj.usb_protocol = intf_protocol
                                out_obj.num_endpoints = num_endpoints

                                # Do UDev device matching:
                                if udev_device_tree:
                                    for node in udev_device_tree:
                                        visit_udev_tree(
                                            usb_dev,
                                            out_obj,
                                            node,
                                            dev_path_to_mm_obj,
                                            target_usb_name=out_obj.full_intf_id,
                                            found_interface=False,
                                        )

                                if (
                                    out_obj.mm_obj
                                    and out_obj.mm_obj.port_type == 'AT'
                                ):
                                    continue
                                    # False positive
                                else:
                                    usb_dev.interfaces.append(out_obj)

    for usb_device in full_device_id_to_usb_device.values():
        if usb_device.interfaces.get_n_items():
            gobjs_out.append(usb_device)
