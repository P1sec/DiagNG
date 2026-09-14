#!/usr/bin/env python3
from diagng.system.wireshark.wireshark_plugin_manager import (
    WiresharkPluginManager,
    ListedPlugin,
)

import gi

gi.require_version('Adw', '1')

from gi.repository import Adw, Gio, Gtk


class WiresharkPluginRow(Adw.ActionRow):
    plugin: ListedPlugin
    manager: WiresharkPluginManager
    parent: Adw.Window

    def __init__(
        self,
        plugin: ListedPlugin,
        manager: WiresharkPluginManager,
        parent: Adw.Window,
    ):
        super().__init__()

        self.plugin = plugin
        self.manager = manager
        self.parent = parent

        self.set_use_markup(False)

        self.set_title(plugin.file_name)
        self.set_subtitle('Last modified ' + ' ' + plugin.last_modified)

        open_button = Gtk.Button.new_with_label('Open')

        def on_open_clicked(*args):
            plugin_file = Gio.File.new_for_path(plugin.file_path)
            Gtk.FileLauncher.new(plugin_file).launch(parent, None, None)

        open_button.connect('clicked', on_open_clicked)
        self.add_suffix(open_button)
