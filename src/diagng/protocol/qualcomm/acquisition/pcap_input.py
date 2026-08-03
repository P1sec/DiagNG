#!/usr/bin/python3

"""
This class should be able to either spawn
a Wireshark subprocess (possibly bypassing
the Flatpak sandbox) and piping PCAP
output to it, or either writing this output
to a on-disk PCAP file.

Support for parsing an existing PCAP(ng) file for
reprocessing purposes
    => Note: PCAPng is not
    even supported by libpcap nor
    by Kaitai and the simplest
    way to add support seems to
    be to use Tshark as an
    external converted command

(Should be also support reading a
PCAP file wrapped in a .GZ stream, like
in QCSuper? If so, should it also
involve a different wrapper class?)
"""


class PcapInput:
    pass  # TODO
