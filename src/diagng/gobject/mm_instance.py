#!/usr/bin/env python3
from gi.repository import GObject

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerInstance(GObject.Object):
    initialized = GObject.Property(type=bool, default=False)
    is_running = GObject.Property(type=bool, default=False)
    pid = GObject.Property(type=int)
    version = GObject.Property(type=str)


# TODO: Do property bindings in the window implementation source?

# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
