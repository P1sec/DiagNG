#!/usr/bin/env python3

from diagng.protocol.qualcomm.struct.gsm_rr_signaling_message import (
    GsmRrSignalingMessage,
)
from diagng.protocol.qualcomm.struct.wcdma_signaling_message import (
    WcdmaSignalingMessage,
)
from diagng.protocol.qualcomm.acquisition.base_input import BaseQCDMInput
from diagng.protocol.qualcomm.struct.diag_logging import DiagLogging
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF
from diagng.protocol.network.gsmtap_v2 import GsmtapV2
from diagng.system.pcap_output import PcapOutput

from enum import IntEnum


class RATType(IntEnum):
    RAT_2G = 1
    RAT_3G = 2
    RAT_4G = 3
    RAT_5G = 4


class OTADecoder:
    # ⚠️ TODO use a GIO I/O channel to plug the PCAP GSMTAP
    # stream to either a subprocess pipe or a PCAP file?

    pcap_stream: PcapOutput
    input_obj: BaseQCDMInput
    current_rat: RATType = None

    def __init__(self, pcap_stream, input_obj):
        self.pcap_stream = pcap_stream
        self.input_obj = input_obj

        def on_log(input_obj: BaseQCDMInput, log: DiagLogF.InnerLog):
            self.handle_log(log)

        self.input_obj.log_received.connect(on_log)

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

                self.pcap_stream.write_gsmtap_packet(
                    GsmtapV2.PacketType.umts_rrc,
                    sub_type,
                    msg.message,
                    msg.is_uplink,
                    arfcn,
                )

        elif code == DiagLogging.LogCode.gsm_rr_signaling_message:  # 0x512f
            msg: GsmRrSignalingMessage = log.content

            ChannelType = GsmRrSignalingMessage.ChannelType
            GsmRrSubtype = GsmtapV2.GsmRrSubtype

            # See:
            # https://github.com/fgsect/scat/blob/v2.0.0/src/scat/parsers/qualcomm/diaggsmlogparser.py#L257

            # See gsm_rr_channel_type_map:
            # https://github.com/wireshark/wireshark/blob/v4.7.2/epan/dissectors/packet-qcdiag_log.c#L333

            # See: gsmtap_channels
            # https://github.com/wireshark/wireshark/blob/v4.7.2/epan/dissectors/packet-gsmtap.c#L297

            # See: gsmtap_gsm_channel_names
            # https://github.com/osmocom/libosmocore/blob/1.14.1/src/core/gsmtap_util.c#L586

            # See:
            # https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py#L222

            self.current_rat = RATType.RAT_2G

            sub_type = {
                ChannelType.dcch: GsmRrSubtype.sdcch8,  # sdcch8 in SCAT and WS 4.7, sdcch in QCSuper - investigate the choice?
                ChannelType.bcch: GsmRrSubtype.bcch,
                ChannelType.l2_rach: GsmRrSubtype.rach,
                ChannelType.ccch: GsmRrSubtype.ccch,
                ChannelType.sacch: GsmRrSubtype.sacch8,  # sacch8 in SCAT and WS 4.7, lsacch in QCSuper - investigate the choice?
                ChannelType.sdcch: GsmRrSubtype.sdcch,
                ChannelType.facch_f: GsmRrSubtype.facch_f,  # facch_f in WS 4.7, sacch_f in QCSuper - a mistake?
                ChannelType.facch_h: GsmRrSubtype.facch_h,  # sacch_h in QCSuper - a mistake?
                ChannelType.l2_rach_with_no_delay: GsmRrSubtype.rach,
            }[msg.channel_type]

            # Diag is delivering us L3 data, but GSMTAP will want L2 for most
            # channels (including a LAPDm header that we don't have), the
            # workaround for this is to set the interface type to A-bis.

            # (NOTE: It's a hack, SCAT and WS 4.7 reconstruct a LAPDm header
            # instead of doing this, and reassemble an ARFCN from the
            # traffic flow, maybe that we should do the same)

            # Other channels that include just a L2 pseudo length before their
            # protocol discriminator will have it removed.

            data = msg.message

            if msg.channel_type in [ChannelType.bcch, ChannelType.ccch]:
                data = data[1:]

            self.pcap_stream.write_gsmtap_packet(
                GsmtapV2.PacketType.abis,
                sub_type,
                data,
                not msg.is_downlink,
            )

        elif isinstance(log.content, bytes):
            # ⚠️ This requires Wireshark 4.7 or above:
            # https://github.com/wireshark/wireshark/blob/v4.7.0/epan/dissectors/packet-qcdiag_log.c

            self.pcap_stream.write_gsmtap_packet(
                GsmtapV2.PacketType.qc_diag,
                0,
                log,
                False,
            )
            pass  # TODO
