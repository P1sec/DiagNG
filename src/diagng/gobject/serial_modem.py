#!/usr/bin/env python3
from gi.repository import GObject, Gio

from diagng.gobject.mm_modem import ModemManagerModem
from diagng.gobject.serial_port import SerialPort


class SerialModem(GObject.Object):
    usb_vid_pid = GObject.Property(type=str)
    mm_obj = GObject.Property(type=ModemManagerModem)
    first_port = GObject.Property(type=SerialPort)
    ports = GObject.Property(type=Gio.ListStore)  # Of SerialPort items

    def __init__(self):
        super().__init__()
        self.ports = Gio.ListStore.new(SerialPort)
