#!/usr/bin/env python3
from diagng.gobject.mm_device import ModemManagerDevice
from gi.repository import GObject, GLib, Gio
from typing import Self

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerModem(GObject.Object):
    modem_name = GObject.Property(type=str)
    modem_device_id = GObject.Property(type=str)
    inhibited = GObject.Property(type=bool, default=False)
    devices = GObject.Property(type=Gio.ListStore)

    def __init__(self):
        super().__init__()
        self.devices = Gio.ListStore.new(ModemManagerDevice)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'modem_name', GLib.Variant.new_string(self.modem_name)
        )
        variant.insert_value(
            'modem_device_id',
            GLib.Variant.new_string(self.modem_device_id),
        )
        variant.insert_value(
            'inhibited', GLib.Variant.new_boolean(self.inhibited)
        )
        variant.insert_value(
            'devices',
            GLib.Variant.new_array(
                GLib.VariantType.new('a{sv}'),
                [
                    self.devices.get_item(position).to_gvariant()
                    for position in range(self.devices.get_n_items())
                ],
            ),
        )

        return variant.end()

    @classmethod
    def from_gvariant(cls, data: GLib.Variant) -> Self:
        modem = cls()
        modem.update(data)
        return modem

    def update(self, data: GLib.Variant):
        with self.freeze_notify():
            self.modem_name = data.lookup_value('modem_name').get_string()
            self.modem_device_id = data.lookup_value(
                'modem_device_id'
            ).get_string()
            self.inhibited = data.lookup_value('inhibited').get_boolean()
            devices = data.lookup_value('devices')
            self.devices.remove_all()
            for pos in range(devices.n_children()):
                self.devices.append(
                    ModemManagerDevice.from_gvariant(
                        devices.get_child_value(pos).get_variant()
                    )
                )


# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
