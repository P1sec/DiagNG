#!/usr/bin/env python3
from diagng.system.adb_client import ADBClient

from gi.repository import GObject, Gio, GLib

# from typing import Union
# from queue import Queue
from enum import Enum

# WIP 2026-07-11


class ADBWatcher(GObject.Object):
    def __init__(self):
        client = ADBClient()
        # client.on_connect(XX)

        # TODO
