#!/usr/bin/env
from diagng.protocol.qualcomm.acquisition.dlf_input import DLFInput
from diagng.protocol.qualcomm.struct.dlf_file import DlfFile

from diagng.protocol.qualcomm.modules.ota_decoder import OTADecoder
from diagng.system.pcap_output import PcapOutput

from argparse import ArgumentParser


def main():
    args = ArgumentParser(description='Convert a .DLF file to a PCAP stream')
    args.add_argument('input_dlf')
    args.add_argument(
        'output_pcap', nargs='?', help='Omit to open a Wireshark instance'
    )

    args = args.parse_args()

    pass  # TODO


if __name__ == '__main__':
    main()
