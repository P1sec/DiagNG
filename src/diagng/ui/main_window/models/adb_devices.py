#!/usr/bin/env python3
from diagng.ui.main_window.templates.adb_device_row import ADBDeviceRow
from diagng.gobject.adb_device import ADBDevice

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_adb_device(dev: ADBDevice, window: 'MainWindow') -> Adw.ActionRow:

    row = ADBDeviceRow()

    def on_row_change(*args):
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

    dev.connect('notify', on_row_change)
    on_row_change()

    # ⚠️  ^ TODO: Use bind_property instead?

    # TODO: Handle unauthorized state

    # TODO: Add TCP connection feature

    # TODO handle Connect button
    # TODO check root state (+ handle escalation, add dedicated ops?)
    # TODO handle transferring ARM bin to Android (incl. 64 variant?)
    # TODO handle dial codes?
    # TODO: Handle magic APK routes (ex. the Xiaomi thing)?
    # Cf. https://web.archive.org/web/20260308201119/https://band.radio/diag
    # ⚠️ http://wiki.dmz.intl.p1sec.io/index.php/Qualcomm_device_USB_bus/Xiaomi_Mi_11#Ways_to_switch_the_diag_endpoint

    return row
