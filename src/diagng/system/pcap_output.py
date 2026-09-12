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

from diagng.gobject.abstract.file_out_mode_selector import (
    FileOutModeSelector,
    FileOutMode,
)
from diagng.protocol.qualcomm.struct.diag_response import DiagResponse
from diagng.protocol.qualcomm.struct.diag_cmd_code import DiagCmdCode
from diagng.protocol.qualcomm.struct.diag_request import DiagRequest
from diagng.utils.kaitai_pretty_print import pretty_print_struct
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF
from diagng.protocol.network.protocol_body import ProtocolBody
from diagng.protocol.network.udp_datagram import UdpDatagram
from diagng.protocol.network.ipv4_packet import Ipv4Packet
from diagng.protocol.network.gsmtap_v3 import GsmtapV3
from diagng.protocol.network.gsmtap_v2 import GsmtapV2
from diagng.protocol.network.gsmtap import Gsmtap
from diagng.protocol.network.pcap import Pcap

from kaitaistruct import ReadWriteKaitaiStruct
from kaitaistruct import KaitaiStream
from gi.repository import Gio, GObject, GLib
from re import search

from typing import Optional, Callable, Union
from logging import error, debug, info
from traceback import format_exc
from shutil import which
from io import BytesIO
from time import time
from os import getenv

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')

GSMTAP_PORT = 4729

DiagCmd = DiagCmdCode.DiagCmd


class StreamState(GObject.GEnum):
    Initializing = 1
    Available = 2
    Closed = 3


