#!/usr/bin/env
from diagng.gobject.abstract.file_out_mode_selector import FileOutModeSelector
from diagng.protocol.qualcomm.acquisition.dlf_input import DLFInput
from diagng.protocol.qualcomm.modules.ota_decoder import OTADecoder
from diagng.utils.logging_central import LoggingCentral
from diagng.system.pcap_output import PcapOutput

from argparse import ArgumentParser
from gi.repository import GLib
from typing import Optional
from logging import info

class ConstantFileOutModeSelector(FileOutModeSelector):
    pass # WIP XX

class InteractiveUIFileOutModeSelector(FileOutModeSelector):
    pass # WIP XX


def main():
    args = ArgumentParser(description='Convert a .DLF file to a PCAP stream')

    # args.add (TODO)
    #  -d, --debug
    #  --extract-sibs
    #  --extract-ip-traffic
    #  --extra-logs-as-gsmtap

    # ⚠️  TODO: Add a KIND OF INPUT PROGRESS
    #  MARKER TO STDERR?

    args.add_argument('input_dlf')
    args.add_argument(
        'output_pcap', nargs='?', help='Omit to open a Wireshark instance'
    )

    args = args.parse_args()
    loop = GLib.MainLoop.new(None, True)

    # ⚠️ TODO ADD A CLI SWITCH TO TURN DEBUG MODE ON/OFF? ⚠️ ⚠️ 🪧
    LoggingCentral(debug_mode=True)

    process_data(args.input_dlf, args.output_pcap)

    loop.run()


def process_data(input_dlf: str, output_pcap: Optional[str]):
    pcap_stream = PcapOutput(bool(not output_pcap), output_pcap)

    def on_stream_active(*args):
        with open(input_dlf, 'rb') as raw_stream:
            dlf_input = DLFInput(raw_stream)

            # Will connect dlf_input.log_received
            OTADecoder(pcap_stream, dlf_input)

            dlf_input.process_stream()

        info('All data was processed')

    pcap_stream.stream_active.connect(on_stream_active)

    pcap_stream.open_stream()


if __name__ == '__main__':
    main()
