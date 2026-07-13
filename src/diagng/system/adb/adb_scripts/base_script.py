#!/usr/bin/env python3

from diagng.system.adb.adb_client import ADBClient, ADBResponse
from diagng.gobject.adb_device import ADBDevice

from gi.repository import GObject
from logging import info, error
from enum import Enum

# TODO: This abstract/base class should
# abstract connecting to the ADB daemon
# through the ADBClient class (ONCE OR MORE) +
# sending the "host:transport:${self.device.serial_str}"
# command each time before sending other commands
# on the TCP stream +
# HOLDING A STATE MACHINE (UNSTARTED, PROGRESS, SUCCESS,
# FAILED) + POSSIBLE TEXT RETURN_INFO


class ConnectionState(Enum):
    Unstarted = 'unstarted'
    ConnectionCut = 'connection_cut'
    Failed = 'failed'
    Success = 'success'


class BaseScript(GObject.Object):
    __gtype_name__ = 'BaseScript'

    device = GObject.Property(type=ADBDevice)
    client = GObject.Property(type=ADBClient)
    state = GObject.Property(type=str, default=str(ConnectionState.Unstarted))
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

        pass  # WIP

    def check_exec_out(self):
        pass  # WIP
