#!/usr/bin/env python3

"""
Secondary entry point of qcsuper, called
after spawning a provilege-elevated
subprocess from main_entry.py
"""


def main():

    # TODO use execlp to privilege escalate (using pkexec
    # or sudo) if non-root here
    pass

    # TODO use https://lazka.github.io/pgi-docs/Jsonrpc-1.0/index.html +
    # https://docs.gtk.org/glib/spawn.html /
    # https://lazka.github.io/pgi-docs/GLib-2.0/functions.html#GLib.spawn_async_with_pipes
    # in order to handle subprocess communication?

    # TODO build app with a different DBus service name
    # than the primary process
    # self.app = Gio.Application.new(
    #     'com.p1security.qcsuperd', Gio.ApplicationFlags.IS_SERVICE
    # )
