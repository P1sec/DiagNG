# WIP ⚠️
meta:
  id: gsmtap_v3
  endian: be
  bit-endian: be

# From: https://gitea.osmocom.org/peremen/gsmtapv3/src/branch/master/GSMTAPv3.md
# From: https://gitea.osmocom.org/peremen/gsmtapv3/src/branch/master/include/osmocom/core/gsmtapv3.h

seq:
  - id: reserved
    doc: reserved for future use (RFU). Must be 0.
    type: u1
    valid:
      eq: 0

  - id: header_len
    doc: length (including metadata) in number of 32bit words
    type: u2
    valid:
      min: 2

  - id: type
    type: u2
    enum: packet_type

  - id: subtype
    doc: type of burst/channel
    type:
      switch-on: type
      cases:
        'packet_type::nr_rrc': nr_rrc_subtype_field
        _: u2

  - id: metadata
    doc: type-specific metadata structure
    type: metadata
    repeat: until
    repeat-until: _.tag == metadata::tag::end_of_metadata

  - id: data
    size-eos: true

#   (WIP)

enums:
  packet_type:
    # 0x00, 0x01: Common and non-3GPP protocols

    0x0000: osmocore_log # libosmocore logging
    0x0001: sim # ISO 7816 smartcard interface
    0x0002: baseband_diag # Baseband diagnostic data
    0x0003: signal_status_report # Radio signal status report
    0x0004: tetra_i1 # TETRA air interface
    0x0005: tetra_i1_burst # TETRA air interface
    0x0006: gmr1_um # GMR-1 L2 packets
    0x0007: e1t1 # E1/T1 Lines
    0x0008: wmx_burst # WiMAX burst

    # 0x02: GSM

    0x0200: um
    0x0201: um_burst # raw burst bits
    0x0202: gb_rlcmac # GPRS Gb interface: RLC/MAC
    0x0203: gb_llc # GPRS Gb interface: LLC
    0x0204: gb_sndcp # GPRS Gb interface: SNDCP
    0x0205: abis
    0x0206: rlp # GSM RLP frames, as per 3GPP TS 24.022

    # 0x03: UMTS/WCDMA

    0x0300: umts_mac # UMTS MAC PDU with context, as per 3GPP TS 25.321
    0x0301: umts_rlc # UMTS RLC PDU with context, as per 3GPP TS 25.322
    0x0302: umts_pdcp # UMTS PDCP PDU with context, as per 3GPP TS 25.323
    0x0303: umts_rrc # UMTS RRC PDU, as per 3GPP TS 25.331

    # 0x04: LTE

    0x0400: lte_mac # LTE MAC PDU with context, as per 3GPP TS 36.321
    0x0401: lte_rlc # LTE RLC PDU with context, as per 3GPP TS 36.322
    0x0402: lte_pdcp # LTE PDCP PDU with context, as per 3GPP TS 36.323
    0x0403: lte_rrc # LTE RRC PDU, as per 3GPP TS 36.331
    0x0404: nas_eps # EPS Non-Access Stratum, as per 3GPP TS 24.301

    # 0x05: NR

    0x0500: nr_mac # NR MAC PDU with context, as per 3GPP TS 38.321
    0x0501: nr_rlc # NR RLC PDU with context, as per 3GPP TS 38.322
    0x0502: nr_pdcp # NR PDCP PDU with context, as per 3GPP TS 38.323
    0x0503: nr_rrc # NR RRC PDU, as per 3GPP TS 38.331
    0x0504: nas_5gs # 5GS Non-Access Stratum, as per 3GPP TS 24.501

  nr_rrc_subtype:
    0: unknown

    # sub-types for TYPE_NR_RRC (0x0503)

    0x0001: bcch_bch
    0x0002: bcch_dl_sch
    0x0003: dl_ccch
    0x0004: dl_dcch
    0x0005: mcch
    0x0006: pcch
    0x0007: ul_ccch
    0x0008: ul_ccch1
    0x0009: ul_dcch

    0x0101: sbcch_sl_bch
    0x0102: scch

    # sub-types for individual NR RRC message

    0x0201: rrc_reconfiguration
    0x0202: rrc_reconfiguration_complete
    0x0203: ue_mrdc_capability
    0x0204: ue_nr_capability
    0x0205: ue_radio_access_capability_information
    0x0206: ue_radio_paging_information
    0x0207: sib1
    0x0208: sib2
    0x0209: sib3
    0x020a: sib4
    0x020b: sib5
    0x020c: sib6
    0x020d: sib7
    0x020e: sib8
    0x020f: sib9
    0x0210: sib10_r16
    0x0211: sib11_r16
    0x0212: sib12_r16
    0x0213: sib13_r16
    0x0214: sib14_r16
    0x0215: sib15_r17
    0x0216: sib16_r17
    0x0217: sib17_r17
    0x0218: sib18_r17
    0x0219: sib19_r17
    0x021a: sib20_r17
    0x021b: sib21_r17
    0x021c: sib22_r18
    0x021d: sib23_r18
    0x021e: sib24_r18
    0x021f: sib25_r18
    0x0220: sib17bis_r18

types:
  metadata:
    seq:
      - id: tag
        type: u2
        enum: tag

      - if: tag != tag::end_of_metadata
        id: len_value
        type: u2

      - if: tag != tag::end_of_metadata
        id: value
        size: len_value
        type:
          switch-on: tag
          cases:
            'tag::channel_number': channel_number

    enums:
      tag:
        # GSMTAPv3 metadata tags
        0x0000: packet_timestamp
        0x0001: packet_comment
        0x0002: channel_number
        0x0003: frequency
        0x0004: band_indicator
        0x0005: bsic_psc_pci
        0x0006: gsm_timeslot
        0x0007: gsm_subslot
        0x0008: system_frame_number
        0x0009: subframe_number
        0x000a: hyperframe_number
        0x000b: tetra_symbol_number
        0x000c: tetra_multiframe_number
        0x000d: antenna_number

        0x0100: signal_level
        0x0101: rssi
        0x0102: snr
        0x0103: sinr
        0x0104: rscp
        0x0105: ecio
        0x0106: rsrp
        0x0107: rsrq
        0x0108: ss_rsrp
        0x0109: csi_rsrp
        0x010a: srs_rsrp
        0x010b: ss_rsrq
        0x010c: csi_rsrq
        0x010d: ss_sinr
        0x010e: csi_sinr

        0x0200: ciphering_key
        0x0201: integrity_key
        0x0202: k_nasenc
        0x0203: k_nasint
        0x0204: k_rrcenc
        0x0205: k_rrcint
        0x0206: k_upenc
        0x0207: k_upint

        0xfffe: end_of_metadata


  channel_number:
    seq:
      - id: is_uplink
        type: b1

      - id: arfcn
        type: b31

  nr_rrc_subtype_field:
    seq:
      - id: subtype
        type: u2
        enum: nr_rrc_subtype

#   (WIP)
