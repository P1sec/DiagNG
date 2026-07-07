#!/usr/bin/env python3
from gi.repository import GObject, GLib
from typing import Self


class SerialPort(GObject.Object):
    tty_device_path = GObject.Property(type=str)
    kernel_name = GObject.Property(type=str)
    connected = GObject.Property(type=bool, default=False)
    sysfs_device_path = GObject.Property(type=str)
    usb_interface = GObject.Property(type=str)
    usb_vid_pid = GObject.Property(type=str)
    usb_vendor = GObject.Property(type=str)
    usb_product = GObject.Property(type=str)
    usb_vendor_alt = GObject.Property(type=str)
    usb_product_alt = GObject.Property(type=str)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'tty_device_path',
            GLib.Variant.new_string(self.tty_device_path or ''),
        )
        variant.insert_value(
            'kernel_name', GLib.Variant.new_string(self.kernel_name or '')
        )
        variant.insert_value(
            'connected', GLib.Variant.new_boolean(self.connected)
        )
        variant.insert_value(
            'sysfs_device_path',
            GLib.Variant.new_string(self.sysfs_device_path or ''),
        )
        variant.insert_value(
            'usb_interface', GLib.Variant.new_string(self.usb_interface or '')
        )
        variant.insert_value(
            'usb_vid_pid', GLib.Variant.new_string(self.usb_vid_pid or '')
        )
        variant.insert_value(
            'usb_vendor', GLib.Variant.new_string(self.usb_vendor or '')
        )
        variant.insert_value(
            'usb_product', GLib.Variant.new_string(self.usb_product or '')
        )
        variant.insert_value(
            'usb_vendor_alt',
            GLib.Variant.new_string(self.usb_vendor_alt or ''),
        )
        variant.insert_value(
            'usb_product_alt',
            GLib.Variant.new_string(self.usb_product_alt or ''),
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        self = cls()
        self.tty_device_path = data.lookup_value(
            'tty_device_path'
        ).get_string()
        self.kernel_name = data.lookup_value('kernel_name').get_string()
        self.connected = data.lookup_value('connected').get_boolean()
        self.sysfs_device_path = data.lookup_value(
            'sysfs_device_path'
        ).get_string()
        self.usb_interface = data.lookup_value('usb_interface').get_string()
        self.usb_vid_pid = data.lookup_value('usb_vid_pid').get_string()
        self.usb_vendor = data.lookup_value('usb_vendor').get_string()
        self.usb_product = data.lookup_value('usb_product').get_string()
        self.usb_vendor_alt = data.lookup_value('usb_vendor_alt').get_string()
        self.usb_product_alt = data.lookup_value(
            'usb_product_alt'
        ).get_string()
        return self
