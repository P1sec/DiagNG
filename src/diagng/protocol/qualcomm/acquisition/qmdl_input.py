#!/usr/bin/env python3
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput
from gzip import decompress
from io import BytesIO


class QMDLInput(BaseQCDMInput):
    stream_io: BytesIO

    def __init__(self, stream_io: BytesIO):
        super().__init__()

        try:
            stream_io = BytesIO(decompress(stream_io.read()))
        except Exception:
            raise
        stream_io.seek(0)

        self.stream_io = stream_io

    def process_stream(self):
        self.stream.seek(0)

        self.process_input(self.stream_io.read())

        self.close()

    def send_raw(self, data: bytes):
        raise IOError('Stream is read-only')

    def close(self):
        self.closed.emit()
