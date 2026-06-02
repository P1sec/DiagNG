#!/usr/bin/env python3
from gi.repository import GObject, GLib
from typing import Self

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerPort(GObject.Object):
    device_path = GObject.Property(type=str)
    is_primary = GObject.Property(type=bool, default=False)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'device_path', GLib.Variant.new_string(self.device_path)
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        modem = cls()
        modem.update(data)
        return modem

    def update(self, data: GLib.Variant):
        with self.freeze_notify():
            self.device_path = data.lookup_value('device_path').get_string()
