#!/usr/bin/env python3
from diagng.gobject.mm_port import ModemManagerPort
from gi.repository import GObject, GLib, Gio
from typing import Self


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
            'modem_name', GLib.Variant.new_string(self.modem_name or '')
        )
        variant.insert_value(
            'modem_imei',
            GLib.Variant.new_string(self.modem_imei or ''),
        )
        variant.insert_value(
            'modem_firmware',
            GLib.Variant.new_string(self.modem_firmware or ''),
        )
        variant.insert_value(
            'modem_device_id',
            GLib.Variant.new_string(self.modem_device_id or ''),
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
        modem.modem_name = data.lookup_value('modem_name').get_string()
        modem.modem_imei = data.lookup_value('modem_imei').get_string()
        modem.modem_firmware = data.lookup_value('modem_firmware').get_string()
        modem.modem_device_id = data.lookup_value(
            'modem_device_id'
        ).get_string()
        modem.inhibited = data.lookup_value('inhibited').get_boolean()
        ports = data.lookup_value('ports')
        modem.ports.remove_all()
        for pos in range(ports.n_children()):
            modem.ports.append(
                ModemManagerPort.from_gvariant(
                    ports.get_child_value(pos).get_variant()
                )
            )
        return modem
