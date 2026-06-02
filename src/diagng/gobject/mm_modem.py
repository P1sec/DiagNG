#!/usr/bin/env python3
from gi.repository import GObject, GLib, Gio

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerModem(GObject.Object):
    modem_name = GObject.Property(type=str)
    modem_device_id = GObject.Property(type=str)
    inhibited = GObject.Property(type=bool, default=False)
    devices = GObject.Property(type=Gio.ListStore) # Of ModemManagerDevice items

    def to_gvariant(self) -> GLib.Variant:
        pass # WIP XX

    @classmethod
    def from_gvariant(cls) -> GLib.Variant:
        pass # WIP XX



# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
