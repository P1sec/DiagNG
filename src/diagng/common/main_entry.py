#!/usr/bin/env python3

from logging import debug, error, info, critical
from traceback import format_exception
from argparse import ArgumentParser
from shlex import join
import sys
import gi

from diagng.gobject.mm_instance import ModemManagerInstance
from diagng.common.main_rpc_server import MainRPCServer
from diagng.common.service_entry import service_main
from diagng.gobject.udev_device import UDevDevice
from diagng.gobject.serial_port import SerialPort
from diagng.common.logging import LoggingCentral
from diagng.ui.window import MyWindow

try:
    from os import setpgrp
except ImportError:  # UNIX-specific

    def setpgrp():
        pass


gi.require_version('Adw', '1')
from gi.repository import Adw, GLib, Gio, GObject

"""
    Primary entry point of diagng, called
    before spawning a provilege-elevated
    subprocess in service_entry.py
"""


def main():
    args = ArgumentParser(description='Prototype for DiagNG 🍕 🎧')

    args.add_argument(
        '--service',
        help=(
            'This flag is present when the main instance of the app '
            + 'is instancying a privileged subprocess for performing '
            + 'privileged operations, such as acquiring data from '
            + 'serial ports'
        ),
        action='store_true',
    )

    args.add_argument(
        '--client-port',
        help=(
            'The JsonRPC TCP port for reaching of the parent, '
            + 'unprivileged process when spawing a privileged child'
        ),
    )

    args = args.parse_args()

    if args.service:
        # We have been using a subprocess spawn + Jsonrpc listen operation
        # (see https://lazka.github.io/pgi-docs/Jsonrpc-1.0/index.html +
        # https://docs.gtk.org/glib/spawn.html +
        # https://lazka.github.io/pgi-docs/GLib-2.0/functions.html#GLib.spawn_async_with_pipes)
        # here

        # We have been passed:
        # argv[0] --service --client-port=${OCAL_TCP_PORT}
        assert args.client_port
        service_main()

    else:
        app = MainApplication(application_id='com.p1security.diagng')
        app.run()


class MainApplication(Adw.Application):
    window: MyWindow

    mm_instance = GObject.Property(type=ModemManagerInstance)
    mm_debug_data = GObject.Property(type=str)

    usb_device_tree = GObject.Property(type=Gio.ListStore)
    spi_device_tree = GObject.Property(type=Gio.ListStore)
    spi_devices = GObject.Property(type=Gio.ListStore)
    udev_debug_data = GObject.Property(type=str)

    def __init__(self, **kwargs):
        LoggingCentral(debug_mode=True)

        # self.setup_signal_handling()
        self.setup_error_handling()

        debug('Initializing app...')

        super().__init__(**kwargs)
        self.mm_instance = ModemManagerInstance()
        self.usb_device_tree = Gio.ListStore.new(UDevDevice)
        self.spi_device_tree = Gio.ListStore.new(UDevDevice)
        self.spi_devices = Gio.ListStore.new(SerialPort)

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

    def on_startup(self, app, *args):
        self.window = MyWindow(self)

        # Spawn or connect to privileged --service
        # subprocess here

        # => Spawn our JsonRpc listener on a local socket

        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketListener.html#Gio.SocketListener.new
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketListener.html#Gio.SocketListener.add_address
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketListener.html#Gio.SocketListener.add_any_inet_port
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/InetAddress.html#Gio.InetAddress.new_loopback
        # => https://lazka.github.io/pgi-docs/Gio-2.0/classes/InetSocketAddress.html#Gio.InetSocketAddress.new
        #    with port 0 + https://lazka.github.io/pgi-docs/Gio-2.0/classes/InetSocketAddress.html#Gio.InetSocketAddress.get_port
        # should return an available port?
        #     Cf. https://github.com/GNOME/glib/blob/2.89.0/gio/gsocketlistener.c#L1172
        #     Cf.
        #  ⚠️ ^ "Listens for TCP connections on any available port number for both IPv6 and IPv4 (if each is available).
        #    This is useful if you need to have a socket for incoming connections but don’t care about the specific port number."
        #   => https://github.com/GNOME/glib/blob/2.89.0/gio/gsocketlistener.c#L1133
        #
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketListener.html#Gio.SocketListener.add_inet_port
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/UnixSocketAddress.html#Gio.UnixSocketAddress.new

        socket_service = Gio.SocketService.new()
        success, bound_address = socket_service.add_address(
            Gio.InetSocketAddress.new(
                Gio.InetAddress.new_loopback(Gio.SocketFamily.IPV4), 0
            ),
            Gio.SocketType.STREAM,
            Gio.SocketProtocol.TCP,
            None,
        )
        if not success or not bound_address:
            critical("Coun't bind to local address")
            exit(1)
        effective_addr: str = bound_address.get_address().to_string()
        effective_port: int = bound_address.get_port()
        info(
            'Binding to local address: %s:%d'
            % (effective_addr, effective_port)
        )

        # Use https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketListener.html#Gio.SocketListener.accept_async
        # in order to obtain an Gio.SocketConnection inheriting Gio.IOStream,
        # to be passed to https://lazka.github.io/pgi-docs/Jsonrpc-1.0/classes/Server.html#Jsonrpc.Server.accept_io_stream
        # (and eventually connect back to a socket through getting RPC called with a TCP endpoint
        # that we will pass to https://lazka.github.io/pgi-docs/Jsonrpc-1.0/classes/Client.html#Jsonrpc.Client.new

        rpc_server = MainRPCServer(self)

        def accept_socket(
            socket_service: Gio.SocketService,
            remote_socket: Gio.SocketConnection,
            source_object,
        ):
            connector: Gio.InetSocketAddress = (
                remote_socket.get_remote_address()
            )
            connector_addr: str = connector.get_address().to_string()
            connector_port: int = connector.get_port()
            info(
                f'Received RPC connection from {connector_addr}:{connector_port}'
            )
            rpc_server.accept_io_stream(remote_socket)

        socket_service.connect('incoming', accept_socket)

        #   => Use --service --client-port=${OUR_PORT} to hopefully
        #      trigger a call first to our JSONRPC socket endpoint
        #      and wait

        child_cmd_line = [
            sys.argv[0],
            '--service',
            '--client-port=' + str(effective_port),
        ]

        # Use GLib.spawn_async so that we
        # can merge the process group of the
        # subprocess if any useful

        child_pid, _, _, _ = GLib.spawn_async(
            child_cmd_line,
            child_setup=setpgrp,  # Do not inherit signals such as SIGINT
        )

        info(f'Spawning "{join(child_cmd_line)}" as pid {child_pid}...')

        def child_exited(pid: int, wait_status: int, *args):
            info('Child process exited with status ' + str(wait_status))
            try:
                GLib.spawn_check_wait_status(wait_status)
            except Exception as err:
                self.quit()
                raise err

        GLib.child_watch_add(
            GLib.PRIORITY_DEFAULT_IDLE, child_pid, child_exited
        )

        # Application will close once it has no longer has active
        # windows attached to it

        self.window.present()

    def on_activate(self, app):
        self.window.present()


if __name__ == '__main__':
    main()
