#!/usr/bin/env python3
# WIP 2026-06-21

# Use pkexec to create privileged dirs like /etc/dbus-1
# when needed

# See: https://dbus.freedesktop.org/doc/dbus-daemon.1.html +
# https://github.com/P1sec/DiagNG/issues/1 for
# standard DBus directories reference

# => Launch the privileged subprocess directly
# if the service is not installed/running/
# launchable

#  => Install the DBus policy file in a stub
#     after running pkexec

#    => Display a status banner about the
#       privileged subprocess in the main UI

from os import makedirs, getenv, chdir, geteuid, execlp
from os.path import dirname, realpath, join, exists
from shutil import which, copy2
from typing import Optional
from subprocess import run
from re import search
from sys import argv

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))

# Polkit and D-Bus related paths:
UI_DIR = realpath(join(MODULE_DIR, 'ui'))
ASSETS_DIR = realpath(join(UI_DIR, 'assets'))
SHARE_DIR = realpath(join(ASSETS_DIR, 'share'))
DBUS_DIR = realpath(join(SHARE_DIR, 'dbus-1'))
POLKIT_DIR = realpath(join(SHARE_DIR, 'polkit-1'))

DBUS_SYSTEM_D_FILE = 'com.p1security.diagmond.conf'
DBUS_SYSTEM_D_DIR = realpath(join(DBUS_DIR, 'system-d'))
DBUS_SYSTEM_D_PATHS = ['/etc/dbus-1/system.d', '/usr/share/dbus-1/system.d']

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


POLKIT_ACTION_FILES = [
    'com.p1security.diagmond.policy',
    'com.p1security.diagmond.capture-serial-port.policy',
    'com.p1security.diagmond.open-usb-interface.policy',
]
POLKIT_ACTIONS_DIR = realpath(join(POLKIT_DIR, 'actions'))
POLKIT_ACTION_PATHS = [
    '/etc/polkit-1/actions/',
    '/usr/local/share/polkit-1/actions/',
    '/usr/share/polkit-1/actions/',
]

# Polkit only reads actions from /etc/polkit-1/actions since version 126,
# older versions (e.g. 124 on Ubuntu 24.04) only read /usr/share
POLKIT_LEGACY_ACTION_PATHS = ['/usr/share/polkit-1/actions/']
POLKIT_ETC_ACTIONS_MIN_VERSION = 126

# Magic exit code to be passed to parent process when needed
WILL_NEED_PRIVESC_EXIT = 42


def get_polkit_version() -> Optional[int]:
    try:
        output = run(
            ['pkaction', '--version'], capture_output=True, text=True
        ).stdout
    except OSError:
        return None

    match = search(r'(\d+)', output)
    return int(match.group(1)) if match else None


def get_polkit_action_paths() -> list[str]:
    version = get_polkit_version()

    if version is not None and version < POLKIT_ETC_ACTIONS_MIN_VERSION:
        return POLKIT_LEGACY_ACTION_PATHS
    return POLKIT_ACTION_PATHS


def escalate_root(privesc_mode: bool):
    if geteuid() != 0:
        if not privesc_mode:
            exit(WILL_NEED_PRIVESC_EXIT)
        execlp('pkexec', 'pkexec', 'env', 'python3', __file__, *argv[1:])
        exit(1)


def install_dbus_and_polkit_files(privesc_mode: bool):

    for path in DBUS_SYSTEM_D_PATHS:
        if exists(join(path, DBUS_SYSTEM_D_FILE)):
            break
    else:
        escalate_root(privesc_mode)
        makedirs(DBUS_SYSTEM_D_PATHS[0], exist_ok=True)
        copy2(
            join(DBUS_SYSTEM_D_DIR, DBUS_SYSTEM_D_FILE), DBUS_SYSTEM_D_PATHS[0]
        )

        if which('restorecon'):
            try:
                run(['restorecon', DBUS_SYSTEM_D_PATHS[0]])
            except OSError:
                pass

        if which('busctl'):
            try:
                run(
                    [
                        'busctl',
                        'call',
                        'org.freedesktop.DBus',
                        '/org/freedesktop/DBus',
                        'org.freedesktop.DBus',
                        'ReloadConfig',
                    ]
                )
            except OSError:
                pass

        elif which('dbus-send'):
            try:
                run(
                    [
                        'dbus-send',
                        '--system',
                        '--type=method_call',
                        '--dest=org.freedesktop.DBus',
                        '/org/freedesktop/DBus',
                        'org.freedesktop.DBus.ReloadConfig',
                    ]
                )
            except OSError:
                pass

    polkit_action_paths = get_polkit_action_paths()

    for file_name in POLKIT_ACTION_FILES:
        for path in polkit_action_paths:
            if exists(join(path, file_name)):
                break
        else:
            escalate_root(privesc_mode)
            makedirs(polkit_action_paths[0], exist_ok=True)
            copy2(join(POLKIT_ACTIONS_DIR, file_name), polkit_action_paths[0])

            if which('restorecon'):
                try:
                    run(['restorecon', polkit_action_paths[0]])
                except OSError:
                    pass


def main():

    input_args = list(argv)
    debug_mode = False
    privesc_mode = False

    if '--debug' in input_args:
        input_args.remove('--debug')
        debug_mode = True

    if '--privesc' in input_args:
        input_args.remove('--privesc')
        privesc_mode = True

    if (
        len(input_args) == 1
        and IS_GIT_TREE
        and not getenv('SUDO_UID')
        and not getenv('PKEXEC_UID')
    ):
        chdir(DIAGMOND_DIR)

        run(
            ['cargo', 'build', *([] if debug_mode else ['--release'])],
            check=True,
        )

    install_dbus_and_polkit_files(privesc_mode)

    if len(input_args) > 1:
        execlp(input_args[1], input_args[1])
    elif IS_GIT_TREE:
        execlp(DIAGMOND_GIT_PATH, DIAGMOND_GIT_PATH)
    elif DIAGMOND_PATH:
        execlp(DIAGMOND_PATH, DIAGMOND_PATH)
    else:
        raise Exception('diagmond is not installed on the system')


if __name__ == '__main__':
    main()
