#!/usr/bin/env python3
from gi.repository import GObject

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerInstance(GObject.Object):
    is_running = GObject.Property(type=bool)


# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
