# WIP ⚠️
meta:
  id: gsmtap_v2
  endian: be
  bit-endian: be
  imports:
    - ../qualcomm/diag/request
    - ../qualcomm/diag/response

# From: https://github.com/osmocom/libosmocore/blob/master/include/osmocom/core/gsmtap.h

seq:
  - id: version
    type: u1
    valid:
      eq: 2
    doc: Support GSMTAP v2 here
  - id: header_len
    type: u1
    valid:
      eq: 4
    doc: This header is 4 words = 32 bytes long
  - id: type
    type: u1
    enum: packet_type
  - id: timeslot
    type: u1
    doc: 0..7 on Um

  - id: pcs_band
    type: b1
    doc: PCS band indicator
  - id: is_uplink
    type: b1
    doc: Uplink or downlink
  - id: arfcn
    type: b14
    doc: ARFCN (frequency)
  - id: signal_dbm
    type: s1
    doc: Signal level in dBm
  - id: snr_db
    type: s1
    doc: Signal/noise ratio in dB

  - id: frame_number
    type: u4
    doc: GSM Frame Number (FN)

  - id: sub_type
    doc: Type of burst/channel
    type:
      switch-on: type
      cases:
        'packet_type::umts_rrc': umts_rrc_subtype_field
        'packet_type::um': gsm_rr_subtype_field
        'packet_type::abis': gsm_rr_subtype_field
        _: u1
  - id: antenna_nr
    type: u1
    doc: Antenna Number
  - id: sub_slot
    type: u1
    doc: Sub-slot within timeslot
  - id: res
    type: u1
    doc: Reserved for future use (RFU)

  - id: data
    size-eos: true
    type:
      switch-on: type
      cases:
        # See: https://github.com/wireshark/wireshark/blob/3c7615d/epan/dissectors/packet-qcdiag.c#L1809
        'packet_type::qc_diag': diag_payload(is_uplink)

types:
  diag_payload:
    params:
      - id: is_uplink
        type: b1
    seq:
      - id: frame
        type:
          switch-on: is_uplink
          cases:
            true: diag_request
            false: diag_response

  umts_rrc_subtype_field:
    seq:
      - id: umts_rrc_subtype
        type: u1
        enum: umts_rrc_subtype

  gsm_rr_subtype_field:
    seq:
      - id: gsm_rr_subtype
        type: u1
        enum: gsm_rr_subtype

enums:
  packet_type:
    0x01: um
    0x02: abis
    0x03: um_burst # Raw burst bits
    0x04: sim # ISO-7816 smartcard interface
    0x05: tetra_i1 # Tetra air interface
    0x06: tetra_i1_burst # Tetra air interface
    0x07: wmx_burst # WiMAX burst
    0x08: gb_llc # GPRS Gb interface: LLC
    0x09: gb_sndcp # GPRS Gb interface: SNDCP
    0x0a: gmr1_um # GMR-1 L2 packets
    0x0b: umts_rlc_mac
    0x0c: umts_rrc
    0x0d: lte_rrc # LTE interface
    0x0e: lte_mac # LTE MAC interface
    0x0f: lte_mac_framed # LTE MAC with context hdr
    0x10: osmocore_log # libosmocore logging
    0x11: qc_diag # Qualcomm DIAG frame
    0x12: lte_nas # LTE Non-Access Stratum
    0x13: e1t1 # E1/T1 Lines
    0x14: gsm_rlp # GSM RLP frames as per 3GPP TS 24.022

  # See: gsmtap_gsm_channel_names
  # https://github.com/osmocom/libosmocore/blob/1.14.1/src/core/gsmtap_util.c#L586

  # See: GSMTAP_CHANNEL_*
  # https://github.com/osmocom/libosmocore/blob/1.14.1/include/osmocom/core/gsmtap.h#L79

  gsm_rr_subtype:
    0x00: unknown
    0x01: bcch
    0x02: ccch
    0x03: rach
    0x04: agch
    0x05: pch
    0x06: sdcch
    0x07: sdcch4
    0x08: sdcch8
    0x09: facch_f
    0x0a: facch_h
    0x0b: pacch
    0x0c: cbch52
    0x0d: pdch
    0x0e: ptcch
    0x0f: cbch51
    0x10: voice_f # voice codec payload (FR/EFR/AMR)
    0x11: voice_h # voice codec payload (HR/AMR)
    0x86: lsacch
    0x87: sacch4
    0x88: sacch8
    0x89: sacch_f
    0x8a: sacch_h

  umts_rrc_subtype:
    0: dl_dcch_message
    1: ul_dcch_message
    2: dl_ccch_message
    3: ul_ccch_message
    4: pcch_message
    5: dl_shcch_message
    6: ul_shcch_message
    7: bcch_fach_message
    8: bcch_bch_message
    9: mcch_message
    10: msch_message
    11: handover_to_utran_command
    12: inter_rathandover_info
    13: system_information_bch
    14: system_information_container
    15: ue_radio_access_capability_info
    16: master_information_block
    17: sys_info_type1
    18: sys_info_type2
    19: sys_info_type3
    20: sys_info_type4
    21: sys_info_type5
    22: sys_info_type5bis
    23: sys_info_type6
    24: sys_info_type7
    25: sys_info_type8
    26: sys_info_type9
    27: sys_info_type10
    28: sys_info_type11
    29: sys_info_type11bis
    30: sys_info_type12
    31: sys_info_type13
    32: sys_info_type13_1
    33: sys_info_type13_2
    34: sys_info_type13_3
    35: sys_info_type13_4
    36: sys_info_type14
    37: sys_info_type15
    38: sys_info_type15bis
    39: sys_info_type15_1
    40: sys_info_type15_1bis
    41: sys_info_type15_2
    42: sys_info_type15_2bis
    43: sys_info_type15_2ter
    44: sys_info_type15_3
    45: sys_info_type15_3bis
    46: sys_info_type15_4
    47: sys_info_type15_5
    48: sys_info_type15_6
    49: sys_info_type15_7
    50: sys_info_type15_8
    51: sys_info_type16
    52: sys_info_type17
    53: sys_info_type18
    54: sys_info_type19
    55: sys_info_type20
    56: sys_info_type21
    57: sys_info_type22
    58: sys_info_type_sb1
    59: sys_info_type_sb2
    60: to_target_rnc_container
    61: target_rnc_to_source_rnc_container

  lte_rrc_subtype:
    0x00: unknown
    0x01: ch_bcch
    0x02: ch_ccch
    0x03: ch_dcch
    0x04: ch_mcch
    0x05: ch_pcch
    0x06: ch_dtch
    0x07: ch_mtch


