#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse

from gi.repository import GObject
from logging import debug


class EnableDiagUsb(BaseScript):
    __gtype_name__ = 'EnableDiagUsb'

    text_output = GObject.Property(type=str)

    def launch_script_for_device(self):

        def callback(resp: ADBResponse):
            debug('Shell ADB command result: %r', resp)

        self.client.shell_run(
            "su -c 'setprop sys.usb.config diag,adb' || "
            + "su 0,0 sh -c 'setprop sys.usb.config diag,adb'",
            callback,
        )

    def on_close(self, *args):
        super().on_close(*args)

        if self.state == ScriptState.Processing:
            data = self.client.content_buffer.decode('utf-8')
            debug('Shell ADB command result: %r', data)

            self.text_output = data

            self.state = ScriptState.Success
            self.finished.emit()
