#!/usr/bin/env python3
from gi.repository import GObject

# WIP

# Store, for the combinations matched by
# logic from
# "diagng.utils.usb_port_detected":
#
# Device vid:pid
# Raw USB class/subclass/protocol information
# Nusb device_id (⚠️ In order to be able to connect to the USB port through nusb/D-Bus later)
# MATCHED UDev base vendor/product name + alt vendor/product name
# MATCHED UDev tty_device_name, IF ANY
# MATCHED UDev kernel_name, IF ANY


class USBInterface(GObject.Object):
    usb_class = GObject.Property(type=int)
    usb_subclass = GObject.Property(type=int)
    usb_protocol = GObject.Property(type=int)

    num_endpoints = GObject.Property(type=int)

    device_id = GObject.Property(type=str)

    udev_vendor_name = GObject.Property(type=str)
    udev_model_name = GObject.Property(type=str)

    udev_alt_vendor_name = GObject.Property(type=str)
    udev_alt_model_name = GObject.Property(type=str)

    udev_tty_device_name = GObject.Property(type=str)
    udev_kernel_name = GObject.Property(type=str)
    pass  # XX WIP
