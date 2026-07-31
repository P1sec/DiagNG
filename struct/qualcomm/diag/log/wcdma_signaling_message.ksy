meta:
  id: wcdma_signaling_message
  endian: le
  bit-endian: be

seq:
  - id: packet_type
    type: b4
    enum: packet_type

  - if: packet_type != packet_type::special
    id: channel_type
    type: b4
    enum: channel_type
  - if: packet_type == packet_type::special
    id: special_type
    type: b4
    enum: special_type

  - id: radio_bearer
    type: u1
    enum: radio_bearer

  - id: len_message
    type: u2

  - if: packet_type == packet_type::explicit_arfcn_psc
    id: uarfcn
    type: u2
  - if: packet_type == packet_type::explicit_arfcn_psc
    id: psc
    type: u2

  - if: packet_type != packet_type::special
    id: message
    size: len_message

  - if: packet_type == packet_type::special
    # uarfcn/psc fields may or may not be
    # present in this case depending on
    # baseband version, don't try to guess
    id: payload
    size-eos: true


enums:
  packet_type:
    0x0: base
    0x8: explicit_arfcn_psc
    0xf: special

  channel_type:
    0: rrclog_sig_ul_ccch # Uplink CCCH logical channel
    1: rrclog_sig_ul_dcch # Uplink DCCH logical channel
    2: rrclog_sig_dl_ccch # Downlink CCCH logical channel
    3: rrclog_sig_dl_dcch # Downlink DCCH logical channel
    4: rrclog_sig_dl_bcch_bch # Downlink BCCH:BCH logical channel
    5: rrclog_sig_dl_bcch_fach # Downlink BCCH:FACH logical channel
    6: rrclog_sig_dl_pcch # Downlink PCCH logical channel
    9: rrclog_extension_sib
    10: rrclog_sib_container

  special_type:
    0x0: unknown_1
    0xe: unknown_2
    0xf: invalid_packet

  radio_bearer:
    0: ccch
    1: dcch_um
    2: dcch_am
    3: dcch_dt_high_pri
    4: dcch_dt_low_pri
    40: bcch_s
    41: bcch_n
    42: bcch_fach
    43: pcch
    44: ctch

instances:
  is_uplink:
    value: |
      channel_type == channel_type::rrclog_sig_ul_ccch or
      channel_type == channel_type::rrclog_sig_ul_dcch
