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

from os.path import dirname, realpath, join, exists
from os import makedirs, geteuid, execlp
from subprocess import run
from typing import Optional
from shutil import copy2
from sys import argv
from re import search

UTILS_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(UTILS_DIR))
UI_DIR = realpath(join(MODULE_DIR, 'ui'))
ASSETS_DIR = realpath(join(UI_DIR, 'assets'))
SHARE_DIR = realpath(join(ASSETS_DIR, 'share'))
DBUS_DIR = realpath(join(SHARE_DIR, 'dbus-1'))
POLKIT_DIR = realpath(join(SHARE_DIR, 'polkit-1'))

DBUS_SYSTEM_D_FILE = 'com.p1security.diagmond.conf'
DBUS_SYSTEM_D_DIR = realpath(join(DBUS_DIR, 'system-d'))
DBUS_SYSTEM_D_PATHS = ['/etc/dbus-1/system.d', '/usr/share/dbus-1/system.d']

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

# Polkit only reads actions from /etc/polkit-1/actions since version 125,
# older versions (e.g. 124 on Ubuntu 24.04) only read /usr/share
POLKIT_LEGACY_ACTION_PATHS = ['/usr/share/polkit-1/actions/']
POLKIT_ETC_ACTIONS_MIN_VERSION = 125


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


def escalate_root(entry_point: str):
    if geteuid() != 0:
        execlp('pkexec', 'pkexec', 'env', 'python3', entry_point, *argv[1:])
        exit(1)


def install_dbus_and_polkit_files(entry_point: str):

    for path in DBUS_SYSTEM_D_PATHS:
        if exists(join(path, DBUS_SYSTEM_D_FILE)):
            break
    else:
        escalate_root(entry_point)
        makedirs(DBUS_SYSTEM_D_PATHS[0], exist_ok=True)
        copy2(
            join(DBUS_SYSTEM_D_DIR, DBUS_SYSTEM_D_FILE), DBUS_SYSTEM_D_PATHS[0]
        )

    polkit_action_paths = get_polkit_action_paths()

    for file_name in POLKIT_ACTION_FILES:
        for path in polkit_action_paths:
            if exists(join(path, file_name)):
                break
        else:
            escalate_root(entry_point)
            makedirs(polkit_action_paths[0], exist_ok=True)
            copy2(
                join(POLKIT_ACTIONS_DIR, file_name),
                polkit_action_paths[0],
            )
