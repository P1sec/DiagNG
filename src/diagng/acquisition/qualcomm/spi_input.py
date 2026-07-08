#!/usr/bin/env python3

from diagng.acquisition.qualcomm.base_input import BaseQCDMInput
from diagng.gobject.serial_port import SerialPort

from logging import error, warning, debug

import gi

gi.require_version('Adw', '1')

from gi.repository import Gio, GLib, Adw

_connected_ports: dict[str, 'SerialQCDMInput'] = {}


class SerialQCDMInput(BaseQCDMInput):
    dbus_serial_device: Gio.DBusProxy
    serial_port: SerialPort
    main_window: Adw.ApplicationWindow

    def __init__(
        self,
        dbus_serial_device: Gio.DBusProxy,
        serial_port: SerialPort,
        main_window: Adw.ApplicationWindow,
    ):
        super().__init__()

        self.dbus_serial_device = dbus_serial_device
        self.serial_port = serial_port
        self.main_window = main_window

        self.serial_port.connected = True
        self.main_window.update_serial_modems()
        _connected_ports[serial_port.tty_device_path] = self

        self.short_name = serial_port.tty_device_path

        self._update_conn_state()

        self.serial_port.connect('notify::connected', self._update_conn_state)
        self.dbus_serial_device.connect('g-signal::Read', self._on_read)
        self.dbus_serial_device.connect('g-signal::Closed', self._on_closed)

    def _update_conn_state(self, *args):
        full_name = ''

        if not self.serial_port.connected:
            full_name += '(DISCONNECTED) - '

        full_name += '%s - ' % self.serial_port.tty_device_path

        if self.serial_port.usb_vendor_alt:
            full_name += '%s %s -' % (
                self.serial_port.usb_vendor_alt or '',
                self.serial_port.usb_product_alt or '',
            )

        full_name += '%s %s (%s)' % (
            self.serial_port.usb_vendor or '',
            self.serial_port.usb_product or '',
            self.serial_port.usb_vid_pid or '',
        )

        self.full_name = full_name

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
        self.closed.emit()
        if self.serial_port.tty_device_path in _connected_ports:
            del _connected_ports[self.serial_port.tty_device_path]
        self.serial_port.connected = False
        self.main_window.update_serial_modems()

        reason = str(parameters[0])
        warning('Serial port closed, reason: ' + reason)

    def send_raw(self, data: bytes):
        def write_cb(proxy, result, obj_path):
            if isinstance(result, Exception):
                error('Failed to write serial port: %r' % result)

        self.dbus_serial_device.Write('(ay)', data, result_handler=write_cb)

    def close(self):
        def close_cb(proxy, result, obj_path):
            self.closed.emit()
            if self.serial_port.tty_device_path in _connected_ports:
                del _connected_ports[self.serial_port.tty_device_path]
            self.serial_port.connected = False
            self.main_window.update_serial_modems()

            if isinstance(result, Exception):
                error('Failed to close serial port: %r' % result)

        self.dbus_serial_device.Close('()', result_handler=close_cb)
