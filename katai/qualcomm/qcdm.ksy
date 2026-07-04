# WIP
# REF: Support until ..DIAG_SECURE_LOG_F==DIAG_LOG_SEC_F + ..DIAG_SUBSYS_QDR/DIAG_SUBSYS_AOSTLM_TEST/DIAG_SUBSYS_CHARGERPD/DIAG_SUBSYS_QSH/DIAG_SUBSYS_DATA_CSM..DIAG_SUBSYS_UWB ?

# BASE OFF SCAT, MI, ETC. ?

# Cf. https://github.com/fgsect/scat/blob/v2.0.0/src/scat/parsers/qualcomm/diagcmd.py
# Cf. https://www.wireshark.org/docs/wsar_html/packet-qcdiag_8h_source.html

# Examples of using enumerations:
# => https://doc.kaitai.io/user_guide.html#enums
# ==> https://doc.kaitai.io/user_guide.html#delimited-struct
# ==> https://doc.kaitai.io/user_guide.html#delimited-struct-advanced
# ==> https://doc.kaitai.io/user_guide.html#custom-process
# => https://formats.kaitai.io/swf/

# => https://ide.kaitai.io/

meta:
  id: diag_stream
  endian: le
  imports:
    - qcdm_message

seq:
  - id: frames
    type: diag_message
    # hdlc_decode will remove escapes
    # (0x7d 0x5e -> 0x7e, 0x7d 0x5d -> 0x7d)
    # + check and remove CRC-16 at
    # end at stream if valid, else fail
    process: diagng.parsing.hdlc.hdlc_decoder
    terminator: 0x7e
    include: true
    repeat: eos
