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
            'sync_modem_status_detailed',
            self.sync_modem_status_detailed_handler,
        )
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

        obj = Json.gobject_deserialize(
            ModemManagerInstance, Json.gvariant_serialize(params)
        )

        with obj.freeze_notify():
            for prop in ModemManagerInstance.list_properties():
                prop = prop.get_name()

                old_val = self.app.mm_instance.get_property(prop)
                new_val = obj.get_property(prop)

                if old_val != new_val:
                    self.app.mm_instance.set_property(prop, new_val)

        peer.reply_async(id, GLib.Variant.new_boolean(True), None)

    def sync_modem_status_detailed_handler(
        self,
        this: Jsonrpc.Server,
        peer: Jsonrpc.Client,
        method: str,
        id: GLib.Variant,
        params: GLib.Variant,
        *user_data,
    ):
        params = loads(Json.gvariant_serialize_data(params)[0])

        info(f'Got call "{id}" for "{method}" with params "{params}"')

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
