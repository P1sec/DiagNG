#!/usr/bin/env python3

from gi.repository import GObject, Gio
from logging import debug

# WIP - Cf. https://docs.gtk.org/gio/class.FileMonitor.html -
#   https://github.com/P1sec/DiagNG/issues/10

#   => https://lazka.github.io/pgi-docs/Gio-2.0/classes/File.html#Gio.File.monitor_directory

UDEV_RULES_DIR = '/run/udev/rules.d'


class UdevRulesMonitor:
    app: 'MainApplication'

    rules_dir: Gio.File
    rules_dir_monitor: Gio.FileMonitor

    def __init__(self, app):

        self.app = app

        self.rules_dir = Gio.File.new_for_path(UDEV_RULES_DIR)
        self.rules_dir_monitor = self.rules_dir.monitor_directory(
            Gio.FileMonitorFlags.NONE, None
        )

        self.rules_dir_monitor.connect('changed', self.dir_event)

    def dir_event(
        self,
        file_monitor: Gio.FileMonitor,
        fd: Gio.File,
        other_file: Gio.File,
        event_type: Gio.FileMonitorEvent,
    ):
        debug(
            'UDev rules directory event received: '
            + 'file=%s - other_file=%s - event=%s'
            % (
                fd.get_path() if fd else None,
                other_file.get_path() if other_file else None,
                event_type.value_name,
            )
        )  # WIP

        """
            TODO:
            Sample data to process:

            [2026-06-29 16:22:01,903] [ui 555365] - DEBUG - UDev rules directory event received: file=/run/udev/rules.d/99-diagmond-blacklist-ttyUSB1.rules - other_file=None - event=G_FILE_MONITOR_EVENT_CREATED (system/udev_rules_dir.py:38)
            [2026-06-29 16:22:01,903] [ui 555365] - DEBUG - UDev rules directory event received: file=/run/udev/rules.d/99-diagmond-blacklist-ttyUSB1.rules - other_file=None - event=G_FILE_MONITOR_EVENT_CHANGED (system/udev_rules_dir.py:38)
            [2026-06-29 16:22:01,904] [ui 555365] - DEBUG - UDev rules directory event received: file=/run/udev/rules.d/99-diagmond-blacklist-ttyUSB1.rules - other_file=None - event=G_FILE_MONITOR_EVENT_CHANGES_DONE_HINT (system/udev_rules_dir.py:38)

            [2026-06-29 16:34:31,331] [ui 588284] - DEBUG - UDev rules directory event received: file=/run/udev/rules.d/99-diagmond-blacklist-ttyUSB1.rules - other_file=None - event=G_FILE_MONITOR_EVENT_DELETED (system/udev_rules_dir.py:38)
            [2026-06-29 16:34:54,914] [ui 588284] - DEBUG - UDev rules directory event received: file=/run/udev/rules.d/99-diagmond-blacklist-ttyUSB0.rules - other_file=None - event=G_FILE_MONITOR_EVENT_DELETED (system/udev_rules_dir.py:38)
        """
