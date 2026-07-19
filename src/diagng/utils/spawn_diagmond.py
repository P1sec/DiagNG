#!/usr/bin/env python3
from os import (
    execlp,
    getenv,
    chdir,
    geteuid,
)
from os.path import dirname, realpath, join, exists
from gi.repository import Gio, GLib
from logging import debug, info
from typing import Callable
from subprocess import run
from shutil import which
from io import StringIO
from csv import reader
import sys

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))

# Exists in Git tree setup only:
SRC_DIR = dirname(realpath(MODULE_DIR))
ROOT_DIR = dirname(realpath(SRC_DIR))
DIAGMOND_DIR = realpath(join(ROOT_DIR, 'diagmond'))
TARGET_DIR = realpath(join(DIAGMOND_DIR, 'target'))
RELEASE_DIR = realpath(join(TARGET_DIR, 'release'))
DIAGMOND_GIT_PATH = realpath(join(RELEASE_DIR, 'diagmond-bin'))

IS_GIT_TREE = exists(DIAGMOND_DIR)

# To use in the context of a system-wide install:
DIAGMOND_PATH = which('diagmond-bin')

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')

# To use in Flatpak setup when going out of sandbox:
sys.path.insert(0, SRC_DIR)

from diagng.utils.dbus_service_installer import install_dbus_and_polkit_files


def get_flatpak_bin_dir(callback: Callable[[str], []]):
    # See https://github.com/flathub/io.github.Archeb.opentrace/blob/master/nexttrace.sh

    proc = Gio.Subprocess.new(
        [
            'flatpak-spawn',
            '--host',
            'flatpak',
            'list',
            '--app',
            '--columns=application,arch,branch',
        ],
        Gio.SubprocessFlags.STDOUT_PIPE,
    )

    def on_complete(proc: Gio.Subprocess, res: Gio.AsyncResult):
        _, stdout, __ = proc.communicate_utf8_finish(res)

        for row in reader(StringIO(stdout), delimiter='\t'):
            if row[0] == 'com.p1security.diagng':
                container_id = '/'.join(row)
                break
        else:
            raise ValueError('Flatpak container could not be found')

        proc_2 = Gio.Subprocess.new(
            [
                'flatpak-spawn',
                '--host',
                'flatpak',
                'info',
                '--show-location',
                container_id,
            ],
            Gio.SubprocessFlags.STDOUT_PIPE,
        )

        def on_complete_2(proc_2: Gio.Subprocess, res_2: Gio.AsyncResult):
            _, stdout, __ = proc_2.communicate_utf8_finish(res_2)

            info('Flatpak base path is: ' + stdout.strip())
            script_path = join(
                stdout.strip(), 'files', __file__.replace('/app/', '', 1)
            )
            bin_path = join(stdout.strip(), 'files', 'bin', 'diagmond-bin')

            callback(script_path, bin_path)

        proc_2.communicate_utf8_async(None, None, on_complete_2)

    proc.communicate_utf8_async(None, None, on_complete)


def spawn_diagmond_as_outer_process(
    script_path: str = None, bin_path: str = None
):
    if IS_FLATPAK:
        if not script_path:
            get_flatpak_bin_dir(spawn_diagmond_as_outer_process)
            return

        debug('Trying to launch from inside Flatpak: ' + script_path)
        debug('Which will launch in turn: ' + bin_path)
        GLib.spawn_async(
            [
                'flatpak-spawn',
                '--host',
                'env',
                'python3',
                script_path,
                bin_path,
            ],
            flags=GLib.SpawnFlags.SEARCH_PATH,
        )

    else:
        debug('Trying to launch: ' + __file__)
        GLib.spawn_async(
            ['env', 'python3', __file__], flags=GLib.SpawnFlags.SEARCH_PATH
        )


def main():

    if (
        len(sys.argv) == 1
        and IS_GIT_TREE
        and not getenv('SUDO_UID')
        and not getenv('PKEXEC_UID')
    ):
        chdir(DIAGMOND_DIR)

        run(['cargo', 'build', '--release'], check=True)

    install_dbus_and_polkit_files(__file__)

    if len(sys.argv) > 1:
        execlp(sys.argv[1], sys.argv[1])
    elif IS_GIT_TREE:
        execlp(DIAGMOND_GIT_PATH, DIAGMOND_GIT_PATH)
    elif DIAGMOND_PATH:
        execlp(DIAGMOND_PATH, DIAGMOND_PATH)
    else:
        raise Exception('diagmond is not installed on the system')


if __name__ == '__main__':
    main()
