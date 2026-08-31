#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse
from diagng.gobject.adb_device import ADBDevice

from gi.repository import GObject
from logging import debug


class QCDMEnableXiaomi(BaseScript):
    __gtype_name__ = 'QCDMEnableXiaomi'

    text_output = GObject.Property
    apk_bytes: bytes
    first_step_done: bool = False

    def __init__(self, device: ADBDevice, apk_bytes: bytes):
        super().__init__(device)

        self.apk_bytes = apk_bytes

    def launch_script_for_device(self):

        if not self.first_step_done:

            def callback(resp: ADBResponse):
                debug('Install package command result: %r', resp)

            self.client.install_package(self.apk_bytes, callback)

        else:

            def callback_2(resp: ADBResponse):
                debug('Shell ADB command result: %r', resp)

            self.client.shell_run(
                'am start -n com.longcheertel.midtest/com.longcheertel.midtest.Diag',
                callback_2,
            )

    def on_close(self, *args):
        super().on_close(*args)

        if self.state == ScriptState.Processing and not self.first_step_done:
            data = self.client.content_buffer.decode('utf-8')
            debug('Install package command result: %r', data)

            self.text_output = data

            self.first_step_done = True
            self.apk_bytes = None
            self.launch()

        elif self.state == ScriptState.Processing and self.first_step_done:
            data = self.client.content_buffer.decode('utf-8')
            debug('Shell ADB command result: %r', data)

            self.text_output += data

            self.state = ScriptState.Success
            self.finished.emit()

    # ⬆️ Commands to emulate:
    # adb install -r PACKAGE.apk
    # adb shell am start -n com.longcheertel.midtest/com.longcheertel.midtest.Diag

    # => Cf. http://wiki.dmz.intl.p1sec.io/index.php/Qualcomm_device_USB_bus/Xiaomi_Mi_11#Ways_to_switch_the_diag_endpoint
