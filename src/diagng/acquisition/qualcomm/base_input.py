#!/usr/bin/env python3

from gi.repository import GObject
from abc import abstractmethod
from typing import Callable

from diagng.parsing.struct.qualcomm.diag_request import DiagRequest
from diagng.parsing.struct.qualcomm.diag_response import DiagResponse


class BaseQCDMInput(GObject.Object):
    short_name = GObject.Property(type=str)
    full_name = GObject.Property(type=str)

    @GObject.Signal
    def frame_sent(self, request):  # response: DiagRequest
        pass

    @GObject.Signal
    def frame_received(self, response):  # response: DiagResponse
        pass

    @GObject.Signal
    def closed(self):  # Add reason arg eventually?
        pass

    @abstractmethod
    def send(self, request: DiagRequest):
        pass

    @abstractmethod
    def close(self):
        pass

    def send_recv(
        self, request: DiagRequest, callback: Callable[DiagResponse, []]
    ):
        def temp_callback(self, *args):
            print('DEBUG temp_callback called with:', args)

        self.frame_received.connect(temp_callback)
        self.send(request)

    def register_logs(self, bit_field: int):
        raise NotImplementedError
