#!/usr/bin/python3

"""
    This class should be able to either spawn
    a Wireshark subprocess (possibly bypassing
    the Flatpak sandbox) and piping PCAP
    output to it, or either writing this output
    to a on-disk PCAP file.

    Eventually we should support parsing
    an existing PCAP(ng) file for
    reprocessing purposes, perhaps in
    a different file?

    ( => Perhaps we should support this
      EARLY so that appending to an
      existing PCAP(ng) file is supported?)

    (Should be also support reading/writing a
     PCAP file wrapped in a .GZ stream, like
     in QCSuper? If so, should it also
     involve a different wrapper class?)

    Cf. https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py
"""

class PcapOutput:
    pass  # TODO
