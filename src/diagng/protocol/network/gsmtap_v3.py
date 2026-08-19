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


class GsmtapV3(ReadWriteKaitaiStruct):
    class NrRrcSubtype(IntEnum):
        unknown = 0
        bcch_bch = 1
        bcch_dl_sch = 2
        dl_ccch = 3
        dl_dcch = 4
        mcch = 5
        pcch = 6
        ul_ccch = 7
        ul_ccch1 = 8
        ul_dcch = 9
        sbcch_sl_bch = 257
        scch = 258
        rrc_reconfiguration = 513
        rrc_reconfiguration_complete = 514
        ue_mrdc_capability = 515
        ue_nr_capability = 516
        ue_radio_access_capability_information = 517
        ue_radio_paging_information = 518
        sib1 = 519
        sib2 = 520
        sib3 = 521
        sib4 = 522
        sib5 = 523
        sib6 = 524
        sib7 = 525
        sib8 = 526
        sib9 = 527
        sib10_r16 = 528
        sib11_r16 = 529
        sib12_r16 = 530
        sib13_r16 = 531
        sib14_r16 = 532
        sib15_r17 = 533
        sib16_r17 = 534
        sib17_r17 = 535
        sib18_r17 = 536
        sib19_r17 = 537
        sib20_r17 = 538
        sib21_r17 = 539
        sib22_r18 = 540
        sib23_r18 = 541
        sib24_r18 = 542
        sib25_r18 = 543
        sib17bis_r18 = 544

    class Type(IntEnum):
        osmocore_log = 0
        sim = 1
        baseband_diag = 2
        signal_status_report = 3
        tetra_i1 = 4
        tetra_i1_burst = 5
        gmr1_um = 6
        e1t1 = 7
        wmx_burst = 8
        um = 512
        um_burst = 513
        gb_rlcmac = 514
        gb_llc = 515
        gb_sndcp = 516
        abis = 517
        rlp = 518
        umts_mac = 768
        umts_rlc = 769
        umts_pdcp = 770
        umts_rrc = 771
        lte_mac = 1024
        lte_rlc = 1025
        lte_pdcp = 1026
        lte_rrc = 1027
        nas_eps = 1028
        nr_mac = 1280
        nr_rlc = 1281
        nr_pdcp = 1282
        nr_rrc = 1283
        nas_5gs = 1284

    def __init__(self, _io=None, _parent=None, _root=None):
        super(GsmtapV3, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.reserved = self._io.read_u1()
        if not self.reserved == 0:
            raise kaitaistruct.ValidationNotEqualError(
                0, self.reserved, self._io, '/seq/0'
            )
        self.header_len = self._io.read_u2be()
        if not self.header_len >= 2:
            raise kaitaistruct.ValidationLessThanError(
                2, self.header_len, self._io, '/seq/1'
            )
        self.type = KaitaiStream.resolve_enum(
            GsmtapV3.Type, self._io.read_u2be()
        )
        _on = self.type
        if _on == GsmtapV3.Type.nr_rrc:
            pass
            self.subtype = GsmtapV3.NrRrcSubtype(self._io, self, self._root)
            self.subtype._read()
        else:
            pass
            self.subtype = self._io.read_u2be()
        self.metadata = []
        i = 0
        while True:
            _t_metadata = GsmtapV3.Metadata(self._io, self, self._root)
            try:
                _t_metadata._read()
            finally:
                _ = _t_metadata
                self.metadata.append(_)
            if _.tag == GsmtapV3.Metadata.Tag.end_of_metadata:
                break
            i += 1
        self.data = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.type
        if _on == GsmtapV3.Type.nr_rrc:
            pass
            self.subtype._fetch_instances()
        else:
            pass
        for i in range(len(self.metadata)):
            pass
            self.metadata[i]._fetch_instances()

    def _write__seq(self, io=None):
        super(GsmtapV3, self)._write__seq(io)
        self._io.write_u1(self.reserved)
        self._io.write_u2be(self.header_len)
        self._io.write_u2be(int(self.type))
        _on = self.type
        if _on == GsmtapV3.Type.nr_rrc:
            pass
            self.subtype._write__seq(self._io)
        else:
            pass
            self._io.write_u2be(self.subtype)
        for i in range(len(self.metadata)):
            pass
            self.metadata[i]._write__seq(self._io)

        self._io.write_bytes(self.data)
        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(
                'data', 0, self._io.size() - self._io.pos()
            )

    def _check(self):
        if not self.reserved == 0:
            raise kaitaistruct.ValidationNotEqualError(
                0, self.reserved, None, '/seq/0'
            )
        if not self.header_len >= 2:
            raise kaitaistruct.ValidationLessThanError(
                2, self.header_len, None, '/seq/1'
            )
        _on = self.type
        if _on == GsmtapV3.Type.nr_rrc:
            pass
            if self.subtype._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'subtype', self._root, self.subtype._root
                )
            if self.subtype._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'subtype', self, self.subtype._parent
                )
        else:
            pass
        if len(self.metadata) == 0:
            raise kaitaistruct.ConsistencyError(
                'metadata', 0, len(self.metadata)
            )
        for i in range(len(self.metadata)):
            pass
            if self.metadata[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'metadata', self._root, self.metadata[i]._root
                )
            if self.metadata[i]._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'metadata', self, self.metadata[i]._parent
                )
            _ = self.metadata[i]
            if (_.tag == GsmtapV3.Metadata.Tag.end_of_metadata) != (
                i == len(self.metadata) - 1
            ):
                raise kaitaistruct.ConsistencyError(
                    'metadata',
                    i == len(self.metadata) - 1,
                    _.tag == GsmtapV3.Metadata.Tag.end_of_metadata,
                )

        self._dirty = False

    class ChannelNumber(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GsmtapV3.ChannelNumber, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.is_uplink = self._io.read_bits_int_be(1) != 0
            self.arfcn = self._io.read_bits_int_be(15)
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(GsmtapV3.ChannelNumber, self)._write__seq(io)
            self._io.write_bits_int_be(1, int(self.is_uplink))
            self._io.write_bits_int_be(15, self.arfcn)

        def _check(self):
            self._dirty = False

    class Metadata(ReadWriteKaitaiStruct):
        class Tag(IntEnum):
            packet_timestamp = 0
            packet_comment = 1
            channel_number = 2
            frequency = 3
            band_indicator = 4
            bsic_psc_pci = 5
            gsm_timeslot = 6
            gsm_subslot = 7
            system_frame_number = 8
            subframe_number = 9
            hyperframe_number = 10
            tetra_symbol_number = 11
            tetra_multiframe_number = 12
            antenna_number = 13
            signal_level = 256
            rssi = 257
            snr = 258
            sinr = 259
            rscp = 260
            ecio = 261
            rsrp = 262
            rsrq = 263
            ss_rsrp = 264
            csi_rsrp = 265
            srs_rsrp = 266
            ss_rsrq = 267
            csi_rsrq = 268
            ss_sinr = 269
            csi_sinr = 270
            ciphering_key = 512
            integrity_key = 513
            k_nasenc = 514
            k_nasint = 515
            k_rrcenc = 516
            k_rrcint = 517
            k_upenc = 518
            k_upint = 519
            end_of_metadata = 65534

        def __init__(self, _io=None, _parent=None, _root=None):
            super(GsmtapV3.Metadata, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.tag = KaitaiStream.resolve_enum(
                GsmtapV3.Metadata.Tag, self._io.read_u2be()
            )
            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                self.len_value = self._io.read_u2be()

            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                _on = self.tag
                if _on == GsmtapV3.Metadata.Tag.channel_number:
                    pass
                    self._raw_value = self._io.read_bytes(self.len_value)
                    _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
                    self.value = GsmtapV3.ChannelNumber(
                        _io__raw_value, self, self._root
                    )
                    self.value._read()
                else:
                    pass
                    self.value = self._io.read_bytes(self.len_value)

            self._dirty = False

        def _fetch_instances(self):
            pass
            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass

            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                _on = self.tag
                if _on == GsmtapV3.Metadata.Tag.channel_number:
                    pass
                    self.value._fetch_instances()
                else:
                    pass

        def _write__seq(self, io=None):
            super(GsmtapV3.Metadata, self)._write__seq(io)
            self._io.write_u2be(int(self.tag))
            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                self._io.write_u2be(self.len_value)

            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                _on = self.tag
                if _on == GsmtapV3.Metadata.Tag.channel_number:
                    pass
                    _io__raw_value = KaitaiStream(
                        BytesIO(bytearray(self.len_value))
                    )
                    self._io.add_child_stream(_io__raw_value)
                    _pos2 = self._io.pos()
                    self._io.seek(self._io.pos() + (self.len_value))

                    def handler(parent, _io__raw_value=_io__raw_value):
                        self._raw_value = _io__raw_value.to_byte_array()
                        if len(self._raw_value) != self.len_value:
                            raise kaitaistruct.ConsistencyError(
                                'raw(value)',
                                self.len_value,
                                len(self._raw_value),
                            )
                        parent.write_bytes(self._raw_value)

                    _io__raw_value.write_back_handler = (
                        KaitaiStream.WriteBackHandler(_pos2, handler)
                    )
                    self.value._write__seq(_io__raw_value)
                else:
                    pass
                    self._io.write_bytes(self.value)

        def _check(self):
            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass

            if self.tag != GsmtapV3.Metadata.Tag.end_of_metadata:
                pass
                _on = self.tag
                if _on == GsmtapV3.Metadata.Tag.channel_number:
                    pass
                    if self.value._root != self._root:
                        raise kaitaistruct.ConsistencyError(
                            'value', self._root, self.value._root
                        )
                    if self.value._parent != self:
                        raise kaitaistruct.ConsistencyError(
                            'value', self, self.value._parent
                        )
                else:
                    pass
                    if len(self.value) != self.len_value:
                        raise kaitaistruct.ConsistencyError(
                            'value', self.len_value, len(self.value)
                        )

            self._dirty = False

    class NrRrcSubtype(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(GsmtapV3.NrRrcSubtype, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.subtype = KaitaiStream.resolve_enum(
                GsmtapV3.NrRrcSubtype, self._io.read_u2be()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(GsmtapV3.NrRrcSubtype, self)._write__seq(io)
            self._io.write_u2be(int(self.subtype))

        def _check(self):
            self._dirty = False
