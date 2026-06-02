#!/usr/bin/env python3
from gi.repository import GObject, GLib, Gio

class ModemManagerInstance(GObject.Object):
    initialized = GObject.Property(type=bool, default=False)
    is_running = GObject.Property(type=bool, default=False)
    pid = GObject.Property(type=int)
    version = GObject.Property(type=str)
    modems = GObject.Property(type=Gio.ListStore) # Of ModemManagerModem items

    def to_gvariant(self) -> GLib.Variant:
        pass # WIP XX

    @classmethod
    def from_gvariant(cls) -> GLib.Variant:
        pass # WIP XX


# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
