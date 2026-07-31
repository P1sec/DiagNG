#!/usr/bin/env python3

from diagng.protocol.qualcomm.struct.wcdma_signaling_message import (
    WcdmaSignalingMessage,
)
from diagng.protocol.qualcomm.struct.diag_logging import DiagLogging
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF

from enum import IntEnum


class RATType(IntEnum):
    RAT_2G = 1
    RAT_3G = 2
    RAT_4G = 3
    RAT_5G = 4


class OTADecoder:
    # ⚠️ TODO use a GIO I/O channel to plug the PCAP GSMTAP
    # stream to either a subprocess pipe or a PCAP file?

    pcap_stream: XX
    current_rat: RATType = None

    def __init__(self):
        self.pcap_stream = XX

        pass  # ➡️ 🪧 WIP

    def write_gsmtap_log(self, XX):
        pass  # WIP

    def handle_log(self, log: DiagLogF.InnerLog):

        code: DiagLogging.LogCode = log.log_code

        if code == DiagLogging.LogCode.wcdma_signaling_message:
            data: WcdmaSignalingMessage = log.content

            self.current_rat = RATType.RAT_3G

            # WIP

        elif XX:
            pass  # TODO
