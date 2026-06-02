#!/usr/bin/env python3
from diagng.gobject.mm_modem import ModemManagerModem
from gi.repository import GObject, GLib, Gio
from typing import Self

# TODO use a metaclass here?


class ModemManagerInstance(GObject.Object):
    initialized = GObject.Property(type=bool, default=False)
    is_running = GObject.Property(type=bool, default=False)
    pid = GObject.Property(type=int)
    version = GObject.Property(type=str)
    modems = GObject.Property(type=Gio.ListStore)  # Of ModemManagerModem items

    def __init__(self):
        super().__init__()
        self.modems = Gio.ListStore.new(ModemManagerModem)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'initialized', GLib.Variant.new_boolean(self.initialized)
        )
        variant.insert_value(
            'is_running', GLib.Variant.new_boolean(self.is_running)
        )
        variant.insert_value('pid', GLib.Variant.new_int64(self.pid))
        variant.insert_value('version', GLib.Variant.new_string(self.version))
        variant.insert_value(
            'modems',
            GLib.Variant.new_array(
                GLib.VariantType.new('a{sv}'),
                [
                    self.modems.get_item(position).to_gvariant()
                    for position in range(self.modems.get_n_items())
                ],
            ),
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        self = cls()
        self.update(data)
        return self

    def update(self, data: GLib.Variant):
        with self.freeze_notify():
            self.initialized = data.lookup_value('initialized').get_boolean()
            self.is_running = data.lookup_value('is_running').get_boolean()
            self.pid = data.lookup_value('pid').get_int64()
            self.version = data.lookup_value('version').get_string()
            modems = data.lookup_value('modems')
            self.modems.remove_all()
            for pos in range(modems.n_children()):
                self.modems.append(
                    ModemManagerModem.from_gvariant(
                        modems.get_child_value(pos).get_variant()
                    )
                )


# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
