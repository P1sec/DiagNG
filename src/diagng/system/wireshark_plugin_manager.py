#!/usr/bin/env python3
from gi.repository import GObject

class WirsharkPluginState(GObject.Enum):
    WiresharkNotFound = 1
    PluginNotInstalled = 2
    PluginNeedsUpdate = 3
    PluginInstalled = 4

class WiresharkPluginManager(GObject.Object):
    XX
