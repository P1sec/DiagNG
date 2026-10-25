#!/usr/bin/env python3

from logging import (
    getLogger,
    StreamHandler,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    log,
    Handler,
    Formatter,
    Logger,
    LogRecord,
)
from typing import List, Dict, Sequence, Optional
from logging.handlers import RotatingFileHandler
from os import umask, chmod, chown, stat
from os.path import dirname, realpath
from re import split, IGNORECASE
from collections import deque
import ctypes

# from shlex import join
import sys

from gi.repository import GObject, GLib


# Features:
# - Hook the Python logging module globally
# - Log truncated, unbuffered log to file (disabled)
# - Log to stdout with colors
# - Persistent log to GTK UI (todo)

SCRIPT_DIR = dirname(realpath(__file__))
MODULE_DIR = dirname(realpath(SCRIPT_DIR))
SRC_DIR = dirname(realpath(MODULE_DIR))
ROOT_DIR = dirname(realpath(SRC_DIR))

LOG_FILE_NAME = ROOT_DIR + '/_test_log.log'
LOG_FILE_SIZE = 10 * 1024 * 1024
MEMORY_LOG_LINES = 5000
LOG_FORMAT = '[{asctime}] [{name} {process}] - {levelname} - {message} ({pathname_last}:{lineno})'

BASE_FORMATTER = Formatter(fmt=LOG_FORMAT, style='{')


class NoColorFormatter(Formatter):
    def format(self, record):
        record.pathname_last = split(
            r'diagng/', record.pathname, flags=IGNORECASE
        ).pop()
        return BASE_FORMATTER.format(record)


class ColorFormatter(Formatter):
    CSI = '\x1b['
    black = ''
    yellow = CSI + '33m'
    red = CSI + '31m'
    magenta = CSI + '35m'
    bold_red = CSI + '31;1m'
    reset = CSI + '0m'
    # format = "%(asctime)s - [pid %(process)s] - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = LOG_FORMAT

    FORMATS = {
        DEBUG: black + format + reset,
        INFO: black + format + reset,
        WARNING: yellow + format + reset,
        ERROR: magenta + format + reset,
        CRITICAL: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        record.pathname_last = split(
            r'diagng/', record.pathname, flags=IGNORECASE
        ).pop()
        formatter = Formatter(log_fmt, style='{')
        return formatter.format(record)


class ScrollbackHandler(Handler):
    def __init__(self):
        Handler.__init__(self)
        self.logs: Sequence[str] = deque(maxlen=MEMORY_LOG_LINES)

    def emit(self, record: LogRecord):
        string: str = self.format(record)
        self.logs.append(string)


class GoodPermissionsRotatingFileHandler(RotatingFileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        dir_info = stat(SCRIPT_DIR)
        uid = dir_info.st_uid
        gid = dir_info.st_gid

        prev_umask = umask(~0o664)
        chmod(self.baseFilename, 0o0664)
        umask(prev_umask)

        chown(self.baseFilename, uid, gid)


class LoggingCentral(GObject.Object):
    logs: deque[LogRecord]
    scrollback_handler: 'ScrollbackHandler'
    signal_handler: object = None
    update_live: bool = False
    logger: Logger
    glib_logger: Logger

    def get_logs(self) -> Sequence[str]:
        return list(self.scrollback_handler.logs)

    def register_signal_handler(self, signal_handler: object):
        self.signal_handler = signal_handler

    def __init__(self, debug_mode: bool):
        super().__init__()

        # Register all logging handlers here...

        self.logger = getLogger()
        self.logger.name = 'diagng'
        self.logger.setLevel(DEBUG)

        self.glib_logger = getLogger('glib_logger')
        self.glib_logger.propagate = False
        self.glib_logger.setLevel(DEBUG)

        stderr_handler = StreamHandler()
        stderr_handler.setLevel(DEBUG)
        if sys.stderr.isatty():
            stderr_handler.setFormatter(ColorFormatter())
        else:
            stderr_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(stderr_handler)

        stderr_handler = StreamHandler()
        stderr_handler.setLevel(DEBUG if debug_mode else ERROR)
        if sys.stderr.isatty():
            stderr_handler.setFormatter(ColorFormatter())
        else:
            stderr_handler.setFormatter(NoColorFormatter())
        self.glib_logger.addHandler(stderr_handler)

        """
        file_handler = GoodPermissionsRotatingFileHandler(
            filename=LOG_FILE_NAME, maxBytes=LOG_FILE_SIZE, backupCount=5
        )
        file_handler.setLevel(DEBUG if debug_mode else INFO)
        file_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(file_handler)
        """

        self.scrollback_handler = ScrollbackHandler()
        self.scrollback_handler.setLevel(DEBUG)
        self.scrollback_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(self.scrollback_handler)

        self.scrollback_handler = ScrollbackHandler()
        self.scrollback_handler.setLevel(DEBUG)
        self.scrollback_handler.setFormatter(NoColorFormatter())
        self.glib_logger.addHandler(self.scrollback_handler)

        self.setup_glib_log_handling()

    def setup_glib_log_handling(self):

        def convert_log_level(log_level: GLib.LogLevelFlags) -> int:
            return {
                GLib.LogLevelFlags.LEVEL_DEBUG: DEBUG,
                GLib.LogLevelFlags.LEVEL_MESSAGE: INFO,
                GLib.LogLevelFlags.LEVEL_INFO: INFO,
                GLib.LogLevelFlags.LEVEL_WARNING: WARNING,
                GLib.LogLevelFlags.LEVEL_ERROR: ERROR,
                GLib.LogLevelFlags.LEVEL_CRITICAL: CRITICAL,
            }[log_level]

        # Handle structured GLib logging
        # ⚠️ Messy, see: https://gitlab.gnome.org/GNOME/pygobject/-/work_items/771

        def log_writer_func(
            log_level: GLib.LogLevelFlags, fields: List[GLib.LogField], *args
        ):
            items = {}
            for item in fields:
                value = ctypes.string_at(item.value, item.length)
                try:
                    value = value.decode('utf-8')
                except Exception:
                    pass
                items[item.key] = value
            items.pop('PRIORITY', None)
            items.pop('SYSLOG_IDENTIFIER', None)
            items.pop('GLIB_OLD_LOG_API', None)
            args = dict(
                name=items.pop('GLIB_DOMAIN', self.logger.name),
                level=convert_log_level(log_level),
                pathname=items.pop('CODE_FILE', '???').strip('./'),
                lineno=int(items.pop('CODE_LINE', '0')),
                msg=items.pop('MESSAGE', '???'),
                args={},
                exc_info=None,
                func=items.pop('CODE_FUNC', None),
                sinfo=None,
            )
            for key, value in items.items():
                args.dict += ' %s=%r' % (key, value)
            self.glib_logger.handle(LogRecord(**args))

            return GLib.LogWriterOutput.HANDLED

        GLib.log_set_writer_func(log_writer_func)

        # Handle unstructured GLib logging
        # No effect because structured logging is enabled

        """
        def log_func(
            log_domain: Optional[str],
            log_level: GLib.LogLevelFlags,
            message: str,
            *args,
        ):
            log(
                convert_log_level(log_level), '[%s] %s' % (log_domain, message)
            )

        for domain in [
            None,
            'Gdk',
            'Gtk',
            'GLib',
            'Gio',
            'GObject',
            'Adw',
            'GtkSource',
        ]:
            GLib.log_set_handler(
                domain, GLib.LogLevelFlags.LEVEL_MASK, log_func
            )
        """
