#!/usr/bin/env python3

from signal import SIGHUP, SIGINT, SIGTERM
from logging import debug, error, critical
from traceback import format_exception
import sys
import gi

from qcsuperd.gobject.serial_device import SerialDevice
from qcsuperd.common.logging import LoggingCentral
from qcsuperd.gobject.process import Process
from qcsuperd.ui.window import MyWindow

gi.require_version('Adw', '1')
from gi.repository import Adw, GLib

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        LoggingCentral(debug_mode = True)

        # self.setup_signal_handling()
        self.setup_error_handling()

        debug('Initializing app...')

        super().__init__(**kwargs)

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
                "Caught Python exception: \n"
                + "".join(format_exception(exctype, value, traceback)).rstrip()
            )

        sys.excepthook = error_handler

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
