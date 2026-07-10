#!/usr/bin/env python3
from diagng.gobject.adb_device import ADBDevice

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_adb_device(dev: ADBDevice, window: 'MainWindow') -> Adw.ActionRow:

    row = Adw.ActionRow.new()
    row.set_title_selectable(True)
    row.set_subtitle_selectable(True)
    row.set_title(
        '<b>%s</b> (transport id #%s, serial ID %s)'
        % (
            GLib.markup_escape_text(dev.model_name or '', -1),
            # ^ TODO gather extra info from UDev?
            GLib.markup_escape_text(dev.transport_id or '', -1),
            GLib.markup_escape_text(dev.serial_str or '', -1),
        )
    )
    row.set_subtitle(GLib.markup_escape_text(dev.text_summary or '', -1))

    connect_btn = Gtk.Button()
    connect_btn.set_label('Disconnect' if dev.connected else 'Connect')
    connect_btn.add_css_class('pill')
    connect_btn.add_css_class('suggested-action')

    # TODO handle connect

    row.add_suffix(connect_btn)

    return row
