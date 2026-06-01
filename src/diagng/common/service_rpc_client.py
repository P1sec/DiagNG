#!/usr/bin/env python3
from logging import debug, error, info, critical

import gi

gi.require_version('Jsonrpc', '1.0')
from gi.repository import GLib, Jsonrpc


class ServiceRPCClient(Jsonrpc.Client):
    def __init__(self, io_stream):
        super().__init__(io_stream=io_stream)
        self.connect('handle-call', self.call_handler)
        self.start_listening()

    def call_handler(
        self,
        this: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
    ):
        info(f'Got call "{id}" for "{method}" with params "{params}"')

        if method == 'test_stoc':
            this.reply_async(id, GLib.Variant.new_boolean(True), None)
            return True
