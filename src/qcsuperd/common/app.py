#!/usr/bin/env python3
from qcsuperd.gobject.serial_device import SerialDevice
from qcsuperd.gobject.process import Process
from qcsuperd.ui.window import MyWindow

# Based on https://github.com/Taiko2k/GTK4PythonTutorial?tab=readme-ov-file#ui-from-graphical-designer

import sys
import gi

gi.require_version('Adw', '1')
from gi.repository import Adw

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('startup', self.on_startup)
        self.connect('activate', self.on_activate)

    def on_startup(self, app, *args):
        self.window = MyWindow()
        self.window.set_application(self)

        # TEST (WIP MMR 2026-05-26)

        """
        process = Process()
        process.process_name = 'ModemManager --TEST'
        process.pid = 12349

        serial_device = SerialDevice()
        serial_device.serial_device_path = '/dev/abcdTEST'
        serial_device.process = process
        """

        # TODO: Create qcsuperd.system.serial.device_scanner
        # background task (leveraging UDEV or just use a
        # glob over /dev/tty* with an interval)?

        # TODO: Create qcsuperd.system.psutil.process_scanner
        # background task (leveraging UDEV or just use a
        # glob over /proc/*/fd/{device_fd} with an interval)?

        ## GLib.idle_add(XX)
        ## GLib.timeout_add(XX)

        # Application will close once it no longer has active windows attached to it

        self.window.present()

    def on_activate(self, app):
        self.window.present()

        # NEXT TODO ==>
        # FILL IN THE TREE VIEW WITH SAMPLE INFORMATION

        # Cf. https://github.com/timlau/yumex-ng/blob/09f15091a2f0f3a8c189bbd4dc59016a80e2debf/yumex/ui/transaction_result.py
        # Cf. https://github.com/timlau/yumex-ng/blob/09f15091a2f0f3a8c189bbd4dc59016a80e2debf/data/ui/transaction_result.blp
        # Cf. too
        # https://github.com/Taiko2k/GTK4PythonTutorial?tab=readme-ov-file#using-gridview


def main():
    app = MyApp(application_id='com.p1security.qcsuperd')
    app.run(sys.argv)


if __name__ == '__main__':
    main()
