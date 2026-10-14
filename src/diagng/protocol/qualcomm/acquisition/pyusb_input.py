#!/usr/bin/env python3

from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput
from diagng.gobject.usb_interface import USBInterface
from diagng.gobject.usb_device import USBDevice

from logging import error, warning, debug
from usb.util import dispose_resources
from usb.core import Endpoint, Device
from traceback import format_exc
from threading import Thread

import gi

gi.require_version('Adw', '1')

from gi.repository import Gio, GLib, Adw

_connected_ports: dict[str, 'PyUSBQCDMInput'] = {}


class PyUSBQCDMInput(BaseQCDMInput):
    pyusb_device: Device
    in_endpoint: Endpoint
    out_endpoint: Endpoint

    usb_dev: USBDevice
    usb_intf: USBInterface
    main_window: Adw.ApplicationWindow

    def __init__(
        self,
        pyusb_device: Device,
        in_endpoint: Endpoint,
        out_endpoint: Endpoint,
        usb_dev: USBDevice,
        usb_intf: USBInterface,
        main_window: Adw.ApplicationWindow,
    ):
        super().__init__()

        self.pyusb_device = pyusb_device
        self.in_endpoint = in_endpoint
        self.out_endpoint = out_endpoint

        self.usb_dev = usb_dev
        self.usb_intf = usb_intf
        self.main_window = main_window

        self.usb_intf.connected = True
        _connected_ports[usb_intf.full_intf_id] = self
        self.main_window.update_usb_devices()

        self.short_name = usb_intf.full_intf_id

        self._update_conn_state()

        self.usb_intf.connect('notify::connected', self._update_conn_state)

        def read_thread():
            while True:
                try:
                    data = bytes(
                        in_endpoint.read(
                            in_endpoint.wMaxPacketSize or 0x200,
                            timeout=0x7FFFFFFF,
                        )
                    )
                except Exception:
                    error('Could not read from USB endpoint: ' + format_exc())
                    GLib.idle_add(self.close)
                    return
                debug('Received data from USB interface: %r' % data)
                GLib.idle_add(self.process_input, data)

        thread = Thread(target=read_thread)
        thread.daemon = True
        thread.start()

    def _update_conn_state(self, *args):
        full_name = ''

        if not self.usb_intf.connected:
            full_name += '(DISCONNECTED) - '

        full_name += '%s - ' % self.usb_intf.full_intf_id

        if self.usb_dev.alt_vendor_name:
            full_name += '%s %s - ' % (
                self.usb_dev.alt_vendor_name or '',
                self.usb_dev.alt_model_name or '',
            )

        full_name += '%s %s (%s)' % (
            self.usb_dev.vendor_name or '',
            self.usb_dev.model_name or '',
            self.usb_dev.vid_pid or '',
        )

        self.full_name = full_name

    def send_raw(self, data: bytes):
        def write_task():
            try:
                self.out_endpoint.write(data)
            except Exception:
                exc_info = format_exc()

                def error_task():
                    error('Failed to write to USB interface: ' + exc_info)
                    dialog = Adw.AlertDialog.new(
                        '⚠️ Failed to write to USB interface', exc_info
                    )
                    dialog.add_response('ok', 'Ok')
                    dialog.choose(self.main_window, None, None)
                    self.close()

                GLib.idle_add(error_task)

        task = Thread(target=write_task)
        task.daemon = True
        task.start()

    def close(self):
        try:
            dispose_resources(self.pyusb_device)
        except Exception:
            error('Failed to close USB interface: ' + format_exc())

        self.closed.emit()
        if self.usb_intf.full_intf_id in _connected_ports:
            del _connected_ports[self.usb_intf.full_intf_id]
        self.usb_intf.connected = False
        self.main_window.update_usb_devices()
