#!/usr/bin/env python3
from diagng.system.adb.adb_client import ADBClient, ADBResponse
from diagng.gobject.adb_device import ADBDevice

from gi.repository import GObject, Gio
from logging import info, error

# See: https://cs.android.com/android/platform/superproject/main/+/main:/packages/modules/adb/docs/dev/protocol.md
# See: https://cs.android.com/android/platform/superproject/main/+/main:/packages/modules/adb/docs/dev/services.md


class ADBWatcher(GObject.Object):
    version = GObject.Property(type=int)

    is_failed = GObject.Property(type=bool, default=False)
    adb_bin_unavailable = GObject.Property(type=bool, default=False)
    is_connected = GObject.Property(type=bool, default=False)
    devices = GObject.Property(type=Gio.ListStore)

    def __init__(self):
        super().__init__()
        self.devices = Gio.ListStore.new(ADBDevice)

        self.try_obtain_version()

    def try_obtain_version(self):
        client = ADBClient()

        def on_conn_error(*args):
            self.is_failed = True
            self.adb_bin_unavailable = client.adb_bin_unavailable
            self.is_connected = False
            error('Could not connect to ADB')

        def on_connect(*args):
            self.is_failed = False
            self.adb_bin_unavailable = False
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

        client.connect_server()

    def watch_for_devices(self):
        client = ADBClient()

        def on_conn_error(*args):
            self.is_failed = True
            self.adb_bin_unavailable = client.adb_bin_unavailable
            self.is_connected = False
            error('Could not connect to ADB')

        def on_connect(*args):
            self.is_failed = False
            self.adb_bin_unavailable = False
            self.is_connected = True

            def on_status(resp: ADBResponse):
                info('Response to "host:track-devices-l" call: %r' % resp)

            client.track_devices(on_status)

        def on_payload(client: ADBClient, chunk: bytes):
            info('Async response to "host:track-devices-l" call: %r' % chunk)

            data = chunk.decode('utf-8').strip()

            known_serial_to_obj: dict[str, ADBDevice] = {}
            up_to_date_serials: set[str] = set()

            for pos in range(self.devices.get_n_items()):
                item = self.devices.get_item(pos)

                known_serial_to_obj[item.serial_str] = item

            for line in data.splitlines():
                fields = line.split()

                device = ADBDevice()
                device.serial_str = fields.pop(0)

                if device.serial_str in known_serial_to_obj:
                    device = known_serial_to_obj[device.serial_str]

                device.state = fields.pop(0)
                device.tags = {
                    field.split(':', 1)[0]: field.split(':', 1)[1]
                    for field in fields
                }
                device.transport_id = device.tags.pop('transport_id', None)
                device.model_name = (
                    device.tags.pop('model', None) or device.serial_str
                )

                summary = 'State: %s' % device.state.title().replace(
                    'Device', 'Online'
                )
                summary += ' | ' + ', '.join(
                    '%s=%s' % (key, value)
                    for key, value in device.tags.items()
                )

                # device.usb_device = XX
                device.text_summary = summary.strip(' |')

                if device.serial_str not in known_serial_to_obj:
                    self.devices.append(device)
                    known_serial_to_obj[device.serial_str] = device

                up_to_date_serials.add(device.serial_str)

                info('ADB device: %r' % device)

            with self.devices.freeze_notify():
                while True:
                    for pos in range(self.devices.get_n_items()):
                        item = self.devices.get_item(pos)

                        if item.serial_str not in up_to_date_serials:
                            self.devices.remove(pos)
                            break
                    else:
                        break

        def on_normal_close(*args):
            self.is_connected = False
            self.is_failed = True

            error('Client watch activity interrupted')

        client.failed.connect(on_conn_error)
        client.connected.connect(on_connect)
        client.payload_received.connect(on_payload)
        client.closed.connect(on_normal_close)

        client.connect_server()
