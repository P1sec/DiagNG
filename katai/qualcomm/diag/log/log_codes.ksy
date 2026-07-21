# WIP

# From https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/protocol/log_types.py

enums:
  log_category:
    1: log_1x
    4: log_wcdma
    5: log_gsm
    6: log_lbs
    7: log_umts
    8: log_tdma
    0xa: log_dtv
    0xb: log_apps_lte_wimax
    0xc: log_dsp
    0xd: log_tdscdma
    0xf: log_tools

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

