#!/usr/bin/env python3
from logging import debug, error, info, critical

import gi

gi.require_version('Jsonrpc', '1.0')
from gi.repository import GLib, Gio, Jsonrpc


class MainRPCServer(Jsonrpc.Server):
    service_rpc: Jsonrpc.Client

    def __init__(self):
        super().__init__()
        self.add_handler('test_ctos', self.test_ctos_handler)

    def test_ctos_handler(
        self,
        this: Jsonrpc.Server,
        peer: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        info(f'Got call "{id}" for "{method}" with params "{params}"')

        peer.reply_async(id, GLib.Variant.new_boolean(True), None)

        peer.call_async(
            'test_stoc',
            GLib.Variant.new_int64(42),
            None,
            None,
        )
