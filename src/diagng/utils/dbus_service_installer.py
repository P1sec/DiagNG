#!/usr/bin/env python3
# WIP 2026-06-21

# TODO use pkexec to create privileged dirs like /run/dbus-1
# when needed +

# See: https://dbus.freedesktop.org/doc/dbus-daemon.1.html +
# https://github.com/P1sec/DiagNG/issues/1 for
# standard DBus directories reference

# => Launch the privileged subprocess directly
# if the service is not installed/running/
# launchable?

#  => Install the DBus policy file in a stub
#     after running pkexec?

#    => Display a status banner about the
#       privileged subprocess in the main UI?

# OR, do no auto-launch until the whole
# thing is distributable?

#  (Maybe later use an integrated build system
#  like meson?)

SLASH_RUN_SERVICE_SPEC_DIR = '/run/dbus-1/system-services'

SYSTEM_WIDE_SERVICE_SPEC_DIRS = [
    '/etc/dbus-1/system-services',
    '/usr/local/share/dbus-1/system-services',
    '/usr/share/dbus-1/system-services',
]


class DiagmondManager:
    WIP  # xx =)
