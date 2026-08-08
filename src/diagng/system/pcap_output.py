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

from diagng.protocol.qualcomm.struct.diag_response import DiagResponse
from diagng.protocol.qualcomm.struct.diag_cmd_code import DiagCmdCode
from diagng.protocol.qualcomm.struct.diag_request import DiagRequest
from diagng.protocol.qualcomm.struct.diag_log_f import DiagLogF
from diagng.protocol.network.protocol_body import ProtocolBody
from diagng.protocol.network.udp_datagram import UdpDatagram
from diagng.protocol.network.ipv4_packet import Ipv4Packet
from diagng.protocol.network.gsmtap_v2 import GsmtapV2
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
from os import getenv

KaitaiStream._ensure_bytes_left_to_write = lambda *args: True

# To use inside a Flatpak sandbox:
IS_FLATPAK = getenv('container') and which('flatpak-spawn')

DiagCmd = DiagCmdCode.DiagCmd


class StreamState(GObject.GEnum):
    Initializing = 1
    Available = 2
    Closed = 3


class PcapOutput(GObject.GObject):
    use_wireshark = GObject.Property(type=bool, default=False)

    wireshark_proc = GObject.Property(type=Gio.Subprocess)
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

    def __init__(self, use_wireshark=False, output_file: Optional[str] = None):
        super().__init__()

        self.use_wireshark = use_wireshark

        if use_wireshark:
            self.spawn_wireshark()
        else:
            self.output_file = Gio.File.new_for_path(output_file)
            # ⚠️ Maybe we should support appending to the file too?
            self.create_async  #  ⚠️ ⚠️ WIP

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

        self.output_stream = self.wireshark_proc.get_stdin_pipe()

        def terminate_cb(*args):
            debug(
                'Wireshark subprocess %s terminated'
                % self.wireshark_proc.get_identifier()
            )
            self.wireshark_proc = None
            self.output_stream = None
            self.stream_active.emit()

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

        if self.output_stream:

            def write_cb(stream: Gio.OutputStream, res: Gio.AsyncResult):
                try:
                    stream.write_all_finish(res)
                except Exception:
                    error(
                        'Failed to write PCAP header to stream: '
                        + format_exc()
                    )
                    self.wireshark_proc = None
                    self.output_stream = None
                    self.stream_closed.emit()
                    # => ⚠️ Enventually dispatch events?/Use ::notify signals over the current object?
                else:
                    info('Written PCAP header to stream')
                    self.output_stream.flush(None)
                    self.stream_active.emit()

            self.output_stream.write_all_async(
                data, GLib.PRIORITY_DEFAULT, None, write_cb
            )  # PCAP header write op

    def write_gsmtap_packet(
        self,
        packet_type: GsmtapV2.PacketType,
        sub_type: ReadWriteKaitaiStruct,
        data: Union[bytes, DiagLogF.InnerLog, DiagRequest, DiagResponse],
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

        if isinstance(data, bytes):
            packet.data = data
        elif isinstance(data, DiagRequest):
            diag_payload = GsmtapV2.DiagPayload(
                True, None, packet, packet._root
            )

            diag_payload.frame = data
            diag_payload._check()

            packet.data = diag_payload
        elif isinstance(data, DiagResponse):
            diag_payload = GsmtapV2.DiagPayload(
                False, None, packet, packet._root
            )

            diag_payload.frame = data
            diag_payload._check()

            packet.data = diag_payload
        elif isinstance(data, DiagLogF.InnerLog):
            diag_payload = GsmtapV2.DiagPayload(
                False, None, packet, packet._root
            )

            diag_log = DiagLogF()
            diag_log.pending_msgs = 0
            diag_log.log_outer_length = data.log_inner_length - 4
            diag_log.inner_log = data
            data._parent = diag_log
            data._root = diag_log._root
            diag_log._check()

            diag_resp = DiagResponse()
            diag_resp.cmd_code = DiagCmd.log_f
            diag_resp.payload = diag_log
            diag_resp._check()

            diag_payload.frame = diag_resp
            diag_payload._check()

            packet.data = diag_payload

        packet._check()

        pass  # WIP 🪧 write to self.pcap_stream

    def write_pcap_record(XX):
        XX
