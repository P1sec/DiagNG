#!/usr/bin/env python3
from os.path import expanduser, dirname, realpath, join
from gi.repository import GObject, Gio
from os import makedirs, scandir
from datetime import datetime

PLUGIN_DIR = expanduser('~/.local/lib/wireshark/plugins')
PLUGIN_PATH = join(PLUGIN_DIR, 'diagng_ext.lua')

ORIG_PLUGIN_DIR = dirname(realpath(__file__))
ORIG_PLUGIN_PATH = join(ORIG_PLUGIN_DIR, 'diagng_ext.lua')


class ListedPlugin(GObject.Object):
    file_name = GObject.Property(type=str)
    file_path = GObject.Property(type=str)
    last_modified = GObject.Property(type=str)


class WiresharkPluginManager(GObject.Object):
    plugin_installed = GObject.Property(type=bool, default=False)

    current_plugins = GObject.Property(
        type=Gio.ListStore
    )  # of ListedPlugin objects

    def __init_(self):
        super().__init__()

        makedirs(PLUGIN_DIR, exist_ok=True)

        # TODO BIND UI ITEM

    def list_plugins(self):
        with self.current_plugins.freeze_notify():
            self.current_plugins.remove_all()

            for dir_entry in scandir(PLUGIN_DIR):
                plugin = ListedPlugin()
                plugin.file_name = dir_entry.name
                plugin.file_path = dir_entry.path
                plugin.last_modified = datetime.fromtimestamp(
                    dir_entry.stat().st_mtime
                ).strftime('%Y-%m-%d %H:%M:%S')

                self.current_plugins.append(dir_entry)

    def watch_plugins(self, callback):
        # TODO use Gio.File.monitor_directory

        XX

    def install_plugin(self):
        # TODO copy $ORIG_PLUGIN_PATH to $PLUGIN_PATH

        XX

    def remove_plugin(self):
        # TODO remove $PLUGIN_PATH

        XX
