meta:
  id: nr5g_rrc_ota_packet
  endian: le
  bit-endian: be
  imports:
    - ../../../gsmtap/gsmtap_v3

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
        1: v1_pdu_type
        2: v2_pdu_type
        3: v3_pdu_type
        4: v4_pdu_type
        5: v5_pdu_type
        6: v6_pdu_type
        7: v7_pdu_type
        8: v8_pdu_type
        9: v9_pdu_type
        10: v10_pdu_type
        11: v11_pdu_type
        12: v11_pdu_type
        13: v13_pdu_type
        14: v14_pdu_type
        15: v15_pdu_type
        16: v16_pdu_type
        17: v17_pdu_type
        18: v17_pdu_type
        19: v17_pdu_type
        20: v20_pdu_type
        23: v20_pdu_type
        24: v20_pdu_type
        25: v17_pdu_type
        26: v26_pdu_type
        28: v26_pdu_type
        _: v20_pdu_type

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

  v1_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: xbcch_bch
        2: dl_xccch
        3: dl_xdcch
        4: ul_xccch
        5: ul_xdcch
        6: beam_id
        7: plmn_id_list
        8: ue_5gra_cap
        9: var_short_mac
        10: default_config

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::xbcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::dl_xccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_xdcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_xccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_xdcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_xccch
          or pdu_type == pdu_type::ul_xdcch

  v2_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: dl_dcch
        3: ul_dcch
        4: reconfig
        5: reconfig_complete
        6: sb1
        7: beam_fail_recovery_config
        8: meas_result_scg_fail
        9: radio_bearer_config
        10: subcarrier_spacing_rach
        11: band_param_comb_list_ul
        12: ue_capability_rat_container_list
        13: ue_mrdc_capability
        14: ue_nr_capability
        15: supported_band_comb
        16: candidate_rs_index_info_list
        17: cellid
        18: meas_obj_eutra
        19: meas_result_list_eutra
        20: meas_result_sstd
        21: phy_cellnr
        22: phys_cellid_eutra
        23: short_mac_i
        24: ue_capability_info
        25: mbsfn_subframe_config_list

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_dcch

  v3_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: dl_dcch
        3: ul_dcch
        4: reconfig
        5: reconfig_complete
        6: sb1
        7: cell_group_config
        8: gscn_value_nr
        9: meas_result_scg_failure
        10: meas_result_celllist_sftd
        11: radio_bearer_config
        12: freq_band_list
        13: ue_capability_rat_containerlist
        14: ue_mrdc_capability
        15: ue_nr_capability
        16: cellid
        17: short_mac_i

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_dcch

  v4_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: mob_from_nr_cmd
        10: reconfig
        11: reconfig_complete
        12: sib1
        13: systeminfo
        14: amf_id
        15: cell_group_config
        16: meas_result_scg_failure
        17: meas_result_celllist_sftd
        18: radio_bearer_config
        19: ue_capability_req_filter_nr
        20: ue_mrdc_capability
        21: ue_nr_capability

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v5_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: reconfig
        10: reconfig_complete
        11: sib1
        12: systeminfo
        13: sib2
        14: sib3
        15: sib4
        16: sib5
        17: sib6
        18: sib7

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v6_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: reconfig
        10: reconfig_complete
        11: sib1
        12: systeminfo
        13: sib2
        14: sib3
        15: sib4
        16: sib5
        17: sib6
        18: sib7
        19: sib8
        20: sib9
        21: cell_group_config
        22: meas_result_celllist_sftd
        23: meas_result_scg_failure
        24: radio_bearer_config
        25: ue_capability_req_filter_nr
        26: ue_mrdc_capability
        27: ue_nr_capability
        28: var_resume_mac_input
        29: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v7_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: reconfig
        10: reconfig_complete
        11: sib1
        12: systeminfo
        13: sib2
        14: sib3
        15: sib4
        16: sib5
        17: sib6
        18: sib7
        19: sib8
        20: sib9
        21: cell_group_config
        22: meas_result_celllist_sftd
        23: meas_result_scg_failure
        24: radio_bearer_config
        25: freq_band_list
        26: ue_capability_req_filter_nr
        27: ue_mrdc_capability
        28: ue_nr_capability
        29: var_resume_mac_input
        30: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v8_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: sysinfo
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: cell_group_config
        23: meas_result_celllist_sftd_nr
        24: meas_result_celllist_eutra
        25: meas_result_scg_fail
        26: radio_bearer_config
        27: freq_band_list
        28: ue_cap_req_filter_nr
        29: ue_mrdc_capability
        30: ue_nr_capability
        31: var_resume_mac_input
        32: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v9_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: sysinfo
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: cell_group_config
        23: meas_result_celllist_eutra
        24: meas_result_scg_fail
        25: radio_bearer_config
        26: freq_band_list
        27: ue_cap_req_filter_nr
        28: ue_mrdc_capability
        29: ue_nr_capability
        30: var_resume_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v10_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: sysinfo
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: cell_group_config
        23: meas_result_celllist_eutra
        24: meas_result_scg_fail
        25: radio_bearer_config
        26: freq_band_list
        27: ue_cap_req_filter_nr
        28: ue_mrdc_capability
        29: ue_nr_capability
        30: var_resume_mac_input
        31: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v11_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: sysinfo
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: sib12_ie_r16
        23: pos_sysinfo_r16
        24: cell_group_config
        25: meas_result_celllist_eutra
        26: meas_result_scg_fail
        27: radio_bearer_config
        28: freq_band_list
        29: ue_cap_req_filter_nr
        30: ue_mrdc_capability
        31: ue_nr_capability
        32: var_resume_mac_input
        33: var_rlf_rpt_r16
        34: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v13_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: sysinfo
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: sib12_ie_r16
        23: pos_sysinfo_r16
        24: cell_group_config
        25: meas_result_celllist_eutra
        26: meas_result_scg_fail
        27: radio_bearer_config
        28: freq_band_list
        29: ue_cap_req_filter_nr
        30: ue_mrdc_capability
        31: ue_nr_capability
        32: ue_nr_capability_v15c0
        33: var_resume_mac_input
        34: var_rlf_rpt_r16
        35: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : pdu_type == pdu_type::ue_nr_capability_v15c0 ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v14_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: systeminformation
        13: overheatingassistance
        14: uecapenquiry_v1560_ie
        15: sib2
        16: sib3
        17: sib4
        18: sib5
        19: sib6
        20: sib7
        21: sib8
        22: sib9
        23: sib12_ie_r16
        24: pos_sysinfo_r16
        25: cell_group_config
        26: meas_result_celllist_eutra
        27: meas_result_scg_fail
        28: radio_bearer_config
        29: freq_band_list
        30: ue_cap_req_filter_nr
        31: ue_mrdc_capability
        32: ue_nr_capability
        33: ue_nr_capability_v15c0
        34: var_resume_mac_input
        35: var_rlf_rpt_r16
        36: var_short_mac_input

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : pdu_type == pdu_type::ue_nr_capability_v15c0 ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v15_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: systeminformation
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: sib12_ie_r16
        23: pos_sysinfo_r16
        24: cell_group_config
        25: meas_result_celllist_eutra
        26: meas_result_scg_fail
        27: radio_bearer_config
        28: freq_band_list
        29: ue_cap_req_filter_nr
        30: ue_mrdc_capability
        31: ue_nr_capability
        32: ue_nr_capability_v15c0
        33: var_resume_mac_input
        34: var_rlf_rpt_r16
        35: var_short_mac_input
        36: locationcoordinates
        37: velocity
        38: locationerror
        39: locationerror_r13
        40: displacementtimestamp_r15

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : pdu_type == pdu_type::ue_nr_capability_v15c0 ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v16_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: systeminformation
        13: uecapenquiry_v1560_ie
        14: sib2
        15: sib3
        16: sib4
        17: sib5
        18: sib6
        19: sib7
        20: sib8
        21: sib9
        22: sib12_ie_r16
        23: pos_sysinfo_r16
        24: cell_group_config
        25: meas_result_celllist_eutra
        26: meas_result_scg_fail
        27: radio_bearer_config
        28: freq_band_list
        29: ue_cap_req_filter_nr
        30: ue_mrdc_capability
        31: ue_nr_capability
        32: ue_nr_capability_v15c0
        33: var_resume_mac_input
        34: var_rlf_rpt_r16
        35: var_short_mac_input
        36: locationcoordinates
        37: velocity
        38: locationerror
        39: locationerror_r13
        40: displacementtimestamp_r15

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : pdu_type == pdu_type::ue_nr_capability_v15c0 ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v17_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: pcch
        6: ul_ccch
        7: ul_ccch1
        8: ul_dcch
        9: rrc_reconfig
        10: rrc_reconfig_complete
        11: sib1
        12: systeminformation
        13: overheatingassistance
        14: uecapenquiry_v1560_ie
        15: sib2
        16: sib3
        17: sib4
        18: sib5
        19: sib6
        20: sib7
        21: sib8
        22: sib9
        23: sib10_r16
        24: sib12_ie_r16
        25: pos_sysinfo_r16
        26: cell_group_config
        27: meas_result_celllist_eutra
        28: meas_result_scg_fail
        29: radio_bearer_config
        30: freq_band_list
        31: ue_cap_req_filter_nr
        32: ue_mrdc_capability
        33: ue_nr_capability
        34: ue_nr_capability_v15c0
        35: var_resume_mac_input
        36: var_rlf_rpt_r16
        37: var_short_mac_input
        38: locationcoordinates
        39: velocity
        40: locationerror
        41: locationsource_r13
        42: displacementtimestamp_r15

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : pdu_type == pdu_type::sib1 ? gsmtap_v3::nr_rrc_subtype::sib1
          : pdu_type == pdu_type::sib2 ? gsmtap_v3::nr_rrc_subtype::sib2
          : pdu_type == pdu_type::sib3 ? gsmtap_v3::nr_rrc_subtype::sib3
          : pdu_type == pdu_type::sib4 ? gsmtap_v3::nr_rrc_subtype::sib4
          : pdu_type == pdu_type::sib5 ? gsmtap_v3::nr_rrc_subtype::sib5
          : pdu_type == pdu_type::sib6 ? gsmtap_v3::nr_rrc_subtype::sib6
          : pdu_type == pdu_type::sib7 ? gsmtap_v3::nr_rrc_subtype::sib7
          : pdu_type == pdu_type::sib8 ? gsmtap_v3::nr_rrc_subtype::sib8
          : pdu_type == pdu_type::sib9 ? gsmtap_v3::nr_rrc_subtype::sib9
          : pdu_type == pdu_type::sib10_r16 ? gsmtap_v3::nr_rrc_subtype::sib10_r16
          : pdu_type == pdu_type::sib12_ie_r16 ? gsmtap_v3::nr_rrc_subtype::sib12_r16
          : pdu_type == pdu_type::ue_mrdc_capability ? gsmtap_v3::nr_rrc_subtype::ue_mrdc_capability
          : pdu_type == pdu_type::ue_nr_capability ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : pdu_type == pdu_type::ue_nr_capability_v15c0 ? gsmtap_v3::nr_rrc_subtype::ue_nr_capability
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v20_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: mcch
        6: pcch
        7: ul_ccch
        8: ul_ccch1
        9: ul_dcch
        10: rrc_reconfig
        11: rrc_reconfig_complete

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::mcch ? gsmtap_v3::nr_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch

  v26_pdu_type:
    seq:
      - id: pdu_type
        type: u1
        enum: pdu_type

    enums:
      pdu_type:
        1: bcch_bch
        2: bcch_dl_sch
        3: dl_ccch
        4: dl_dcch
        5: mcch
        6: pcch
        7: ul_ccch
        8: ul_ccch1
        9: ul_dcch
        11: rrc_reconfig
        12: rrc_reconfig_complete

    instances:
      gsmtap_subtype:
        value: |
          pdu_type == pdu_type::bcch_bch ? gsmtap_v3::nr_rrc_subtype::bcch_bch
          : pdu_type == pdu_type::bcch_dl_sch ? gsmtap_v3::nr_rrc_subtype::bcch_dl_sch
          : pdu_type == pdu_type::dl_ccch ? gsmtap_v3::nr_rrc_subtype::dl_ccch
          : pdu_type == pdu_type::dl_dcch ? gsmtap_v3::nr_rrc_subtype::dl_dcch
          : pdu_type == pdu_type::mcch ? gsmtap_v3::nr_rrc_subtype::mcch
          : pdu_type == pdu_type::pcch ? gsmtap_v3::nr_rrc_subtype::pcch
          : pdu_type == pdu_type::ul_ccch ? gsmtap_v3::nr_rrc_subtype::ul_ccch
          : pdu_type == pdu_type::ul_ccch1 ? gsmtap_v3::nr_rrc_subtype::ul_ccch1
          : pdu_type == pdu_type::ul_dcch ? gsmtap_v3::nr_rrc_subtype::ul_dcch
          : pdu_type == pdu_type::rrc_reconfig ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration
          : pdu_type == pdu_type::rrc_reconfig_complete ? gsmtap_v3::nr_rrc_subtype::rrc_reconfiguration_complete
          : gsmtap_v3::nr_rrc_subtype::unknown

      is_uplink:
        value: |
          pdu_type == pdu_type::ul_ccch
          or pdu_type == pdu_type::ul_ccch1
          or pdu_type == pdu_type::ul_dcch



