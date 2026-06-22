#!/usr/bin/env python3
from gi.repository import GObject, GLib
from typing import Self


class SerialPort(GObject.Object):
    tty_device_path = GObject.Property(type=str)
    sysfs_device_path = GObject.Property(type=str)
    usb_interface = GObject.Property(type=str)
    usb_vid_pid = GObject.Property(type=str)
    usb_vendor = GObject.Property(type=str)
    usb_product = GObject.Property(type=str)
    is_mm_detected = GObject.Property(type=bool, default=False)
    is_mm_inhibited = GObject.Property(type=bool, default=False)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'tty_device_path', GLib.Variant.new_string(self.tty_device_path)
        )
        variant.insert_value(
            'sysfs_device_path',
            GLib.Variant.new_string(self.sysfs_device_path),
        )
        variant.insert_value(
            'usb_interface', GLib.Variant.new_string(self.usb_interface)
        )
        variant.insert_value(
            'usb_vid_pid', GLib.Variant.new_string(self.usb_vid_pid)
        )
        variant.insert_value(
            'usb_vendor', GLib.Variant.new_string(self.usb_vendor)
        )
        variant.insert_value(
            'usb_product', GLib.Variant.new_string(self.usb_product)
        )
        variant.insert_value(
            'is_mm_detected', GLib.Variant.new_boolean(self.is_mm_detected)
        )
        variant.insert_value(
            'is_mm_inhibited', GLib.Variant.new_boolean(self.is_mm_inhibited)
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        self = cls()
        self.tty_device_path = data.lookup_value(
            'tty_device_path'
        ).get_string()
        self.sysfs_device_path = data.lookup_value(
            'sysfs_device_path'
        ).get_string()
        self.usb_interface = data.lookup_value('usb_interface').get_string()
        self.usb_vid_pid = data.lookup_value('usb_vid_pid').get_string()
        self.usb_vendor = data.lookup_value('usb_vendor').get_string()
        self.usb_product = data.lookup_value('usb_product').get_string()
        self.is_mm_detected = data.lookup_value('is_mm_detected').get_boolean()
        self.is_mm_inhibited = data.lookup_value(
            'is_mm_inhibited'
        ).get_boolean()
        return self
