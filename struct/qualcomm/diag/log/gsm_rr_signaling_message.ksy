meta:
  id: gsm_rr_signaling_message
  endian: le
  bit-endian: be

# See also: ➡️ https://github.com/wireshark/wireshark/blob/60851bf/epan/dissectors/packet-qcdiag_log.c#L2929

seq:
  - id: is_downlink
    type: b1
  - id: channel_type
    type: b7
    enum: channel_type

  - id: message_type
    type: u1

  - id: len_message
    type: u1

  - id: message
    size: len_message

enums:
  channel_type:
    0x00: dcch
    0x01: bcch
    0x02: l2_rach
    0x03: ccch
    0x04: sacch
    0x05: sdcch
    0x06: facch_f
    0x07: facch_h
    0x08: l2_rach_with_no_delay
