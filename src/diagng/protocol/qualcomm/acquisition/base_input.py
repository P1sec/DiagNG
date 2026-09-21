#!/usr/bin/env python3

from logging import warning, debug, error, info
from gi.repository import GObject, Gio, GLib
from kaitaistruct import KaitaiStream
from collections.abc import Callable
from traceback import format_exc
from abc import abstractmethod
from enum import IntEnum
from io import BytesIO
from re import sub

from diagng.protocol.qualcomm.utils.hdlc import (
    hdlc_encode,
    hdlc_decode,
    TRAILER_CHAR,
)
from diagng.protocol.qualcomm.struct.diag_response import DiagResponse
from diagng.protocol.qualcomm.struct.diag_cmd_code import DiagCmdCode
from diagng.protocol.qualcomm.struct.diag_request import DiagRequest
from diagng.utils.kaitai_pretty_print import pretty_print_struct
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF

DiagCmd = DiagCmdCode.DiagCmd
KaitaiStream._ensure_bytes_left_to_write = lambda *args: True


class InputState(IntEnum):
    Initializing = 1
    Processing = 2
    Closed = 3


class BaseQCDMInput(GObject.Object):
    short_name = GObject.Property(type=str)
    full_name = GObject.Property(type=str)
    state = GObject.Property(type=int, default=InputState.Initializing)

    buffered_data: bytes = b''

    @GObject.Signal(
        arg_types=(object, object),
    )
    def frame_sent(self, request: DiagRequest, raw_frame: bytes):
        pass

    @GObject.Signal(
        arg_types=(object, object, int, int),
    )
    def frame_received(
        self,
        response: DiagResponse,
        raw_frame: bytes,
        num_frame: int,
        total_frames: int,
    ):
        if response.cmd_code == DiagCmd.cmd_ext_f:
            response = response.payload.payload

        if response.cmd_code == DiagCmd.log_f:
            self.log_received.emit(response.payload.inner_log, 1, 1)

    @GObject.Signal(
        arg_types=(object, int, int),
    )
    def log_received(self, log: DiagLogF, num_log: int, total_logs: int):
        pass

    @GObject.Signal
    def initialized(self):
        if self.state == InputState.Initializing:
            self.state = InputState.Processing

    @GObject.Signal
    def closed(self):
        self.state = InputState.Closed

    @abstractmethod
    def send_raw(self, data: bytes):
        pass

    @abstractmethod
    def process_stream(self, cancellable: Gio.Cancellable, background=True):
        pass

    @abstractmethod
    def close(self):
        pass

    def process_input(self, data: bytes, cancellable: Gio.Cancellable = None):
        debug('Demuxing pseudo-HDLC data: %r' % data)

        self.buffered_data += data

        total_frames = self.buffered_data.count(TRAILER_CHAR)
        num_frame = 0

        while TRAILER_CHAR in self.buffered_data:
            if cancellable and cancellable.is_cancelled():
                break
            payload, sep, self.buffered_data = self.buffered_data.partition(
                TRAILER_CHAR
            )
            if total_frames > 1:
                num_frame += 1
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
                    info(
                        'Successfully parsed Diag response: %s'
                        % sub(
                            r' logs_on_bitfield: .+',
                            ' logs_on_bitfield: [...]',
                            pretty_print_struct(resp),
                        )
                    )

                    GLib.idle_add(
                        self.frame_received.emit,
                        resp,
                        data,
                        num_frame,
                        total_frames,
                    )

    def send(self, request: DiagRequest):
        buf = BytesIO()
        stream = KaitaiStream(buf)
        request._write(stream)

        self.frame_sent.emit(request, buf.getvalue())

        hdlc_data = hdlc_encode(buf.getvalue())

        debug('Trying to send diag frame: %r' % hdlc_data)

        self.send_raw(hdlc_data)

    def send_recv(
        self,
        request: DiagRequest,
        callback: Callable[[DiagResponse], None],
        accept_error: bool = True,
        retry: bool = True,
        retry_delay: int = 4,
    ):
        def temp_callback(
            self,
            diag_response: DiagResponse,
            raw_response: bytes,
            num_frame: int,
            total_frames: int,
        ):
            nonlocal handler_id
            nonlocal timeout_id

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
                if timeout_id is not None:
                    GLib.source_remove(timeout_id)
                self.frame_received.disconnect(handler_id)

                callback(diag_response)

        if retry:

            def on_timeout():
                nonlocal timeout_id

                if self.state == InputState.Closed:
                    timeout_id = None
                    return GLib.SOURCE_REMOVE

                try:
                    warning(
                        'Receiving a response timed out, trying to re-send frame...'
                    )
                    self.send(request)

                except Exception as err:
                    error('Could not try to resend frame: %r' % err)
                    timeout_id = None
                    return GLib.SOURCE_REMOVE

                return GLib.SOURCE_CONTINUE

            timeout_id = GLib.timeout_add_seconds(retry_delay, on_timeout)

        else:
            timeout_id = None

        handler_id = self.frame_received.connect(temp_callback)
        self.send(request)

    def register_logs(self, bit_field: int):
        raise NotImplementedError
