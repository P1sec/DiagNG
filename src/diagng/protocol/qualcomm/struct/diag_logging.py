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


class DiagLogging(ReadWriteKaitaiStruct):
    class Log1x(IntEnum):
        data_protocol_logging_c = 4587
        data_protocol_logging_network_ip_rm_tx_80_bytes_c = 5490
        data_protocol_logging_network_ip_rm_rx_80_bytes_c = 5491
        data_protocol_logging_network_ip_rm_tx_full_c = 5492
        data_protocol_logging_network_ip_rm_rx_full_c = 5493
        data_protocol_logging_network_ip_um_tx_80_bytes_c = 5494
        data_protocol_logging_network_ip_um_rx_80_bytes_c = 5495
        data_protocol_logging_network_ip_um_tx_full_c = 5496
        data_protocol_logging_network_ip_um_rx_full_c = 5497

    class LogCategory(IntEnum):
        log_1x = 4096
        log_wcdma = 16384
        log_gsm = 20480
        log_lbs = 24576
        log_umts = 28672
        log_tdma = 32768
        log_dtv = 40960
        log_lte = 45056
        log_wimax = 46080
        log_nr = 47104
        log_dsp = 49152
        log_tdscdma = 53248
        log_tools = 61440

    class LogGsm(IntEnum):
        gsm_rr_signaling_message_c = 20783
        gprs_mac_signaling_message_c = 21030

    class LogLte(IntEnum):
        rrc_ota_msg_log_c = 45248
        nas_esm_ota_in_msg_log_c = 45282
        nas_esm_ota_out_msg_log_c = 45283
        nas_emm_ota_in_msg_log_c = 45292
        nas_emm_ota_out_msg_log_c = 45293

    class LogMasks(IntEnum):
        log_category_mask = 61440
        log_category_mask_extended = 64512

    class LogNr(IntEnum):
        nr_rrc_ota_msg_log_c = 47137

    class LogUmts(IntEnum):
        nas_ota_message_log_packet_c = 28986

    class LogWcdma(IntEnum):
        signalling_message = 16687

    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagLogging, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(DiagLogging, self)._write__seq(io)

    def _check(self):
        self._dirty = False
