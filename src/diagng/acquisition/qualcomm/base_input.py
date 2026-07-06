#!/usr/bin/env python3

from logging import warning, debug, info
from kaitaistruct import KaitaiStream
from collections.abc import Callable
from gi.repository import GObject
from traceback import format_exc
from abc import abstractmethod
from io import BytesIO

from diagng.parsing.hdlc import hdlc_encode, hdlc_decode, TRAILER_CHAR
from diagng.parsing.struct.qualcomm.diag_response import DiagResponse
from diagng.parsing.struct.qualcomm.diag_cmd_code import DiagCmdCode
from diagng.parsing.struct.qualcomm.diag_request import DiagRequest

DiagCmd = DiagCmdCode.DiagCmd


class BaseQCDMInput(GObject.Object):
    short_name = GObject.Property(type=str)
    full_name = GObject.Property(type=str)

    buffered_data: bytes = b''

    @GObject.Signal(
        arg_types=(object, object),
    )
    def frame_sent(self, request: DiagRequest, raw_frame: bytes):
        pass

    @GObject.Signal(
        arg_types=(object, object),
    )
    def frame_received(self, response: DiagResponse, raw_frame: bytes):
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
        debug('Demuxing pseudo-HDLC data: %r' % data)

        self.buffered_data += data

        while TRAILER_CHAR in self.buffered_data:
            payload, sep, self.buffered_data = self.buffered_data.partition(
                TRAILER_CHAR
            )
            try:
                data = hdlc_decode(payload + sep)
            except AssertionError:
                warning(
                    'Could not demux pseudo-HDLC frame: %r' % (payload + sep)
                )
            else:
                try:
                    stream = KaitaiStream(BytesIO(data))
                    resp = DiagResponse(stream)
                    resp._read()
                except Exception:
                    warning('Failed to parse Diag response: ' + format_exc())
                else:
                    info('Successfully parsed Diag response: %r' % resp)

                    self.frame_received.emit(resp, data)

    def send(self, request: DiagRequest):
        buf = BytesIO()
        stream = KaitaiStream(buf)
        stream._ensure_bytes_left_to_write = lambda *args: True
        request._write(stream)

        self.frame_sent.emit(request, buf.getvalue())

        self.send_raw(hdlc_encode(buf.getvalue()))

    def send_recv(
        self,
        request: DiagRequest,
        callback: Callable[[DiagResponse], None],
        accept_error: bool = False,
    ):
        def temp_callback(
            self, diag_response: DiagResponse, raw_response: bytes
        ):
            nonlocal handler_id

            OPCODE_ERRORS = [
                DiagCmd.bad_cmd_f,
                DiagCmd.bad_parm_f,
                DiagCmd.bad_len_f,
                DiagCmd.bad_mode_f,
                DiagCmd.bad_spc_mode_f,
                DiagCmd.bad_sec_mode_f,
                DiagCmd.bad_trans_f,
            ]

            if diag_response.cmd_code == request.cmd_code or (
                accept_error and diag_response.cmd_code in OPCODE_ERRORS
            ):
                callback(diag_response)
                self.frame_received.disconnect(handler_id)

        # TODO handle some kind of timeout here?

        handler_id = self.frame_received.connect(temp_callback)
        self.send(request)

    def register_logs(self, bit_field: int):
        raise NotImplementedError