class PcapOutput(GObject.GObject):
    use_wireshark = GObject.Property(type=bool, default=False)

    header: Optional[Pcap]

    wireshark_proc = GObject.Property(type=Gio.Subprocess)
    file_path = GObject.Property(type=str)
    output_file = GObject.Property(type=Gio.File)
    output_stream = GObject.Property(type=Gio.OutputStream)

    stream_state = GObject.Property(
        type=StreamState, default=StreamState.Initializing
    )  # WIP ⚠

    @GObject.Signal
    def stream_active(self):
        self.stream_state = StreamState.Available

    @GObject.Signal
    def stream_closed(self):
        self.stream_state = StreamState.Closed

        if self.output_stream:
            self.output_stream.close_async(GLib.PRIORITY_DEFAULT, None, None)
            self.output_stream = None

    def __init__(
        self,
        use_wireshark: bool = False,
        mode_selector: Optional[FileOutModeSelector] = None,
        output_file: Optional[str] = None,
    ):
        super().__init__()

        self.use_wireshark = use_wireshark
        self.mode_selector = mode_selector
        self.file_path = output_file

    def open_stream(self):
        if self.use_wireshark:
            self.spawn_wireshark()
        else:

            def callback(selected_mode: FileOutMode):
                self.output_file = Gio.File.new_for_path(self.file_path)
                # ⚠️ Maybe we should support appending to the file too?
                self.output_file.XX  #  ⚠️ ⚠️ TODO: ACTUALLY SET UP A FILE HERE
                #    => Use replace_readwrite_async ?
                #       OR append_to_async / open_readwrite_async ?

                # => ⚠️ SHOULD WE prompt THE USER ON
                #  WHETHER TO REPLACE THE FILE OR
                #  APPEND TO IT WHENEVER IT EXISTS?

                #   => ⚠️ 🪧 ADD
                #    - AN INTERACTIVE CLI PROMPT PATH
                #    - AN EXPLICIT, NON-INTERACTIVE CLI PROMPT PATH (THROUGH ARGPARSE)
                #    - AN INTERACTIVE GUI PROMPT PATH

            self.mode_selector.query_file_out_mode(callback)

        pass  # ⚠️ TODO spawn Wireshark with Gio async funcs if chosen options
        pass  # ⚠️ TODO open file with Gio async funcs? if chosen option

    @staticmethod
    def check_wireshark_version(callback: Callable[[Optional[str]], []]):

        try:
            child = Gio.Subprocess.new(
                (['flatpak-spawn', '--host'] if IS_FLATPAK else [])
                + ['wireshark', '--version'],
                Gio.SubprocessFlags.STDOUT_PIPE,
            )
        except Exception:
            callback(None)

        def on_complete(child: Gio.Subprocess, res: Gio.AsyncResult):
            success, stdout_buf, stderr_buf = child.communicate_utf8_finish(
                res
            )

            debug('Got output from "wireshark --version": %r', stdout_buf)

            if not success:
                callback(None)
            ver_string = search(r'Wireshark (\d\S+)', stdout_buf)
            if not ver_string:
                callback(None)
            ver_string = ver_string.group(1).strip('.')
            callback(ver_string)

        child.communicate_utf8_async(None, None, on_complete)

        # ⚠️ ➡️➡️ LATER: Think to install the _5G decoding Lua plug-in_
        #       for Wireshark somewhere?

        # ℹ️ How do we device between
        #  Gio.Subprocess
        # and
        # GLib.spawn_async_* ?

        #  => Gio.Subprocess has an object model but
        #     GLib.spawn_async_* can have a preexec function

        #      => ⚠️ Is `setpgrp` required for an independant
        #         process group (SIGINT handling?)

        # ^ ⚠️ <== THiS SHOULD EVENTUALLY PROVIDE SOME KIND OF UI FEEDBACK? ⚠️
        # (=> CURRENT WIP 2026-08-06)

    def spawn_wireshark(self):

        # TODO: SEE: https://lazka.github.io/pgi-docs/Gio-2.0/classes/SubprocessLauncher.html
        # https://lazka.github.io/pgi-docs/Gio-2.0/classes/SubprocessLauncher.html
        self.wireshark_proc = Gio.Subprocess.new(
            (['flatpak-spawn', '--host'] if IS_FLATPAK else [])
            + ['wireshark', '-k', '-i', '-'],
            flags=Gio.SubprocessFlags.STDIN_PIPE,
        )

        proc_pid = self.wireshark_proc.get_identifier()

        self.output_stream = self.wireshark_proc.get_stdin_pipe()

        def terminate_cb(*args):
            debug('Wireshark subprocess %s terminated' % proc_pid)
            self.close()

        self.wireshark_proc.wait_async(
            None, terminate_cb
        )  # Close callback (TODO)

        self.write_pcap_header()

    def write_pcap_header(self):

        header = Pcap()
        header.magic_number = Pcap.Magic.le_microseconds

        # Cf. https://ietf-opsawg-wg.github.io/draft-ietf-opsawg-pcap/draft-ietf-opsawg-pcap.html

        sub_header = Pcap.Header(None, header, header._root)
        sub_header._is_le = True
        sub_header.version_major = 2
        sub_header.version_minor = 4
        sub_header.thiszone = 0
        sub_header.sigfigs = 0
        sub_header.snaplen = 65535
        sub_header.network = Pcap.Linktype.raw  # IPv4/IPv6 auto-detect
        sub_header._check()

        header.hdr = sub_header
        header.packets = []
        header._check()

        buf = BytesIO()
        stream = KaitaiStream(buf)
        header._write(stream)

        data = buf.getvalue()

        self.header = header

        if self.output_stream:
            try:
                self.output_stream.write_all(data, None)
            except Exception:
                error('Failed to write PCAP header to stream: ' + format_exc())
                self.close()
            else:
                self.output_stream.flush(None)
                info(
                    'Wrote PCAP header to stream: '
                    + pretty_print_struct(header)
                )
                self.stream_active.emit()

    def write_gsmtap_v3_packet(
        self,
        packet_type: GsmtapV3.Type,
        sub_type: Union[ReadWriteKaitaiStruct, int],
        data: bytes,
        is_uplink: bool = False,
        arfcn: Optional[int] = 0,
        # ⚠️⚠️ 🪧 ➡️ TODO make timestamp a dedicated argument instead of inferring it poorly
    ):
        packet = Gsmtap()
        packet.version = 3

        content = GsmtapV3()
        content.reserved = 0

        content.type = packet_type
        content.subtype = sub_type

        # Add metadata tags:

        # 0x0002: Channel number (inc. downlink bit) = (u4) (arcfn | (is_uplink << 31))

        channel_tag = GsmtapV3.ChannelNumber()
        channel_tag.is_uplink = is_uplink
        channel_tag.arfcn = arfcn
        channel_tag._check()

        content.metadata = [channel_tag]
        content.data = data

        content.header_len = 4  # 2x32 bits header + 1 T16L16V32 metadata field
        packet.content = content

        content._check()
        packet._check()

        self.write_gsmtap_packet(packet, data)

    def write_gsmtap_v2_packet(
        self,
        packet_type: GsmtapV2.PacketType,
        sub_type: Union[ReadWriteKaitaiStruct, int],
        data: Union[bytes, DiagLogF.InnerLog, DiagRequest, DiagResponse],
        is_uplink: bool = False,
        arfcn: Optional[int] = 0,
    ):
        packet = Gsmtap()
        packet.version = 2

        content = GsmtapV2()
        content.header_len = 4
        content.type = packet_type
        content.timeslot = 0

        content.pcs_band = False
        content.is_uplink = is_uplink
        content.arfcn = arfcn
        content.signal_dbm = 0
        content.snr_db = 0

        content.frame_number = 0

        if isinstance(sub_type, ReadWriteKaitaiStruct):
            sub_type._parent = content
            sub_type._root = content._root
            sub_type._check()
        content.sub_type = sub_type

        content.antenna_nr = 0
        content.sub_slot = 0
        content.res = 0

        if isinstance(data, bytes):
            content.data = data
        elif isinstance(data, DiagRequest):
            diag_payload = GsmtapV2.DiagPayload(
                True, None, content, content._root
            )

            diag_payload.frame = data
            diag_payload._check()

            content.data = diag_payload
        elif isinstance(data, DiagResponse):
            diag_payload = GsmtapV2.DiagPayload(
                False, None, content, content._root
            )

            diag_payload.frame = data
            diag_payload._check()

            content.data = diag_payload
        elif isinstance(data, DiagLogF.InnerLog):
            diag_payload = GsmtapV2.DiagPayload(
                False, None, content, content._root
            )

            diag_log = DiagLogF()
            diag_log.pending_msgs = 0
            diag_log.len_inner_log = data.log_inner_length
            diag_log.inner_log = data
            data._parent = diag_log
            data._root = diag_log._root
            data._check()
            diag_log._check()

            diag_resp = DiagResponse()
            diag_resp.cmd_code = DiagCmd.log_f
            diag_resp.payload = diag_log
            diag_resp._check()

            diag_payload.frame = diag_resp
            diag_payload._check()

            content.data = diag_payload

        content._check()

        packet.content = content
        packet._check()

        self.write_gsmtap_packet(packet, data)

    def write_gsmtap_packet(
        self,
        packet: Gsmtap,
        data: Union[bytes, DiagLogF.InnerLog, DiagRequest, DiagResponse],
    ):
        # Write UDP header

        buf = BytesIO()
        stream = KaitaiStream(buf)
        packet._write(stream)

        encoded_packet = buf.getvalue()

        udp = UdpDatagram()
        udp.src_port = GSMTAP_PORT
        udp.dst_port = GSMTAP_PORT
        udp.length = len(encoded_packet) + 8
        udp.checksum = 0  # TODO ?
        udp.body = packet
        udp._check()

        # Write IPv4 header

        ipv4 = Ipv4Packet()
        ipv4.b1 = 0x45
        ipv4.b2 = 0x00
        ipv4.total_length = len(encoded_packet) + 8 + 4 * 5
        ipv4.identification = 0
        ipv4.b67 = 0
        ipv4.ttl = 64
        ipv4.protocol = ProtocolBody.ProtocolEnum.udp
        ipv4.header_checksum = 0  # TODO ?
        ipv4.src_ip_addr = bytes([127, 0, 0, 1])
        ipv4.dst_ip_addr = bytes([127, 0, 0, 1])

        options = Ipv4Packet.Ipv4Options(None, ipv4, ipv4._root)
        options.entries = []
        options._check()
        ipv4.options = options

        body = ProtocolBody(ipv4.protocol, None, ipv4, ipv4._root)
        body.body = udp
        body._check()
        ipv4.body = body

        ipv4._check()

        if isinstance(data, DiagLogF.InnerLog):
            self.write_ipv4_record(ipv4, data.unix_ts)
        elif isinstance(data, DiagResponse) and data.cmd_code == DiagCmd.log_f:
            self.write_ipv4_record(ipv4, data.payload.inner_log.unix_ts)
        else:
            self.write_ipv4_record(ipv4, time())

    def write_ipv4_record(self, ipv4: Ipv4Packet, timestamp: float = 0.0):
        packet = Pcap.Packet(None, self.header, self.header._root)

        body = ProtocolBody(ProtocolBody.ProtocolEnum.ipv4)
        body.body = ipv4
        body._check()

        packet._is_le = True
        packet.ts_sec = int(timestamp)
        packet.ts_usec = int((timestamp * 1_000_000) % 1_000_000)
        packet.incl_len = ipv4.total_length
        packet.orig_len = ipv4.total_length
        packet.body = body
        packet._check()

        # Write PCAP to output buffer

        buf = BytesIO()
        stream = KaitaiStream(buf)
        packet._write(stream)

        encoded_packet = buf.getvalue()

        if self.output_stream:
            try:
                self.output_stream.write_all(encoded_packet, None)
            except Exception:
                error('Failed to write PCAP packet to stream: ' + format_exc())
                self.close()
            else:
                self.output_stream.flush(None)
                # DEBUG write record to stderr here
                debug('Wrote packet to PCAP: ' + pretty_print_struct(packet))

    def close(self):
        self.stream_closed.emit()
