#!/usr/bin/env python3
from diagng.gobject.nusb_interface import USBInterface
from logging import debug

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, GLib


def create_usb_interface(
    item: USBInterface, window: 'MainWindow'
) -> Adw.ExpanderRow:

    debug('WIP: Rendering %s' % item)
