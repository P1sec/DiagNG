#!/usr/bin/env python3
# WIP 2026-06-21

# TODO use pkexec to create privileged dirs like /run/dbus-1
# when needed +

# See: https://dbus.freedesktop.org/doc/dbus-daemon.1.html +
# https://github.com/P1sec/DiagNG/issues/1 for
# standard DBus directories reference

SLASH_RUN_DBUS_SYSTEM_SERVICE_SPEC_DIR = '/run/dbus-1/system-services'

SYSTEM_WIDE_DBUS_SYSTEM_SERVICE_SPEC_DIRS = [
    '/etc/dbus-1/system-services',
    '/usr/local/share/dbus-1/system-services',
    '/usr/share/dbus-1/system-services',
]

# =)
