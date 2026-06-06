#!/usr/bin/env python3
from typing import List, Optional
from logging import info, debug

import gi

gi.require_version('GUsb', '1.0')
from gi.repository import GLib, Gio, GUsb

class UsbScanner:
    state_update_pending: bool = False

    rpc_wrapper: 'ServiceApplication'
    json_state: Optional[List[dict]] = None

    def __init__(self, rpc_wrapper: 'ServiceApplication'):
        self.rpc_wrapper = rpc_wrapper

        self.state_update_pending = False

        context = GUsb.Context.new()
        context.enumerate()

        print('TEST', context.get_devices()) # <-- Causes core dump?

        # WIP XX

    def queue_state_update(self):
        pass # TODO

if __name__ == '__main__':
    pass
