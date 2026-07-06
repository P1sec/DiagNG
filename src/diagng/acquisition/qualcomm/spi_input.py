#!/usr/bin/env python3

from diagng.acquisition.qualcomm.base_input import BaseQCDMInput
from diagng.gobject.serial_port import SerialPort

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
        self.full_name = '%s - %s %s (%s)' % (
            serial_port.tty_device_path,
            serial_port.usb_vendor or '',
            serial_port.usb_product or '',
            serial_port.usb_vid_pid or '',
        )

        self.dbus_serial_device.connect('g-signal::Read', self._read_next)

    def _read_next(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        data = bytes(parameters[0])
        print('DEBUG: read_cb received: %r' % data)
        self.process_input(data)

    def send_raw(self, data: bytes):
        def write_cb(proxy, result, obj_path):
            print('DEBUG: send_cb called: %r' % data)
            if isinstance(result, Exception):
                raise result
            # TODO propagate WRITE signal

        self.dbus_serial_device.Write('(ay)', data, result_handler=write_cb)

    def close(self):
        def close_cb(proxy, result, obj_path):
            print('DEBUG: close_cb called')
            if isinstance(result, Exception):
                raise result
            # TODO propagate CLOSE signal

        self.dbus_serial_device.Close('()', result_handler=close_cb)
