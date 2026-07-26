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
from shutil import copy2
from sys import argv

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

    for file_name in POLKIT_ACTION_FILES:
        for path in POLKIT_ACTION_PATHS:
            if exists(join(path, file_name)):
                break
        else:
            escalate_root(entry_point)
            makedirs(POLKIT_ACTION_PATHS[0], exist_ok=True)
            copy2(
                join(POLKIT_ACTIONS_DIR, file_name),
                POLKIT_ACTION_PATHS[0],
            )
