#!/usr/bin/env python3
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput

from diagng.protocol.qualcomm.struct.dlf_file import DlfFile
from gzip import decompress

from kaitaistruct import KaitaiStream
from gi.repository import Gio
from threading import Thread
from io import BytesIO

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True


class DLFInput(BaseQCDMInput):
    stream: KaitaiStream

    def __init__(self, stream_io: BytesIO):
        super().__init__()

        try:
            stream_io = BytesIO(decompress(stream_io.read()))
        except Exception:
            pass
        stream_io.seek(0)

        self.stream = KaitaiStream(stream_io)

    def process_stream(self, cancellable: Gio.Cancellable, background=True):
        def processor():
            self.stream.seek(0)

            dlf = DlfFile(self.stream)
            dlf._read()

            for num_log, inner_log in enumerate(dlf.logs):
                if cancellable and cancellable.is_cancelled():
                    break
                self.log_received.emit(inner_log, num_log + 1, len(dlf.logs))

            self.close()

        if background:
            Thread(target=processor, daemon=True).start()
        else:
            processor()

    def send_raw(self, data: bytes):
        raise IOError('Stream is read-only')

    def close(self):
        self.closed.emit()
