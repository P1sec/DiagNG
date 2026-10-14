#!/usr/bin/env python3
from collections.abc import Callable
from shutil import which
from os import getenv

from gi.repository import Gio


class FlatpakHelper:
    @staticmethod
    def is_flatpak() -> bool:
        return getenv('container')

    @staticmethod
    def is_flatpak_spawn_available() -> bool:
        if getenv('container') and which('flatpak-spawn'):
            try:
                Gio.Subprocess.new(
                    ['flatpak-spawn', '--host', 'id'],
                    Gio.SubprocessFlags.STDOUT_SILENCE
                    | Gio.SubprocessFlags.STDERR_SILENCE,
                ).wait_check(None)

            except Exception:
                return False
            else:
                return True

        else:
            return False
