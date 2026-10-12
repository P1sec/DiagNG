#!/usr/bin/env python3

from logging import debug, error, warning
from traceback import format_exception
from argparse import ArgumentParser
from json import dumps
import sys
import gi

from diagng.system.diagmond_serialdevice_om import DiagmondSerialDeviceOM
from diagng.system.diagmond_communicator import DiagmondCommunicator
from diagng.system.modem_manager_dbus import ModemManagerIntf
from diagng.system.udev_device_scanner import DeviceScanner
from diagng.utils.logging_central import LoggingCentral
from diagng.utils.flatpak_helper import FlatpakHelper
from diagng.system.adb.adb_watcher import ADBWatcher
from diagng.ui.main_window.imp import MainWindow

# Register resources
import diagng.utils.gresources

gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')
from gi.repository import Adw, Gtk, Gdk, GLib, Gio, GObject

"""
    Primary entry point of diagng
"""


def main():
    args = ArgumentParser(
        description='DiagNG is a general-purpose client for '
        + 'mobile basebands, allowing to product 2G/3G/4G/5G network traces'
    )

    args.add_argument(
        '-d',
        '--debug',
        help='Compile the diagmond binary with debugging symbols whenever it '
        + 'has changed',
        action='store_true',
    )

    args.add_argument(
        '-n',
        '--no-spawn',
        help='Disallow spawning external commands in order to simulate a '
        + 'Flatpak sandbox',
        action='store_true',
    )

    args = args.parse_args()

    GLib.set_prgname('com.p1security.diagng')

    app = MainApplication(
        args.no_spawn, application_id='com.p1security.diagng'
    )
    app.run()


class MainApplication(Adw.Application):
    window: MainWindow = None

    logging_central: LoggingCentral = None

    can_spawn_commands = GObject.Property(type=bool, default=False)
    force_no_spawn = GObject.Property(type=bool, default=False)

    diagmond_communicator: DiagmondCommunicator = None
    diagmond_serialdevice_om: DiagmondSerialDeviceOM = None
    adb_watcher: ADBWatcher
    modem_manager: ModemManagerIntf = None
    device_scanner: DeviceScanner = None

    mm_debug_data = GObject.Property(type=str)
    udev_debug_data = GObject.Property(type=str)
    nusb_debug_data = GObject.Property(type=str)
    tokio_serial_debug_data = GObject.Property(type=str)

    def __init__(self, no_spawn: bool, **kwargs):
        self.logging_central = LoggingCentral(debug_mode=True)

        # self.setup_signal_handling()
        self.setup_error_handling()

        debug('Initializing app...')

        icon_theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
        icon_theme.add_resource_path('/com/p1security/diagng/')

        super().__init__(**kwargs)
        self.force_no_spawn = no_spawn

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
            tb_string = ''.join(
                format_exception(exctype, value, traceback)
            ).rstrip()

            error('Caught Python exception: \n' + tb_string)

            if self.window:
                dialog = Adw.AlertDialog.new(
                    '⚠️ Caught Python exception', tb_string
                )
                dialog.add_response('ok', 'Ok')
                dialog.choose(None, None, None)

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

        def on_flatpak_status(flatpak_spawn_available: bool):

            is_flatpak: bool = FlatpakHelper.is_flatpak()

            self.can_spawn_commands = (
                flatpak_spawn_available or not is_flatpak
            ) and not self.force_no_spawn

            self.diagmond_communicator = DiagmondCommunicator(self)

            self.modem_manager = ModemManagerIntf(self)
            self.device_scanner = DeviceScanner(self)
            self.adb_watcher = ADBWatcher()

            self.window = MainWindow(self)

            self.diagmond_serialdevice_om = DiagmondSerialDeviceOM(
                self.window, self.diagmond_communicator.connection
            )

        FlatpakHelper.is_flatpak_spawn_available(on_flatpak_status)

        # ^ ⚠️ ⚠️ TODO propagate logging.error errors to
        # main_window using a CUSTOM LOGGING HANDLER
        # when the GUI IS ENABLED?

        # Application will close once it has no longer has active
        # windows attached to it

        self.window.present()

    def on_activate(self, app):
        self.window.present()


if __name__ == '__main__':
    main()
