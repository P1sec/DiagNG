#!/usr/bin/env python3

from gi.repository import GObject, Gio
from logging import debug
# XX WIP 2026-06-23

#  ⚠️ ⚠️   https://docs.gtk.org/gio/func.bus_watch_name.html
#     => https://lazka.github.io/pgi-docs/Gio-2.0/functions.html#Gio.bus_watch_name
# "You are guaranteed that one of the handlers will be invoked after calling this function"

# https://docs.gtk.org/gio/type_func.DBusProxy.new_for_bus.html


class DiagmondCommunicator(GObject.Object):
    system_bus: Gio.DBusConnection

    def __init__(self):
        super().__init__()

        self.system_bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)

        Gio.bus_watch_name_on_connection(
            self.system_bus,
            'com.p1security.diagmond',
            Gio.BusNameWatcherFlags.AUTO_START,
            self.name_appeared_closure,
            self.name_vanished_closure,
        )

    def name_appeared_closure(self, connection, bus_name, conn_name):
        debug('Diagmond bus available')

    def name_vanished_closure(self, connection, bus_name):
        debug('Diagmond bus unavailable')
