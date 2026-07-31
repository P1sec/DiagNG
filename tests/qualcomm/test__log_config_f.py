#!/usr/bin/env python3
from diagng.protocol.qualcomm.struct.diag_log_config_f_req import (
    DiagLogConfigFReq,
)
from diagng.protocol.qualcomm.struct.diag_response import DiagResponse
from diagng.protocol.qualcomm.struct.diag_cmd_code import DiagCmdCode
from diagng.protocol.qualcomm.struct.diag_request import DiagRequest
from diagng.utils.kaitai_pretty_print import pretty_print_struct
from diagng.protocol.qualcomm.utils.hdlc import hdlc_encode

from kaitaistruct import KaitaiStream
from io import BytesIO

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True
DiagCmd = DiagCmdCode.DiagCmd


def test__retrieve_id_ranges_op():
    payload = DiagLogConfigFReq()
    payload.padding = b''
    payload.operation = DiagLogConfigFReq.Operation.retrieve_id_ranges_op

    action = DiagLogConfigFReq.RetrieveIdRanges(None, payload, payload._root)
    action._check()

    payload.action = action
    payload._check()

    diag_request = DiagRequest()
    diag_request.cmd_code = DiagCmd.log_config_f
    diag_request.payload = payload
    diag_request._check()

    buf = BytesIO()
    stream = KaitaiStream(buf)
    diag_request._write(stream)

    hdlc_data = hdlc_encode(buf.getvalue())

    assert hdlc_data == b's\x00\x00\x00\x01\x00\x00\x00a\x9d~'


"""
    ℹ️ See: https://pydevtools.com/handbook/tutorial/setting-up-testing-with-pytest-and-uv/
"""
