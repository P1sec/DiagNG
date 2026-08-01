#!/usr/bin/env python3

from diagng.protocol.qualcomm.struct.gsm_rr_signaling_message import (
    GsmRrSignalingMessage,
)
from diagng.protocol.qualcomm.struct.wcdma_signaling_message import (
    WcdmaSignalingMessage,
)
from diagng.protocol.qualcomm.struct.diag_logging import DiagLogging
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF
from diagng.protocol.qualcomm.struct.gsmtap_v2 import GsmtapV2

from kaitaistruct import ReadWriteKaitaiStruct
from typing import Optional
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

    def write_gsmtap_packet(
        self,
        packet_type: GsmtapV2.PacketType,
        sub_type: ReadWriteKaitaiStruct,
        data: bytes,
        is_uplink: bool = False,
        arfcn: Optional[int] = 0,
    ):
        packet = GsmtapV2()
        packet.version = 2
        packet.header_len = 4
        packet.type = packet_type
        packet.timeslot = 0

        packet.pcs_band = False
        packet.is_uplink = is_uplink
        packet.arfcn = arfcn
        packet.signal_dbm = 0
        packet.snr_db = 0

        packet.frame_number = 0

        packet.sub_type = sub_type
        packet.antenna_nr = 0
        packet.sub_slot = 0
        packet.res = 0

        packet.data = data

        packet._check()

        pass  # WIP 🪧 write to self.pcap_stream

    def handle_log(self, log: DiagLogF.InnerLog):

        code: DiagLogging.LogCode = log.log_code

        if code == DiagLogging.LogCode.wcdma_signaling_message:  # 0x412f
            msg: WcdmaSignalingMessage = log.content

            PacketType = WcdmaSignalingMessage.PacketType
            ChannelType = WcdmaSignalingMessage.ChannelType
            UmtsRrcSubtype = GsmtapV2.UmtsRrcSubtype

            self.current_rat = RATType.RAT_3G

            if (
                msg.packet_type != PacketType.special
                and msg.channel_type < ChannelType.rrclog_extension_sib
            ):
                # Frames containing only a MIB or extension SIB
                # are already present in RRC frames, ignore them
                sub_type = WcdmaSignalingMessage.UmtsRrcSubtypeField()
                sub_type.umts_rrc_subtype = {
                    ChannelType.rrclog_sig_ul_ccch: UmtsRrcSubtype.ul_ccch_message,
                    ChannelType.rrclog_sig_ul_dcch: UmtsRrcSubtype.ul_dcch_message,
                    ChannelType.rrclog_sig_dl_ccch: UmtsRrcSubtype.dl_ccch_message,
                    ChannelType.rrclog_sig_dl_dcch: UmtsRrcSubtype.dl_dcch_message,
                    ChannelType.rrclog_sig_dl_bcch_bch: UmtsRrcSubtype.bcch_bch_message,
                    ChannelType.rrclog_sig_dl_bcch_fach: UmtsRrcSubtype.bcch_fach_message,
                    ChannelType.rrclog_sig_dl_pcch: UmtsRrcSubtype.pcch_message,
                    ChannelType.rrclog_sig_dl_mcch: UmtsRrcSubtype.mcch_message,
                    ChannelType.rrclog_sig_dl_msch: UmtsRrcSubtype.msch_message,
                }[msg.channel_type]
                sub_type._check()

                if msg.packet_type == PacketType.explicit_arfcn_psc:
                    arfcn = msg.uarfcn & 0x3F
                else:
                    arfcn = 0

                self.write_gsmtap_packet(
                    GsmtapV2.PacketType.umts_rrc,
                    sub_type,
                    msg.message,
                    msg.is_uplink,
                    arfcn,
                )

        elif code == DiagLogging.LogCode.gsm_rr_signaling_message:  # 0x512f
            msg: GsmRrSignalingMessage = log.content

            # See gsm_rr_channel_type_map:
            # https://github.com/wireshark/wireshark/blob/60851bf/epan/dissectors/packet-qcdiag_log.c#L333

            # See:
            # https://github.com/fgsect/scat/blob/v2.0.0/src/scat/parsers/qualcomm/diaggsmlogparser.py#L257

            # See:
            # https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py#L222

            self.current_rat = RATType.RAT_2G

            sub_type = {WIP}.get(msg.channel_type)

            if not sub_type:
                raise 'xx'

            # Diag is delivering us L3 data, but GSMTAP will want L2 for most
            # channels (including a LAPDm header that we don't have), the
            # workaround for this is to set the interface type to A-bis.

            # Other channels that include just a L2 pseudo length before their
            # protocol discriminator will have it removed.

            self.write_gsmtap_packet(
                GsmtapV2.PacketType.abis,
                sub_type,
                msg.message,
                not msg.is_downlink,
            )

        elif isinstance(log.content, bytes):
            # ⚠️ This requires Wireshark 4.7 or above:
            # https://github.com/wireshark/wireshark/blob/v4.7.0/epan/dissectors/packet-qcdiag_log.c

            self.write_gsmtap_packet(
                GsmtapV2.PacketType.qc_diag,
                None,
                log.content,
                False,
            )
            pass  # TODO
