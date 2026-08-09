#!/usr/bin/env
from diagng.gobject.abstract.file_out_mode_selector import (
    FileOutModeSelector,
    FileOutMode,
)
from diagng.protocol.qualcomm.acquisition.dlf_input import DLFInput
from diagng.protocol.qualcomm.modules.ota_decoder import OTADecoder
from diagng.utils.logging_central import LoggingCentral
from diagng.system.pcap_output import PcapOutput

from argparse import ArgumentParser, Namespace
from collections.abc import Callable
from gi.repository import GLib
from typing import Optional
from logging import info


class ConstantFileOutModeSelector(FileOutModeSelector):
    constant_mode: FileOutMode

    def __init__(self, constant_mode: FileOutMode):
        self.constant_mode = constant_mode

    def query_file_out_mode(self, callback: Callable[[FileOutMode], None]):
        callback(self.constant_mode)


class InteractiveCLIFileOutModeSelector(FileOutModeSelector):
    def query_file_out_mode(callback: Callable[[FileOutMode], None]):
        raise NotImplementedError  # WIP XX


def main():
    args = ArgumentParser(description='Convert a .DLF file to a PCAP stream')

    # args.add (TODO)
    #  -d, --debug
    #  --extract-sibs
    #  --extract-ip-traffic
    #  --extra-logs-as-gsmtap

    group = args.add_mutually_exclusive_group()

    group.add_argument(
        '-o',
        '--overwrite',
        action='store_true',
        help='Force overwrite if the file already exists rather than ask',
    )

    group.add_argument(
        '-a',
        '--append',
        action='store_true',
        help='Force append if the file already exists rather than ask',
    )

    args.add_argument('input_dlf')
    args.add_argument(
        'output_pcap', nargs='?', help='Omit to open a Wireshark instance'
    )

    args = args.parse_args()
    loop = GLib.MainLoop.new(None, True)

    # ⚠️ TODO ADD A CLI SWITCH TO TURN DEBUG MODE ON/OFF? ⚠️ ⚠️ 🪧
    LoggingCentral(debug_mode=True)

    process_data(args)

    loop.run()


def process_data(
    args: Namespace,
):  # (input_dlf: str, output_pcap: Optional[str]):
    if args.overwrite:
        mode_selector = ConstantFileOutModeSelector(FileOutMode.Overwrite)
    elif args.append:
        mode_selector = ConstantFileOutModeSelector(FileOutMode.Append)
    else:
        mode_selector = InteractiveCLIFileOutModeSelector()

    pcap_stream = PcapOutput(
        bool(not args.output_pcap), mode_selector, args.output_pcap
    )

    def on_stream_active(*arg):
        with open(args.input_dlf, 'rb') as raw_stream:
            dlf_input = DLFInput(raw_stream)

            # Will connect dlf_input.log_received
            OTADecoder(pcap_stream, dlf_input)

            def on_closed(*arg):
                pcap_stream.close()
                exit(0)

            dlf_input.closed.connect(on_closed)
            dlf_input.process_stream()

        info('All data was processed')

    pcap_stream.stream_active.connect(on_stream_active)

    pcap_stream.open_stream()


if __name__ == '__main__':
    main()
