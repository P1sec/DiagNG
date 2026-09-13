#!/usr/bin/env python3

from collections.abc import Callable
from gi.repository import GObject
from abc import abstractmethod


class FileOutMode(GObject.GEnum):
    Append = 1
    Overwrite = 2
    Dismiss = 3


class FileOutModeSelector:
    @abstractmethod
    def query_file_out_mode(self, callback: Callable[[FileOutMode], None]):
        pass
