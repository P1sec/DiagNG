#!/usr/bin/python3

"""
This class should be able to either spawn
a Wireshark subprocess (possibly bypassing
the Flatpak sandbox) and piping PCAP
output to it, or either writing this output
to a on-disk PCAP file.

(Should be also support writing a
PCAP file wrapped in a .GZ stream, like
in QCSuper? If so, should it also
involve a different wrapper class?)

                => THIS SHALL BE INSTANCIED FROM: ⚠️ ⚠️ ➡️ℹ️tools.dlf_to_pcap + qcdm_window
                => HAVE METHODS BE CALLED FROM: ⚠️ ⚠️ XX    => ota_decoder.py ? ℹ️
                =>    AND IMPORT ;; => THE KAITAI PCAP+IP+UDP+GSMTAP encoder ?
                    ( ⚠️ MOVE FUNCTION FROM OTA_DECODER FOR ENCODING A GSMTAP HEADER)
                =>    AND CALL; :  ⚠️ XX


        # See: ➡️ "adb_client.py" and "spawn_diagmond.py" for a
        #  reference about how to INTERWORK with the Flatpak sandbox.

Cf. https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py
"""

from diagng.protocol.network.protocol_body import ProtocolBody
from diagng.protocol.network.udp_datagram import UdpDatagram
from diagng.protocol.network.ipv4_packet import Ipv4Packet
from diagng.protocol.network.gsmtap_v2 import GsmtapV2
from diagng.protocol.network.pcap import Pcap

from kaitaistruct import ReadWriteKaitaiStruct
from kaitaistruct import KaitaiStream
from gi.repository import Gio, GLib

from typing import Optional
from shutil import which
from os import getenv

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')


class PcapOutput:
    use_wireshark: bool
    output_file: str | None
    XX: XX  # TODO (WIP)

    def __init__(self, use_wireshark=False, output_file: str | None = None):
        self.use_wireshark = use_wireshark
        self.output_file = output_file

        pass # ⚠️ TODO spawn Wireshark with Gio async funcs if chosen options
        pass # ⚠️ TODO open file with Gio async funcs? if chosen option

    def spawn_wireshark(XX):
        XX

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

    def write_pcap_record(XX):
        XX
