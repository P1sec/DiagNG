#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.info_gathering import IGKeyValue

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_adb_device_info(key_value: IGKeyValue) -> Adw.ActionRow:
    row = Adw.ActionRow.new()
    row.set_title_selectable(True)
    row.set_title(
        GLib.markup_escape_text(f'{key_value.key}: {key_value.value}', -1)
    )

    return row
