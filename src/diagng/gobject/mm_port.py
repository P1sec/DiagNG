#!/usr/bin/env python3
from gi.repository import GObject, GLib
from typing import Self

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerPort(GObject.Object):
    device_path = GObject.Property(type=str)
    port_type = GObject.Property(type=str)
    is_primary = GObject.Property(type=bool, default=False)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'device_path', GLib.Variant.new_string(self.device_path)
        )
        variant.insert_value(
            'port_type', GLib.Variant.new_string(self.port_type)
        )
        variant.insert_value(
            'is_primary', GLib.Variant.new_boolean(self.is_primary)
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        port = cls()
        port.device_path = data.lookup_value('device_path').get_string()
        port.port_type = data.lookup_value('port_type').get_string()
        port.is_primary = data.lookup_value('is_primary').get_boolean()
        return port
