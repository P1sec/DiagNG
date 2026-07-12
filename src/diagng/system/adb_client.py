#!/usr/bin/env python3
# from diagng.system.adb_proxy import ADBProxy, ADBQueueItem, ADBQueueItemType
from diagng.gobject.adb_device import ADBDevice

# from adbutils import AdbClient, AdbDeviceInfo
from socket import SOL_SOCKET, IPPROTO_TCP
from logging import error, warning, info
from traceback import format_exc
from shutil import which
from os import getenv
import socket
# from queue import Queue, Empty
# from threading import Thread

import gi

gi.require_version('Adw', '1')

from gi.repository import GObject, Gio, GLib, Adw

SO_KEEPALIVE = getattr(socket, 'SO_KEEPALIVE', None)
TCP_KEEPIDLE = getattr(socket, 'TCP_KEEPIDLE', None)
TCP_KEEPALIVE = getattr(socket, 'TCP_KEEPALIVE', None)
TCP_KEEPINTVL = getattr(socket, 'TCP_KEEPINTVL', None)
TCP_KEEPCNT = getattr(socket, 'TCP_KEEPCNT', None)

# TODO: Use own impl?
# https://cs.android.com/android/platform/superproject/main/+/main:packages/modules/adb/docs/dev/services.md
# strace -s999999 adb exec-out "id ; sleep 2 ; id"
# strace -s999999 adb devices -l
# id > /tmp/id; strace -s999999 adb push /tmp/id /data/local/tmp/id
# https://cs.android.com/android/platform/superproject/main/+/main:packages/modules/adb/docs/dev/sync.md
# ⚠️ https://lazka.github.io/pgi-docs/Gio-2.0/classes/Socket.html#Gio.Socket.set_option
# => https://lazka.github.io/pgi-docs/Gio-2.0/classes/TcpConnection.html#Gio.TcpConnection
# https://lazka.github.io/pgi-docs/Gio-2.0/classes/SocketClient.html
# https://man7.org/linux/man-pages/man1/flatpak-spawn.1.html
# ⚠️ ⚠️ ⚠️ => Improve global app logging?
# ⚠️ ⚠️ => Découpler les classes GObject de la partie GUI, utiliser des signaux à la place?

# ⚠️ https://cs.android.com/android/platform/superproject/+/android-latest-release:packages/modules/adb/sysdeps_unix.cpp;l=24?q=TCP_KEEPCNT%20adb


