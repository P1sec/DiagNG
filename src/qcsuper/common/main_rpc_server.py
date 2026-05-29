#!/usr/bin/env python3
from logging import debug, error, info, critical

import gi

gi.require_version('Jsonrpc', '1.0')
from gi.repository import GLib, Gio, Jsonrpc


class MainRPCServer(Jsonrpc.Server):
    service_rpc: Jsonrpc.Client

    def __init__(self):
        super().__init__()
        self.add_handler('connect_back', self.connect_back_handler)

    def connect_back_handler(
        self,
        server: Jsonrpc.Server,
        client: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        info(f'Got call "{id}" for "{method}" with params "{params}"')

        child_port = params.get_int64()

        # Back-connect to the RPC server of the child
        socket = Gio.SocketClient.new()
        socket.connect_async(
            Gio.InetSocketAddress.new(
                Gio.InetAddress.new_loopback(Gio.SocketFamily.IPV4),
                child_port,
            ),
            None,
            self.connected_to_child,
            child_port,
        )

        client.reply_async(id, GLib.Variant.new_boolean(True), None)

    def connected_to_child(
        self,
        socket: Gio.SocketClient,
        result: Gio.AsyncResult,
        client_port: int,
    ):
        client: Gio.TcpConnection = socket.connect_finish(result)
        if not client:
            critical('Connection to child socket failed')
            return

        self.service_rpc = Jsonrpc.Client.new(client)

        info(f'Back-connected to child socket at port {client_port}')
