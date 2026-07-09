#!/usr/bin/env python3
from gi.repository import GObject, Gio

from diagng.gobject.mm_modem import ModemManagerModem


class USBDevice(GObject.Object):
    vid_pid = GObject.Property(type=str)
    device_id = GObject.Property(type=str)  # Unused for the moment?

    vendor_name = GObject.Property(type=str)
    model_name = GObject.Property(type=str)

    alt_vendor_name = GObject.Property(type=str)
    alt_model_name = GObject.Property(type=str)

    mm_obj = GObject.Property(type=ModemManagerModem)

    interfaces = GObject.Property(type=Gio.ListStore)  # Of USBInterface items
