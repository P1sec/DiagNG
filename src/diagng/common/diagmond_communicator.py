#!/usr/bin/env python3

from gi.repository import GObject, Gio
from typing import Optional
from logging import debug
# XX WIP 2026-06-23

#  ⚠️ ⚠️   https://docs.gtk.org/gio/func.bus_watch_name.html
#     => https://lazka.github.io/pgi-docs/Gio-2.0/functions.html#Gio.bus_watch_name
# "You are guaranteed that one of the handlers will be invoked after calling this function"

# https://docs.gtk.org/gio/type_func.DBusProxy.new_for_bus.html


class DiagmondCommunicator(GObject.Object):
    connection: Gio.DBusConnection
    proxy: Gio.DBusProxy
    bus_connected = GObject.Property(type=bool, default=False)

    def __init__(self):
        super().__init__()

        self.connection = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)

        XML_TREE = (
            Gio.resources_lookup_data(
                '/com/p1security/diagng/com.p1security.diagmond.xml', 0
            )
            .get_data()
            .decode('utf-8')
        )

        dbus_info = Gio.DBusNodeInfo.new_for_xml(XML_TREE)
        interface_info = dbus_info.lookup_interface('com.p1security.diagmond')
        assert interface_info

        self.proxy = Gio.DBusProxy.new_sync(
            self.connection,
            Gio.DBusProxyFlags.NONE,
            interface_info,
            'com.p1security.diagmond',
            '/com/p1security/diagmond',
            'com.p1security.diagmond',
            None,
        )

        self.proxy.connect('notify::g-name-owner', self.status_changed)
        self.status_changed()

    def status_changed(self, *args):
        self.bus_connected = bool(self.proxy.get_name_owner())
        if self.bus_connected:
            debug('Diagmond bus available')
        else:
            debug('Diagmond bus unavailable')
