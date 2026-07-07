#!/usr/bin/env python3

from diagng.acquisition.qualcomm.base_input import BaseQCDMInput
from diagng.gobject.serial_port import SerialPort

from logging import error, warning, debug
from gi.repository import Gio, GLib


class SerialQCDMInput(BaseQCDMInput):
    dbus_serial_device: Gio.DBusProxy
    serial_port: SerialPort

    def __init__(
        self,
        dbus_serial_device: Gio.DBusProxy,
        serial_port: SerialPort,
    ):
        super().__init__()

        self.dbus_serial_device = dbus_serial_device
        self.serial_port = serial_port

        self.short_name = serial_port.tty_device_path
        self.full_name = '%s - ' + serial_port.tty_device_path

        if serial_port.usb_vendor_alt:
            self.full_name += '%s %s -' % (
                serial_port.usb_vendor_alt or '',
                serial_port.usb_product_alt or '',
            )

        self.full_name += '%s %s (%s)' % (
            serial_port.usb_vendor or '',
            serial_port.usb_product or '',
            serial_port.usb_vid_pid or '',
        )

        self.dbus_serial_device.connect('g-signal::Read', self._on_read)
        self.dbus_serial_device.connect('g-signal::Closed', self._on_closed)

    def _on_read(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        data = bytes(parameters[0])
        debug('Received data from serial port: %r' % data)
        self.process_input(data)

    def _on_closed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        reason = str(parameters[0])
        warning('Serial port closed, reason: ' + reason)
        # TODO: Process this

    def send_raw(self, data: bytes):
        def write_cb(proxy, result, obj_path):
            if isinstance(result, Exception):
                error('Failed to write serial port: %r' % result)

        self.dbus_serial_device.Write('(ay)', data, result_handler=write_cb)

    def close(self):
        def close_cb(proxy, result, obj_path):
            self.closed.emit()
            if isinstance(result, Exception):
                error('Failed to close serial port: %r' % result)

        self.dbus_serial_device.Close('()', result_handler=close_cb)
