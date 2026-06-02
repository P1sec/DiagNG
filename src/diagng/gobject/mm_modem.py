#!/usr/bin/env python3
from diagng.gobject.mm_port import ModemManagerPort
from gi.repository import GObject, GLib, Gio
from typing import Self

# XX WIP 2026-06-01 Define a structure and add tests


class ModemManagerModem(GObject.Object):
    modem_name = GObject.Property(
        type=str
    )  # get_manufacturer() + " " + get_model()
    modem_imei = GObject.Property(type=str)  # get_equipment_identifier()
    modem_firmware = GObject.Property(type=str)  # get_revision()
    modem_device_id = GObject.Property(type=str)  # get_device()
    inhibited = GObject.Property(type=bool, default=False)
    ports = GObject.Property(type=Gio.ListStore)

    def __init__(self):
        super().__init__()
        self.ports = Gio.ListStore.new(ModemManagerPort)

    def to_gvariant(self) -> GLib.Variant:
        variant = GLib.VariantDict.new(None)
        variant.insert_value(
            'modem_name', GLib.Variant.new_string(self.modem_name)
        )
        variant.insert_value(
            'modem_imei',
            GLib.Variant.new_string(self.modem_imei),
        )
        variant.insert_value(
            'modem_firmware',
            GLib.Variant.new_string(self.modem_firmware),
        )
        variant.insert_value(
            'modem_device_id',
            GLib.Variant.new_string(self.modem_device_id),
        )
        variant.insert_value(
            'inhibited', GLib.Variant.new_boolean(self.inhibited)
        )
        variant.insert_value(
            'ports',
            GLib.Variant.new_array(
                GLib.VariantType.new('a{sv}'),
                [
                    self.ports.get_item(position).to_gvariant()
                    for position in range(self.ports.get_n_items())
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
            self.modem_imei = data.lookup_value('modem_imei').get_string()
            self.modem_firmware = data.lookup_value(
                'modem_firmware'
            ).get_string()
            self.modem_device_id = data.lookup_value(
                'modem_device_id'
            ).get_string()
            self.inhibited = data.lookup_value('inhibited').get_boolean()
            ports = data.lookup_value('ports')
            self.ports.remove_all()
            for pos in range(ports.n_children()):
                self.ports.append(
                    ModemManagerPort.from_gvariant(
                        ports.get_child_value(pos).get_variant()
                    )
                )


# (Test conversion between GObject <-> GLib-JSON issued GVariant <-> JSON and vice versa)
