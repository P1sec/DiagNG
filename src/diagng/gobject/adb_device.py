#!/usr/bin/env python3

from gi.repository import GObject


class ADBDevice(GObject.Object):
    __gtype_name__ = 'ADBDevice'

    serial_str = GObject.Property(type=str)
    transport_id = GObject.Property(type=str)
    text_summary = GObject.Property(type=str)
    # WIP 2026-07-10
