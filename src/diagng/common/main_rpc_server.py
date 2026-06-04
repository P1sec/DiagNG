#!/usr/bin/env python3
from logging import debug, error, info, critical
from json import loads

from diagng.gobject.mm_instance import ModemManagerInstance

import gi

gi.require_version('Jsonrpc', '1.0')
gi.require_version('Json', '1.0')
from gi.repository import GLib, Gio, Jsonrpc, Json


class MainRPCServer(Jsonrpc.Server):
    service_rpc: Jsonrpc.Client
    app: 'MainApplication'

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.add_handler('sync_modem_status', self.sync_modem_status_handler)
        self.add_handler(
            'sync_modem_debug_info', self.sync_modem_debug_info_handler
        )
        self.add_handler('sync_udev_info', self.sync_udev_info_handler)
        self.add_handler('test_ctos', self.test_ctos_handler)

        self.connect('client-accepted', self.daemon_connected)

    def daemon_connected(self, this: Jsonrpc.Server, peer: Jsonrpc.Client):
        self.service_rpc = peer

    def sync_modem_status_handler(
        self,
        this: Jsonrpc.Server,
        peer: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        info(f'Got call "{id}" for "{method}" with params "{params}"')

        self.app.mm_instance.update(params)

        peer.reply_async(id, GLib.Variant.new_boolean(True), None)

    def sync_modem_debug_info_handler(
        self,
        this: Jsonrpc.Server,
        peer: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        raw_json = Json.to_string(Json.gvariant_serialize(params), True)

        info(f'Got call "{id}" for "{method}"')

        self.app.mm_debug_data = raw_json

        peer.reply_async(id, GLib.Variant.new_boolean(True), None)

    def sync_udev_info_handler(
        self,
        this: Jsonrpc.Server,
        peer: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        # raw_json = Json.to_string(Json.gvariant_serialize(params), True)

        info(f'Got call "{id}" for "{method}"')

        # self.app.udev_debug_data = raw_json

        peer.reply_async(id, GLib.Variant.new_boolean(True), None)

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

        info('Sent "test_stoc" call to child')
