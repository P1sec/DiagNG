#!/usr/bin/env python3
from diagng.gobject.serial_modem import SerialModem

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


class SPIModemRow(Adw.ExpanderRow):
    def __init__(self, item: SerialModem, window: 'MainWindow'):
        super().__init__()

        first_port = item.first_port

        markup = '<b>%s %s</b> - %s' % (
            GLib.markup_escape_text(first_port.usb_vendor or ''),
            GLib.markup_escape_text(first_port.usb_product or ''),
            GLib.markup_escape_text(first_port.usb_vid_pid or ''),
        )

        if first_port.usb_vendor_alt:
            markup = (
                '<b>%s %s</b> - '
                % (
                    GLib.markup_escape_text(first_port.usb_vendor_alt or ''),
                    GLib.markup_escape_text(first_port.usb_product_alt or ''),
                )
                + markup
            )

        self.set_expanded(True)
        self.set_title_selectable(True)
        self.set_title(markup)

        if item.mm_obj:
            mm_modem = item.mm_obj

            self.set_subtitle(
                'IMEI: %s | Firmware: %s'
                % (
                    GLib.markup_escape_text(mm_modem.modem_imei or '??'),
                    GLib.markup_escape_text(mm_modem.modem_firmware or '??'),
                )
            )

        for position in range(item.ports.get_n_items()):
            port = item.ports.get_item(position)

            port_row = Adw.ActionRow.new()
            port_row.set_title_selectable(True)
            port_row.set_subtitle_selectable(True)
            port_row.set_title(
                '<b>%s</b>'
                % (GLib.markup_escape_text(port.tty_device_path or ''))
            )
            port_row.set_tooltip_text(port.sysfs_device_path)

            connect_btn = Gtk.Button()
            connect_btn.set_label(
                'Disconnect' if port.connected else 'Connect'
            )
            connect_btn.add_css_class('pill')
            connect_btn.add_css_class('suggested-action')

            if port.connected:
                connect_btn.connect(
                    'clicked',
                    window.disconnect_spi_port,
                    port,
                )
            else:
                connect_btn.connect(
                    'clicked',
                    window.connect_spi_port,
                    port,
                )

            port_row.add_suffix(connect_btn)

            # Annotate devices with USB interface

            subtitle = 'Interface: %s' % port.usb_interface

            # Annotate devices with ModemManager function

            if port.mm_obj:
                subtitle += ' | Type: %s' % port.mm_obj.port_type

            port_row.set_subtitle(GLib.markup_escape_text(subtitle))

            self.add_row(port_row)
