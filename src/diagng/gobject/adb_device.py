#!/usr/bin/env python3

from gi.repository import GObject

from diagng.gobject.usb_device import USBDevice


class ADBDevice(GObject.Object):
    __gtype_name__ = 'ADBDevice'

    serial_str = GObject.Property(type=str)
    state = GObject.Property(type=str)
    tags: dict[str, str]
    transport_id = GObject.Property(type=str)
    model_name = GObject.Property(type=str)
    connected = GObject.Property(type=bool, default=False)
    usb_device = GObject.Property(type=USBDevice)
    checked_exec_out = GObject.Property(type=bool, default=False)
    prefer_exec_out = GObject.Property(type=bool, default=True)
    text_summary = GObject.Property(type=str)

    def __repr__(self):
        return 'ADBDevice(serial_str=%r, state=%r, tags=%r)' % (
            self.serial_str,
            self.state,
            self.tags,
        )
