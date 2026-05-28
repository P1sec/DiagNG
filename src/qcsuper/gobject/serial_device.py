#!/usr/bin/env python3
from gi.repository import GObject

from qcsuper.gobject.process import Process


class SerialDevice(GObject.Object):
    serial_device_path = GObject.Property(type=str)
    process = GObject.Property(type=Process)
