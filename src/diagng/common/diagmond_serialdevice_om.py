#!/usr/bin/env python3

from logging import debug, info, error
from typing import Optional

from diagng.acquisition.qualcomm.spi_input import SerialQCDMInput
from diagng.acquisition.qualcomm.usb_input import USBQCDMInput
from diagng.gobject.usb_interface import USBInterface
from diagng.gobject.serial_port import SerialPort
from diagng.common.qcdm_window import QCDMWindow
from diagng.gobject.usb_device import USBDevice

import gi

gi.require_version('Adw', '1')

from gi.repository import GObject, Gio, Adw

# In this class we enumerate and watch for SerialDevice
# objects with DBusObjectManagerClient. get_objects(), etc.
#
# Cf. https://docs.gtk.org/gio/class.DBusObjectManagerClient.html
# + ➡️ https://lazka.github.io/pgi-docs/Gio-2.0/interfaces/DBusObjectManager.html


class DiagmondSerialDeviceOM(GObject.Object):
    om: Gio.DBusObjectManagerClient = None
    connection: Gio.DBusConnection

    interface_info: Gio.DBusInterfaceInfo

    main_window: Adw.ApplicationWindow

    def __init__(
        self,
        main_window: Adw.ApplicationWindow,
        connection: Gio.DBusConnection,
    ):
        super().__init__()

        self.main_window = main_window
        self.connection = connection

        XML_TREE = (
            Gio.resources_lookup_data(
                '/com/p1security/diagng/com.p1security.diagmond.SerialDevice.xml',
                0,
            )
            .get_data()
            .decode('utf-8')
        )

        dbus_info = Gio.DBusNodeInfo.new_for_xml(XML_TREE)
        self.interface_info = dbus_info.lookup_interface(
            'com.p1security.diagmond.SerialDevice'
        )
        assert self.interface_info

        Gio.DBusObjectManagerClient.new(
            self.connection,
            Gio.DBusObjectManagerClientFlags.DO_NOT_AUTO_START,
            'com.p1security.diagmond',
            '/com/p1security/diagmond/SerialDevices',
            None,
            None,
            None,
            self.om_ready,
            None,
        )

    def om_ready(
        self,
        source_object: Optional[GObject.Object],
        result: Gio.AsyncResult,
        data: Optional[object],
    ):
        self.om = Gio.DBusObjectManagerClient.new_finish(result)

        self.om.connect('object-added', self.on_object_added)
        self.om.connect('object-removed', self.on_object_removed)
        self.om.connect('interface-added', self.on_interface_added)
        self.om.connect('interface-removed', self.on_interface_removed)

        self.remove_dangling_objects()

    def remove_dangling_objects(self):
        for obj in self.om.get_objects():
            debug('Cleaning up dangling SerialDevice object: %r' % obj)

            obj_path = obj.get_object_path()

            proxy = Gio.DBusProxy.new_sync(
                self.connection,
                Gio.DBusProxyFlags.NONE,
                self.interface_info,
                'com.p1security.diagmond',
                obj_path,
                'com.p1security.diagmond.SerialDevice',
                None,
            )

            def port_closed(proxy, result, obj_path):
                if isinstance(result, Exception):
                    error(
                        'Did not receive cleanup response for SerialDevice: %r'
                        % result
                    )
                else:
                    info('Dangling %s port closed successfully' % obj_path)

            proxy.Close(
                '()',
                result_handler=port_closed,
                user_data=obj_path,
            )

    def create_qcdm_window_spi(
        self, object_path: str, serial_port: SerialPort
    ):
        proxy = Gio.DBusProxy.new_sync(
            self.connection,
            Gio.DBusProxyFlags.NONE,
            self.interface_info,
            'com.p1security.diagmond',
            object_path,
            'com.p1security.diagmond.SerialDevice',
            None,
        )

        # Spawn a GLib task reading and logging
        # pseudo-HDLC events from the serial stream,
        # using SPI-specific adapter code
        #
        #   ===> This leverages a GObject-based
        #    interface (the BaseInput class),
        #    callbacks and signal-based connectivity
        #    that can be extended to provide different
        #    adapters for different input sources (USB,
        #    ADB, SPI, DLF file, etc.) through
        #    subclassing

        input_obj = SerialQCDMInput(proxy, serial_port, self.main_window)

        QCDMWindow(self.main_window, input_obj)

    def create_qcdm_window_usb(
        self, object_path: str, usb_dev: USBDevice, usb_intf: USBInterface
    ):
        proxy = Gio.DBusProxy.new_sync(
            self.connection,
            Gio.DBusProxyFlags.NONE,
            self.interface_info,
            'com.p1security.diagmond',
            object_path,
            'com.p1security.diagmond.SerialDevice',
            None,
        )

        input_obj = USBQCDMInput(proxy, usb_dev, usb_intf, self.main_window)

        QCDMWindow(self.main_window, input_obj)

    def on_object_added(self, om: Gio.DBusObjectManager, obj: Gio.DBusObject):
        debug('SerialDevice object added: %r' % obj)

    def on_object_removed(
        self, om: Gio.DBusObjectManager, obj: Gio.DBusObject
    ):
        # TODO ⚠️ Freeze QCDMWindow
        debug('SerialDevice object removed: %r' % obj)

    def on_interface_added(
        self,
        om: Gio.DBusObjectManager,
        obj: Gio.DBusObject,
        intf: Gio.DBusInterface,
    ):
        # Never called?
        debug('SerialDevice interface added: %r->%r' % (obj, intf))

    def on_interface_removed(
        self,
        om: Gio.DBusObjectManager,
        obj: Gio.DBusObject,
        intf: Gio.DBusInterface,
    ):
        # Never called?
        debug('SerialDevice interface removed: %r->%r' % (obj, intf))
