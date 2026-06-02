#!/usr/bin/env python3
from gi.repository import GObject, GLib, Gio

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerDevice(GObject.Object):
    device_path = GObject.Property(type=str)

    def to_gvariant(self) -> GLib.Variant:
        pass # WIP XX

    @classmethod
    def from_gvariant(cls) -> GLib.Variant:
        pass # WIP XX
