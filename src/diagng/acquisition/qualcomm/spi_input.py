#!/usr/bin/env python3

from diagng.parsing.struct.qualcomm.diag_request import DiagRequest
from diagng.acquisition.qualcomm.base_input import BaseQCDMInput
from diagng.gobject.serial_port import SerialPort

from gi.repository import Gio, GObject
from kaitaistruct import KaitaiStream
from io import BytesIO


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

        self.read_next()

    def read_next(self):
        def read_cb(proxy, result, obj_path):
            print('DEBUG: read_cb received: %r' % result)
            if isinstance(result, Exception):
                raise result
            # TODO propagate READ signal
            self.read_next()

        self.dbus_serial_device.Read('()', result_handler=read_cb)

    def send(self, request: DiagRequest):
        def write_cb(proxy, result, obj_path):
            print('DEBUG: send_cb called: %r / %r', request, buf.getvalue())
            if isinstance(result, Exception):
                raise result
            # TODO propagate WRITE signal

        buf = BytesIO()
        stream = KaitaiStream(buf)
        request._check()
        request._write(stream)

        self.dbus_serial_device.Write(
            '(ay)', buf.getvalue(), result_handler=write_cb
        )

    def close(self):
        def close_cb(proxy, result, obj_path):
            print('DEBUG: close_cb called')
            if isinstance(result, Exception):
                raise result
            # TODO propagate CLOSE signal

        self.dbus_serial_device.Close('()', result_handler=close_cb)
