#!/usr/bin/env python3
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput

from diagng.protocol.qualcomm.struct.dlf_file import DlfFile

from kaitaistruct import KaitaiStream
from io import BytesIO

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True


class DLFInput(BaseQCDMInput):
    stream: KaitaiStream

    def __init__(self, stream_io: BytesIO):
        super().__init__()

        self.stream = KaitaiStream(stream_io)

    def process_stream(self):
        dlf = DlfFile(self.stream)
        dlf._read()

        for inner_log in dlf.logs:
            self.log_received.emit(inner_log)

    def send_raw(self, data: bytes):
        raise IOError('Stream is read-only')

    def close(self):
        if self.stream:
            self.stream = None
