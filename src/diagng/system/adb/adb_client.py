#!/usr/bin/env python3
from diagng.gobject.adb_device import ADBDevice

from logging import error, warning, debug, info
from socket import SOL_SOCKET, IPPROTO_TCP
from typing import Callable, Optional
from traceback import format_exc
from enum import IntEnum
from shutil import which
from io import SEEK_END
from time import time
from os import getenv
import socket

import gi

gi.require_version('Adw', '1')

from gi.repository import GObject, Gio, GLib, Adw

SO_KEEPALIVE = getattr(socket, 'SO_KEEPALIVE', None)
TCP_KEEPIDLE = getattr(socket, 'TCP_KEEPIDLE', None)
TCP_KEEPALIVE = getattr(socket, 'TCP_KEEPALIVE', None)
TCP_KEEPINTVL = getattr(socket, 'TCP_KEEPINTVL', None)
TCP_KEEPCNT = getattr(socket, 'TCP_KEEPCNT', None)

# We use our own implementation of the ADB server protocol
# in order to integrate smoothly with the GLib event loop

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


class ConnectionState(IntEnum):
    Unstarted = 1
    ClosedServerNotInstalled = 2
    ClosedServerUnreachable = 3
    Connected = 4
    ClosedBufferUnderrun = 5
    ClosedWriteFailed = 6
    ClosedNormal = 7


class ADBResponse:
    pass


class ADBOkayResponse(ADBResponse):
    def __repr__(self):
        return 'ADBOkayResponse()'


class ADBFailResponse(ADBResponse):
    reason: bytes

    def __repr__(self):
        return 'ADBFailResponse(reason=%r)' % self.reason


class ADBConnectionClosed(ADBResponse):
    def __repr__(self):
        return 'ADBConnectionClosed()'


