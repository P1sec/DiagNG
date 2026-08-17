#!/usr/bin/env python3
from diagng.system.wireshark.wireshark_plugin_manager import (
    WiresharkPluginManager,
    ListedPlugin,
)

import gi

gi.require_version('Adw', '1')

from gi.repository import Adw


class WiresharkPluginRow(Adw.ActionRow):
    plugin: ListedPlugin
    manager: WiresharkPluginManager

    def __init__(self, plugin: ListedPlugin, manager: WiresharkPluginManager):
        super().__init__()

        self.plugin = plugin
        self.manager = manager

        self.set_use_markup(False)

        self.set_title(plugin.file_name)
        self.set_subtitle('Last modified ' + ' ' + plugin.last_modified)
