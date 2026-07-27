#!/usr/bin/env python3

from diagng.protocol.qualcomm.struct.diag_log_config_f_req import (
    DiagLogConfigFReq,
)
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput
from diagng.protocol.qualcomm.struct.diag_response import DiagResponse
from diagng.protocol.qualcomm.struct.diag_cmd_code import DiagCmdCode
from diagng.protocol.qualcomm.struct.diag_logging import DiagLogging
from diagng.protocol.qualcomm.struct.diag_request import DiagRequest
from diagng.utils.kaitai_pretty_print import pretty_print_struct
from diagng.system.adb.adb_client import ADBResponse

from logging import info, debug, warning
from gi.repository import GObject, Gio
from typing import Callable, Optional

DiagCmd = DiagCmdCode.DiagCmd

# TODO 2026-07-20


class LogItem(GObject.Object):
    value = GObject.Property(type=int)


class LogRange(GObject.Object):
    min_value: GObject.Property(type=int)
    max_value: GObject.Property(type=int)

    def __init__(self, min_value: int, max_value: int):
        super().__init__()

        self.min_value = min_value
        self.max_value = max_value


class FullLogMask(GObject.Object):
    items = GObject.Property(type=Gio.ListStore)
    ranges = GObject.Property(type=Gio.ListStore)

    def __init__(self):
        super().__init__()

        self.items = Gio.ListStore.new(LogItem)
        self.ranges = Gio.ListStore.new(LogRange)

    def to_bytes(self) -> bytes:
        pass  # TODO


"""
    For now this class will support only
    single-stream logging configuration
    (configured via diag_cmd.log_config_f).

    Dual-stream logging configuration
    (via ext_log_config_req), F3/messages
    and event processing configuration
    should be implemented later.
"""


class LogManager(GObject.Object):
    # See https://github.com/P1sec/QCSuper/pull/149
    #     => Supports DIAG_QSR4_EXT_MSG_TERSE_F

    current_mask = GObject.Property(type=FullLogMask)

    source: BaseQCDMInput

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

    def __init__(self, source: BaseQCDMInput):
        super().__init__()

        self.current_mask = FullLogMask()
        self.source = source
        pass  # TODO

    def disable_logs(self, callback: Callable[[ADBResponse], None]):
        payload = DiagLogConfigFReq()
        payload.padding = b''
        payload.operation = DiagLogConfigFReq.Operation.disable_op

        payload.payload = DiagLogConfigFReq.Disable()
        payload.payload._root = payload._root
        payload.payload._parent = payload

        payload.payload._check()
        payload._check()

        diag_request = DiagRequest()
        diag_request.cmd_code = DiagCmd.log_config_f
        diag_request.payload = payload
        diag_request._check()

        def req_cb(response: DiagResponse):
            info(
                'DiagResponse received for DiagCmd.log_config_f: %r' % response
            )

            debug(
                'Parsed DiagCmd.log_config_f response: %s',
                pretty_print_struct(response),
            )

            callback(response)

        self.source.send_recv(
            diag_request, req_cb, accept_error=True, retry=True, retry_delay=2
        )

    def get_supported_log_ranges(
        self, callback: Callable[[ADBResponse, Optional[FullLogMask]], None]
    ):
        # TODO
        # 1. Send: ➡️ diag_log_config_f_req + retrieve_id_ranges_op
        # 2. Handle value into internal callback
        # 3. Pass [ADBResponse, Optional[FullLogMask]] value to internal callback

        payload = DiagLogConfigFReq()
        payload.padding = b''
        payload.operation = DiagLogConfigFReq.Operation.retrieve_id_ranges_op

        payload.payload = DiagLogConfigFReq.RetrieveIdRanges()
        payload.payload._root = payload._root
        payload.payload._parent = payload

        payload.payload._check()
        payload._check()

        diag_request = DiagRequest()
        diag_request.cmd_code = DiagCmd.log_config_f
        diag_request.payload = payload
        diag_request._check()

        def req_cb(response: DiagResponse):
            info(
                'DiagResponse received for DiagCmd.log_config_f: %r' % response
            )

            # ⚠️ TODO ➡️ Add due error HANDLING Here?

            debug(
                'Parsed DiagCmd.log_config_f response: %s',
                pretty_print_struct(response),
            )

            for equip_id_raw, max_item in enumerate(
                response.payload.payload.last_item
            ):
                if not max_item:
                    continue
                try:
                    equip_id = DiagLogging.EquipmentId(equip_id_raw)
                except Exception:
                    warning('Unknown equipment ID: %d', equip_id_raw)
                else:
                    info(
                        'Max item for %s (0x%x) = %03x'
                        % (equip_id.name, equip_id.value, max_item)
                    )

            debug(
                'All received max items: %r / %r',
                list(DiagLogging.EquipmentId),
                response.payload.payload.last_item,
            )

            log_mask_todo = None  # XX

            # =+> TODO add retrieve_valid_mask_op
            # queries here? ⚠️

            callback(response, log_mask_todo)

        self.source.send_recv(
            diag_request, req_cb, accept_error=True, retry=True, retry_delay=2
        )

    def register_ota_related_logs(
        self, callback: Callable[[ADBResponse], None]
    ):
        pass  # ⚠️ == ➡️ ➡️ NEXT WIP ⬅️ ⬅️ ==

    def register_logs(
        self, log_codes: FullLogMask, callback: Callable[[ADBResponse], None]
    ):
        pass  # TODO

    def unregister_logs(
        self, log_codes: FullLogMask, callback: Callable[[ADBResponse], None]
    ):
        pass  # TODO

    def get_full_log_mask(
        self, callback: Callable[[ADBResponse, Optional[FullLogMask]], None]
    ):
        pass  # TODO