class ADBClient(GObject.Object):
    __gtype_name__ = 'ADBClient'

    @GObject.Signal(arg_types=(object,))
    def response_received(self, resp: ADBResponse):
        self.resp_buffer.append(resp)
        if self.response_handler is not None:
            callback = self.response_handler
            self.response_handler = None
            callback(resp)

    @GObject.Signal(arg_types=(object,))
    def payload_received(self, new_chunk: bytes):
        pass

    @GObject.Signal
    def closed(self):
        self.response_received.emit(ADBConnectionClosed())

    @GObject.Signal
    def connected(self):
        pass

    state = GObject.Property(type=int, default=ConnectionState.Unstarted)
    device = GObject.Property(type=ADBDevice)
    streaming_mode = GObject.Property(type=bool, default=False)

    response_handler: Optional[int]
    sock_buffer: bytes
    resp_buffer: list[ADBResponse]
    content_buffer: bytes

    adb_address: Gio.InetSocketAddress
    raw_socket: Gio.Socket
    tcp_conn: Gio.TcpConnection
    socket_reader: Gio.InputStream
    socket_writer: Gio.OutputStream

    def __init__(self):
        super().__init__()

        self.response_handler = None
        self.sock_buffer = b''
        self.resp_buffer = []
        self.content_buffer = b''

    def connect_server(self):
        # NOTE: To be called only once,
        # just after the signals are
        # set up

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
                self.state = ConnectionState.ClosedServerUnreachable
                self.closed.emit()
        else:
            self.socket_reader = self.tcp_conn.get_input_stream()
            self.socket_writer = self.tcp_conn.get_output_stream()

            self.socket_reader.read_bytes_async(
                4096, GLib.PRIORITY_DEFAULT, None, self.on_read
            )

            info('Connected to ADB socket')
            self.state = ConnectionState.Connected
            self.connected.emit()

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
        self.state = ConnectionState.ClosedServerNotInstalled
        self.closed.emit()

    def spawn_daemon(self, use_flatpak=False):

        # ⚠️ TODO: Eventually use bundled ADB binary?

        def on_adb_result(obj: Gio.Subprocess, res: Gio.AsyncResult):
            try:
                obj.wait_check_finish(res)
            except Exception:
                self.failed.emit()
                raise

            info('ADB server started successfully on localhost:5037')

            self.reconnect(True)

        info('ADB not running, starting server...')

        Gio.Subprocess.new(
            ([] if not use_flatpak else ['flatpak-spawn', '--host'])
            + ['adb', 'start-server'],
            Gio.SubprocessFlags.SEARCH_PATH_FROM_ENVP,
        ).wait_check_async(None, on_adb_result)

    def send_cmd(
        self, cmd: str, callback: Optional[Callable[[ADBResponse], []]] = None
    ):
        def on_write(obj: Gio.OutputStream, res: Gio.AsyncResult):
            try:
                obj.write_all_finish(res)
            except Exception:
                error('Could not send ADB command: ' + format_exc())
                self.state = ConnectionState.ClosedWriteFailed
                self.closed.emit()

        raw_cmd = cmd.encode('utf-8')
        payload = b'%04x' % len(raw_cmd) + raw_cmd

        info('Writing to ADB socket: %r' % payload)

        if callback:
            self.response_handler = callback
        self.socket_writer.clear_pending()
        self.socket_writer.write_all_async(
            payload, GLib.PRIORITY_DEFAULT, None, on_write
        )

    def send_sync_chunk(
        self,
        chunk: bytes,
        callback: Optional[Callable[[ADBResponse], []]] = None,
    ):
        def on_write(obj: Gio.OutputStream, res: Gio.AsyncResult):
            try:
                obj.write_all_finish(res)
            except Exception:
                error('Could not send ADB command: ' + format_exc())
                self.state = ConnectionState.ClosedWriteFailed
                self.closed.emit()

        info('Writing to ADB socket: %r' % chunk)

        if callback:
            self.response_handler = callback
        self.socket_writer.clear_pending()
        self.socket_writer.write_all_async(
            chunk, GLib.PRIORITY_DEFAULT, None, on_write
        )

    def version(self, callback=None):
        self.send_cmd('host:version', callback)

    def adbd_root(self, callback=None):
        def callback_2(resp: ADBResponse):
            self.streaming_mode = True
            if callback:
                callback(resp)

        self.send_cmd('root:', callback_2)

    def track_devices(self, callback=None):
        # track-devices-l is available since 2017:
        # https://cs.android.com/android/_/android/platform/packages/modules/adb/+/3212463a692c359e7dc10c788c49b5406f3c25bb
        # = Version bump 39->40 (https://cs.android.com/android/_/android/platform/packages/modules/adb/+/ee7b44d91c809f64cbabc4ced8c05360991c29b2)

        self.send_cmd('host:track-devices-l', callback)

    def set_device(self, device: ADBDevice, callback=None):
        self.device = device
        self.send_cmd(f'host:transport:{device.serial_str}', callback)

    def shell_run(self, command: str, callback=None):
        # ----->  SET ⚠️ checked_exec_out + prefer_exec_out if not set
        # For this, launch a secondary client for testing purposes
        # before actually launch the requested command

        can_use_exec_out = True
        if self.device:
            if not self.device.checked_exec_out:
                self.device.prefer_exec_out = False
                client_2 = ADBClient()

                def on_connect(*args):
                    def callback_2(resp: ADBResponse):
                        if isinstance(resp, ADBOkayResponse):

                            def callback_3(resp: ADBResponse):
                                client_2.streaming_mode = True
                                if isinstance(resp, ADBOkayResponse):
                                    self.device.prefer_exec_out = True
                                client_2.raw_socket.close()

                            client_2.send_cmd('exec:id', callback_3)

                        else:
                            client_2.raw_socket.close()

                    client_2.set_device(self.device, callback_2)

                def on_close(*args):
                    self.device.checked_exec_out = True
                    self.shell_run(command, callback)

                client_2.connected.connect(on_connect)
                client_2.closed.connect(on_close)
                client_2.connect_server()
                return

            else:
                can_use_exec_out = self.device.prefer_exec_out

        def callback_4(resp: ADBResponse):
            self.streaming_mode = True
            if callback:
                callback(resp)

        self.send_cmd(
            ('exec' if can_use_exec_out else 'shell') + ':' + command,
            callback_4,
        )

    def install_package(
        self,
        apk_bytes: bytes,
        callback=None,
    ):
        def on_sync_enter(resp: ADBResponse):
            if not isinstance(resp, ADBOkayResponse):
                if callback:
                    callback(resp)
                self.raw_socket.close()
                return

            def on_file_written(resp: ADBResponse):

                if callback:
                    callback(resp)
                self.raw_socket.close()

            self.streaming_mode = True
            self.send_sync_chunk(apk_bytes, on_file_written)

        file_len = len(apk_bytes)

        # See https://android.googlesource.com/platform/frameworks/base/+/master/services/core/java/com/android/server/pm/PackageManagerShellCommand.java#3421
        # for arguments list

        self.send_cmd(
            'abb_exec:'
            + '\x00'.join(
                ['package', 'install', '-r', '-S', '%09d' % file_len]
            ),
            on_sync_enter,
        )

    def push(
        self,
        local_file: str,
        remote_file: str,
        is_executable: bool = False,
        callback=None,
    ):
        def on_sync_enter(resp: ADBResponse):
            if not isinstance(resp, ADBOkayResponse):
                if callback:
                    callback(resp)
                self.raw_socket.close()
                return

            write_buffer = b''

            send_payload = (
                remote_file
                + ','
                + str(0o100775 if is_executable else 0o100664)
            )
            send_payload = send_payload.encode('utf-8')
            write_buffer += (
                b'SEND'
                + len(send_payload).to_bytes(4, 'little')
                + send_payload
            )

            with open(local_file, 'rb') as fd:
                while True:
                    data_payload = fd.read(64000)
                    if not data_payload:
                        break
                    write_buffer += (
                        b'DATA'
                        + len(data_payload).to_bytes(4, 'little')
                        + data_payload
                    )

            write_buffer += b'DONE' + int(time()).to_bytes(4, 'little')

            def on_file_written(resp: ADBResponse):

                self.streaming_mode = True
                self.send_sync_chunk(b'QUIT\0\0\0\0')
                if callback:
                    callback(resp)
                self.raw_socket.close()

            self.send_sync_chunk(write_buffer, on_file_written)

        self.send_cmd('sync:', on_sync_enter)

        pass  # TODO

    def on_read(self, obj: Gio.InputStream, res: Gio.AsyncResult):

        try:
            data: bytes = self.socket_reader.read_bytes_finish(res).get_data()
        except Exception as err:
            info('ADB connection closed: ' + repr(err))
            self.state = (
                ConnectionState.ClosedBufferUnderrun
                if self.sock_buffer
                else ConnectionState.ClosedNormal
            )
            self.closed.emit()
            return
        else:
            if not data:
                info('ADB connection closed')
                self.state = (
                    ConnectionState.ClosedBufferUnderrun
                    if self.sock_buffer
                    else ConnectionState.ClosedNormal
                )
                self.closed.emit()
                return

        self.sock_buffer += data

        debug('Read bytes from ADB socket: %r' % data)

        while len(self.sock_buffer) >= 4:
            marker = self.sock_buffer[:4]

            if self.streaming_mode:
                self.content_buffer += self.sock_buffer
                self.payload_received.emit(self.sock_buffer)
                self.sock_buffer = b''

            elif marker == b'OKAY':
                self.sock_buffer = self.sock_buffer[4:]
                resp = ADBOkayResponse()
                self.response_received.emit(resp)

            elif marker == b'FAIL':
                if len(self.sock_buffer) < 8:
                    break
                size = int(self.sock_buffer[4:8], 16)
                if len(self.sock_buffer) < size + 8:
                    break
                fail_reason = self.sock_buffer[8 : size + 8]
                self.sock_buffer = self.sock_buffer[size + 8 :]
                resp = ADBFailResponse()
                resp.reason = fail_reason
                self.response_received.emit(resp)

            else:
                size = int(marker, 16)
                if len(self.sock_buffer) < size + 4:
                    break
                payload = self.sock_buffer[4 : size + 4]
                self.sock_buffer = self.sock_buffer[size + 4 :]
                self.content_buffer += payload
                self.payload_received.emit(payload)

        self.socket_reader.read_bytes_async(
            4096, GLib.PRIORITY_DEFAULT, None, self.on_read
        )
