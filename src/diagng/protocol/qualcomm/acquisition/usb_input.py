#!/usr/bin/env python3

from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput
from diagng.gobject.usb_interface import USBInterface
from diagng.gobject.usb_device import USBDevice

from logging import error, warning, debug

import gi

gi.require_version('Adw', '1')

from gi.repository import Gio, GLib, Adw

_connected_ports: dict[str, 'USBQCDMInput'] = {}


class USBQCDMInput(BaseQCDMInput):
    dbus_serial_device: Gio.DBusProxy
    usb_dev: USBDevice
    usb_intf: USBInterface
    main_window: Adw.ApplicationWindow

    def __init__(
        self,
        dbus_serial_device: Gio.DBusProxy,
        usb_dev: USBDevice,
        usb_intf: USBInterface,
        main_window: Adw.ApplicationWindow,
    ):
        super().__init__()

        self.dbus_serial_device = dbus_serial_device
        self.usb_dev = usb_dev
        self.usb_intf = usb_intf
        self.main_window = main_window

        self.usb_intf.connected = True
        _connected_ports[usb_intf.full_intf_id] = self
        self.main_window.update_usb_devices()

        self.short_name = usb_intf.full_intf_id

        self._update_conn_state()

        self.usb_intf.connect('notify::connected', self._update_conn_state)
        self.dbus_serial_device.connect('g-signal::Read', self._on_read)
        self.dbus_serial_device.connect('g-signal::Closed', self._on_closed)

    def _update_conn_state(self, *args):
        full_name = ''

        if not self.usb_intf.connected:
            full_name += '(DISCONNECTED) - '

        full_name += '%s - ' % self.usb_intf.full_intf_id

        if self.usb_dev.alt_vendor_name:
            full_name += '%s %s -' % (
                self.usb_dev.alt_vendor_name or '',
                self.usb_dev.alt_model_name or '',
            )

        full_name += '%s %s (%s)' % (
            self.usb_dev.vendor_name or '',
            self.usb_dev.model_name or '',
            self.usb_dev.vid_pid or '',
        )

        self.full_name = full_name

    def _on_read(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        data = bytes(parameters[0])
        debug('Received data from USB interface: %r' % data)
        self.process_input(data)

    def _on_closed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        self.closed.emit()
        if self.usb_intf.full_intf_id in _connected_ports:
            del _connected_ports[self.usb_intf.full_intf_id]
        self.usb_intf.connected = False
        self.main_window.update_usb_devices()

        reason = str(parameters[0])
        warning('USB interface closed, reason: ' + reason)

    def send_raw(self, data: bytes):
        def write_cb(proxy, result, obj_path):
            if isinstance(result, Exception):
                error('Failed to write to USB interface: %r' % result)
                dialog = Adw.AlertDialog.new(
                    '⚠️ Failed to write to USB interface', repr(result)
                )
                dialog.add_response('ok', 'Ok')
                dialog.choose(self.main_window, None, None)
                self.close()

        self.dbus_serial_device.Write('(ay)', data, result_handler=write_cb)

    def close(self):
        def close_cb(proxy, result, obj_path):
            self.closed.emit()
            if self.usb_intf.full_intf_id in _connected_ports:
                del _connected_ports[self.usb_intf.full_intf_id]
            self.usb_intf.connected = False
            self.main_window.update_usb_devices()

            if isinstance(result, Exception):
                error('Failed to close USB interface: %r' % result)

        self.dbus_serial_device.Close('()', result_handler=close_cb)
