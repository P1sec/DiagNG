#!/usr/bin/env python3

from kaitaistruct import KaitaiStream
from gi.repository import GObject
from abc import abstractmethod
from typing import Callable
from io import BytesIO

from diagng.parsing.struct.qualcomm.diag_response import DiagResponse
from diagng.parsing.struct.qualcomm.diag_request import DiagRequest
from diagng.parsing.hdlc import hdlc_encode


class BaseQCDMInput(GObject.Object):
    short_name = GObject.Property(type=str)
    full_name = GObject.Property(type=str)

    @GObject.Signal
    def frame_sent(self, request):  # request: DiagRequest
        pass

    @GObject.Signal
    def frame_received(self, response):  # response: DiagResponse
        pass

    @GObject.Signal
    def closed(self):  # Add reason arg eventually?
        pass

    @abstractmethod
    def send_raw(self, data: bytes):
        pass

    @abstractmethod
    def close(self):
        pass

    def process_input(self, data: bytes):
        print('DEBUG todo pls demux:', data)

    def send(self, request: DiagRequest):
        buf = BytesIO()
        stream = KaitaiStream(buf)
        stream._ensure_bytes_left_to_write = lambda *args: True
        request._write(stream)

        self.send_raw(hdlc_encode(buf.getvalue()))

    def send_recv(
        self, request: DiagRequest, callback: Callable[DiagResponse, None]
    ):
        def temp_callback(self, *args):
            print('DEBUG temp_callback called with:', args)

        self.frame_received.connect(temp_callback)
        self.send(request)

    def register_logs(self, bit_field: int):
        raise NotImplementedError
