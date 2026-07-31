meta:
  id: wcdma_signaling_message
  endian: le

seq:
  - id: channel_type
    type: u1
    enum: channel_type
  - id: radio_bearer
    type: u1
  - id: len_message
    type: u2
  - id: message
    size: len_message

enums:
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

instances:
  is_uplink:
    value: |
      channel_type == channel_type::rrclog_sig_ul_ccch or
      channel_type == channel_type::rrclog_sig_ul_dcch
