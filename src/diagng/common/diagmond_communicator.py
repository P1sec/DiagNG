#!/usr/bin/env python3

from gi.repository import GObject, GLib, Gio
from typing import List, Dict
from json import dumps, loads
from logging import debug

from diagng.gobject.nusb_device import NusbDevice
from diagng.gobject.udev_rule import UDevRule

#  ⚠️ ⚠️   https://docs.gtk.org/gio/func.bus_watch_name.html
#     => https://lazka.github.io/pgi-docs/Gio-2.0/functions.html#Gio.bus_watch_name
# "You are guaranteed that one of the handlers will be invoked after calling this function"

# https://docs.gtk.org/gio/type_func.DBusProxy.new_for_bus.html


class DiagmondCommunicator(GObject.Object):
    connection: Gio.DBusConnection
    proxy: Gio.DBusProxy
    bus_connected = GObject.Property(type=bool, default=False)

    nusb_device_tree = GObject.Property(type=Gio.ListStore)
    udev_rules_model: Gio.ListStore

    main_app: 'MainApplication'

    def __init__(self, main_app: 'MainApplication'):
        super().__init__()

        self.main_app = main_app
        self.connection = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)

        self.nusb_device_tree = Gio.ListStore.new(NusbDevice)

        self.udev_rules_model = Gio.ListStore()

        XML_TREE = (
            Gio.resources_lookup_data(
                '/com/p1security/diagng/com.p1security.diagmond.xml', 0
            )
            .get_data()
            .decode('utf-8')
        )

        dbus_info = Gio.DBusNodeInfo.new_for_xml(XML_TREE)
        interface_info = dbus_info.lookup_interface('com.p1security.diagmond')
        assert interface_info

        self.proxy = Gio.DBusProxy.new_sync(
            self.connection,
            Gio.DBusProxyFlags.NONE,
            interface_info,
            'com.p1security.diagmond',
            '/com/p1security/diagmond',
            'com.p1security.diagmond',
            None,
        )

        self.proxy.connect('notify::g-name-owner', self.status_changed)
        self.proxy.connect('g-signal::USBDataUpdated', self.usb_data_changed)
        self.proxy.connect(
            'g-signal::TokioSerialDataUpdated', self.tokio_serial_data_changed
        )
        self.proxy.connect(
            'g-signal::UDevRulesUpdated', self.udev_rules_changed
        )
        # NOTIFY ON USBDataUpdated signal triggered
        # (= OR JUST WHEN PROP :USBData CHANGED?)
        self.status_changed()

    def status_changed(self, *args):
        self.bus_connected = bool(self.proxy.get_name_owner())
        if self.bus_connected:
            debug('Diagmond bus available')

            usb_data_raw = self.proxy.get_cached_property('USBData')
            usb_data_pretty = self.proxy.get_cached_property('USBDataPretty')
            if usb_data_raw:
                self.process_usb_data(
                    loads(usb_data_raw.get_string()),
                    loads(usb_data_pretty.get_string()),
                )

            tokio_serial_data_raw = self.proxy.get_cached_property(
                'TokioSerialData'
            )
            if tokio_serial_data_raw:
                self.process_tokio_serial_data(
                    loads(tokio_serial_data_raw.get_string())
                )

            udev_rules_raw = self.proxy.get_cached_property('UDevRules')
            if udev_rules_raw:
                self.process_udev_rules(loads(udev_rules_raw.get_string()))
        else:
            debug('Diagmond bus unavailable')

            # If the connection of Diagmond to the
            # system bus disappeared then this
            # means that devices inhibited
            # using the InhibitDevice call
            # to ModemManager aren't
            # inhibited anymore

            if self.main_app.modem_manager:
                num_items = self.main_app.modem_manager.mm_instance.modems.get_n_items()

                for pos in range(num_items):
                    item = self.main_app.modem_manager.mm_instance.modems.get_item(
                        pos
                    )
                    item.inhibited = False

                if num_items:
                    self.main_app.modem_manager.queue_state_update()

    def usb_data_changed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        self.process_usb_data(loads(parameters[0]), loads(parameters[1]))

    def process_usb_data(self, usb_data: dict, usb_data_pretty: dict):
        if usb_data:
            debug('nusb data updated')

            self.main_app.nusb_debug_data = dumps(usb_data, indent=4)

            if usb_data_pretty:
                with self.nusb_device_tree.freeze_notify():
                    self.nusb_device_tree.remove_all()

                    def visit(store: Gio.ListStore, item: dict[str, object]):
                        obj = NusbDevice()
                        obj.description = item['description']
                        obj.original_json = item['original_json']
                        obj.children = Gio.ListStore()

                        for child in item['children']:
                            visit(obj.children, child)

                        obj.is_empty = not bool(len(obj.children))

                        store.append(obj)

                    for item in usb_data_pretty['devices']:
                        visit(self.nusb_device_tree, item)

    def tokio_serial_data_changed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        self.process_tokio_serial_data(loads(parameters[0]))

    def process_tokio_serial_data(self, tokio_serial_data: dict):
        if tokio_serial_data:
            debug('tokio-serial data updated')

            self.main_app.tokio_serial_debug_data = dumps(
                tokio_serial_data, indent=4
            )

    def udev_rules_changed(
        self,
        dbus_proxy: Gio.DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ):
        self.process_udev_rules(loads(parameters[0]))

    def process_udev_rules(self, udev_rules: List[Dict[str, str]]):
        with self.udev_rules_model.freeze_notify():
            self.udev_rules_model.remove_all()

            for udev_rule_dict in udev_rules:
                udev_rule_obj = UDevRule()
                udev_rule_obj.rule_file_name = udev_rule_dict['rule_file_name']
                udev_rule_obj.rule_text = udev_rule_dict['rule_text']
                self.udev_rules_model.append(udev_rule_obj)
