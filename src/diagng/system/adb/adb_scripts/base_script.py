#!/usr/bin/env python3

from diagng.system.adb.adb_client import (
    ADBClient,
    ConnectionState,
    ADBOkayResponse,
    ADBResponse,
)
from diagng.gobject.adb_device import ADBDevice

from logging import info, error, warning
from gi.repository import GObject, GLib
from abc import abstractmethod
from enum import IntEnum

# TODO: This abstract/base class should
# abstract connecting to the ADB daemon
# through the ADBClient class (ONCE OR MORE) +
# sending the "host:transport:${self.device.serial_str}"
# command each time before sending other commands
# on the TCP stream +
# HOLDING A STATE MACHINE (UNSTARTED, PROGRESS, SUCCESS,
# FAILED) + POSSIBLE TEXT RETURN_INFO


class ScriptState(IntEnum):
    Unstarted = 1
    Processing = 2
    Failed = 3
    Success = 4


class BaseScript(GObject.Object):
    __gtype_name__ = 'BaseScript'

    device = GObject.Property(type=ADBDevice)
    client = GObject.Property(type=ADBClient)
    state = GObject.Property(type=int, default=ScriptState.Unstarted)
    text_output = GObject.Property(type=str)

    @GObject.Signal
    def finished(self):
        pass

    def __init__(self, device):
        super().__init__()

        self.device = device

        pass  # WIP

    def launch(self):
        self.client = ADBClient()

        self.client.connected.connect(self.on_connect)
        self.client.closed.connect(self.on_close)
        self.state = ScriptState.Processing
        self.client.connect_server()

        # If called from a timer, don't repeat
        return GLib.SOURCE_REMOVE

    def on_connect(self, *args):
        def on_device_set(resp: ADBResponse):
            if isinstance(resp, ADBOkayResponse):
                info('Device set to %r in script %r' % (self.device, self))
            else:
                error('Could not set device in ADB client session: %r' % resp)
                self.state = ScriptState.Failed

            self.launch_script_for_device()

        self.client.set_device(self.device, on_device_set)

    def on_close(self, *args):
        if (
            self.client.state != ConnectionState.ClosedNormal
            or self.client.response_handler
        ):
            warning(
                'Connection closed, reason: %r'
                % ConnectionState(self.client.state)
            )
            self.state = ScriptState.Failed

    @abstractmethod
    def launch_script_for_device(self):
        pass
