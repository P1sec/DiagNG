meta:
  id: diag_cmd_code
  endian: le

enums:
  diag_cmd:
    # Version Number Request/Response
    0: verno_f

    # Mobile Station ESN Request/Response
    1: esn_f

    # Peek byte Request/Response
    2: peekb_f

    # Peek word Request/Response
    3: peekw_f

    # Peek dword Request/Response
    4: peekd_f

    # Poke byte Request/Response
    5: pokeb_f

    # Poke word Request/Response
    6: pokew_f

    # Poke dword Request/Response
    7: poked_f

    # Byte output Request/Response
    8: outp_f

    # Word output Request/Response
    9: outpw_f

    # Byte input Request/Response
    10: inp_f

    # Word input Request/Response
    11: inpw_f

    # DMSS status Request/Response
    12: status_f

    # 13-14 Reserved

    # Set logging mask Request/Response
    15: logmask_f

    # Log packet Request/Response
    16: log_f

    # Peek at NV memory Request/Response
    17: nv_peek_f

    # Poke at NV memory Request/Response
    18: nv_poke_f

    # Invalid Command Response
    19: bad_cmd_f

    # Invalid parmaeter Response
    20: bad_parm_f

    # Invalid packet length Response
    21: bad_len_f

    # 22-23 Reserved

    # Packet not allowed in this mode (online vs offline)
    24: bad_mode_f

    # info for TA power and voice graphs
    25: tagraph_f

    # Markov statistics
    26: markov_f

    # Reset of Markov statistics
    27: markov_reset_f

    # Return diag version for comparison to detect incompatabilities
    28: diag_ver_f

    # Return a timestamp
    29: ts_f

    # Set TA parameters
    30: ta_parm_f

    # Request for msg report
    31: msg_f

    # Handset Emulation -- keypress
    32: hs_key_f

    # Handset Emulation -- lock or unlock
    33: hs_lock_f

    # Handset Emulation -- display request
    34: hs_screen_f

    # 35 Reserved

    # Parameter Download
    36: parm_set_f

    # 37 Reserved

    # Read NV item
    38: nv_read_f

    # Write NV item
    39: nv_write_f

    # 40 Reserved

    # Mode change request
    41: control_f

    # Error record retreival
    42: err_read_f

    # Error record clear
    43: err_clear_f

    # Symbol error rate counter reset
    44: ser_reset_f

    # Symbol error rate counter report
    45: ser_report_f

    # Run a specified test
    46: test_f

    # Retreive the current dip switch setting
    47: get_dipsw_f

    # Write new dip switch setting
    48: set_dipsw_f

    # Start/Stop Vocoder PCM loopback
    49: voc_pcm_lb_f

    # Start/Stop Vocoder PKT loopback
    50: voc_pkt_lb_f

    # 51-52 Reserved

    # Originate a call
    53: orig_f

    # End a call
    54: end_f

    # 55-57 Reserved

    # Switch to downloader
    58: dload_f

    # Test Mode Commands and FTM commands
    59: tmob_f # Or DIAG_FTM_CMD_F

    # 60-62 Reserved
    61: test_state_f

    # Return the current state of the phone
    63: state_f

    # Return all current sets of pilots
    64: pilot_sets_f

    # Send the Service Prog. Code to allow SP
    65: spc_f

    # Invalid nv_read/write because SP is locked
    66: bad_spc_mode_f

    # get parms obsoletes PARM_GET
    67: parm_get2_f

    # Serial mode change Request/Response
    68: serial_chg_f

    # 69 Reserved

    # Send password to unlock secure operations the phone
    # to be in a security state that is wasn't - like unlocked.
    70: password_f

    # An operation was attempted which required
    71: bad_sec_mode_f

    # Write Preferred Roaming list to the phone.
    72: pr_list_wr_f

    # Read Preferred Roaming list from the phone.*/
    73: pr_list_rd_f

    # 74 Reserved

    # Subssytem dispatcher (extended diag cmd)
    75: cmd_f

    # 76-80 Reserved

    # Asks the phone what it supports
    81: feature_query_f

    # 82 Reserved

    # Read SMS message out of NV
    83: sms_read_f

    # Write SMS message into NV
    84: sms_write_f

    # info for Frame Error Rate on multiple channels
    85: sup_fer_f

    # Supplemental channel walsh codes
    86: sup_walsh_codes_f

    # Sets the maximum # supplemental channels
    87: set_max_sup_ch_f

    # get parms including SUPP and MUX2: obsoletes PARM_GET and PARM_GET_2
    88: parm_get_is95b_f

    # Performs an Embedded File System (EFS) operation.
    89: fs_op_f

    # AKEY Verification.
    90: akey_verify_f

    # Handset emulation - Bitmap screen
    91: bmp_hs_screen_f

    # Configure communications
    92: config_comm_f

    # Extended logmask for > 32 bits. This cmd is Obsolete and replaced
    # by cmd 115, but left in place to support Legacy tools.
    93: ext_logmask_f

    # 94-95 reserved

    # Static Event reporting.
    96: event_report_f

    # Load balancing and more!
    97: streaming_config_f

    # Parameter retrieval
    98: parm_retrieve_f

    # A state/status snapshot of the DMSS.
    99: status_snapshot_f

    # 100 obsolete

    # Get_property requests
    101: get_property_f

    # Put_property requests
    102: put_property_f

    # Get_guid requests
    103: get_guid_f

    # Invocation of user callbacks
    104: user_cmd_f

    # Get permanent properties
    105: get_perm_property_f

    # Put permanent properties
    106: put_perm_property_f

    # Permanent user callbacks
    107: perm_user_cmd_f

    # GPS Session Control
    108: gps_sess_ctrl_f

    # GPS search grid
    109: gps_grid_f

    # GPS Statistics
    110: gps_statistics_f

    # Packet routing for multiple instances of diag
    111: route_f

    # IS2000 status
    112: is2000_status_f

    # RLP statistics reset
    113: rlp_stat_reset_f

    # (S)TDSO statistics reset
    114: tdso_stat_reset_f

    # Logging configuration packet
    115: log_config_f

    # Static Trace Event reporting
    116: trace_event_report_f

    # SBI Read
    117: sbi_read_f

    # SBI Write
    118: sbi_write_f

    # SSD Verify
    119: ssd_verify_f

    # Log on Request
    120: log_on_demand_f

    # Request for extended msg report
    121: ext_msg_f

    # ONCRPC diag packet
    122: oncrpc_f

    # Diagnostics protocol loopback.
    123: protocol_loopback_f

    # Extended build ID text
    124: ext_build_id_f

    # Request for extended msg report
    125: ext_msg_config_f

    # Extended messages in terse format
    126: ext_msg_terse_f

    # Translate terse format message identifier
    127: ext_msg_terse_xlate_f

    # Subssytem dispatcher Version 2 (delayed response capable)
    128: cmd_ver_2_f

    # Get the event mask
    129: event_mask_get_f

    # Set the event mask
    130: event_mask_set_f

    # RESERVED CODES: 131-139

    # Command Code for Changing Port Settings
    140: change_port_settings

    # Country network information for assisted dialing
    141: cntry_info_f

    # Send a Supplementary Service Request
    142: sups_req_f

    # Originate SMS request for MMS
    143: mms_orig_sms_request_f

    # Change measurement mode
    144: meas_mode_f

    # Request measurements for HDR channels
    145: meas_req_f

    # Send Optimized F3 messages
    146: qsr_ext_msg_terse_f

    # Packet ID for command/responses sent over DCI
    147: dci_cmd_req

    # Packet ID for delayed responses sent over DCI
    148: dci_delayed_rsp

    # Error response code on DCI (only APSS side)
    149: bad_trans_f

    # Error response code for cmomands disallowed by SSM
    150: ssm_disallowed_cmd_f

    # Log on extended Request
    151: log_on_demand_ext_f

    # Packet ID for extended event/log/F3 pkt
    152: cmd_ext_f # alias multi_radio_cmd_f

    # Qshrink4 command code for Qshrink 4 packet
    153: qsr4_ext_msg_terse_f

    # DCI command code for dci control packet
    154: dci_control_packet

    # Compressed diag data which is sent out by the DMSS to the host
    155: compressed_pkt

    # QDL (QTI Diagnostic Lite) command code
    156: msg_small_f

    # Payload data for streaming mode of QSH Trace logging feature
    157: qsh_trace_payload_f

    # Secure Logging
    158: log_sec_f

  diag_subsys:
    0: oem # Reserved for OEM use
    1: zrex # ZREX
    2: sd # System Determination
    3: bt # Bluetooth
    4: wcdma # WCDMA
    5: hdr # 1xEvDO
    6: diablo # DIABLO
    7: trex # TREX - Off-target testing environments
    8: gsm # GSM
    9: umts # UMTS
    10: hwtc # HWTC
    11: ftm # Factory Test Mode
    12: rex # Rex
    # Alt name: DIAG_SUBSYS_OS
    13: gps # Global Positioning System
    14: wms # Wireless Messaging Service (WMS, SMS)
    15: cm # Call Manager
    16: hs # Handset
    17: audio_settings # Audio Settings
    18: diag_serv # DIAG Services
    19: fs # File System - EFS2
    20: port_map_settings # Port Map Settings
    21: mediaplayer # QCT Mediaplayer
    22: qcamera # QCT QCamera
    23: mobimon # QCT MobiMon
    24: gunimon # QCT GuniMon
    25: lsm # Location Services Manager
    26: qcamcorder # QCT QCamcorder
    27: mux1x # Multiplexer
    28: data1x # Data
    29: srch1x # Searcher
    30: callp1x # Call Processor
    31: apps # Applications
    32: settings # Settings
    33: gsdi # Generic SIM Driver Interface
    34: tmc # Task Main Controller
    35: usb # Universal Serial Bus
    36: pm # Power Management
    37: debug
    38: qtv
    39: clkrgm # Clock Regime
    40: devices
    41: wlan # 802.11 Technology
    42: ps_data_logging # Data Path Logging
    # Alt name: DIAG_SUBSYS_PS
    43: mflo # MediaFLO
    44: dtv # Digital TV
    45: rrc # WCDMA Radio Resource Control state
    46: prof # Miscellaneous Profiling Related
    47: tcxomgr
    48: nv # Non Volatile Memory
    49: autoconfig
    50: params # Parameters required for debugging subsystems
    51: mddi # Mobile Display Digital Interface
    52: ds_atcop
    53: l4linux # L4/Linux
    54: mvs # Multimode Voice Services
    55: cnv # Compact NV
    56: apione_program # apiOne
    57: hit # Hardware Integration Test
    58: drm # Digital Rights Management
    59: dm # Device Management
    60: fc # Flow Controller
    61: memory # Malloc Manager
    62: fs_alternate # Alternate File System
    63: regression # Regression Test Commands
    64: sensors # The sensors subsystem
    65: flute # FLUTE
    66: analog # Analog die subsystem
    67: apione_program_modem # apiOne Program On Modem Processor
    68: lte # LTE
    69: brew # BREW
    70: pwrdb # Power Debug Tool
    71: chord # Chaos Coordinator
    72: sec # Security
    73: time # Time Services
    74: q6_core # Q6 core services
    75: corebsp # CoreBSP
    76: mflo2 # Media Flow
    77: ulog # ULog Services
    78: apr # Asynchronous Packet Router
    79: qnp # QNP
    80: stride
    81: oemdpp # to read/write calibration to DPP partition
    82: q5_core # Requested by ADSP team
    83: uscript # core/power team USCRIPT tool
    84: nas # Requested by 3GPP NAS team
    85: cmapi # Requested by CMAPI
    86: ssm
    87: tdscdma # Requested by TDSCDMA team
    88: ssm_test
    89: mpower # Requested by MPOWER team
    90: qdss # For QDSS STM commands
    91: cxm
    92: gnss_soc # Secondary GNSS system
    93: ttlite
    94: ftm_ant
    95: mlog
    96: limitsmgr
    97: efsmonitor
    98: display_calibration
    99: version_report
    100: ds_ipa
    101: system_operations
    102: cnss_power
    103: lwip
    104: ims_qvp_rtp
    105: storage
    106: wci2
    107: aostlm_test
    108: cmapi_user_pd
    109: core_services
    110: cvd
    111: mcfg
    112: modem_stressfw
    113: ds_ds3g
    114: trm
    115: ims
    116: ota_firewall # OTA Firewall
    117: i15p4 # IEEE 802.15.4 technologies
    118: qdr # QTI Dead Reckoning core service
    119: mcs # Modem Common Services (MCS)
    120: modemfw # MODEM FW
    121: qnad # Memory Test/CPU tests etc
    122: f_reserved # reserved
    123: v2x
    124: qmesa
    125: sleep
    126: quest
    127: cdsp_qmesa
    128: pcie
    129: qdsp_stress_test
    130: chargerpd
    131: ds_ipa_tr
    132: mace
    133: qsh
    134: spu_test_fw
    135: qwes
    136: data_csm
    137: qms_cmd
    138: qmct
    139: wifi_dl
    140: uwb
    250: reserved_oem_0
    251: reserved_oem_1
    252: reserved_oem_2
    253: reserved_oem_3
    254: reserved_oem_4
    255: legacy

