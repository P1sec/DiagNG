#!/usr/bin/env python3
from gi.repository import GObject


class Process(GObject.Object):
    process_name = GObject.Property(type=str)
    pid = GObject.Property(type=str)
