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


class GsmtapV2(ReadWriteKaitaiStruct):
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
        self.header_len = self._io.read_u2be()
        if not self.header_len == 4:
            raise kaitaistruct.ValidationNotEqualError(
                4, self.header_len, self._io, '/seq/1'
            )
        self.type = KaitaiStream.resolve_enum(
            GsmtapV2.PacketType, self._io.read_u1()
        )
        self.timeslot = self._io.read_u1()
        self.arfcn = self._io.read_u2be()
        self.signal_dbm = self._io.read_s1()
        self.snr_db = self._io.read_s1()
        self.frame_number = self._io.read_u4be()
        self.sub_type = self._io.read_u1()
        self.antenna_nr = self._io.read_u1()
        self.sub_slot = self._io.read_u1()
        self.res = self._io.read_u1()
        self.data = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(GsmtapV2, self)._write__seq(io)
        self._io.write_u1(self.version)
        self._io.write_u2be(self.header_len)
        self._io.write_u1(int(self.type))
        self._io.write_u1(self.timeslot)
        self._io.write_u2be(self.arfcn)
        self._io.write_s1(self.signal_dbm)
        self._io.write_s1(self.snr_db)
        self._io.write_u4be(self.frame_number)
        self._io.write_u1(self.sub_type)
        self._io.write_u1(self.antenna_nr)
        self._io.write_u1(self.sub_slot)
        self._io.write_u1(self.res)
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
        self._dirty = False
