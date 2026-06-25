#!/usr/bin/env python3

from gi.repository import GObject, GLib, Gio
from json import dumps, loads
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

    main_app: 'MainApplication'

    def __init__(self, main_app: 'MainApplication'):
        super().__init__()

        self.main_app = main_app
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
        self.proxy.connect('g-signal::USBDataUpdated', self.usb_data_changed)
        # TODO NOTIFY ON USBDataUpdated signal triggered
        # (= OR JUST WHEN PROP :USBData CHANGED?)
        self.status_changed()

    def status_changed(self, *args):
        self.bus_connected = bool(self.proxy.get_name_owner())
        if self.bus_connected:
            debug('Diagmond bus available')

            usb_data_raw = self.proxy.get_cached_property('USBData')
            if usb_data_raw:
                self.process_usb_data(loads(usb_data_raw.get_string()))
        else:
            debug('Diagmond bus unavailable')

    def usb_data_changed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        self.process_usb_data(loads(parameters[0]))

    def process_usb_data(self, usb_data: dict):
        if usb_data:
            debug('nusb data updated')

            self.main_app.nusb_debug_data = dumps(usb_data, indent=4)
