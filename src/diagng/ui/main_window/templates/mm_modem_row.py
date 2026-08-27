#!/usr/bin/env python3
from diagng.gobject.mm_modem import ModemManagerModem

import gi

gi.require_version('Adw', '1')

from gi.repository import Adw, GLib


class MMModemRow(Adw.ExpanderRow):
    def __init__(self, item: ModemManagerModem):
        super().__init__()

        self.set_expanded(True)
        self.set_title_selectable(True)
        self.set_title(
            '<b>%s</b>' % GLib.markup_escape_text(item.modem_name or '??')
        )
        self.set_subtitle(
            'IMEI: %s | Firmware: %s'
            % (
                GLib.markup_escape_text(item.modem_imei or '??'),
                GLib.markup_escape_text(item.modem_firmware or '??'),
            )
        )
        for pos in range(item.ports.get_n_items()):
            port = item.ports.get_item(pos)

            port_title = port.device_path or ''
            port_title += ' (type: %s)' % port.port_type
            if port.is_primary:
                port_title += ' - Primary'

            port_row = Adw.ActionRow.new()
            port_row.set_title_selectable(True)
            port_row.set_title(GLib.markup_escape_text(port_title))

            self.add_row(port_row)
