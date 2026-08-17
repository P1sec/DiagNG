#!/usr/bin/env python3
from diagng.system.wireshark.wireshark_plugin_manager import (
    WiresharkPluginManager,
    ListedPlugin,
)
from diagng.ui.qcdm_window.templates.wireshark_plugin_row import (
    WiresharkPluginRow,
)

import gi

gi.require_version('Adw', '1')

from gi.repository import Adw


def create_wireshark_plugin(
    plugin: ListedPlugin, manager: WiresharkPluginManager
) -> Adw.ActionRow:

    row = WiresharkPluginRow(plugin, manager)

    return row
