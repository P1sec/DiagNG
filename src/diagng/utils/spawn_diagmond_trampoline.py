#!/usr/bin/env python3
from os.path import dirname, realpath, join
from logging import debug, info
from shutil import which
from io import StringIO
from csv import reader
from os import getenv

import gi

gi.require_version('Adw', '1')

from gi.repository import Gio, Adw

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))

LAUNCHER_PATH = join(UTILS_DIR, 'spawn_diagmond.py')

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')

# Magic exit code to be passed by the child process when needed
WILL_NEED_PRIVESC_EXIT = 42


class DiagmondLaunchTrampoline:
    is_debug: bool
    parent_window: Adw.ApplicationWindow
    needs_privesc: bool = False

    def __init__(self, parent_window: Adw.ApplicationWindow, is_debug: bool):
        self.parent_window = parent_window
        self.is_debug = is_debug

        self.try_spawn_outer_process()

    def try_spawn_outer_process(
        self, script_path: str = None, bin_path: str = None
    ):
        extra_args = []
        if self.is_debug:
            extra_args.append('--debug')
        if self.needs_privesc:
            extra_args.append('--privesc')

        if IS_FLATPAK:
            if not script_path:
                self.get_flatpak_bin_dir()
                return

            debug('Trying to launch from inside Flatpak: ' + script_path)
            debug('Which will launch in turn: ' + bin_path)
            proc = Gio.Subprocess.new(
                [
                    'flatpak-spawn',
                    '--host',
                    'env',
                    'python3',
                    script_path,
                    *extra_args,
                    bin_path,
                ],
                Gio.SubprocessFlags.NONE,
            )

        else:
            debug('Trying to launch: ' + LAUNCHER_PATH)
            proc = Gio.Subprocess.new(
                ['env', 'python3', LAUNCHER_PATH, *extra_args],
                Gio.SubprocessFlags.NONE,
            )

        def on_child_end(proc: Gio.Subprocess, res: Gio.AsyncResult):
            proc.wait_finish(res)

            if proc.get_if_exited():
                exit_code = proc.get_exit_status()

                if exit_code == WILL_NEED_PRIVESC_EXIT:
                    self.needs_privesc = True

                    def on_agree(
                        alert_dialog: Adw.AlertDialog, result: Gio.AsyncResult
                    ):
                        alert_dialog.choose_finish(result)

                        self.try_spawn_outer_process(script_path, bin_path)

                    dialog = Adw.AlertDialog.new(
                        'System restart may be needed',
                        'As this operation will add a D-Bus '
                        + 'system service and Polkit rules to '
                        + 'your system, restarting your system '
                        + 'or desktop session may be needed in '
                        + 'order to use DiagNG.',
                    )
                    dialog.add_response('continue', 'Continue')
                    dialog.set_default_response('continue')
                    dialog.set_close_response('continue')
                    dialog.choose(self.parent_window, None, on_agree)

                else:
                    info(
                        'spawn_diagmond.py returned with exit code: %d'
                        % exit_code
                    )

        proc.wait_async(None, on_child_end)

    def get_flatpak_bin_dir(self):
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

                self.try_spawn_outer_process(script_path, bin_path)

            proc_2.communicate_utf8_async(None, None, on_complete_2)

        proc.communicate_utf8_async(None, None, on_complete)
