#!/usr/bin/env python3

from gi.repository import GObject, GLib
from typing import Self


class UDevRule(GObject.Object):
    __gtype_name__ = 'UDevRule'

    rule_file_name = GObject.Property(type=str)
    rule_text = GObject.Property(type=str)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'rule_file_name', GLib.Variant.new_string(self.rule_file_name)
        )
        variant.insert_value(
            'rule_text', GLib.Variant.new_string(self.rule_text)
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        self = cls()
        self.rule_file_name = data.lookup_value('rule_file_name').get_string()
        self.rule_text = data.lookup_value('rule_text').get_string()
        return self
