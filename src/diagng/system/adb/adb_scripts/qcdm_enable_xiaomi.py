#!/usr/bin/env python3
from diagng.system.adb.adb_scripts.base_script import BaseScript, ScriptState
from diagng.system.adb.adb_client import ADBResponse

from gi.repository import GObject
from logging import debug


class QCDMEnableXiaomi(BaseScript):
    __gtype_name__ = 'QCDMEnableXiaomi'

    text_output = GObject.Property(type=str)

    # WIP
