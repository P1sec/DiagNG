#!/usr/bin/env python3
from diagng.gobject.adb_device import ADBDevice

from adbutils import AdbClient, AdbDeviceInfo
from traceback import format_exc
from logging import error, info
from queue import Queue, Empty
from threading import Thread
from typing import Union
from time import sleep
from enum import Enum

import gi

gi.require_version('Adw', '1')

from gi.repository import GObject, Gio, GLib, Adw


class ADBQueueItemType(Enum):
    TryRoot = 1
    SwitchXiaomiDiag = 2
    SamsungQCDialCode = 3
    OneplusQCDialCode = 4


class ADBQueueItem:
    item_type: ADBQueueItemType
    item: Union[None]

    def __init__(self, item_type, item=None):
        self.item_type = item_type
        self.item = item


class ADBClient(GObject.Object):
    __gtype_name__ = 'ADBClient'

    main_window: 'ApplicationWindow'
    queue: Queue[ADBQueueItem]

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.queue = Queue()

        thread = Thread(target=self.device_list_poll_thread)
        thread.daemon = True
        thread.start()

    def propagate_error(self, error_str):

        def main_thread_cb(error_str):
            error('Error in the ADB thread: ' + error_str)

            dialog = Adw.AlertDialog.new(
                '⚠️ Error in the ADB thread', repr(error_str)
            )
            dialog.add_response('ok', 'Ok')
            dialog.choose(self.main_window, None, None)

        GLib.idle_add(main_thread_cb, error_str)

    def process_device_list(self, devices: list[AdbDeviceInfo]):
        with self.main_window.adb_devices.freeze_notify():
            self.main_window.adb_devices.remove_all()

            for device in devices:
                # print('=====> WIP ⚠️ PROCESS', device)

                obj = ADBDevice()
                obj.serial_str = device.serial
                obj.transport_id = device.tags.get('transport_id')
                obj.model_name = device.tags.get('model')
                obj.state = device.state

                summary = 'State: %s' % {
                    'offline': 'Offline',
                    'bootloader': 'Bootloader',
                    'device': 'Online',
                }.get(obj.state)

                summary += ' | ' + ', '.join(
                    '%s=%s' % (key, value)
                    for key, value in device.tags.items()
                )

                # obj.usb_device = XX
                obj.text_summary = summary.strip(' |')
                self.main_window.adb_devices.append(obj)

    def device_list_poll_thread(self):

        # TODO: Eventually allow to
        # customize the connection target
        # from the man UI (e.g use TCP, etc.)
        try:
            info('Trying to connect to ADB client...')
            client = AdbClient()
            info('Connection to ADB client established')

            # TODO: Use some kind of message queue
            # in order to read commands from the
            # main thread instead of polling
            # the device whenever some
            # order gets received here?
            #
            # (with a 2 sec. timeout to keep
            # polling the devices list still?)

            WAIT_TIMEOUT = 2

            while True:
                try:
                    queue_item: ADBQueueItem = self.queue.get(
                        True, WAIT_TIMEOUT
                    )
                except Empty:
                    pass
                else:
                    if (
                        queue_item.item_type
                        == ADBQueueItemType.SwitchXiaomiDiag
                    ):
                        pass  # TODO process queue_item

                try:
                    GLib.idle_add(
                        self.process_device_list,
                        list(client.list(extended=True)),
                    )

                except Exception:
                    self.propagate_error(format_exc())

                # next(client.track_devices(), None)

        except Exception:
            self.propagate_error(format_exc())

        # WIP: See https://github.com/openatx/adbutils#connect-adb-server
