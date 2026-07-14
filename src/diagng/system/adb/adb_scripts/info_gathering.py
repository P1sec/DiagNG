#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript
from diagng.system.adb.adb_client import ADBResponse

from logging import warning, debug

# NEXT WIP : ➡️ ➡️ write a single Info Gathering script


class InformationGathering(BaseScript):
    __gtype_name__ = 'InformationGathering'

    def __init__(self, dev):
        super().__init__(dev)

        warning('⚠️ ⚠️ WIP: Information gathering script')
        pass

    def launch_script_for_device(self):
        warning('TODO: Launch shell commands here')

        def callback(resp: ADBResponse):
            debug('Shell ADB command result: %r', resp)

        self.client.closed.connect(self.on_close)
        self.client.shell_run('which su', callback)

    def on_close(self, *args):
        debug('Shell ADB command result: %r', self.client.content_buffer)

    # WIP
    # Cf.:
    # ====> ; https://cs.android.com/android/platform/superproject/main/+/main:packages/modules/adb/docs/dev/services.md

    # TODO: Gather: getprop sys.usb.config diag,adb => current USB configuration

    # TODO: Gather: id => check root status

    # TODO: Gather: root status

    # TODO: Gather: su availability

    # etc.

    # Check Baseband vendor

    # Check Diag device readable

    # Check Diag device wriable
