# WIP ⚠️
meta:
  id: gsmtap_v2
  endian: be

# From: https://github.com/osmocom/libosmocore/blob/master/include/osmocom/core/gsmtap.h

seq:
  - id: version
    type: u1
    valid:
      eq: 2
    doc: Support GSMTAP v2 here
  - id: header_len
    type: u2
    valid:
      eq: 4
    doc: This header is 4 words = 32 bytes long
  - id: type
    type: u1
    enum: packet_type
  - id: timeslot
    type: u1
    doc: 0..7 on Um

  - id: arfcn
    type: u2
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
    type: u1
    # type:
    #  switch-on:
    #    WIP
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

