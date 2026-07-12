#!/usr/bin/env python3
from diagng.system.adb_client import ADBClient

from gi.repository import GObject, Gio, GLib

# WIP 2026-07-11


class ADBWatcher(GObject.Object):
    def __init__(self):
        client = ADBClient()
        # client.connect('notify::connected', lamdba: XX) # TODO bind prop?
        # client.connect('notify::failed', lamdba: XX) # TODO bind prop?
        client.connect_from_host('localhost:5037')  # TODO take host from UI
        # client.on_connect(XX)

        # TODO