class ADBClient(GObject.Object):
    __gtype_name__ = 'ADBClient'

    adb_address: Gio.InetSocketAddress
    raw_socket: Gio.Socket
    tcp_conn: Gio.TcpConnection
    socket_reader: Gio.InputStream
    socket_writer: Gio.OutputStream
    # queue: Queue[ADBQueueItem]
    # proxy: ADBProxy

    def __init__(self):
        super().__init__()

        self.reconnect()

    def reconnect(self, is_retry: bool = False):
        # ⚠️ TODO CLOSE STALE CONNECTIONS HERE?

        self.adb_address = Gio.InetSocketAddress.new_from_string(
            '127.0.0.1', 5037
        )

        self.raw_socket = Gio.Socket.new(
            Gio.SocketFamily.IPV4,
            Gio.SocketType.STREAM,
            Gio.SocketProtocol.TCP,
        )

        self.tcp_conn = self.raw_socket.connection_factory_create_connection()

        assert self.tcp_conn.get_socket() == self.raw_socket

        interval, num_tries = 1, 10  # Original ADB client values
        # interval, num_tries = 10, 3 # adbutils values

        try:
            self.try_enable_keepalive(interval, num_tries)
        except Exception:
            warning(
                'Could not enable TCP keepalive on socket: ' + format_exc()
            )

        self.raw_socket.set_timeout(3)
        self.tcp_conn.connect_async(
            self.adb_address, None, self.on_connect, is_retry
        )

    """
        Based on:
        https://cs.android.com/android/platform/superproject/+/aml_adb_331113120:packages/modules/adb/sysdeps_unix.cpp

        @returns Whether the TCP keepalive was successfully set
          on the passed socket
    """

    def try_enable_keepalive(self, interval: int, num_tries: int) -> bool:
        # Enable keepalive
        if not SO_KEEPALIVE:
            raise ValueError('SO_KEEPALIVE unavailable')
        self.raw_socket.set_option(SOL_SOCKET, SO_KEEPALIVE, 1)

        # Set idle time before sending the first keep-alive
        if TCP_KEEPIDLE:
            self.raw_socket.set_option(IPPROTO_TCP, TCP_KEEPIDLE, interval)
        elif TCP_KEEPALIVE:
            self.raw_socket.set_option(IPPROTO_TCP, TCP_KEEPALIVE, interval)

        # Set keepalive interval
        if TCP_KEEPINTVL:
            self.raw_socket.set_option(IPPROTO_TCP, TCP_KEEPINTVL, interval)

        # Set number of keepalives before timeout
        if TCP_KEEPCNT:
            self.raw_socket.set_option(IPPROTO_TCP, TCP_KEEPCNT, num_tries)

    def on_connect(
        self, obj: Gio.SocketClient, res: Gio.AsyncResult, is_retry: bool
    ):
        self.raw_socket.set_timeout(0)
        try:
            assert self.tcp_conn.connect_finish(res)
        except Exception:
            if not is_retry:
                self.daemon_launch_path()
            else:
                error('Could not connect to ADB: ' + format_exc())
            return
        self.socket_reader = self.tcp_conn.get_input_stream()
        self.socket_writer = self.tcp_conn.get_output_stream()

        self.socket_reader.read_bytes_async(
            4096, GLib.PRIORITY_DEFAULT, None, self.on_read
        )

        print('ℹ️ CONNECT TO ADB OK')

    def daemon_launch_path(self):
        # Do we need to go through a Flatpak portal?

        if which('adb'):
            self.spawn_daemon(False)

        elif getenv('container') and which('flatpak-spawn'):

            def on_which_result(obj: Gio.Subprocess, res: Gio.AsyncResult):
                try:
                    assert obj.wait_check_finish(res)
                except Exception:
                    self.daemon_unavailable()
                else:
                    self.spawn_daemon(True)

            Gio.Subprocess.new(
                ['flatpak-spawn', '--host', 'which', 'adb'],
                Gio.SubprocessFlags.STDOUT_PIPE,
            ).wait_check_async(None, on_which_result)

        else:
            self.daemon_unavailable()

    def daemon_unavailable(self):
        error('ADB not available on this sytem')
        error(
            '⚠️ TODO: Communicate back to the main UI (display a warning signalling through a GObject property, etc.)'
        )

    def spawn_daemon(self, use_flatpak=False):

        # ⚠️ Use bundled ADB daemon when available

        def on_adb_result(obj: Gio.Subprocess, res: Gio.AsyncResult):
            obj.wait_check_finish(res)

            info('ADB server started successfully on localhost:5037')

            self.reconnect(True)

        info('ADB not running, starting server...')

        Gio.Subprocess.new(
            ([] if not use_flatpak else ['flatpak-spawn', '--host'])
            + ['adb', 'start-server'],
            Gio.SubprocessFlags.SEARCH_PATH_FROM_ENVP,
        ).wait_check_async(None, on_adb_result)

    def shell(self, *args):
        pass  # TODO

    def push(self, *args):
        pass  # TODO

    def on_read(self, obj: Gio.InputStream, res: Gio.AsyncResult):

        try:
            data: bytes = self.socket_reader.read_bytes_finish(res).get_data()
            assert data
        except Exception:
            error('ADB connection closed: ' + format_exc())
            # TODO ⚠️ EMIT SIGNAL / call user callback?
            self.on_close()

        print('⚠️ ⚠️ TODO ADB SOCKET WAS READ FROM =>', data)

        self.socket_reader.read_bytes_async(
            4096, GLib.PRIORITY_DEFAULT, None, self.on_read
        )

    def on_close(self):

        print('⚠️ ⚠️ TODO ADB SOCKET WAS CLOSED, EMIT EVENT')

    """
        self.queue = Queue()

        self.proxy = ADBProxy(self.queue)

        thread = Thread(target=self.device_list_poll_thread)
        thread.daemon = True
        thread.start()

    def propagate_error(self, error_str):

        def main_thread_cb(error_str):
            error('Error in the ADB thread: ' + error_str)

            dialog = Adw.AlertDialog.new(
                '⚠️ Error in the ADB thread', repr(error_str)
            )
            dialog.add_response('ok', 'Ok')
            dialog.choose(self.main_window, None, None)

        GLib.idle_add(main_thread_cb, error_str)

    def process_device_list(self, devices: list[AdbDeviceInfo]):
        with self.main_window.adb_devices.freeze_notify():
            self.main_window.adb_devices.remove_all()

            for device in devices:
                # print('=====> WIP ⚠️ PROCESS', device)

                obj = ADBDevice()
                obj.serial_str = device.serial
                obj.transport_id = device.tags.get('transport_id')
                obj.model_name = device.tags.get('model') or device.serial
                obj.state = device.state

                summary = 'State: %s' % obj.state.title()

                summary += ' | ' + ', '.join(
                    '%s=%s' % (key, value)
                    for key, value in device.tags.items()
                )

                # obj.usb_device = XX
                obj.text_summary = summary.strip(' |')
                self.main_window.adb_devices.append(obj)

    def device_list_poll_thread(self):

        # TODO: Eventually allow to
        # customize the connection target
        # from the man UI (e.g use TCP, etc.)
        try:
            info('Trying to connect to ADB client...')
            client = AdbClient()
            info('Connection to ADB client established')

            # TODO: Use some kind of message queue
            # in order to read commands from the
            # main thread instead of polling
            # the device whenever some
            # order gets received here?
            #
            # (with a 2 sec. timeout to keep
            # polling the devices list still?)

            WAIT_TIMEOUT = 2

            while True:
                try:
                    GLib.idle_add(
                        self.process_device_list,
                        list(client.list(extended=True)),
                    )

                except Exception:
                    self.propagate_error(format_exc())

                try:
                    queue_item: ADBQueueItem = self.queue.get(
                        True, WAIT_TIMEOUT
                    )
                except Empty:
                    pass
                else:
                    if (
                        queue_item.item_type
                        == ADBQueueItemType.SwitchXiaomiDiag
                    ):
                        pass  # TODO process queue_item

                # next(client.track_devices(), None)

        except Exception:
            self.propagate_error(format_exc())

        # WIP: See https://github.com/openatx/adbutils#connect-adb-server
    """
