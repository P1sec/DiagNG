#!/usr/bin/env python3
from gi.repository import GObject, GLib, Gio
from typing import Self


class NusbDevice(GObject.Object):
    __gtype_name__ = 'NusbDevice'

    text_summary = GObject.Property(type=str)
    is_empty = GObject.Property(
        type=bool, default=True
    )  # Data binding used in Gtk.BuilderListItemFactory
    children = GObject.Property(type=Gio.ListStore)  # Of NusbDevice items
