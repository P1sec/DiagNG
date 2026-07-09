#!/usr/bin/env python3
from diagng.gobject.usb_interface import USBInterface
from diagng.gobject.usb_device import USBDevice
from logging import debug

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_usb_interfaces(
    usb_dev: USBDevice, window: 'MainWindow'
) -> Adw.ExpanderRow:

    markup = '<b>%s %s</b> - %s' % (
        GLib.markup_escape_text(usb_dev.vendor_name or '', -1),
        GLib.markup_escape_text(usb_dev.model_name or '', -1),
        GLib.markup_escape_text(usb_dev.vid_pid or '', -1),
    )

    if usb_dev.alt_vendor_name:
        markup = (
            '<b>%s %s</b> - '
            % (
                GLib.markup_escape_text(usb_dev.alt_vendor_name or '', -1),
                GLib.markup_escape_text(usb_dev.alt_model_name or '', -1),
            )
            + markup
        )

    main_row = Adw.ExpanderRow.new()
    main_row.set_expanded(True)
    main_row.set_title_selectable(True)
    main_row.set_title(markup)

    for pos in range(usb_dev.interfaces.get_n_items()):
        item = usb_dev.interfaces.get_item(pos)

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

            if item.mm_obj:
                intf_subtitle += ', type=%s' % item.mm_obj.port_type

        intf_row = Adw.ActionRow.new()
        intf_row.set_title_selectable(True)
        intf_row.set_subtitle_selectable(True)
        intf_row.set_title(GLib.markup_escape_text(intf_title, -1))
        intf_row.set_subtitle(GLib.markup_escape_text(intf_subtitle, -1))

        main_row.add_row(intf_row)

    return main_row
