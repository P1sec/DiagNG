# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagCmdCode(ReadWriteKaitaiStruct):
    class DiagCmd(IntEnum):
        verno_f = 0
        esn_f = 1
        peekb_f = 2
        peekw_f = 3
        peekd_f = 4
        pokeb_f = 5
        pokew_f = 6
        poked_f = 7
        outp_f = 8
        outpw_f = 9
        inp_f = 10
        inpw_f = 11
        status_f = 12
        logmask_f = 15
        log_f = 16
        nv_peek_f = 17
        nv_poke_f = 18
        bad_cmd_f = 19
        bad_parm_f = 20
        bad_len_f = 21
        bad_mode_f = 24
        tagraph_f = 25
        markov_f = 26
        markov_reset_f = 27
        diag_ver_f = 28
        ts_f = 29
        ta_parm_f = 30
        msg_f = 31
        hs_key_f = 32
        hs_lock_f = 33
        hs_screen_f = 34
        parm_set_f = 36
        nv_read_f = 38
        nv_write_f = 39
        control_f = 41
        err_read_f = 42
        err_clear_f = 43
        ser_reset_f = 44
        ser_report_f = 45
        test_f = 46
        get_dipsw_f = 47
        set_dipsw_f = 48
        voc_pcm_lb_f = 49
        voc_pkt_lb_f = 50
        orig_f = 53
        end_f = 54
        dload_f = 58
        tmob_f = 59
        test_state_f = 61
        state_f = 63
        pilot_sets_f = 64
        spc_f = 65
        bad_spc_mode_f = 66
        parm_get2_f = 67
        serial_chg_f = 68
        password_f = 70
        bad_sec_mode_f = 71
        pr_list_wr_f = 72
        pr_list_rd_f = 73
        cmd_f = 75
        feature_query_f = 81
        sms_read_f = 83
        sms_write_f = 84
        sup_fer_f = 85
        sup_walsh_codes_f = 86
        set_max_sup_ch_f = 87
        parm_get_is95b_f = 88
        fs_op_f = 89
        akey_verify_f = 90
        bmp_hs_screen_f = 91
        config_comm_f = 92
        ext_logmask_f = 93
        event_report_f = 96
        streaming_config_f = 97
        parm_retrieve_f = 98
        status_snapshot_f = 99
        get_property_f = 101
        put_property_f = 102
        get_guid_f = 103
        user_cmd_f = 104
        get_perm_property_f = 105
        put_perm_property_f = 106
        perm_user_cmd_f = 107
        gps_sess_ctrl_f = 108
        gps_grid_f = 109
        gps_statistics_f = 110
        route_f = 111
        is2000_status_f = 112
        rlp_stat_reset_f = 113
        tdso_stat_reset_f = 114
        log_config_f = 115
        trace_event_report_f = 116
        sbi_read_f = 117
        sbi_write_f = 118
        ssd_verify_f = 119
        log_on_demand_f = 120
        ext_msg_f = 121
        oncrpc_f = 122
        protocol_loopback_f = 123
        ext_build_id_f = 124
        ext_msg_config_f = 125
        ext_msg_terse_f = 126
        ext_msg_terse_xlate_f = 127
        cmd_ver_2_f = 128
        event_mask_get_f = 129
        event_mask_set_f = 130
        change_port_settings = 140
        cntry_info_f = 141
        sups_req_f = 142
        mms_orig_sms_request_f = 143
        meas_mode_f = 144
        meas_req_f = 145
        qsr_ext_msg_terse_f = 146
        dci_cmd_req = 147
        dci_delayed_rsp = 148
        bad_trans_f = 149
        ssm_disallowed_cmd_f = 150
        log_on_demand_ext_f = 151
        cmd_ext_f = 152
        qsr4_ext_msg_terse_f = 153
        dci_control_packet = 154
        compressed_pkt = 155
        msg_small_f = 156
        qsh_trace_payload_f = 157
        log_sec_f = 158

    class DiagSubsys(IntEnum):
        oem = 0
        zrex = 1
        sd = 2
        bt = 3
        wcdma = 4
        hdr = 5
        diablo = 6
        trex = 7
        gsm = 8
        umts = 9
        hwtc = 10
        ftm = 11
        rex = 12
        gps = 13
        wms = 14
        cm = 15
        hs = 16
        audio_settings = 17
        diag_serv = 18
        fs = 19
        port_map_settings = 20
        mediaplayer = 21
        qcamera = 22
        mobimon = 23
        gunimon = 24
        lsm = 25
        qcamcorder = 26
        mux1x = 27
        data1x = 28
        srch1x = 29
        callp1x = 30
        apps = 31
        settings = 32
        gsdi = 33
        tmc = 34
        usb = 35
        pm = 36
        debug = 37
        qtv = 38
        clkrgm = 39
        devices = 40
        wlan = 41
        ps_data_logging = 42
        mflo = 43
        dtv = 44
        rrc = 45
        prof = 46
        tcxomgr = 47
        nv = 48
        autoconfig = 49
        params = 50
        mddi = 51
        ds_atcop = 52
        l4linux = 53
        mvs = 54
        cnv = 55
        apione_program = 56
        hit = 57
        drm = 58
        dm = 59
        fc = 60
        memory = 61
        fs_alternate = 62
        regression = 63
        sensors = 64
        flute = 65
        analog = 66
        apione_program_modem = 67
        lte = 68
        brew = 69
        pwrdb = 70
        chord = 71
        sec = 72
        time = 73
        q6_core = 74
        corebsp = 75
        mflo2 = 76
        ulog = 77
        apr = 78
        qnp = 79
        stride = 80
        oemdpp = 81
        q5_core = 82
        uscript = 83
        nas = 84
        cmapi = 85
        ssm = 86
        tdscdma = 87
        ssm_test = 88
        mpower = 89
        qdss = 90
        cxm = 91
        gnss_soc = 92
        ttlite = 93
        ftm_ant = 94
        mlog = 95
        limitsmgr = 96
        efsmonitor = 97
        display_calibration = 98
        version_report = 99
        ds_ipa = 100
        system_operations = 101
        cnss_power = 102
        lwip = 103
        ims_qvp_rtp = 104
        storage = 105
        wci2 = 106
        aostlm_test = 107
        cmapi_user_pd = 108
        core_services = 109
        cvd = 110
        mcfg = 111
        modem_stressfw = 112
        ds_ds3g = 113
        trm = 114
        ims = 115
        ota_firewall = 116
        i15p4 = 117
        qdr = 118
        mcs = 119
        modemfw = 120
        qnad = 121
        f_reserved = 122
        v2x = 123
        qmesa = 124
        sleep = 125
        quest = 126
        cdsp_qmesa = 127
        pcie = 128
        qdsp_stress_test = 129
        chargerpd = 130
        ds_ipa_tr = 131
        mace = 132
        qsh = 133
        spu_test_fw = 134
        qwes = 135
        data_csm = 136
        qms_cmd = 137
        qmct = 138
        wifi_dl = 139
        uwb = 140
        reserved_oem_0 = 250
        reserved_oem_1 = 251
        reserved_oem_2 = 252
        reserved_oem_3 = 253
        reserved_oem_4 = 254
        legacy = 255

    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagCmdCode, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(DiagCmdCode, self)._write__seq(io)

    def _check(self):
        self._dirty = False
