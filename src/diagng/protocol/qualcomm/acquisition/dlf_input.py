#!/usr/bin/env python3
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput

from diagng.protocol.qualcomm.struct.dlf_file import DlfFile
from gzip import decompress

from kaitaistruct import KaitaiStream
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

    def process_stream(self):
        self.stream.seek(0)

        dlf = DlfFile(self.stream)
        dlf._read()

        for num_log, inner_log in enumerate(dlf.logs):
            self.log_received.emit(inner_log, num_log + 1, len(dlf.logs))

        self.close()

    def send_raw(self, data: bytes):
        raise IOError('Stream is read-only')

    def close(self):
        self.closed.emit()
