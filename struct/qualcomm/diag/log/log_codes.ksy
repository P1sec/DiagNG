meta:
  id: diag_logging

# From https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/protocol/log_types.py

enums:
  log_masks_readable:
    0xf000: category_log_mask
    # if (log_type & log_category_mask == 0xb000
    #  or log_type & log_category_mask == 0xd000)
    0xfc00: category_log_mask_extended

  log_masks_qcdm:
    0xf000: equipment_id_mask
    0x0fff: item_id_mask

  equipment_id:
    0x1: log_1x
    0x4: log_wcdma
    0x5: log_gsm
    0x6: log_lbs
    0x7: log_umts
    0x8: log_tdma
    0xa: log_dtv
    0xb: log_lte_wimax_nr
    0xc: log_dsp
    0xd: log_tdscdma
    0xf: log_tools

  log_category:
    0x1000: log_1x
    0x4000: log_wcdma
    0x5000: log_gsm
    0x6000: log_lbs
    0x7000: log_umts
    0x8000: log_tdma
    0xa000: log_dtv
    0xb000: log_lte
    0xb400: log_wimax
    0xb800: log_nr
    0xc000: log_dsp
    0xd000: log_tdscdma
    0xf000: log_tools

  log_1x:
    # Upper layers
    0x11eb: data_protocol_logging_c

    # Extended DPL (Data Protocol Logging) - Network IP variants:
    0x1572: data_protocol_logging_network_ip_rm_tx_80_bytes_c
    0x1573: data_protocol_logging_network_ip_rm_rx_80_bytes_c
    0x1574: data_protocol_logging_network_ip_rm_tx_full_c
    0x1575: data_protocol_logging_network_ip_rm_rx_full_c
    0x1576: data_protocol_logging_network_ip_um_tx_80_bytes_c
    0x1577: data_protocol_logging_network_ip_um_rx_80_bytes_c
    0x1578: data_protocol_logging_network_ip_um_tx_full_c
    0x1579: data_protocol_logging_network_ip_um_rx_full_c

  log_wcdma:
    # 3G layer 3 packets
    0x412f: signalling_message

  log_gsm:
    0x512f: gsm_rr_signaling_message_c
    0x5226: gprs_mac_signaling_message_c

  log_lte:
    0xb0c0: rrc_ota_msg_log_c
    0xb0e2: nas_esm_ota_in_msg_log_c
    0xb0e3: nas_esm_ota_out_msg_log_c
    0xb0ec: nas_emm_ota_in_msg_log_c
    0xb0ed: nas_emm_ota_out_msg_log_c

  log_nr:
    0xb821: nr_rrc_ota_msg_log_c

  log_umts:
    0x713a: nas_ota_message_log_packet_c

