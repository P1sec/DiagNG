#!/usr/bin/env python3

from diagng.protocol.qualcomm.acquisition.input import BaseInput

# TODO 2026-07-20


class LogManager:
    # See https://github.com/P1sec/QCSuper/pull/149
    #     => Supports DIAG_QSR4_EXT_MSG_TERSE_F

    # See protocol docs ?

    # List opcodes to examinate:
    # - logmask_f
    # - log_f
    # - ext_logmask_f obsoleted by log_config_f
    # - ext_msg_f, trace_event_report_f,
    #   log_on_demand_ext_f, event_mask_set_f,
    #   event_mask_get_f, ext_msg_terse_xlate_f,
    #   ext_msg_terse_f, ext_msg_config_f, etc.
    # - log_sec_f ?
    # - msg_small_f ?
    # - qsr4_ext_msg_terse_f ?
    # - cmd_ext_f ?
    # XX

    # Look at SCAT code?
    # => https://github.com/fgsect/scat/tree/master/src/scat/parsers/qualcomm
    # Look at MobileInsight code?
    # => https://github.com/search?q=org%3Amobile-insight%20diag_log&type=code

    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/modules/_enable_log_mixin.py
    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/modules/pcap_dump.py
    # See https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/inputs/_base_input.py

    # + http://ne-virtualization.dmz.intl.p1sec.io/
    # ssh ne-virtualization

    # Action points:
    # a) Document protocol-related things e.g on a wiki or through MD files?
    # b) Implement only one opcode pair at once (e.g DIAG_LOG_F first)?
    # c) First try to implement the shortest circuit to handling
    #    DIAG_LOG_F towards printing logs to stderr, then the
    #    shortest circuit to having to a having OTA messages
    #    encapsulated into a PCAP file, etc.?

    source: BaseInput

    def __init__(self, source: BaseInput):
        self.source = source
        pass  # TODO

    def register_logs(self, log_mask):
        pass  # TODO

    def unregister_logs(self, log_mask):
        pass  # TODO
