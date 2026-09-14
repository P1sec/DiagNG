#!/usr/bin/env python3
from os.path import expanduser, dirname, realpath, exists, join
from os import makedirs, unlink, scandir
from gi.repository import GObject, Gio
from typing import Optional, Callable
from datetime import datetime
from shutil import copy2

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

    file_monitor: Optional[Gio.FileMonitor]

    def __init__(self):
        super().__init__()

        makedirs(PLUGIN_DIR, exist_ok=True)

        self.current_plugins = Gio.ListStore.new(ListedPlugin)

        # We'll bind UI item in the caller class

        self.list_plugins()

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

                self.current_plugins.append(plugin)

    def watch_plugins(
        self, callback: Optional[Callable[[Gio.ListStore], None]] = None
    ) -> Gio.Cancellable:

        cancellable = Gio.Cancellable()

        folder = Gio.File.new_for_path(PLUGIN_DIR)
        self.file_monitor = folder.monitor_directory(
            Gio.FileMonitorFlags.WATCH_MOVES, cancellable
        )

        def on_change(*args):
            self.list_plugins()
            if callback:
                callback(self.current_plugins)

        self.file_monitor.connect('changed', on_change)

        return cancellable

    def install_plugin(self):
        # Copy $ORIG_PLUGIN_PATH to $PLUGIN_PATH

        copy2(ORIG_PLUGIN_PATH, PLUGIN_PATH)

    def remove_plugin(self):
        # Remove $PLUGIN_PATH

        if exists(PLUGIN_PATH):
            unlink(PLUGIN_PATH)
