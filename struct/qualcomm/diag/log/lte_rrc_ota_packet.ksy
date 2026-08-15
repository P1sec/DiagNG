meta:
  id: lte_rrc_ota_packet
  endian: le
  bit-endian: be
  imports:
    - ../../../gsmtap/gsmtap_v2

# See also: https://github.com/wireshark/wireshark/blob/60851bf/epan/dissectors/packet-qcdiag_log.c#L2942
# See: https://github.com/P1sec/QCSuper/blob/2.1.3/src/qcsuper/modules/pcap_dump.py#L319
# See: https://github.com/fgsect/scat/blob/ce1044b/src/scat/parsers/qualcomm/diagltelogparser.py#L1272
# See: https://github.com/mobile-insight/mobileinsight-core/blob/v6.0.0/dm_collector_c/log_packet.h#L224
# See: https://github.com/moiji-mobile/diag-parser/blob/402523f/diag_input.c#L206

seq:
  - id: packet_version
    type: u1

  - id: rrc_rel
    type: u1
  - id: rrc_ver_major
    type: b4
  - id: rrc_ver_minor
    type: b4

  - if: packet_version >= 25
    id: nc_rrc_rel
    type: u1
  - if: packet_version >= 25
    id: nc_rrc_ver_major
    type: b4
  - if: packet_version >= 25
    id: nc_rrc_ver_minor
    type: b4

  - id: bearer_id
    type: u1

  - id: phy_cellid
    type: u2

  - if: packet_version >= 8
    id: earfcn_long
    type: u4
  - if: packet_version < 8
    id: earfcn_short
    type: u2

  - id: sfn_subfn
    type: u2

  - id: is_special
    type: b1

  - if: not is_special
    id: pdu_type
    type:
      switch-on: packet_version
      cases:
        1: v1_pdu_type
        2: v2_pdu_type
        3: v3_pdu_type
        4: v4_pdu_type
        5: v4_pdu_type
        6: v6_pdu_type
        7: v7_pdu_type
        8: v8_pdu_type
        9: v9_pdu_type
        10: v10_pdu_type
        11: v11_pdu_type
        12: v12_pdu_type
        13: v13_pdu_type
        14: v14_pdu_type
        15: v15_pdu_type
        16: v16_pdu_type
        17: v17_pdu_type
        18: v18_pdu_type
        19: v19_pdu_type
        20: v20_pdu_type
        21: v21_pdu_type
        22: v22_pdu_type
        23: v23_pdu_type
        24: v24_pdu_type
        25: v25_pdu_type
        26: v26_pdu_type
        27: v27_pdu_type
        _: v27_pdu_type

  - if: packet_version >= 5
    id: sib_mask
    type: u4

  - id: len_message
    type: u2

  - if: packet_version >= 30
    id: unk1
    type: u1
  - if: packet_version >= 30
    id: unk2
    type: u1
  - if: packet_version >= 30
    id: segment_id
    type: u1

  - id: message
    size: len_message


