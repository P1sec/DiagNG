#!/usr/bin/env python3
from os.path import dirname, realpath, join
from gi.repository import Gio, GLib
from logging import debug, info
from typing import Callable
from shutil import which
from io import StringIO
from csv import reader
from os import getenv

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))

LAUNCHER_PATH = join(UTILS_DIR, 'spawn_diagmond.py')

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')


def get_flatpak_bin_dir(
    callback: Callable[[bool, str, str], []], is_debug: bool
):
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
            script_dir = join(
                stdout.strip(),
                'files',
                dirname(__file__.replace('/app/', '', 1)),
            )
            script_path = join(script_dir, 'spawn_diagmond.py')
            bin_path = join(stdout.strip(), 'files', 'bin', 'diagmond-bin')

            callback(is_debug, script_path, bin_path)

        proc_2.communicate_utf8_async(None, None, on_complete_2)

    proc.communicate_utf8_async(None, None, on_complete)


def spawn_diagmond_as_outer_process(
    is_debug: bool, script_path: str = None, bin_path: str = None
):
    extra_args = []
    if is_debug:
        extra_args.append('--debug')

    if IS_FLATPAK:
        if not script_path:
            get_flatpak_bin_dir(spawn_diagmond_as_outer_process, is_debug)
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
                *extra_args,
                bin_path,
            ],
            flags=GLib.SpawnFlags.SEARCH_PATH,
        )

    else:
        debug('Trying to launch: ' + LAUNCHER_PATH)
        GLib.spawn_async(
            ['env', 'python3', LAUNCHER_PATH, *extra_args],
            flags=GLib.SpawnFlags.SEARCH_PATH,
        )
