#!/usr/bin/env python3

from gi.repository import GObject, Gio, GLib
from typing import Union
from queue import Queue
from enum import Enum

# WIP 2026-07-11

# ➡️ Write a GLib-based async callback-based wrapper
# over the adb_client module for sending commands
# from modules easily


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


class ADBProxy(GObject.Object):
    queue: Queue[ADBQueueItem]

    def __init__(self, queue: Queue[ADBQueueItem]):
        super().__init__()

        self.queue = queue

        # TODO

    def shell(self, *args):
        pass  # TODO

    def push(self, *args):
        pass  # TODO
