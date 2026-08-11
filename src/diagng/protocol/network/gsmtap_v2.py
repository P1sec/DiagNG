# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_response
from diagng.protocol.qualcomm.struct import diag_request
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class GsmtapV2(ReadWriteKaitaiStruct):
    class GsmRrSubtype(IntEnum):
        unknown = 0
        bcch = 1
        ccch = 2
        rach = 3
        agch = 4
        pch = 5
        sdcch = 6
        sdcch4 = 7
        sdcch8 = 8
        facch_f = 9
        facch_h = 10
        pacch = 11
        cbch52 = 12
        pdch = 13
        ptcch = 14
        cbch51 = 15
        voice_f = 16
        voice_h = 17
        lsacch = 134
        sacch4 = 135
        sacch8 = 136
        sacch_f = 137
        sacch_h = 138

    class LteRrcSubtype(IntEnum):
        ch_bcch = 1
        ch_ccch = 2
        ch_dcch = 3
        ch_mcch = 4
        ch_pcch = 5
        ch_dtch = 6
        ch_mtch = 7

    class PacketType(IntEnum):
        um = 1
        abis = 2
        um_burst = 3
        sim = 4
        tetra_i1 = 5
        tetra_i1_burst = 6
        wmx_burst = 7
        gb_llc = 8
        gb_sndcp = 9
        gmr1_um = 10
        umts_rlc_mac = 11
        umts_rrc = 12
        lte_rrc = 13
        lte_mac = 14
        lte_mac_framed = 15
        osmocore_log = 16
        qc_diag = 17
        lte_nas = 18
        e1t1 = 19
        gsm_rlp = 20

    class UmtsRrcSubtype(IntEnum):
        dl_dcch_message = 0
        ul_dcch_message = 1
        dl_ccch_message = 2
        ul_ccch_message = 3
        pcch_message = 4
        dl_shcch_message = 5
        ul_shcch_message = 6
        bcch_fach_message = 7
        bcch_bch_message = 8
        mcch_message = 9
        msch_message = 10
        handover_to_utran_command = 11
        inter_rathandover_info = 12
        system_information_bch = 13
        system_information_container = 14
        ue_radio_access_capability_info = 15
        master_information_block = 16
        sys_info_type1 = 17
        sys_info_type2 = 18
        sys_info_type3 = 19
        sys_info_type4 = 20
        sys_info_type5 = 21
        sys_info_type5bis = 22
        sys_info_type6 = 23
        sys_info_type7 = 24
        sys_info_type8 = 25
        sys_info_type9 = 26
        sys_info_type10 = 27
        sys_info_type11 = 28
        sys_info_type11bis = 29
        sys_info_type12 = 30
        sys_info_type13 = 31
        sys_info_type13_1 = 32
        sys_info_type13_2 = 33
        sys_info_type13_3 = 34
        sys_info_type13_4 = 35
        sys_info_type14 = 36
        sys_info_type15 = 37
        sys_info_type15bis = 38
        sys_info_type15_1 = 39
        sys_info_type15_1bis = 40
        sys_info_type15_2 = 41
        sys_info_type15_2bis = 42
        sys_info_type15_2ter = 43
        sys_info_type15_3 = 44
        sys_info_type15_3bis = 45
        sys_info_type15_4 = 46
        sys_info_type15_5 = 47
        sys_info_type15_6 = 48
        sys_info_type15_7 = 49
        sys_info_type15_8 = 50
        sys_info_type16 = 51
        sys_info_type17 = 52
        sys_info_type18 = 53
        sys_info_type19 = 54
        sys_info_type20 = 55
        sys_info_type21 = 56
        sys_info_type22 = 57
        sys_info_type_sb1 = 58
        sys_info_type_sb2 = 59
        to_target_rnc_container = 60
        target_rnc_to_source_rnc_container = 61

    def __init__(self, _io=None, _parent=None, _root=None):
        super(GsmtapV2, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.version = self._io.read_u1()
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(
                2, self.version, self._io, '/seq/0'
            )
        self.header_len = self._io.read_u1()
        if not self.header_len == 4:
            raise kaitaistruct.ValidationNotEqualError(
                4, self.header_len, self._io, '/seq/1'
            )
        self.type = KaitaiStream.resolve_enum(
            GsmtapV2.PacketType, self._io.read_u1()
        )
        self.timeslot = self._io.read_u1()
        self.pcs_band = self._io.read_bits_int_be(1) != 0
        self.is_uplink = self._io.read_bits_int_be(1) != 0
        self.arfcn = self._io.read_bits_int_be(14)
        self.signal_dbm = self._io.read_s1()
        self.snr_db = self._io.read_s1()
        self.frame_number = self._io.read_u4be()
        _on = self.type
        if _on == GsmtapV2.PacketType.abis:
            pass
            self.sub_type = GsmtapV2.GsmRrSubtypeField(
                self._io, self, self._root
            )
            self.sub_type._read()
        elif _on == GsmtapV2.PacketType.um:
            pass
            self.sub_type = GsmtapV2.GsmRrSubtypeField(
                self._io, self, self._root
            )
            self.sub_type._read()
        elif _on == GsmtapV2.PacketType.umts_rrc:
            pass
            self.sub_type = GsmtapV2.UmtsRrcSubtypeField(
                self._io, self, self._root
            )
            self.sub_type._read()
        else:
            pass
            self.sub_type = self._io.read_u1()
        self.antenna_nr = self._io.read_u1()
        self.sub_slot = self._io.read_u1()
        self.res = self._io.read_u1()
        _on = self.type
        if _on == GsmtapV2.PacketType.qc_diag:
            pass
            self._raw_data = self._io.read_bytes_full()
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = GsmtapV2.DiagPayload(
                self.is_uplink, _io__raw_data, self, self._root
            )
            self.data._read()
        else:
            pass
            self.data = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.type
        if _on == GsmtapV2.PacketType.abis:
            pass
            self.sub_type._fetch_instances()
        elif _on == GsmtapV2.PacketType.um:
            pass
            self.sub_type._fetch_instances()
        elif _on == GsmtapV2.PacketType.umts_rrc:
            pass
            self.sub_type._fetch_instances()
        else:
            pass
        _on = self.type
        if _on == GsmtapV2.PacketType.qc_diag:
            pass
            self.data._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(GsmtapV2, self)._write__seq(io)
        self._io.write_u1(self.version)
        self._io.write_u1(self.header_len)
        self._io.write_u1(int(self.type))
        self._io.write_u1(self.timeslot)
        self._io.write_bits_int_be(1, int(self.pcs_band))
        self._io.write_bits_int_be(1, int(self.is_uplink))
        self._io.write_bits_int_be(14, self.arfcn)
        self._io.write_s1(self.signal_dbm)
        self._io.write_s1(self.snr_db)
        self._io.write_u4be(self.frame_number)
        _on = self.type
        if _on == GsmtapV2.PacketType.abis:
            pass
            self.sub_type._write__seq(self._io)
        elif _on == GsmtapV2.PacketType.um:
            pass
            self.sub_type._write__seq(self._io)
        elif _on == GsmtapV2.PacketType.umts_rrc:
            pass
            self.sub_type._write__seq(self._io)
        else:
            pass
            self._io.write_u1(self.sub_type)
        self._io.write_u1(self.antenna_nr)
        self._io.write_u1(self.sub_slot)
        self._io.write_u1(self.res)
        _on = self.type
        if _on == GsmtapV2.PacketType.qc_diag:
            pass
            _io__raw_data = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_data)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_data=_io__raw_data):
                self._raw_data = _io__raw_data.to_byte_array()
                parent.write_bytes(self._raw_data)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(data)', 0, parent.size() - parent.pos()
                    )

            _io__raw_data.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.data._write__seq(_io__raw_data)
        else:
            pass
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'data', 0, self._io.size() - self._io.pos()
                )

    def _check(self):
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(
                2, self.version, None, '/seq/0'
            )
        if not self.header_len == 4:
            raise kaitaistruct.ValidationNotEqualError(
                4, self.header_len, None, '/seq/1'
            )
        _on = self.type
        if _on == GsmtapV2.PacketType.abis:
            pass
            if self.sub_type._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self._root, self.sub_type._root
                )
            if self.sub_type._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self, self.sub_type._parent
                )
        elif _on == GsmtapV2.PacketType.um:
            pass
            if self.sub_type._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self._root, self.sub_type._root
                )
            if self.sub_type._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self, self.sub_type._parent
                )
        elif _on == GsmtapV2.PacketType.umts_rrc:
            pass
            if self.sub_type._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self._root, self.sub_type._root
                )
            if self.sub_type._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sub_type', self, self.sub_type._parent
                )
        else:
            pass
        _on = self.type
        if _on == GsmtapV2.PacketType.qc_diag:
            pass
            if self.data._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'data', self._root, self.data._root
                )
            if self.data._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'data', self, self.data._parent
                )
            if self.data.is_uplink != self.is_uplink:
                raise kaitaistruct.ConsistencyError(
                    'data', self.is_uplink, self.data.is_uplink
                )
        else:
            pass
        self._dirty = False

    class DiagPayload(ReadWriteKaitaiStruct):
        def __init__(self, is_uplink, _io=None, _parent=None, _root=None):
            super(GsmtapV2.DiagPayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_uplink = is_uplink

        def _read(self):
            _on = self.is_uplink
            if _on == False:
                pass
                self.frame = diag_response.DiagResponse(self._io)
                self.frame._read()
            elif _on == True:
                pass
                self.frame = diag_request.DiagRequest(self._io)
                self.frame._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            _on = self.is_uplink
            if _on == False:
                pass
                self.frame._fetch_instances()
            elif _on == True:
                pass
                self.frame._fetch_instances()

        def _write__seq(self, io=None):
            super(GsmtapV2.DiagPayload, self)._write__seq(io)
            _on = self.is_uplink
            if _on == False:
                pass
                self.frame._write__seq(self._io)
            elif _on == True:
                pass
                self.frame._write__seq(self._io)

        def _check(self):
            _on = self.is_uplink
            if _on == False:
                pass
            elif _on == True:
                pass
            self._dirty = False

    class GsmRrSubtypeField(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GsmtapV2.GsmRrSubtypeField, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.gsm_rr_subtype = KaitaiStream.resolve_enum(
                GsmtapV2.GsmRrSubtype, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(GsmtapV2.GsmRrSubtypeField, self)._write__seq(io)
            self._io.write_u1(int(self.gsm_rr_subtype))

        def _check(self):
            self._dirty = False

    class UmtsRrcSubtypeField(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GsmtapV2.UmtsRrcSubtypeField, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.umts_rrc_subtype = KaitaiStream.resolve_enum(
                GsmtapV2.UmtsRrcSubtype, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(GsmtapV2.UmtsRrcSubtypeField, self)._write__seq(io)
            self._io.write_u1(int(self.umts_rrc_subtype))

        def _check(self):
            self._dirty = False
