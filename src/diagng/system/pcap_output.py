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

                        => THIS SHALL BE INSTANCIED FROM: ⚠️ ⚠️ XX
                        => HAVE METHODS BE CALLED FROM: ⚠️ ⚠️ XX    => ota_decoder.py ? ℹ️
                        =>    AND IMPORT ;; => THE KAITAI PCAP+IP+UDP+GSMTAP encoder ?
                            ( ⚠️ MOVE FUNCTION FROM OTA_DECODER FOR ENCODING A GSMTAP HEADER)
                        =>    AND CALL; :  ⚠️ XX

    Cf. https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py
"""


class PcapOutput:
    XX: XX  # TODO (WIP)

    def __init__(self, XX):
        self.XX = XX

    def write_gsmtap_frame(XX, XX, XX, XX):
        XX

    def write_pcap_record(XX):
        XX