types:
  v1_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        2: bcch_dl_sch
        3: pcch
        4: dl_ccch
        5: dl_dcch
        6: ul_ccch
        7: ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v2_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: ue_eutra_cap
        10: var_short_mac_input
        11: ue_eutra_cap_v9a0_ies
        12: sysinfo_block_type1

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v3_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: sysinfo_block_type1_v8h0_ies
        10: sysinfo_block_type2_v8h0_ies
        11: sysinfo_block_type5_v8h0_ies
        12: sysinfo_block_type6_v8h0_ies
        13: ue_eutra_cap
        14: ue_eutra_cap_v9a0_ies
        15: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v4_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: sysinfo_block_type1
        10: sysinfo_block_type1_v8h0_ies
        11: sysinfo_block_type2_v8h0_ies
        12: sysinfo_block_type5_v8h0_ies
        13: sysinfo_block_type6_v8h0_ies
        14: ue_eutra_cap
        15: ue_eutra_cap_v9a0_ies
        16: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v6_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: sysinfo_block_type1_v8h0_ies
        10: sysinfo_block_type2_v8h0_ies
        11: sysinfo_block_type5_v8h0_ies
        12: sysinfo_block_type6_v8h0_ies
        13: carrier_freqlist_mbms_r11
        14: ue_eutra_cap
        15: ue_eutra_cap_v9a0_ies
        16: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v7_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: sysinfo_block_type1
        10: sysinfo_block_type1_v8h0_ies
        11: sysinfo_block_type2_v8h0_ies
        12: sysinfo_block_type5_v8h0_ies
        13: sysinfo_block_type6_v8h0_ies
        14: ue_eutra_cap
        15: ue_eutra_cap_v9a0_ies
        16: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v8_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: connectionrelease_v9e0_ie
        10: sysinfo_block_type1
        11: sysinfo_block_type1_v8h0_ies
        12: ueinforesponse_v9e0_ie
        13: sysinfo_block_type2_v8h0_ies
        14: sysinfo_block_type5_v8h0_ies
        15: sysinfo_block_type6_v8h0_ies
        16: ue_eutra_cap
        17: ue_eutra_cap_v9a0_ies

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v9_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: ellipsoid_point
        2: ellipsoid_point_uncertainty_circle
        3: ellipsoid_point_uncertainty_ellipse
        4: ellipsoid_point_altitude
        5: ellipsoid_point_altitude_uncertainty_ellipsoid
        6: ellipsoid_arc
        7: horizontal_velocity
        8: bcch_bch
        9: bcch_dl_sch
        10: mcch
        11: pcch
        12: dl_ccch
        13: dl_dcch
        14: ul_ccch
        15: ul_dcch
        16: rrcconnrelease_v9e0_ies
        17: sysinfo_block_type1
        18: sysinfo_block_type1_v8h0_ies
        19: ueinforesponse_v9e0_ies
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type5_v8h0_ies
        22: sysinfo_block_type6_v8h0_ies
        23: ue_eutra_cap
        24: ue_eutra_cap_v9a0_ies

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v10_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: ellipsoid_point
        2: ellipsoid_point_uncertainty_circle
        3: ellipsoid_point_uncertainty_ellipse
        4: ellipsoid_point_altitude
        5: ellipsoid_point_altitude_uncertainty_ellipsoid
        6: ellipsoid_arc
        7: horizontal_velocity
        8: bcch_bch
        9: bcch_dl_sch
        10: mcch
        11: pcch
        12: dl_ccch
        13: dl_dcch
        14: ul_ccch
        15: ul_dcch
        16: rrcconnrelease_v9e0_ies
        17: sysinfo_block_type1
        18: sysinfo_block_type1_v8h0_ies
        19: ueinforesponse_v9e0_ies
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type5_v8h0_ies
        22: sysinfo_block_type6_v8h0_ies
        23: ue_eutra_cap
        24: ue_eutra_cap_v9a0_ies

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v11_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: ellipsoid_point
        2: ellipsoid_point_uncertainty_circle
        3: ellipsoid_point_uncertainty_ellipse
        4: ellipsoid_point_altitude
        5: ellipsoid_point_altitude_uncertainty_ellipsoid
        6: ellipsoid_arc
        7: horizontal_velocity
        8: bcch_bch
        9: bcch_dl_sch
        10: mcch
        11: pcch
        12: dl_ccch
        13: dl_dcch
        14: ul_ccch
        15: ul_dcch
        16: rrcconnrelease_v9e0_ies
        17: sysinfo_block_type1
        18: sysinfo_block_type1_v8h0_ies
        19: ueinforesponse_v9e0_ies
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type5_v8h0_ies
        22: sysinfo_block_type6_v8h0_ies
        23: csi_im_configid_r12
        24: eutra_ellipsoid_point
        25: eutra_ellipsoid_point_altitude
        26: eutra_ellipsoid_point_altitude_uncertainty_ellipsoid
        27: eutra_ellipsoid_arc
        28: eutra_ellipsoid_point_uncertainty_circle
        29: eutra_ellipsoid_point_uncertainty_ellipse
        30: eutra_horizontal_velocity
        31: polygon
        32: meas_ref_time
        33: ue_eutra_cap
        34: ue_eutra_cap_v9a0_ies

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch

  v12_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: ellipsoid_point
        2: ellipsoid_point_uncertainty_circle
        3: ellipsoid_point_uncertainty_ellipse
        4: ellipsoid_point_altitude
        5: ellipsoid_point_altitude_uncertainty_ellipsoid
        6: ellipsoid_arc
        7: horizontal_velocity
        8: bcch_bch
        9: bcch_dl_sch
        10: mcch
        11: pcch
        12: dl_ccch
        13: dl_dcch
        14: ul_ccch
        15: ul_dcch
        16: rrcconnection_reconfiguration
        17: rrcconnection_reconfiguration_complete
        18: rrcconnrelease_v9e0_ies
        19: sysinfo_block_type1
        20: sysinfo_block_type1_v8h0_ies
        21: uecapabilityenquiry
        22: uecapabilityinformation
        23: ueinforesponse_v9e0_ies
        24: sysinfo_block_type2_v8h0_ies
        25: sysinfo_block_type5_v8h0_ies
        26: sysinfo_block_type6_v8h0_ies
        27: csi_im_configid_r1
        28: eutra_rrc_definitions_ellipsoid_point
        29: eutra_rrc_definitions_ellipsoid_altitude
        30: eutra_rrc_definitions_ellipsoid_altitude_uncertainty_ellipsoid
        31: eutra_rrc_definitions_ellipsoid_arc
        32: eutra_rrc_definitions_ellipsoid_uncertainty_circle
        33: eutra_rrc_definitions_ellipsoid_uncertainty_ellipse
        34: eutra_rrc_definitions_horizontal_velocity
        35: polygon
        36: measurement_ref_time
        37: ue_eutra_cap
        38: ue_eutra_cap_v9a0_ies
        39: var_short_mac_input
        40: els_sib1_signature
        41: els_sysinfo_block_type1
        42: nhn_plmn_identity_list
        43: els_dl_ccch
        44: els_dl_dcch
        45: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::els_ul_dcch

  v13_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: rrcconnection_reconfiguration
        10: rrcconnrelease_v8m0_ies
        11: rrcconnection_reconfiguration_complete
        12: rrcconnrelease_v9e0_ies
        13: sysinfo_block_type1
        14: sysinfo_block_type1_v8h0_ies
        15: uecapabilityenquiry
        16: uecapabilityinformation
        17: ueinforesponse_v9e0_ies
        18: sysinfo_block_type2_v8h0_ies
        19: sysinfo_block_type5_v8h0_ies
        20: sysinfo_block_type6_v8h0_ies
        21: tdd_configsl_r12
        22: ellipsoid_point
        23: ellipsoid_point_altitude
        24: ellipsoid_point_altitude_uncertainty_ellipsoid
        25: ellipsoid_arc
        26: ellipsoid_point_uncertainty_circle
        27: ellipsoid_point_uncertainty_ellipse
        28: horizontal_velocity
        29: polygon
        30: measurement_ref_time
        31: rsrp_rangsl3_r12
        32: ue_eutra_cap
        33: ue_eutra_cap_v9a0_ies
        34: var_short_mac_input
        35: els_sib1_signature
        36: els_sysinfo_block_type1
        37: nhn_plmn_identity_list
        38: els_dl_ccch
        39: els_dl_dcch
        40: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::els_ul_dcch

  v14_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: rrcconnection_reconfiguration
        11: rrcconnrelease_v8m0_ies
        12: rrcconnection_reconfiguration_complete
        13: rrcconnrelease_v9e0_ies
        14: sysinfo_block_type1
        15: sysinfo_block_type1_v8h0_ies
        16: uecapabilityenquiry
        17: uecapabilityinformation
        18: ueinforesponse_v9e0_ies
        19: sysinfo_block_type2_v8h0_ies
        20: sysinfo_block_type5_v8h0_ies
        21: redistributionfactor_r13
        22: sysinfo_block_type6_v8h0_ies
        23: tdd_configsl_r12
        24: ellipsoid_point
        25: ellipsoid_point_altitude
        26: ellipsoid_point_altitude_uncertainty_ellipsoid
        27: ellipsoid_arc
        28: ellipsoid_point_uncertainty_circle
        29: ellipsoid_point_uncertainty_ellipse
        30: horizontal_velocity
        31: polygon
        32: measurement_ref_time
        33: rsrp_rangsl3_r12
        34: ue_eutra_cap
        35: ue_eutra_cap_v9a0_ies
        36: laa_params_r13
        37: var_short_mac_input
        38: els_sib1_signature
        39: els_sysinfo_block_type1
        40: nhn_plmn_identity_list
        41: els_dl_ccch
        42: els_dl_dcch
        43: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::els_ul_dcch

  v15_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: sc_mcch_r13
        11: rrcconnection_reconfiguration
        12: rrcconnrelease_v8m0_ies
        13: rrcconnection_reconfiguration_complete
        14: rrcconnrelease_v9e0_ies
        15: sysinfo_block_type1
        16: sysinfo_block_type1_v8h0_ies
        17: uecapabilityenquiry
        18: uecapabilityinformation
        19: ueinforesponse_v9e0_ies
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type3_v10j0_ies
        22: sysinfo_block_type5_v8h0_ies
        23: sysinfo_block_type6_v8h0_ies
        24: tdd_configsl_r12
        25: ellipsoid_point
        26: ellipsoid_point_altitude
        27: ellipsoid_point_altitude_uncertainty_ellipsoid
        28: ellipsoid_arc
        29: ellipsoid_point_uncertainty_circle
        30: ellipsoid_point_uncertainty_ellipse
        31: horizontal_velocity
        32: polygon
        33: measurement_ref_time
        34: rsrp_rangsl3_r12
        35: ue_eutra_cap
        36: ue_eutra_cap_v9a0_ies
        37: ue_eutra_cap_v10j0_ies
        38: sl_txpoolid_r13
        39: var_short_mac_input
        40: bcch_bch_nb
        41: bcch_dl_sch_nb
        42: pcch_nb
        43: dl_ccch_nb
        44: dl_dcch_nb
        45: ul_ccch_nb
        46: ul_dcch_nb
        47: els_sib1_signature
        48: els_sysinfo_block_type1
        49: nhn_plmn_identity_list
        50: els_dl_ccch
        51: els_dl_dcch
        52: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::sc_mcch_r13 ? gsmtap_v2::lte_rrc_subtype::sc_mcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v16_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: sc_mcch_r13
        11: rrcconnection_reconfiguration
        12: rrcconnrelease_v8m0_ies
        13: rrcconnection_reconfiguration_complete
        14: rrcconnrelease_v9e0_ies
        15: sysinfo_block_type1
        16: sysinfo_block_type1_v8h0_ies
        17: uecapabilityenquiry
        18: uecapabilityinformation
        19: ueinforesponse_v9e0_ies
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type3_v10j0_ies
        22: sysinfo_block_type5_v8h0_ies
        23: sysinfo_block_type6_v8h0_ies
        24: tdd_configsl_r12
        25: ellipsoid_point
        26: ellipsoid_point_altitude
        27: ellipsoid_point_altitude_uncertainty_ellipsoid
        28: ellipsoid_arc
        29: ellipsoid_point_uncertainty_circle
        30: ellipsoid_point_uncertainty_ellipse
        31: horizontal_velocity
        32: polygon
        33: measurement_ref_time
        34: rsrp_rangsl3_r12
        35: ue_eutra_cap
        36: ue_eutra_cap_v9a0_ies
        37: ue_eutra_cap_v10j0_ies
        38: sl_txpoolid_r13
        39: var_short_mac_input
        40: bcch_bch_nb
        41: bcch_dl_sch_nb
        42: pcch_nb
        43: dl_ccch_nb
        44: dl_dcch_nb
        45: ul_ccch_nb
        46: ul_dcch_nb
        47: els_sib1_signature
        48: els_sysinfo_block_type1
        49: els_dl_dcch
        50: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::sc_mcch_r13 ? gsmtap_v2::lte_rrc_subtype::sc_mcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v17_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: rrcconnection_reconfiguration
        10: rrcconnrelease_v8m0_ies
        11: rrcconnection_reconfiguration_complete
        12: rrcconnrelease_v9e0_ies
        13: sysinfo_block_type1
        14: sysinfo_block_type1_v8h0_ies
        15: uecapabilityenquiry
        16: uecapabilityinformation
        17: ueinforesponse_v9e0_ies
        18: sysinfo_block_type2_v8h0_ies
        19: sysinfo_block_type5_v8h0_ies
        20: sysinfo_block_type6_v8h0_ies
        21: csi_im_configid_r12
        22: ellipsoid_point
        23: ellipsoid_point_altitude
        24: ellipsoid_point_altitude_uncertainty_ellipsoid
        25: ellipsoid_arc
        26: ellipsoid_point_uncertainty_circle
        27: ellipsoid_point_uncertainty_ellipse
        28: horizontal_velocity
        29: polygon
        30: measurement_ref_time
        31: ue_eutra_cap
        32: ue_eutra_cap_v9a0_ies
        33: var_short_mac_input
        34: els_sib1_signature
        35: els_sysinfo_block_type1
        36: nhn_plmn_identity_list
        37: els_dl_ccch
        38: els_dl_dcch
        39: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::els_ul_dcch

  v18_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: pcch_type
        6: dl_ccch
        7: dl_ccch_type
        8: dl_dcch
        9: dl_dcch_type
        10: ul_ccch
        11: ul_ccch_type
        12: ul_dcch
        13: ul_dcch_type
        14: rrcconnection_reconfiguration
        15: rrcconnection_reconfiguration_v8m0_ies
        16: rrcconnection_reconfiguration_complete
        17: rrcconnrelease_v9e0_ies
        18: sysinfo
        19: sysinfo_block_type1
        20: sysinfo_block_type1_v8h0_ies
        21: uecapabilityenquiry
        22: uecapabilityinformation
        23: ueinforesponse_v9e0_ies
        24: sysinfo_block_type2_v8h0_ies
        25: sysinfo_block_type5_v8h0_ies
        26: sysinfo_block_type6_v8h0_ies
        27: csi_im_configid_r12
        28: ellipsoid_point
        29: ellipsoid_point_altitude
        30: ellipsoid_point_altitude_uncertainty_ellipsoid
        31: ellipsoid_arc
        32: ellipsoid_point_uncertainty_circle
        33: ellipsoid_point_uncertainty_ellipse
        34: horizontal_velocity
        35: polygon
        36: measurement_ref_time
        37: ue_eutra_cap
        38: ue_eutra_cap_v9a0_ies
        39: ue_radio_paging_r12
        40: var_short_mac_input
        41: els_sib1_signature
        42: els_sysinfo_block_type1
        43: nhn_plmn_identity_list
        44: els_dl_ccch
        45: els_dl_dcch
        46: els_ul_dcch
        47: bcch_bch_mf
        48: bcch_dl_sch_mf
        49: pcch_mf
        50: dl_ccch_mf
        51: dl_dcch_mf
        52: ul_ccch_mf
        53: ul_dcch_mf
        54: sysinfo_block_typemf1

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::pcch_type ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_ccch_type ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::dl_dcch_type ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch_type ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::ul_dcch_type ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_mf ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch_mf ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::pcch_mf ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch_mf ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch_mf ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch_mf ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch_mf ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch_type
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_dcch_type
          or pdu_type == pdu_type::els_ul_dcch
          or pdu_type == pdu_type::ul_ccch_mf
          or pdu_type == pdu_type::ul_dcch_mf

  v19_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_mbms
        3: bcch_dl_sch
        4: bcch_dl_sch_br
        5: bcch_dl_sch_mbms
        6: mcch
        7: pcch
        8: dl_ccch
        9: dl_dcch
        10: ul_ccch
        11: ul_dcch
        12: sc_mcch_r13
        13: rrcconnection_reconfiguration
        14: rrcconnection_reconfiguration_v8m0_ies
        15: rrcconnection_reconfiguration_complete
        16: rrcconnrelease_v9e0_ies
        17: scgfail_info_v12d0
        18: sysinfo_block_type1
        19: sysinfo_block_type1_v8h0_ies
        20: uecapabilityenquiry
        21: uecapabilityinformation
        22: ueinforesponse_v9e0_ies
        23: sysinfo_block_type2_v8h0_ies
        24: sysinfo_block_type3_v10j0_ies
        25: sysinfo_block_type5_v8h0_ies
        26: sysinfo_block_type6_v8h0_ies
        27: csi_rs_configid_r14xy
        28: pusch_config_dedscell_r14xy
        29: tdd_config_sl_r12
        30: ellipsoid_point
        31: ellipsoid_point_altitude
        32: ellipsoid_point_altitude_uncertainty_ellipsoid
        33: ellipsoid_arc
        34: ellipsoid_point_uncertainty_circle
        35: ellipsoid_point_uncertainty_ellipse
        36: horizontal_velocity
        37: polygon
        38: measurement_ref_time
        39: rsrp_rangesl3_r12
        40: ue_eutra_cap
        41: ue_eutra_cap_v9a0_ies
        42: ue_eutra_cap_v10j0_ies
        43: var_short_mac_input
        44: sl_offset_ind_sync_r14
        45: bcch_bch_nb
        46: bcch_dl_sch_nb
        47: pcch_nb
        48: dl_ccch_nb
        49: dl_dcch_nb
        50: ul_ccch_nb
        51: sc_mcch_nb
        52: ul_dcch_nb
        53: els_sib1_signature
        54: els_sysinfo_block_type1
        55: els_dl_dcch
        56: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::bcch_dl_sch_mbms ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_mbms
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::sc_mcch_r13 ? gsmtap_v2::lte_rrc_subtype::sc_mcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v20_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: rrcconnection_reconfiguration
        11: rrcconnection_reconfiguration_v8m0_ies
        12: rrcconnection_reconfiguration_complete
        13: rrcconnrelease_v9e0_ies
        14: sysinfo_block_type1
        15: sysinfo_block_type1_v8h0_ies
        16: uecapabilityenquiry
        17: uecapabilityinformation
        18: ueinforesponse_v9e0_ies
        19: sysinfo_block_type2
        20: sysinfo_block_type2_v8h0_ies
        21: sysinfo_block_type3_v10j0_ies
        22: sysinfo_block_type5_v8h0_ies
        23: sysinfo_block_type6_v8h0_ies
        24: rsrp_rangesl3_r12
        25: rsrp_rangesl4_r13
        26: wlan_status_r13
        27: wlan_status_v1430
        28: ue_eutra_cap
        29: ue_eutra_cap_v9a0_ies
        30: ue_eutra_cap_v10j0_ies
        31: v2x_band_width_class_r14
        32: supported_band_infolist_r12
        33: freq_band_indicatorlist_eutra_r12
        34: var_short_mac_input
        35: pci_arfcn_r13
        36: sl_anchor_carrier_freqlist_v2x_r14
        37: sl_comm_tx_pool_list_r12
        38: sl_comm_tx_pool_list_ext_r13
        39: sl_comm_rx_pool_list_r12
        40: sl_disc_sysinfo_report_r13
        41: sl_gap_request_r13
        42: sl_offset_indicator_sync_r14
        43: sl_sync_config_list_r12
        44: sl_sync_config_listnfreq_r13
        45: ellipsoid_point
        46: ellipsoid_point_altitude
        47: ellipsoid_point_altitude_uncertainty_ellipsoid
        48: ellipsoid_arc
        49: ellipsoid_point_uncertainty_circle
        50: ellipsoid_point_uncertainty_ellipse
        51: horizontal_velocity
        52: polygon
        53: measurement_ref_time
        54: bcch_bch_nb
        55: bcch_dl_sch_nb
        56: pcch_nb
        57: dl_ccch_nb
        58: dl_dcch_nb
        59: ul_ccch_nb
        60: sc_mcch_nb
        61: ul_dcch_nb
        62: els_sib1_signature
        63: els_sysinfo_block_type1
        64: els_dl_dcch
        65: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v21_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: pcch_type
        6: dl_ccch
        7: dl_ccch_type
        8: dl_dcch
        9: dl_dcch_type
        10: ul_ccch
        11: ul_ccch_type
        12: ul_dcch
        13: ul_dcch_type
        14: rrcconnection_reconfiguration
        15: rrcconnection_reconfiguration_v8m0_ies
        16: rrcconnection_reconfiguration_complete
        17: rrcconnrelease_v9e0_ies
        18: sysinfo
        19: sysinfo_block_type1
        20: sysinfo_block_type1_v8h0_ies
        21: uecapabilityenquiry
        22: uecapabilityinformation
        23: ueinforesponse_v9e0_ies
        24: sysinfo_block_type2_v8h0_ies
        25: sysinfo_block_type5_v8h0_ies
        26: sysinfo_block_type6_v8h0_ies
        27: csi_im_configid_r12
        28: ellipsoid_point
        29: ellipsoid_point_altitude
        30: ellipsoid_point_altitude_uncertainty_ellipsoid
        31: ellipsoid_arc
        32: ellipsoid_point_uncertainty_circle
        33: ellipsoid_point_uncertainty_ellipse
        34: horizontal_velocity
        35: polygon
        36: measurement_ref_time
        37: meas_objid_v1310
        38: ue_eutra_cap
        39: ue_eutra_cap_v9a0_ies
        40: ue_radio_paging_r12
        41: var_short_mac_input
        42: els_sib1_signature
        43: els_sysinfo_block_type1
        44: nhn_plmn_identity_list
        45: els_dl_ccch
        46: els_dl_dcch
        47: els_ul_dcch
        48: bcch_bch_mf
        49: bcch_dl_sch_mf
        50: pcch_mf
        51: dl_ccch_mf
        52: dl_dcch_mf
        53: ul_ccch_mf
        54: ul_dcch_mf
        55: sysinfo_block_typemf1

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::pcch_type ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_ccch_type ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::dl_dcch_type ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch_type ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::ul_dcch_type ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_mf ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch_mf ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::pcch_mf ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch_mf ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch_mf ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch_mf ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch_mf ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch_type
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_dcch_type
          or pdu_type == pdu_type::els_ul_dcch
          or pdu_type == pdu_type::ul_ccch_mf
          or pdu_type == pdu_type::ul_dcch_mf

  v22_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: mcch
        4: pcch
        5: dl_ccch
        6: dl_dcch
        7: ul_ccch
        8: ul_dcch
        9: rrcconnection_reconfiguration
        10: rrcconnection_reconfiguration_v8m0_ies
        11: rrcconnection_reconfiguration_complete
        12: rrcconnrelease_v9e0_ies
        13: sysinfo_block_type1
        14: sysinfo_block_type1_v8h0_ies
        15: uecapabilityenquiry
        16: uecapabilityinformation
        17: ueinforesponse_v9e0_ies
        18: sysinfo_block_type2_v8h0_ies
        19: sysinfo_block_type5_v8h0_ies
        20: sysinfo_block_type6_v8h0_ies
        21: tdd_configsl_r12
        22: ellipsoid_point
        23: ellipsoid_point_altitude
        24: ellipsoid_point_altitude_uncertainty_ellipsoid
        25: ellipsoid_arc
        26: ellipsoid_point_uncertainty_circle
        27: ellipsoid_point_uncertainty_ellipse
        28: horizontal_velocity
        29: polygon
        30: measurement_ref_time
        31: rsrp_rangsl3_r12
        32: ue_eutra_cap
        33: ue_eutra_cap_v9a0_ies
        34: var_short_mac_input
        35: els_sib1_signature
        36: els_sysinfo_block_type1
        37: els_dl_dcch
        38: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::els_ul_dcch

  v23_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: master_information_block_mbms_r14
        11: rrcconnection_reconfiguration
        12: rrcconnection_reconfiguration_v8m0_ies
        13: rrcconnection_reconfiguration_complete
        14: rrcconnection_release_v9e0_ies
        15: scgfailure_information_v12d0_ies
        16: scptmconfiguration_r13
        17: scptmconfiguration_br_r14
        18: system_information_mbms_r14
        19: system_information_block_type1
        20: system_information_block_type1_v8h0_ies
        21: system_information_block_type1_mbms_r14
        22: uecapability_enquiry
        23: uecapability_information
        24: ueinformation_response_v9e0_ies
        25: system_information_block_type2
        26: system_information_block_type2_v8h0_ies
        27: system_information_block_type3_v10j0_ies
        28: system_information_block_type5_v8h0_ies
        29: system_information_block_type6_v8h0_ies
        30: tdd_config_sl_r12
        31: rsrp_range_sl3_r12
        32: ue_eutra_capability
        33: ue_eutra_capability_v9a0_ies
        34: ue_eutra_capability_v10j0_ies
        35: sl_offset_indicator_sync_r14
        36: var_short_mac_input
        37: ellipsoid_point
        38: ellipsoid_point_with_altitude
        39: ellipsoid_point_with_altitude_and_uncertainty_ellipsoid
        40: ellipsoid_arc
        41: ellipsoid_point_with_uncertainty_circle
        42: ellipsoid_point_with_uncertainty_ellipse
        43: horizontal_velocity
        44: polygon
        45: measurement_reference_time
        46: bcch_bch_nb
        47: bcch_dl_sch_nb
        48: pcch_nb
        49: dl_ccch_nb
        50: dl_dcch_nb
        51: ul_ccch_nb
        52: sc_mcch_nb
        53: ul_dcch_nb
        54: els_sib1_signature
        55: els_system_information_block_type1
        56: els_dl_dcch
        57: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v24_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: master_information_block_mbms_r14
        11: rrcconnection_reconfiguration
        12: rrcconnection_reconfiguration_v8m0_ies
        13: rrcconnection_reconfiguration_complete
        14: rrcconnection_release_v9e0_ies
        15: scgfailure_information_v12d0_ies
        16: scptmconfiguration_r13
        17: scptmconfiguration_br_r14
        18: system_information_mbms_r14
        19: system_information_block_type1
        20: system_information_block_type1_v8h0_ies
        21: system_information_block_type1_mbms_r14
        22: uecapability_enquiry
        23: uecapability_information
        24: ueinformation_response_v9e0_ies
        25: system_information_block_type2
        26: system_information_block_type2_v8h0_ies
        27: system_information_block_type2_v10m0_ies
        28: system_information_block_type3_v10j0_ies
        29: system_information_block_type5_v8h0_ies
        30: system_information_block_type6_v8h0_ies
        31: tdd_config_sl_r12
        32: rsrp_range_sl3_r12
        33: ue_eutra_capability
        34: ue_eutra_capability_v9a0_ies
        35: ue_eutra_capability_v10j0_ies
        36: sl_offset_indicator_sync_r14
        37: var_short_mac_input
        38: ellipsoid_point
        39: ellipsoid_point_with_altitude
        40: ellipsoid_point_with_altitude_and_uncertainty_ellipsoid
        41: ellipsoid_arc
        42: ellipsoid_point_with_uncertainty_circle
        43: ellipsoid_point_with_uncertainty_ellipse
        44: horizontal_velocity
        45: polygon
        46: measurement_reference_time
        47: bcch_bch_nb
        48: bcch_dl_sch_nb
        49: pcch_nb
        50: dl_ccch_nb
        51: dl_dcch_nb
        52: ul_ccch_nb
        53: sc_mcch_nb
        54: ul_dcch_nb
        55: els_sib1_signature
        56: els_system_information_block_type1
        57: els_dl_dcch
        58: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v25_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: bcch_dl_sch_br
        4: mcch
        5: pcch
        6: dl_ccch
        7: dl_dcch
        8: ul_ccch
        9: ul_dcch
        10: master_information_block_mbms_r14
        11: rrcconnection_reconfiguration
        12: rrcconnection_reconfiguration_v8m0_ies
        13: rrcconnection_reconfiguration_complete
        14: rrcconnection_release_v9e0_ies
        15: scgfailure_information_v12d0_ies
        16: scptmconfiguration_r13
        17: scptmconfiguration_br_r14
        18: system_information_mbms_r14
        19: system_information_block_type1
        20: system_information_block_type1_v8h0_ies
        21: system_information_block_type1_mbms_r14
        22: uecapability_enquiry
        23: uecapability_information
        24: ueinformation_response_v9e0_ies
        25: system_information_block_type2
        26: system_information_block_type2_v8h0_ies
        27: system_information_block_type2_v10m0_ies
        28: system_information_block_type3_v10j0_ies
        29: system_information_block_type5_v8h0_ies
        30: system_information_block_type6_v8h0_ies
        31: sps_config_dl_stti_r15
        32: tdd_config_sl_r12
        33: rsrp_range_sl3_r12
        34: ue_eutra_capability
        35: ue_eutra_capability_v9a0_ies
        36: ue_eutra_capability_v10j0_ies
        37: var_short_mac_input
        38: ellipsoid_point
        39: ellipsoid_point_with_altitude
        40: ellipsoid_point_with_altitude_and_uncertainty_ellipsoid
        41: ellipsoid_arc
        42: ellipsoid_point_with_uncertainty_circle
        43: ellipsoid_point_with_uncertainty_ellipse
        44: horizontal_velocity
        45: polygon
        46: measurement_reference_time
        47: bcch_bch_nb
        48: bcch_bch_tdd_nb
        49: bcch_dl_sch_nb
        50: pcch_nb
        51: dl_ccch_nb
        52: dl_dcch_nb
        53: ul_ccch_nb
        54: sc_mcch_nb
        55: ul_dcch_nb
        56: ue_capability_nb_ext_r14_ies
        57: els_sib1_signature
        58: els_system_information_block_type1
        59: els_dl_dcch
        60: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_bch_tdd_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_tdd_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v26_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_bch_mbms
        3: bcch_dl_sch
        4: bcch_dl_sch_br
        5: bcch_dl_sch_mbms
        6: mcch
        7: pcch
        8: dl_ccch
        9: dl_dcch
        10: ul_ccch
        11: ul_dcch
        12: sc_mcch_r13
        13: rrcconnection_reconfiguration
        14: rrcconnection_reconfiguration_v8m0_ies
        15: rrcconnection_reconfiguration_complete
        16: rrcconnection_release_v9e0_ies
        17: scgfailure_information_v12d0_ies
        18: system_information_block_type1
        19: system_information_block_type1_v8h0_ies
        20: uecapability_enquiry
        21: uecapability_information
        22: ueinformation_response_v9e0_ies
        23: system_information_block_type2
        24: system_information_block_type2_v8h0_ies
        25: system_information_block_type2_v10m0_ies
        26: system_information_block_type3_v10j0_ies
        27: system_information_block_type5_v8h0_ies
        28: system_information_block_type6_v8h0_ies
        29: tdd_config_sl_r12
        30: rsrp_range_sl3_r12
        31: ue_eutra_capability
        32: ue_eutra_capability_v9a0_ies
        33: ue_eutra_capability_v10j0_ies
        34: var_short_mac_input
        35: ellipsoid_point
        36: ellipsoid_point_with_altitude
        37: ellipsoid_point_with_altitude_and_uncertainty_ellipsoid
        38: ellipsoid_arc
        39: ellipsoid_point_with_uncertainty_circle
        40: ellipsoid_point_with_uncertainty_ellipse
        41: horizontal_velocity
        42: polygon
        43: measurement_reference_time
        44: bcch_bch_nb
        45: bcch_bch_tdd_nb
        46: bcch_dl_sch_nb
        47: pcch_nb
        48: dl_ccch_nb
        49: dl_dcch_nb
        50: ul_ccch_nb
        51: sc_mcch_nb
        52: ul_dcch_nb
        53: ue_capability_nb_ext_r14_ies
        54: els_sib1_signature
        55: els_system_information_block_type1
        56: els_dl_dcch
        57: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_bch_mbms ? gsmtap_v2::lte_rrc_subtype::bcch_bch_mbms
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::bcch_dl_sch_mbms ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_mbms
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::sc_mcch_r13 ? gsmtap_v2::lte_rrc_subtype::sc_mcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_bch_tdd_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_tdd_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

  v27_pdu_type:
    seq:
      - id: pdu_type
        type: b7
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_bch_mbms
        3: bcch_dl_sch
        4: bcch_dl_sch_br
        5: bcch_dl_sch_mbms
        6: mcch
        7: pcch
        8: dl_ccch
        9: dl_dcch
        10: ul_ccch
        11: ul_dcch
        12: sc_mcch_r13
        13: rrcconnection_reconfiguration
        14: rrcconnection_reconfiguration_v8m0_ies
        15: rrcconnection_reconfiguration_complete
        16: rrcconnection_release_v9e0_ies
        17: scgfailure_information_v12d0b_ies
        18: system_information_block_type1
        19: system_information_block_type1_v8h0_ies
        20: uecapability_enquiry
        21: uecapability_information
        22: ueinformation_response_v9e0_ies
        23: type_ffs
        24: system_information_block_type2
        25: system_information_block_type2_v8h0_ies
        26: system_information_block_type2_v10m0_ies
        27: system_information_block_type3_v10j0_ies
        28: system_information_block_type5_v8h0_ies
        29: system_information_block_type6_v8h0_ies
        30: tdd_config_sl_r12
        31: meas_result_scg_failure_mrdc_r15
        32: rsrp_range_sl3_r12
        33: ue_eutra_capability
        34: ue_eutra_capability_v9a0_ies
        35: ue_eutra_capability_v10j0_ies
        36: ue_eutra_capability_v13e0b_ies
        37: var_short_mac_input
        38: var_short_resume_mac_input_r13
        39: ellipsoid_point
        40: ellipsoid_point_with_altitude
        41: ellipsoid_point_with_altitude_and_uncertainty_ellipsoid
        42: ellipsoid_arc
        43: ellipsoid_point_with_uncertainty_circle
        44: ellipsoid_point_with_uncertainty_ellipse
        45: horizontal_velocity
        46: polygon
        47: measurement_reference_time
        48: bcch_bch_nb
        49: bcch_bch_tdd_nb
        50: bcch_dl_sch_nb
        51: pcch_nb
        52: dl_ccch_nb
        53: dl_dcch_nb
        54: ul_ccch_nb
        55: sc_mcch_nb
        56: ul_dcch_nb
        57: ue_capability_nb_ext_r14_ies
        58: els_sib1_signature
        59: els_system_information_block_type1
        60: els_dl_dcch
        61: els_ul_dcch

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v2::lte_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_bch_mbms ? gsmtap_v2::lte_rrc_subtype::bcch_bch_mbms
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::bcch_dl_sch_br ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_br
          : pdu_type == pdu_type::bcch_dl_sch_mbms ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_mbms
          : pdu_type == pdu_type::mcch ? gsmtap_v2::lte_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v2::lte_rrc_subtype::pcch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v2::lte_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v2::lte_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::sc_mcch_r13 ? gsmtap_v2::lte_rrc_subtype::sc_mcch
          : pdu_type == pdu_type::bcch_bch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_nb
          : pdu_type == pdu_type::bcch_bch_tdd_nb ? gsmtap_v2::lte_rrc_subtype::bcch_bch_tdd_nb
          : pdu_type == pdu_type::bcch_dl_sch_nb ? gsmtap_v2::lte_rrc_subtype::bcch_dl_sch_nb
          : pdu_type == pdu_type::pcch_nb ? gsmtap_v2::lte_rrc_subtype::pcch_nb
          : pdu_type == pdu_type::dl_ccch_nb ? gsmtap_v2::lte_rrc_subtype::dl_ccch_nb
          : pdu_type == pdu_type::dl_dcch_nb ? gsmtap_v2::lte_rrc_subtype::dl_dcch_nb
          : pdu_type == pdu_type::ul_ccch_nb ? gsmtap_v2::lte_rrc_subtype::ul_ccch_nb
          : pdu_type == pdu_type::sc_mcch_nb ? gsmtap_v2::lte_rrc_subtype::sc_mcch_nb
          : pdu_type == pdu_type::ul_dcch_nb ? gsmtap_v2::lte_rrc_subtype::ul_dcch_nb
          : pdu_type == pdu_type::els_dl_dcch ? gsmtap_v2::lte_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::els_ul_dcch ? gsmtap_v2::lte_rrc_subtype::ul_dcch
          : gsmtap_v2::lte_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_dcch
          or pdu_type == pdu_type::ul_ccch_nb
          or pdu_type == pdu_type::ul_dcch_nb
          or pdu_type == pdu_type::els_ul_dcch

