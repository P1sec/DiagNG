#!/usr/bin/env python3

from logging import (
    getLogger,
    StreamHandler,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    Handler,
    Formatter,
    Logger,
    LogRecord,
)
from logging.handlers import RotatingFileHandler
from os import umask, chmod, chown, stat
from typing import List, Dict, Sequence
from os.path import dirname, realpath
from collections import deque
from shlex import join
import sys


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
MEMORY_LOG_LINES = 400
LOG_FORMAT = '[{asctime}] [main {process}] - {levelname} - {message} ({pathname_last}:{lineno})'

if '--service' in join(sys.argv).lower():
    LOG_FORMAT = LOG_FORMAT.replace('main ', 'service ')

BASE_FORMATTER = Formatter(fmt=LOG_FORMAT, style='{')


class NoColorFormatter(Formatter):
    def format(self, record):
        record.pathname_last = record.pathname.split('qcsuper/')[-1]
        return BASE_FORMATTER.format(record)


class ColorFormatter(Formatter):
    CSI = '\x1b['
    grey = CSI + '38m'
    yellow = CSI + '33m'
    red = CSI + '31m'
    magenta = CSI + '35m'
    bold_red = CSI + '31;1m'
    reset = CSI + '0m'
    # format = "%(asctime)s - [pid %(process)s] - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = LOG_FORMAT

    FORMATS = {
        DEBUG: grey + format + reset,
        INFO: grey + format + reset,
        WARNING: yellow + format + reset,
        ERROR: magenta + format + reset,
        CRITICAL: red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        record.pathname_last = record.pathname.split('qcsuper/')[-1]
        formatter = Formatter(log_fmt, style='{')
        return formatter.format(record)


class ScrollbackHandler(Handler):
    def __init__(self, logging_central: 'LoggingCentral'):
        Handler.__init__(self)
        self.logging_central = logging_central
        self.logs: Sequence[Dict[str, str]] = deque(maxlen=MEMORY_LOG_LINES)

    def emit(self, record: LogRecord):
        # string : str = self.format(record)
        # self.logs.append(string)

        log_entry: dict = {
            'log_class': record.levelname.lower(),
            'log_raw': self.format(record),
        }

        self.logs.append(log_entry)

        # Dispatch to signal handlers, if present

        if self.logging_central.signal_handler:
            self.logging_central.signal_handler.broadcast_message(
                {'type': 'APPEND_EVENT_LOG', 'log': log_entry}
            )

        # XX : Store metadata?


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


class LoggingCentral:
    logs: deque[LogRecord]
    scrollback_handler: 'ScrollbackHandler'
    signal_handler: object = None
    logger: Logger

    def get_logs(self) -> List[str]:
        return list(self.scrollback_handler.logs)

    def register_signal_handler(self, signal_handler: object):
        self.signal_handler = signal_handler

    def __init__(self, debug_mode: bool):

        self.logs = MEMORY_LOG_LINES

        # Register all logging handlers here...

        self.logger = getLogger()
        self.logger.setLevel(DEBUG)

        stderr_handler = StreamHandler()
        stderr_handler.setLevel(DEBUG if debug_mode else INFO)
        if sys.stderr.isatty():
            stderr_handler.setFormatter(ColorFormatter())
        else:
            stderr_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(stderr_handler)

        """
        file_handler = GoodPermissionsRotatingFileHandler(
            filename=LOG_FILE_NAME, maxBytes=LOG_FILE_SIZE, backupCount=5
        )
        file_handler.setLevel(DEBUG if debug_mode else INFO)
        file_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(file_handler)
        """

        """
        self.scrollback_handler = ScrollbackHandler(self)
        self.scrollback_handler.setLevel(INFO)
        self.scrollback_handler.setFormatter(NoColorFormatter())
        self.logger.addHandler(self.scrollback_handler)
        """
