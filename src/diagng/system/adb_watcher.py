#!/usr/bin/env python3
from diagng.system.adb_client import ADBClient, ADBResponse

from gi.repository import GObject, Gio
from logging import info, error

# WIP 2026-07-11

# See: https://cs.android.com/android/platform/superproject/main/+/main:/packages/modules/adb/docs/dev/protocol.md
# See: https://cs.android.com/android/platform/superproject/main/+/main:/packages/modules/adb/docs/dev/services.md


class ADBDevice(GObject.Object):
    name = GObject.Property(type=str)
    state = GObject.Property(type=str)
    tags: dict[str, str]

    def __repr__(self):
        return 'ADBDevice(name=%r, state=%r, tags=%r)' % (
            self.name,
            self.state,
            self.tags,
        )


class ADBWatcher(GObject.Object):
    target_host = GObject.Property(type=str)
    version = GObject.Property(type=int)
    is_failed = GObject.Property(type=bool, default=False)
    bad_address = GObject.Property(type=bool, default=False)
    is_connected = GObject.Property(type=bool, default=False)
    devices = GObject.Property(type=Gio.ListStore)

    def __init__(self):
        super().__init__()
        self.target_host = 'localhost:5037'
        self.devices = Gio.ListStore.new(ADBDevice)

        self.try_obtain_version()

    def try_obtain_version(self):
        client = ADBClient()

        def on_conn_error(*args):
            self.is_failed = True
            self.bad_address = client.bad_address
            self.is_connected = False
            error('Could not connect to ADB')

        def on_connect(*args):
            self.is_failed = False
            self.bad_address = False
            self.is_connected = True

            def on_version(resp: ADBResponse):
                info('Response to "host:version" call: %s' % resp)

            client.version(on_version)

        def on_normal_close(*args):
            self.is_connected = False

            if client.content_buffer:
                self.version = int(
                    client.content_buffer.decode('utf-8').strip(), 16
                )
                info('ADB_SERVER_VERSION value received: %d' % self.version)

                self.watch_for_devices()
            else:
                error('Could receive version string')
                self.is_failed = True

        client.failed.connect(on_conn_error)
        client.connected.connect(on_connect)
        client.closed.connect(on_normal_close)

        client.connect_from_host(self.target_host)

    def watch_for_devices(self):
        client = ADBClient()

        def on_conn_error(*args):
            self.is_failed = True
            self.bad_address = client.bad_address
            self.is_connected = False
            error('Could not connect to ADB')

        def on_connect(*args):
            self.is_failed = False
            self.bad_address = False
            self.is_connected = True

            def on_status(resp: ADBResponse):
                info('Response to "host:track-devices-l" call: %r' % resp)

            client.track_devices(on_status)

        def on_payload(client: ADBClient, chunk: bytes):
            info('Async response to "host:track-devices-l" call: %r' % chunk)

            data = chunk.decode('utf-8').strip()
            with self.devices.freeze_notify():
                self.devices.remove_all()
                for line in data.splitlines():
                    fields = line.split()

                    device = ADBDevice()
                    device.name = fields.pop(0)
                    device.state = fields.pop(0)
                    device.tags = {
                        field.split(':', 1)[0]: field.split(':', 1)[1]
                        for field in fields
                    }
                    self.devices.append(device)

                    info('ADB device: %r' % device)

        def on_normal_close(*args):
            self.is_connected = False
            self.is_failed = True

            error('Client watch activity interrupted')

        client.failed.connect(on_conn_error)
        client.connected.connect(on_connect)
        client.payload_received.connect(on_payload)
        client.closed.connect(on_normal_close)

        client.connect_from_host(self.target_host)
