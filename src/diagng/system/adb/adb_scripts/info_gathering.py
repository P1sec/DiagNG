#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse
from re import finditer, MULTILINE

from gi.repository import GLib, GObject
from logging import warning, debug

# NEXT WIP : ➡️ ➡️ write a single Info Gathering script


class IGKeyValue(GObject.Object):
    key = GObject.Property(type=str)
    value = GObject.Property(type=str)


class InformationGathering(BaseScript):
    __gtype_name__ = 'InformationGathering'

    read_keys_dict = GObject.Property(type=object)
    read_keys_text = GObject.Property(type=str)

    def __init__(self, dev):
        super().__init__(dev)

        self.read_keys_dict = {}
        self.read_keys_text = ''

        warning('⚠️ ⚠️ WIP: Information gathering script')
        pass

    def launch_script_for_device(self):
        warning('TODO: Launch shell commands here')

        def callback(resp: ADBResponse):
            debug('Shell ADB command result: %r', resp)

        self.client.shell_run(
            'echo SU_PATH=$(which su || echo NOT_FOUND); '
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
            + 'echo MARKETNAME=$(getprop ro.product.marketname); '
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
        super().on_close(*args)

        if self.state == ScriptState.Processing:
            data = self.client.content_buffer.decode('utf-8')
            debug('Shell ADB command result: %r', data)

            # => ℹ️ Parse command results into a kind of array or object

            out_dict = {}
            out_text = ''

            for match in finditer(r'^([A-Z_]+)=(.*?)$', data, flags=MULTILINE):
                key = match.group(1)
                value = match.group(2)

                if value:
                    out_dict[key] = value
                    out_text += '%s: %s\n' % (
                        key.strip().replace('\n', ''),
                        value.strip().replace('\n', ''),
                    )

            self.read_keys_dict = out_dict
            self.read_keys_text = out_text

            if not out_dict.get('BASEBAND_RIL'):
                # gsm.version.* module not loaded
                # right after device bootup, wait a
                # bit
                GLib.timeout_add_seconds(3, self.launch)

            else:
                self.state = ScriptState.Success
                self.finished.emit()

        # => ℹ️ TODO: (Display in some child of the ADBDeviceRow ExpanderRow)
        # => ℹ️ TODO: Show a popup to ask the permission for using "su" if available (Magisk may need to show an authorization, etc.)
        # => ℹ️ TODO: If the popup is confirmed, run a second script that will try to access the /dev/diag device over root / possibly fetch available USB configurations

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
