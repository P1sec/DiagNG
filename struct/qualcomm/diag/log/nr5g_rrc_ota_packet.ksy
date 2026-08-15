meta:
  id: nr5g_rrc_ota_packet
  endian: le
  bit-endian: be
  imports:
    - ../../../gsmtap/gsmtap_v2

# See also: https://github.com/wireshark/wireshark/blob/60851bf/epan/dissectors/packet-qcdiag_log.c#L2628
# See: https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/wireshark_plugin/diag_nr_rrc_dissector.lua
# See: https://github.com/fgsect/scat/blob/ce1044b/src/scat/parsers/qualcomm/diagnrlogparser.py#L275
# See: https://github.com/mobile-insight/mobileinsight-core/blob/v6.0.0/dm_collector_c/log_packet.h#L410

seq:
  - id: packet_version
    type: u4

  - id: rrc_rel
    type: u1
  - id: rrc_ver_major
    type: b4
  - id: rrc_ver_minor
    type: b4

  - id: bearer_id
    type: u1

  - id: phy_cellid # PCI
    type: u2
    valid:
      min: 0
      max: 503

  - if: packet_version >= 16
    id: nr_global_cellid # NCGI
    type: u8

  - id: frequency # NARFCN
    type: u4
    valid:
      min: 0
      max: 262143

  - id: sfn_subfn
    type:
      switch-on: packet_version
      cases:
        1: sfn_subfn_u2
        2: sfn_subfn_u2

        3: sfn_subfn_u4
        4: sfn_subfn_u4
        5: sfn_subfn_u4
        6: sfn_subfn_u4
        7: sfn_subfn_u4
        8: sfn_subfn_u4
        9: sfn_subfn_u4
        10: sfn_subfn_u4
        11: sfn_subfn_u4

        _: sfn_subfn_u3

  - id: pdu_type
    type:
      switch-on: packet_version
      cases:
        XX_TO_BE_GENERATED

  - id: sib_mask
    type: u4

  - id: len_message
    type: u2

  - if: packet_version >= 19
    id: unknown_1
    type: u1

  - if: packet_version >= 23
    id: unknown_2
    type: u2

  - if: packet_version >= 23
    id: segment_id
    type: u1

  - id: message
    size: len_message

types:
  sfn_subfn_u2:
    seq:
      - id: sub_fn
        type: b4
      - id: sys_fn
        type: b10
      - id: reserved
        type: b2

  sfn_subfn_u4:
    seq:
      - id: reserved
        type: b3
      - id: sub_fn
        type: b6
      - id: sys_fn
        type: b10
      - id: reserved_2
        type: b13

  sfn_subfn_u3:
    seq:
      - id: slot_n
        type: b3
      - id: sub_fn
        type: b6
      - id: sys_fn
        type: b9
      - id: reserved_2
        type: b6



