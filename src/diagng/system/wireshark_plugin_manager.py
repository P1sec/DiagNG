#!/usr/bin/env python3
from os.path import expanduser, join
from gi.repository import GObject

PLUGIN_DIR = expanduser('~/.local/lib/wireshark/plugins')

PLUGIN_PATH = join(PLUGIN_DIR, 'diagng_ext.lua')

ORIG_PLUGIN_PATH = XX

class WiresharkPluginManager(GObject.Object):
    plugin_installed = GObject.Property(type=bool, default=False)

    def __init_(self):
        XX

    def list_plugins(self):
        XX

    def watch_plugins(self, callback):
        XX

    def install_plugin(self):
        XX

    def remove_plugin(self):
        XX
