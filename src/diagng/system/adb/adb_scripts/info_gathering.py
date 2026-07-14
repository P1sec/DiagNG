#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript

from logging import warning

# NEXT WIP : ➡️ ➡️ write a single Info Gathering script


class InformationGathering(BaseScript):
    __gtype_name__ = 'InformationGathering'

    def __init__(self, dev):
        super().__init__(dev)

        warning('⚠️ ⚠️ WIP: Information gathering script')
        pass

    def launch_script_for_device(self):
        warning('TODO: Launch shell commands here')
        # WIP XX

        # In implem func. : self.client.shell('XX')

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
