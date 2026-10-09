#!/usr/bin/env python3
from collections.abc import Callable
from shutil import which
from os import getenv

from gi.repository import Gio

# WIP XX - https://github.com/P1sec/DiagNG/issues/46


class FlatpakHelper:
    @staticmethod
    def is_flatpak_spawn_available(callback: Callable[bool, []]) -> bool:
        if getenv('container') and which('flatpak-spawn'):

            def on_which_result(obj: Gio.Subprocess, res: Gio.AsyncResult):
                try:
                    assert obj.wait_check_finish(res)
                except Exception:
                    callback(False)
                else:
                    callback(True)

            Gio.Subprocess.new(
                ['flatpak-spawn', '--host', 'id'],
                Gio.SubprocessFlags.STDOUT_PIPE,
            ).wait_check_async(None, on_which_result)

        else:
            callback(False)
