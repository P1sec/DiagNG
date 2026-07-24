
meta:
  id: diag_stream
  endian: le
  imports:
    - response

seq:
  - id: frames
    type: diag_response
    # hdlc_decode will remove escapes
    # (0x7d 0x5e -> 0x7e, 0x7d 0x5d -> 0x7d)
    # + check and remove CRC-16
    # and trailer char at end at stream
    # if present and valid, else fail
    process: diagng.protocol.qualcomm.utils.hdlc.hdlc_decoder
    terminator: 0x7e
    include: true
    repeat: eos
