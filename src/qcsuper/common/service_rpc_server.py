#!/usr/bin/env python3
from logging import debug, error, info, critical

import gi

gi.require_version('Jsonrpc', '1.0')
from gi.repository import GLib, Jsonrpc


class ServiceRPCServer(Jsonrpc.Server):
    def __init__(self):
        super().__init__()
        self.add_handler('test', self.test_handler)

    def test_handler(
        self,
        client: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        user_data,
    ):
        info(f'Got call "{id}" for "{method}" with params "{params}"')
