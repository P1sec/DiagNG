#!/usr/bin/env python3
from os.path import expanduser, join
from gi.repository import GObject
from os import makedirs, scandir

PLUGIN_DIR = expanduser('~/.local/lib/wireshark/plugins')

PLUGIN_PATH = join(PLUGIN_DIR, 'diagng_ext.lua')

ORIG_PLUGIN_PATH = XX

class WiresharkPluginManager(GObject.Object):
    plugin_installed = GObject.Property(type=bool, default=False)

    def __init_(self):
        super().__init__()

        makedirs(PLUGIN_DIR, exist_ok = True)

        XX

    def list_plugins(self):
        for plugin in scandir(PLUGIN_DIR):
            XX

    def watch_plugins(self, callback):
        XX

    def install_plugin(self):
        XX

    def remove_plugin(self):
        XX
