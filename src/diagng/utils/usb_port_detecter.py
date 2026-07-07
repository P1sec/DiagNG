#!/usr/bin/env python3
from gi.repository import Gio

from diagng.gobject.usb_interface import USBInterface

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


def detect_diag_usb_ports(
    udev_device_tree: list[dict], nusb_device_tree: list[dict]
) -> Gio.ListStore[USBInterface]:
    pass  # WIP
