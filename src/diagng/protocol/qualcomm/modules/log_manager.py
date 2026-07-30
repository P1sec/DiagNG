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
from collections import defaultdict

DiagCmd = DiagCmdCode.DiagCmd

# TODO 2026-07-20


"""
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


TYPES_FOR_RAW_PACKET_LOGGING = [
    # Layer 2:
    DiagLogging.LogCode.gprs_mac_signaling_message,  # 0x5226
    # Layer 3:
    DiagLogging.LogCode.gsm_rr_signaling_message,  # 0x512f
    DiagLogging.LogCode.wcdma_signaling_messages,  # 0x412f
    DiagLogging.LogCode.lte_rrc_ota_packet,  # 0xb0c0
    DiagLogging.LogCode.nr5g_rrc_ota_packet,  # 0xb821
    # NAS:
    DiagLogging.LogCode.umts_ue_ota,  # 0x713a
    DiagLogging.LogCode.lte_nas_esm_plain_ota_incoming_message,  # 0xb0e2
    DiagLogging.LogCode.lte_nas_esm_plain_ota_outgoing_message,  # 0xb0e3
    DiagLogging.LogCode.lte_nas_emm_plain_ota_incoming_message,  # 0xb0ec
    DiagLogging.LogCode.lte_nas_emm_plain_ota_outgoing_message,  # 0xb0ed
]

# User IP traffic (DPL):
# Data arrives on 0x11EB, but registering the extended Network IP codes
# is required to trigger DPL delivery on some basebands.
TYPES_FOR_IP_TRAFFIC_LOGGING = [
    DiagLogging.LogCode.data_protocol_logging,  # 0x11eb
    DiagLogging.LogCode.data_protocol_logging_network_ip_rm_tx_full,  # 0x1574
    DiagLogging.LogCode.data_protocol_logging_network_ip_rm_rx_full,  # 0x1575
]


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

    # current_mask = GObject.Property(type=FullLogMask)

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

        # self.current_mask = FullLogMask()
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
        self,
        callback: Callable[[ADBResponse], None],  # , Optional[FullLogMask]
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

            # log_mask_todo = None  # XX

            # =+> TODO add retrieve_valid_mask_op
            # queries here? ⚠️

            callback(response)  # , log_mask_todo

        self.source.send_recv(
            diag_request, req_cb, accept_error=True, retry=True, retry_delay=2
        )

    def register_ota_related_logs(
        self, callback: Callable[[ADBResponse], None]
    ):
        # See TYPES_FOR_RAW_PACKET_LOGGING = [
        #  https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/_enable_log_mixin.py#L48

        # log_mask = FullLogMask()

        all_log_codes = set(
            map(
                int,
                TYPES_FOR_RAW_PACKET_LOGGING + TYPES_FOR_IP_TRAFFIC_LOGGING,
            )
        )

        self.register_logs(all_log_codes, callback)

    def register_logs(
        self, log_codes: set[int], callback: Callable[[ADBResponse], None]
    ):
        sheduled_diag_requests: list[DiagRequest] = []

        last_diag_response: Optional[ADBResponse] = None

        equip_id_to_log_codes: dict[int, list[int]] = defaultdict(list)
        for log_code in sorted(log_codes):
            equip_id_to_log_codes[log_code >> 12].append(log_code)

        for equip_id, log_codes in sorted(equip_id_to_log_codes.items()):
            bit_field: list[bool] = [False] * ((max(log_codes) & 0x0FFF) + 1)
            for log_code in log_codes:
                bit_field[log_code & 0x0FFF] = True

            payload = DiagLogConfigFReq()
            payload.padding = b''
            payload.operation = DiagLogConfigFReq.Operation.set_mask_op

            payload.payload = DiagLogConfigFReq.SetMask()
            payload.payload._root = payload._root
            payload.payload._parent = payload

            payload.payload.log_mask = DiagLogConfigFReq.LogMask()
            payload.payload.log_mask._root = payload._root
            payload.payload.log_mask._parent = payload.payload

            payload.payload.log_mask.equipment_id = equip_id
            payload.payload.log_mask.logs_on_bitfield = bit_field
            payload.payload.log_mask.num_logs_on_bitfield = len(bit_field)

            payload.payload.log_mask._check()
            payload.payload._check()
            payload._check()

            diag_request = DiagRequest()
            diag_request.cmd_code = DiagCmd.log_config_f
            diag_request.payload = payload
            diag_request._check()

            sheduled_diag_requests.append(diag_request)

        def process_next_request():
            if not sheduled_diag_requests:
                callback(last_diag_response)
                return

            next_request = sheduled_diag_requests.pop(0)

            def req_cb(response: DiagResponse):
                info(
                    'DiagResponse received for DiagCmd.log_config_f: %r'
                    % response
                )

                # ⚠️ TODO Handle error

                debug(
                    'Parsed DiagCmd.log_config_f response: %s',
                    pretty_print_struct(response),
                )

                nonlocal last_diag_response
                last_diag_response = response

                process_next_request()

            self.source.send_recv(
                next_request,
                req_cb,
                accept_error=True,
                retry=True,
                retry_delay=2,
            )

        process_next_request()

        pass  # ⚠️ == ➡️ ➡️ NEXT WIP ⬅️ ⬅️ ==

    """
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
    """
