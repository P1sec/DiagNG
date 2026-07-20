#!/usr/bin/env python3

from diagng.protocol.qualcomm.acquisition.input import BaseInput

# TODO 2026-07-20


class LogManager:
    # See https://github.com/P1sec/QCSuper/pull/149
    #     => Supports DIAG_QSR4_EXT_MSG_TERSE_F

    # See protocol docs ?

    # List opcodes to support:
    # XX

    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/modules/_enable_log_mixin.py
    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/modules/pcap_dump.py
    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/inputs/_base_input.py

    source: BaseInput

    def __init__(self, source: BaseInput):
        self.source = source
        pass  # TODO

    def register_logs(self, log_mask):
        pass  # TODO

    def unregister_logs(self, log_mask):
        pass  # TODO
