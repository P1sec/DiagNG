#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse

from gi.repository import GObject
from logging import debug


class QCDMEnableXiaomi(BaseScript):
    __gtype_name__ = 'QCDMEnableXiaomi'

    text_output = GObject.Property(type=str)

    # WIP

    # TODO: Commands to emulate:
    # adb install -r PACKAGE.apk
    # adb shell am start -n com.longcheertel.midtest/com.longcheertel.midtest.Diag

    # => Cf. http://wiki.dmz.intl.p1sec.io/index.php/Qualcomm_device_USB_bus/Xiaomi_Mi_11#Ways_to_switch_the_diag_endpoint
