#!/usr/bin/env python3
from logging import debug, info, error, critical
from traceback import format_exception
from shlex import join
import sys

from diagng.system.modemmanager.modem_manager_dbus import ModemManagerIntf
from diagng.common.service_rpc_client import ServiceRPCClient
from diagng.common.logging import LoggingCentral

import gi

gi.require_version('Json', '1.0')
gi.require_version('Jsonrpc', '1.0')
from gi.repository import GLib, Gio, Json, Jsonrpc

"""
Secondary entry point of diagng, called
after spawning a provilege-elevated
subprocess from main_entry.py
"""

# WIP as of 2026-05-29

# TODO: Use inotify (or just mtime checks)
#   to restart the daemon when source code
#   has changed and no connections are
#   alive?

# In the meantime, lookup this variable
# when in development:

QUIT_WHEN_ZERO_CONNECTIONS = True


class ServiceApplication(Gio.Application):
    modem_manager: ModemManagerIntf
    number_clients: int = 0
    effective_addr: str
    effective_port: int
    port_to_client: dict[int, Jsonrpc.Client]

    def __init__(self, **kwargs):
        LoggingCentral(debug_mode=True)

        # self.setup_signal_handling()
        self.setup_error_handling()

        debug('Initializing service...')

        super().__init__(**kwargs)

        self.connect('startup', self.on_startup)
        self.connect('activate', self.on_activate)
        self.connect('command-line', self.on_command_line)
        # self.connect('handle-local-options', self.connect_parent_rpc)

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

    def on_startup(self, app):
        info('Got startup signal')

        # TODO use execlp to privilege escalate (using pkexec
        # or sudo) if non-root here

        # Start the GLib event loop

        self.hold()

        # Bind a socket for our RPC server

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
        self.effective_addr: str = bound_address.get_address().to_string()
        self.effective_port: int = bound_address.get_port()
        info(
            'Binding to local address: %s:%d'
            % (self.effective_addr, self.effective_port)
        )

        # Spawn a RPC server in on_command_line

        self.port_to_client = {}

        # WIP 2026-06-01 spawn ModemManager seeking background task

        self.modem_manager = ModemManagerIntf(self)

    def incr_connection_count(self):
        self.number_clients += 1
        info(f'We now have {self.number_clients} connections open')

    def decr_connection_count(self):
        self.number_clients -= 1
        info(f'We now have {self.number_clients} connections open')

        if QUIT_WHEN_ZERO_CONNECTIONS and self.number_clients < 1:
            # Quit the event loop

            info('Servicing zero connections, sunsetting')
            self.release()

    def on_activate(self, app):
        info('Got activate signal')

    def on_command_line(self, app, command_line: Gio.ApplicationCommandLine):
        self.connect_parent_rpc(app, command_line.get_options_dict())
        return 0

    def connect_parent_rpc(self, app, args: GLib.VariantDict):
        client_port = args.lookup_value(
            'client-port', GLib.VariantType.new('i')
        ).get_int32()
        info(f'Got client port "{client_port}"')

        # Connect to the RPC server of the parent
        # and send the TCP port for our server
        socket = Gio.SocketClient.new()
        socket.connect_async(
            Gio.InetSocketAddress.new(
                Gio.InetAddress.new_loopback(Gio.SocketFamily.IPV4),
                client_port,
            ),
            None,
            self.connected_to_parent,
            client_port,
        )

        self.incr_connection_count()

    def connected_to_parent(
        self,
        socket: Gio.SocketClient,
        result: Gio.AsyncResult,
        client_port: int,
    ):
        try:
            client: Gio.TcpConnection = socket.connect_finish(result)
        except Exception as err:
            self.decr_connection_count()
            raise err

        if not client:
            critical('Connection to parent socket failed')
            self.decr_connection_count()
            return

        parent_rpc = ServiceRPCClient(client)
        self.port_to_client[client_port] = parent_rpc
        parent_rpc.connect('failed', self.client_closed, client_port)

        parent_rpc.call_async(
            'test_ctos',
            GLib.Variant.new_int64(42),
            None,
            None,
        )

        info(f'Sent "test_ctos" call to parent {client_port}')

        self.modem_manager.update_remote_state()

        # XX set client into a global dict (use port as
        # a key) until it disconnects, so that we
        # can sent Diag traffic to it, etc

    def broadcast_message(self, method: str, value: GLib.Variant):

        for port, client in sorted(self.port_to_client.items()):
            client.call_async(
                method,
                value,
                None,
                None,
            )

    def client_closed(self, client: Jsonrpc.Client, client_port: int):
        if client_port in self.port_to_client:
            self.port_to_client[client_port].close_async(None, None)
            del self.port_to_client[client_port]
            self.decr_connection_count()


def service_main():

    app = ServiceApplication(
        application_id='com.p1security.diagngd',
        flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
    )
    app.add_main_option(
        long_name='service',
        short_name=0,
        flags=GLib.OptionFlags.NONE,
        arg=GLib.OptionArg.NONE,
        description='',
        arg_description=None,
    )
    app.add_main_option(
        long_name='client-port',
        short_name=0,
        flags=GLib.OptionFlags.NONE,
        arg=GLib.OptionArg.INT,
        description='',
        arg_description=None,
    )
    app.run(sys.argv)

    # TODO use https://lazka.github.io/pgi-docs/Jsonrpc-1.0/index.html +
    # https://docs.gtk.org/glib/spawn.html /
    # https://lazka.github.io/pgi-docs/GLib-2.0/functions.html#GLib.spawn_async_with_pipes
    # in order to handle subprocess communication?

    # TODO build app with a different DBus service name
    # than the primary process
    # self.app = Gio.Application.new(
    #     'com.p1security.diagngd', Gio.ApplicationFlags.IS_SERVICE
    # )

    """
    # TEST (WIP MMR 2026-05-26)

    process = Process()
    process.process_name = 'ModemManager --TEST'
    process.pid = 12349

    serial_device = SerialDevice()
    serial_device.serial_device_path = '/dev/abcdTEST'
    serial_device.process = process
    """

    # TODO: Create diagng.system.serial.device_scanner
    # background task (leveraging UDEV or just use a
    # glob over /dev/tty* with an interval)?

    # TODO: Create diagng.system.psutil.process_scanner
    # background task (leveraging UDEV or just use a
    # glob over /proc/*/fd/{device_fd} with an interval)?

    ## GLib.idle_add(XX)
    ## GLib.timeout_add(XX)
