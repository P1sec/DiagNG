#!/usr/bin/env python3

from diagng.parsing.struct.qualcomm.diag_request import DiagRequest
from diagng.acquisition.qualcomm.base_input import BaseQCDMInput
from diagng.gobject.serial_port import SerialPort

from gi.repository import Gio


class SerialQCDMInput(BaseQCDMInput):
    def __init__(
        self,
        dbus_serial_device: Gio.DBusProxy,
        serial_port: SerialPort,
    ):
        pass  # WIP

    def send(self, request: DiagRequest):
        pass  # WIP

    def close(self):
        pass  # WIP
