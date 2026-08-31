#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse

from gi.repository import GObject
from logging import debug


class AdbdRootTrigger(BaseScript):
    __gtype_name__ = 'AdbdRootTrigger'

    text_output = GObject.Property(type=str)

    def launch_script_for_device(self):

        def callback(resp: ADBResponse):
            debug('ADBD root command result: %r', resp)

        self.client.adbd_root(
            callback,
        )

    def on_close(self, *args):
        super().on_close(*args)

        if self.state == ScriptState.Processing:
            data = self.client.content_buffer.decode('utf-8')
            debug('ADBD root command result: %r', data)

            self.text_output = data

            self.state = ScriptState.Success
            self.finished.emit()
