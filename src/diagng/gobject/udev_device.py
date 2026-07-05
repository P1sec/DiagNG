#!/usr/bin/env python3
from gi.repository import GObject, GLib, Gio
from typing import Self


class UDevDevice(GObject.Object):
    __gtype_name__ = 'UDevDevice'

    text_summary = GObject.Property(type=str)
    is_empty = GObject.Property(
        type=bool, default=True
    )  # Data binding used in Gtk.BuilderListItemFactory
    children = GObject.Property(type=Gio.ListStore)  # Of UDevDevice items

    def __init__(self):
        super().__init__()
        self.children = Gio.ListStore.new(UDevDevice)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'text_summary', GLib.Variant.new_string(self.text_summary or '')
        )
        variant.insert_value(
            'is_empty', GLib.Variant.new_boolean(self.is_empty)
        )
        variant.insert_value(
            'children',
            GLib.Variant.new_array(
                GLib.VariantType.new('a{sv}'),
                [
                    self.children.get_item(position).to_gvariant()
                    for position in range(self.children.get_n_items())
                ],
            ),
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        self = cls()
        self.text_summary = data.lookup_value('text_summary').get_string()
        self.is_empty = data.lookup_value('is_empty').get_boolean()
        children = data.lookup_value('children')
        self.children.remove_all()
        for pos in range(children.n_children()):
            self.children.append(
                UDevDevice.from_gvariant(
                    children.get_child_value(pos).get_variant()
                )
            )
        return self
