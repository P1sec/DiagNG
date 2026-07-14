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
        self.client.shell_run(
            'echo SU_PATH=$(which su || echo NOTFOUND); '
            + 'echo DIAG_WRITEABLE=$(test -w /dev/diag && echo Y || echo N); '
            + 'echo DIAG_EXISTS=$(test -e /dev/diag && echo Y || echo N); '
            + 'echo DEV_READABLE=$(test -r /dev && echo Y || echo N); '
            + 'echo FFS_DIAG_EXISTS=$(test -e /dev/ffs-diag && echo Y || echo N); '
            + 'echo USB_CONFIG=$(getprop sys.usb.config 2>&1); '
            + 'echo KERNEL=$(uname -a); '
            + 'echo CPU_ABI=$(getprop ro.product.cpu.abi); '
            + 'echo CPU_ABILIST=$(getprop ro.product.cpu.abilist); '
            + 'echo BASEBAND=$(getprop ro.baseband); '
            + 'echo BASEBAND_VERSION=$(getprop gsm.version.baseband); '
            + 'echo BASEBAND_RIL=$(getprop gsm.version.ril-impl); '
            + 'echo BASEBAND_RIL_MODEL=$(getprop ril.model_id); '
            + 'echo BASEBAND_RIL_BOARD=$(getprop ril.modem.board); '
            + 'echo BASEBAND_RIL_PRODUCT=$(getprop ril.product_code); '
            + 'echo RILD=$(getprop rild.libpath); '
            + 'echo SOC=$(getprop ro.board.platform); '
            + 'echo MODEL=$(getprop ro.product.model); '
            + 'echo DEVICE=$(getprop ro.product.device); '
            + 'echo BOARD=$(getprop ro.product.board); '
            + 'echo PRODUCT=$(getprop ro.product.name); '
            + 'echo BRAND=$(getprop ro.product.brand); '
            + 'echo MANUFACTURER=$(getprop ro.product.manufacturer); '
            + 'echo SYSTEM_MODEL=$(getprop ro.product.system.model); '
            + 'echo SYSTEM_DEVICE=$(getprop ro.product.system.device); '
            + 'echo SYSTEM_BOARD=$(getprop ro.product.system.board); '
            + 'echo SYSTEM_PRODUCT=$(getprop ro.product.system.name); '
            + 'echo SYSTEM_BRAND=$(getprop ro.product.system.brand); '
            + 'echo SYSTEM_MANUFACTURER=$(getprop ro.product.system.manufacturer); '
            + 'echo BUILD_ID=$(getprop ro.build.id); '
            + 'echo BUILD_DATE=$(getprop ro.build.date); '
            + 'echo BUILD_INFO=$(getprop ro.build.description); '
            + 'echo ANDROID_VERSION=$(getprop ro.build.version.release); '
            + 'echo ANDROID_SDK=$(getprop ro.build.version.sdk); '
            + 'echo OTA_VERSION=$(getprop ro.build.version.incremental); '
            + 'echo FIRMWARE_STRING=$(getprop ro.build.fingerprint); ',
            callback,
        )

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
