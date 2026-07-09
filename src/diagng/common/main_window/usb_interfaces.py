#!/usr/bin/env python3
from diagng.gobject.usb_interface import USBInterface
from logging import debug

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_usb_interface(
    item: USBInterface, window: 'MainWindow'
) -> Adw.ExpanderRow:

    markup = '<b>%s %s</b> - %s' % (
        GLib.markup_escape_text(item.vendor_name or '', -1),
        GLib.markup_escape_text(item.model_name or '', -1),
        GLib.markup_escape_text(item.vid_pid or '', -1),
    )

    if item.alt_vendor_name:
        markup = (
            '<b>%s %s</b> - '
            % (
                GLib.markup_escape_text(item.alt_vendor_name or '', -1),
                GLib.markup_escape_text(item.alt_model_name or '', -1),
            )
            + markup
        )

    main_row = Adw.ExpanderRow.new()
    main_row.set_expanded(True)
    main_row.set_title_selectable(True)
    main_row.set_title(markup)

    intf_title = 'Configuration %d%s, interface %d%s, alt setting %d' % (
        item.conf_num,
        '' if not item.conf_name else ' (%s)' % item.conf_name,
        item.intf_num,
        '' if not item.intf_name else ' (%s)' % item.intf_name,
        item.alt_setting_num,
    )

    intf_subtitle = 'class=%s/subclass=%s/protocol=%s' % (
        item.usb_class,
        item.usb_subclass,
        item.usb_protocol,
    )

    if item.udev_tty_device_path:
        intf_subtitle += ', dev=%s' % item.udev_tty_device_path

    intf_row = Adw.ActionRow.new()
    intf_row.set_title_selectable(True)
    intf_row.set_subtitle_selectable(True)
    intf_row.set_title(GLib.markup_escape_text(intf_title, -1))
    intf_row.set_subtitle(GLib.markup_escape_text(intf_subtitle, -1))

    main_row.add_row(intf_row)

    debug('WIP: Rendering %s' % item)

    return main_row
