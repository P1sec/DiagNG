#!/usr/bin/env python3

from gi.repository import GObject, Gio
from logging import debug, info
from typing import Optional

# ⚠️ TODO Move to a subclass of `DBusObjectManagerClient`
# as we will need to ⚠️ enumerate and watch for ⚠️
# SerialDevice objects with DBusObjectManagerClient.
# get_objects(), etc.?
# Cf. https://docs.gtk.org/gio/class.DBusObjectManagerClient.html
# + ➡️ https://lazka.github.io/pgi-docs/Gio-2.0/interfaces/DBusObjectManager.html


class DiagmondSerialDeviceOM(GObject.Object):
    om: Gio.DBusObjectManagerClient
    connection: Gio.DBusConnection
    interface_info: Gio.DBusInterfaceInfo

    def __init__(self, connection: Gio.DBusConnection):
        super().__init__()

        self.connection = connection

        XML_TREE = (
            Gio.resources_lookup_data(
                '/com/p1security/diagng/com.p1security.diagmond.SerialDevice.xml',
                0,
            )
            .get_data()
            .decode('utf-8')
        )

        dbus_info = Gio.DBusNodeInfo.new_for_xml(XML_TREE)
        self.interface_info = dbus_info.lookup_interface(
            'com.p1security.diagmond.SerialDevice'
        )
        assert self.interface_info

        Gio.DBusObjectManagerClient.new(
            self.connection,
            Gio.DBusObjectManagerClientFlags.DO_NOT_AUTO_START,
            'com.p1security.diagmond',
            '/com/p1security/diagmond/SerialDevices',
            None,  # self.get_proxy_type,
            None,
            None,
            self.om_ready,
            None,
        )

    def get_proxy_type(
        self,
        manager: Gio.DBusObjectManagerClient,
        object_path: str,
        interface_name: Optional[str],
        data: Optional[object],
    ) -> GObject.GType:
        debug(
            'Received get_proxy_type_func call for '
            + f'path={object_path} interface={interface_name}'
        )

        if interface_name:
            return Gio.DBusProxy
        else:
            return Gio.DBusObjectProxy

    def process_objects(self):
        for obj in self.om.get_objects():
            debug('Found dangling SerialDevice object at startup: %r' % obj)

            obj_path = obj.get_object_path()

            proxy = Gio.DBusProxy.new_sync(
                self.connection,
                Gio.DBusProxyFlags.NONE,
                self.interface_info,
                'com.p1security.diagmond',
                obj_path,
                'com.p1security.diagmond.SerialDevice',
                None,
            )

            def port_closed(proxy, result, obj_path):
                if isinstance(result, Exception):
                    raise result
                else:
                    info('Dangling %s port closed successfully' % obj_path)

            proxy.Close(
                '()',
                result_handler=port_closed,
                user_data=obj_path,
            )

    def on_object_added(self, om: Gio.DBusObjectManager, obj: Gio.DBusObject):
        debug('SerialDevice object added: %r' % obj)

    def on_object_removed(
        self, om: Gio.DBusObjectManager, obj: Gio.DBusObject
    ):
        debug('SerialDevice object removed: %r' % obj)

    def on_interface_added(
        self,
        om: Gio.DBusObjectManager,
        obj: Gio.DBusObject,
        intf: Gio.DBusInterface,
    ):
        # Never called?
        debug('SerialDevice interface added: %r->%r' % (obj, intf))

    def on_interface_removed(
        self,
        om: Gio.DBusObjectManager,
        obj: Gio.DBusObject,
        intf: Gio.DBusInterface,
    ):
        # Never called?
        debug('SerialDevice interface removed: %r->%r' % (obj, intf))

    def om_ready(
        self,
        source_object: Optional[GObject.Object],
        result: Gio.AsyncResult,
        data: Optional[object],
    ):
        self.om = Gio.DBusObjectManagerClient.new_finish(result)

        self.om.connect('object-added', self.on_object_added)
        self.om.connect('object-removed', self.on_object_removed)
        self.om.connect('interface-added', self.on_interface_added)
        self.om.connect('interface-removed', self.on_interface_removed)

        self.process_objects()
