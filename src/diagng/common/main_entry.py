#!/usr/bin/env python3

from logging import debug, error, warning
from traceback import format_exception
from argparse import ArgumentParser
from json import dumps
import sys
import gi

from diagng.common.diagmond_communicator import DiagmondCommunicator
from diagng.system.modem_manager_dbus import ModemManagerIntf
from diagng.gobject.mm_instance import ModemManagerInstance
from diagng.system.udev_device_scanner import DeviceScanner
from diagng.utils.logging import LoggingCentral
from diagng.common.window import MyWindow

# Register resources
import diagng.utils.gresources

gi.require_version('Adw', '1')
from gi.repository import Adw, GLib, Gio, GObject

"""
    Primary entry point of diagng
"""


def main():
    args = ArgumentParser(description='Prototype for DiagNG 🍕 🎧')
    args = args.parse_args()

    app = MainApplication(application_id='com.p1security.diagng')
    app.run()


class MainApplication(Adw.Application):
    window: MyWindow

    diagmond_communicator: DiagmondCommunicator
    modem_manager: ModemManagerIntf
    device_scanner: DeviceScanner

    mm_debug_data = GObject.Property(type=str)
    udev_debug_data = GObject.Property(type=str)

    def __init__(self, **kwargs):
        LoggingCentral(debug_mode=True)

        # self.setup_signal_handling()
        self.setup_error_handling()

        debug('Initializing app...')

        super().__init__(**kwargs)
        self.mm_instance = ModemManagerInstance()

        self.connect('startup', self.on_startup)
        self.connect('activate', self.on_activate)

    """
    def setup_signal_handling(self):

        def signal_handler(signal_id):
            critical("Caught %s, sunsetting" % signal_id)
            self.release()

        GLib.unix_signal_add(GLib.PRIORITY_HIGH, SIGHUP, signal_handler, "SIGHUP")
        GLib.unix_signal_add(GLib.PRIORITY_HIGH, SIGINT, signal_handler, "SIGINT")
        GLib.unix_signal_add(GLib.PRIORITY_HIGH, SIGTERM, signal_handler, "SIGTERM")
    """

    def setup_error_handling(self):
        # Generic error handler for non-bubbled exceptions raised in GLib callbacks
        # "This works because exception hooks are called in PyErr_Print."
        # Cf. https://gitlab.gnome.org/GNOME/pygobject/-/blob/3.48.2/tests/test_generictreemodel.py#L335

        def error_handler(exctype, value, traceback):
            error(
                'Caught Python exception: \n'
                + ''.join(format_exception(exctype, value, traceback)).rstrip()
            )

        sys.excepthook = error_handler

    def do_dbus_register(
        self, connection: Gio.DBusConnection, object_path: str
    ):

        # See ⚠️ https://lazka.github.io/pgi-docs/Gio-2.0/structs/Resource.html#Gio.Resource.lookup_data
        # See: https://lazka.github.io/pgi-docs/Gio-2.0/classes/DBusConnection.html#Gio.DBusConnection.register_object_with_closures2
        # See: https://lazka.github.io/pgi-docs/Gio-2.0/classes/DBusConnection.html#Gio.DBusConnection.register_object_with_closures2
        # See: ⚠️ https://gitlab.gnome.org/GNOME/glib/-/blob/HEAD/gio/tests/gapplication-example-dbushooks.c
        XML_TREE = (
            Gio.resources_lookup_data(
                '/com/p1security/diagng/com.p1security.diagmetad.xml', 0
            )
            .get_data()
            .decode('utf-8')
        )

        dbus_info = Gio.DBusNodeInfo.new_for_xml(XML_TREE)
        interface_info = dbus_info.lookup_interface('com.p1security.diagmetad')
        assert interface_info

        connection.register_object_with_closures2(
            object_path,
            interface_info,
            self.on_method_call,
            self.on_property_get,
            self.on_property_set,
        )
        return True

    def on_method_call(self, *args):
        warning('Unhandled: on_method_call: %r', args)

    def on_property_get(
        self,
        dbus_connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        property_name: str,
    ) -> GLib.Variant:
        if property_name == 'MMDebugInfo':
            return GLib.Variant.new_string(
                dumps(self.modem_manager.json_state, indent=4)
            )
        elif property_name == 'MMStatusInfo':
            return self.modem_manager.mm_instance.to_gvariant()
        elif property_name == 'UDevUSBDebugInfo':
            return GLib.Variant.new_string(
                dumps(self.device_scanner.json_state, indent=4)
            )
        elif property_name == 'UDevUSBDeviceTree':
            return self.device_scanner.usb_tree_gobjs
        elif property_name == 'UDevSPIDeviceTree':
            return self.device_scanner.spi_tree_gobjs
        elif property_name == 'SPIDeviceInformation':
            return self.device_scanner.spi_gobjs
        else:
            warning(
                'Unhandled yet: on_property_get: %s.%s',
                interface_name,
                property_name,
            )

    def on_property_set(self, *args):
        warning('Unhandled: on_property_set: %r', args)

    def do_dbus_unregister(self, connection: Gio.DBusConnection, path: str):
        pass

    def on_startup(self, app, *args):
        self.diagmond_communicator = DiagmondCommunicator()
        self.modem_manager = ModemManagerIntf(self)
        self.device_scanner = DeviceScanner(self)

        self.window = MyWindow(self)

        # Application will close once it has no longer has active
        # windows attached to it

        self.window.present()

    def on_activate(self, app):
        self.window.present()


if __name__ == '__main__':
    main()
