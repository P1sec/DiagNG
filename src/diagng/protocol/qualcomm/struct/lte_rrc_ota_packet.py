# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
from diagng.protocol.network import gsmtap_v2


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class LteRrcOtaPacket(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(LteRrcOtaPacket, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.ext_header_ver = self._io.read_u1()
        self.rrc_rel = self._io.read_u1()
        self.rrc_ver_major = self._io.read_bits_int_be(4)
        self.rrc_ver_minor = self._io.read_bits_int_be(4)
        if self.ext_header_ver >= 25:
            pass
            self.nc_rrc_rel = self._io.read_u1()

        if self.ext_header_ver >= 25:
            pass
            self.nc_rrc_ver_major = self._io.read_bits_int_be(4)

        if self.ext_header_ver >= 25:
            pass
            self.nc_rrc_ver_minor = self._io.read_bits_int_be(4)

        self.bearer_id = self._io.read_u1()
        self.phy_cellid = self._io.read_u2le()
        if self.ext_header_ver >= 8:
            pass
            self.earfcn_long = self._io.read_u4le()

        if self.ext_header_ver < 8:
            pass
            self.earfcn_short = self._io.read_u2le()

        self.sfn_subfn = self._io.read_u2le()
        self.is_special = self._io.read_bits_int_be(1) != 0
        if not (self.is_special):
            pass
            _on = self.ext_header_ver
            if _on == 1:
                pass
                self.pdu_type = LteRrcOtaPacket.V1PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 10:
                pass
                self.pdu_type = LteRrcOtaPacket.V10PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 11:
                pass
                self.pdu_type = LteRrcOtaPacket.V11PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 12:
                pass
                self.pdu_type = LteRrcOtaPacket.V12PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 13:
                pass
                self.pdu_type = LteRrcOtaPacket.V13PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 14:
                pass
                self.pdu_type = LteRrcOtaPacket.V14PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 15:
                pass
                self.pdu_type = LteRrcOtaPacket.V15PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 16:
                pass
                self.pdu_type = LteRrcOtaPacket.V16PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 17:
                pass
                self.pdu_type = LteRrcOtaPacket.V17PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 18:
                pass
                self.pdu_type = LteRrcOtaPacket.V18PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 19:
                pass
                self.pdu_type = LteRrcOtaPacket.V19PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 2:
                pass
                self.pdu_type = LteRrcOtaPacket.V2PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 20:
                pass
                self.pdu_type = LteRrcOtaPacket.V20PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 21:
                pass
                self.pdu_type = LteRrcOtaPacket.V21PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 22:
                pass
                self.pdu_type = LteRrcOtaPacket.V22PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 23:
                pass
                self.pdu_type = LteRrcOtaPacket.V23PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 24:
                pass
                self.pdu_type = LteRrcOtaPacket.V24PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 25:
                pass
                self.pdu_type = LteRrcOtaPacket.V25PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 26:
                pass
                self.pdu_type = LteRrcOtaPacket.V26PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 27:
                pass
                self.pdu_type = LteRrcOtaPacket.V27PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 3:
                pass
                self.pdu_type = LteRrcOtaPacket.V3PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 4:
                pass
                self.pdu_type = LteRrcOtaPacket.V4PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 5:
                pass
                self.pdu_type = LteRrcOtaPacket.V4PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 6:
                pass
                self.pdu_type = LteRrcOtaPacket.V6PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 7:
                pass
                self.pdu_type = LteRrcOtaPacket.V7PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 8:
                pass
                self.pdu_type = LteRrcOtaPacket.V8PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            elif _on == 9:
                pass
                self.pdu_type = LteRrcOtaPacket.V9PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()
            else:
                pass
                self.pdu_type = LteRrcOtaPacket.V27PduType(
                    self._io, self, self._root
                )
                self.pdu_type._read()

        if self.ext_header_ver >= 5:
            pass
            self.sib_message = self._io.read_u4le()

        self.len_message = self._io.read_u2le()
        if self.ext_header_ver >= 30:
            pass
            self.unk1 = self._io.read_u1()

        if self.ext_header_ver >= 30:
            pass
            self.unk2 = self._io.read_u1()

        if self.ext_header_ver >= 30:
            pass
            self.segment_id = self._io.read_u1()

        self.message = self._io.read_bytes(self.len_message)
        self._dirty = False

    def _fetch_instances(self):
        pass
        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 8:
            pass

        if self.ext_header_ver < 8:
            pass

        if not (self.is_special):
            pass
            _on = self.ext_header_ver
            if _on == 1:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 10:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 11:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 12:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 13:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 14:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 15:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 16:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 17:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 18:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 19:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 2:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 20:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 21:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 22:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 23:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 24:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 25:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 26:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 27:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 3:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 4:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 5:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 6:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 7:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 8:
                pass
                self.pdu_type._fetch_instances()
            elif _on == 9:
                pass
                self.pdu_type._fetch_instances()
            else:
                pass
                self.pdu_type._fetch_instances()

        if self.ext_header_ver >= 5:
            pass

        if self.ext_header_ver >= 30:
            pass

        if self.ext_header_ver >= 30:
            pass

        if self.ext_header_ver >= 30:
            pass

    def _write__seq(self, io=None):
        super(LteRrcOtaPacket, self)._write__seq(io)
        self._io.write_u1(self.ext_header_ver)
        self._io.write_u1(self.rrc_rel)
        self._io.write_bits_int_be(4, self.rrc_ver_major)
        self._io.write_bits_int_be(4, self.rrc_ver_minor)
        if self.ext_header_ver >= 25:
            pass
            self._io.write_u1(self.nc_rrc_rel)

        if self.ext_header_ver >= 25:
            pass
            self._io.write_bits_int_be(4, self.nc_rrc_ver_major)

        if self.ext_header_ver >= 25:
            pass
            self._io.write_bits_int_be(4, self.nc_rrc_ver_minor)

        self._io.write_u1(self.bearer_id)
        self._io.write_u2le(self.phy_cellid)
        if self.ext_header_ver >= 8:
            pass
            self._io.write_u4le(self.earfcn_long)

        if self.ext_header_ver < 8:
            pass
            self._io.write_u2le(self.earfcn_short)

        self._io.write_u2le(self.sfn_subfn)
        self._io.write_bits_int_be(1, int(self.is_special))
        if not (self.is_special):
            pass
            _on = self.ext_header_ver
            if _on == 1:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 10:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 11:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 12:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 13:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 14:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 15:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 16:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 17:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 18:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 19:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 2:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 20:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 21:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 22:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 23:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 24:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 25:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 26:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 27:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 3:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 4:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 5:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 6:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 7:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 8:
                pass
                self.pdu_type._write__seq(self._io)
            elif _on == 9:
                pass
                self.pdu_type._write__seq(self._io)
            else:
                pass
                self.pdu_type._write__seq(self._io)

        if self.ext_header_ver >= 5:
            pass
            self._io.write_u4le(self.sib_message)

        self._io.write_u2le(self.len_message)
        if self.ext_header_ver >= 30:
            pass
            self._io.write_u1(self.unk1)

        if self.ext_header_ver >= 30:
            pass
            self._io.write_u1(self.unk2)

        if self.ext_header_ver >= 30:
            pass
            self._io.write_u1(self.segment_id)

        self._io.write_bytes(self.message)

    def _check(self):
        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 25:
            pass

        if self.ext_header_ver >= 8:
            pass

        if self.ext_header_ver < 8:
            pass

        if not (self.is_special):
            pass
            _on = self.ext_header_ver
            if _on == 1:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 10:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 11:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 12:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 13:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 14:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 15:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 16:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 17:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 18:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 19:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 2:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 20:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 21:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 22:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 23:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 24:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 25:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 26:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 27:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 3:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 4:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 5:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 6:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 7:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 8:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            elif _on == 9:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )
            else:
                pass
                if self.pdu_type._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self._root, self.pdu_type._root
                    )
                if self.pdu_type._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'pdu_type', self, self.pdu_type._parent
                    )

        if self.ext_header_ver >= 5:
            pass

        if self.ext_header_ver >= 30:
            pass

        if self.ext_header_ver >= 30:
            pass

        if self.ext_header_ver >= 30:
            pass

        if len(self.message) != self.len_message:
            raise kaitaistruct.ConsistencyError(
                'message', self.len_message, len(self.message)
            )
        self._dirty = False

    class V10PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            ellipsoid_point = 1
            ellipsoid_point_uncertainty_circle = 2
            ellipsoid_point_uncertainty_ellipse = 3
            ellipsoid_point_altitude = 4
            ellipsoid_point_altitude_uncertainty_ellipsoid = 5
            ellipsoid_arc = 6
            horizontal_velocity = 7
            bcch_bch = 8
            bcch_dl_sch = 9
            mcch = 10
            pcch = 11
            dl_ccch = 12
            dl_dcch = 13
            ul_ccch = 14
            ul_dcch = 15
            rrcconnrelease_v9e0_ies = 16
            sysinfo_block_type1 = 17
            sysinfo_block_type1_v8h0_ies = 18
            ueinforesponse_v9e0_ies = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type5_v8h0_ies = 21
            sysinfo_block_type6_v8h0_ies = 22
            ue_eutra_cap = 23
            ue_eutra_cap_v9a0_ies = 24

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V10PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V10PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V10PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V10PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V10PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V10PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V10PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V10PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V10PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V10PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V10PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V10PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V10PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V11PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            ellipsoid_point = 1
            ellipsoid_point_uncertainty_circle = 2
            ellipsoid_point_uncertainty_ellipse = 3
            ellipsoid_point_altitude = 4
            ellipsoid_point_altitude_uncertainty_ellipsoid = 5
            ellipsoid_arc = 6
            horizontal_velocity = 7
            bcch_bch = 8
            bcch_dl_sch = 9
            mcch = 10
            pcch = 11
            dl_ccch = 12
            dl_dcch = 13
            ul_ccch = 14
            ul_dcch = 15
            rrcconnrelease_v9e0_ies = 16
            sysinfo_block_type1 = 17
            sysinfo_block_type1_v8h0_ies = 18
            ueinforesponse_v9e0_ies = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type5_v8h0_ies = 21
            sysinfo_block_type6_v8h0_ies = 22
            csi_im_configid_r12 = 23
            eutra_ellipsoid_point = 24
            eutra_ellipsoid_point_altitude = 25
            eutra_ellipsoid_point_altitude_uncertainty_ellipsoid = 26
            eutra_ellipsoid_arc = 27
            eutra_ellipsoid_point_uncertainty_circle = 28
            eutra_ellipsoid_point_uncertainty_ellipse = 29
            eutra_horizontal_velocity = 30
            polygon = 31
            meas_ref_time = 32
            ue_eutra_cap = 33
            ue_eutra_cap_v9a0_ies = 34

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V11PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V11PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V11PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V11PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V11PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V11PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V11PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V11PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V11PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V11PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V11PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V11PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V11PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V12PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            ellipsoid_point = 1
            ellipsoid_point_uncertainty_circle = 2
            ellipsoid_point_uncertainty_ellipse = 3
            ellipsoid_point_altitude = 4
            ellipsoid_point_altitude_uncertainty_ellipsoid = 5
            ellipsoid_arc = 6
            horizontal_velocity = 7
            bcch_bch = 8
            bcch_dl_sch = 9
            mcch = 10
            pcch = 11
            dl_ccch = 12
            dl_dcch = 13
            ul_ccch = 14
            ul_dcch = 15
            rrcconnection_reconfiguration = 16
            rrcconnection_reconfiguration_complete = 17
            rrcconnrelease_v9e0_ies = 18
            sysinfo_block_type1 = 19
            sysinfo_block_type1_v8h0_ies = 20
            uecapabilityenquiry = 21
            uecapabilityinformation = 22
            ueinforesponse_v9e0_ies = 23
            sysinfo_block_type2_v8h0_ies = 24
            sysinfo_block_type5_v8h0_ies = 25
            sysinfo_block_type6_v8h0_ies = 26
            csi_im_configid_r1 = 27
            eutra_rrc_definitions_ellipsoid_point = 28
            eutra_rrc_definitions_ellipsoid_altitude = 29
            eutra_rrc_definitions_ellipsoid_altitude_uncertainty_ellipsoid = 30
            eutra_rrc_definitions_ellipsoid_arc = 31
            eutra_rrc_definitions_ellipsoid_uncertainty_circle = 32
            eutra_rrc_definitions_ellipsoid_uncertainty_ellipse = 33
            eutra_rrc_definitions_horizontal_velocity = 34
            polygon = 35
            measurement_ref_time = 36
            ue_eutra_cap = 37
            ue_eutra_cap_v9a0_ies = 38
            var_short_mac_input = 39
            els_sib1_signature = 40
            els_sysinfo_block_type1 = 41
            nhn_plmn_identity_list = 42
            els_dl_ccch = 43
            els_dl_dcch = 44
            els_ul_dcch = 45

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V12PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V12PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V12PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V12PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V12PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V12PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V12PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V12PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V12PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V12PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V12PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V12PduType.PduType.els_dl_ccch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V12PduType.PduType.els_dl_dcch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V12PduType.PduType.els_ul_dcch
                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V12PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V12PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V12PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V13PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            rrcconnection_reconfiguration = 9
            rrcconnrelease_v8m0_ies = 10
            rrcconnection_reconfiguration_complete = 11
            rrcconnrelease_v9e0_ies = 12
            sysinfo_block_type1 = 13
            sysinfo_block_type1_v8h0_ies = 14
            uecapabilityenquiry = 15
            uecapabilityinformation = 16
            ueinforesponse_v9e0_ies = 17
            sysinfo_block_type2_v8h0_ies = 18
            sysinfo_block_type5_v8h0_ies = 19
            sysinfo_block_type6_v8h0_ies = 20
            tdd_configsl_r12 = 21
            ellipsoid_point = 22
            ellipsoid_point_altitude = 23
            ellipsoid_point_altitude_uncertainty_ellipsoid = 24
            ellipsoid_arc = 25
            ellipsoid_point_uncertainty_circle = 26
            ellipsoid_point_uncertainty_ellipse = 27
            horizontal_velocity = 28
            polygon = 29
            measurement_ref_time = 30
            rsrp_rangsl3_r12 = 31
            ue_eutra_cap = 32
            ue_eutra_cap_v9a0_ies = 33
            var_short_mac_input = 34
            els_sib1_signature = 35
            els_sysinfo_block_type1 = 36
            nhn_plmn_identity_list = 37
            els_dl_ccch = 38
            els_dl_dcch = 39
            els_ul_dcch = 40

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V13PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V13PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V13PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V13PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V13PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V13PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V13PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V13PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V13PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V13PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V13PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V13PduType.PduType.els_dl_ccch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V13PduType.PduType.els_dl_dcch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V13PduType.PduType.els_ul_dcch
                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V13PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V13PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V13PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V14PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            rrcconnection_reconfiguration = 10
            rrcconnrelease_v8m0_ies = 11
            rrcconnection_reconfiguration_complete = 12
            rrcconnrelease_v9e0_ies = 13
            sysinfo_block_type1 = 14
            sysinfo_block_type1_v8h0_ies = 15
            uecapabilityenquiry = 16
            uecapabilityinformation = 17
            ueinforesponse_v9e0_ies = 18
            sysinfo_block_type2_v8h0_ies = 19
            sysinfo_block_type5_v8h0_ies = 20
            redistributionfactor_r13 = 21
            sysinfo_block_type6_v8h0_ies = 22
            tdd_configsl_r12 = 23
            ellipsoid_point = 24
            ellipsoid_point_altitude = 25
            ellipsoid_point_altitude_uncertainty_ellipsoid = 26
            ellipsoid_arc = 27
            ellipsoid_point_uncertainty_circle = 28
            ellipsoid_point_uncertainty_ellipse = 29
            horizontal_velocity = 30
            polygon = 31
            measurement_ref_time = 32
            rsrp_rangsl3_r12 = 33
            ue_eutra_cap = 34
            ue_eutra_cap_v9a0_ies = 35
            laa_params_r13 = 36
            var_short_mac_input = 37
            els_sib1_signature = 38
            els_sysinfo_block_type1 = 39
            nhn_plmn_identity_list = 40
            els_dl_ccch = 41
            els_dl_dcch = 42
            els_ul_dcch = 43

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V14PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V14PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V14PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V14PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V14PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V14PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V14PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V14PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V14PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V14PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V14PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V14PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V14PduType.PduType.els_dl_ccch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V14PduType.PduType.els_dl_dcch
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V14PduType.PduType.els_ul_dcch
                                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V14PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V14PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V14PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V15PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            sc_mcch_r13 = 10
            rrcconnection_reconfiguration = 11
            rrcconnrelease_v8m0_ies = 12
            rrcconnection_reconfiguration_complete = 13
            rrcconnrelease_v9e0_ies = 14
            sysinfo_block_type1 = 15
            sysinfo_block_type1_v8h0_ies = 16
            uecapabilityenquiry = 17
            uecapabilityinformation = 18
            ueinforesponse_v9e0_ies = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type3_v10j0_ies = 21
            sysinfo_block_type5_v8h0_ies = 22
            sysinfo_block_type6_v8h0_ies = 23
            tdd_configsl_r12 = 24
            ellipsoid_point = 25
            ellipsoid_point_altitude = 26
            ellipsoid_point_altitude_uncertainty_ellipsoid = 27
            ellipsoid_arc = 28
            ellipsoid_point_uncertainty_circle = 29
            ellipsoid_point_uncertainty_ellipse = 30
            horizontal_velocity = 31
            polygon = 32
            measurement_ref_time = 33
            rsrp_rangsl3_r12 = 34
            ue_eutra_cap = 35
            ue_eutra_cap_v9a0_ies = 36
            ue_eutra_cap_v10j0_ies = 37
            sl_txpoolid_r13 = 38
            var_short_mac_input = 39
            bcch_bch_nb = 40
            bcch_dl_sch_nb = 41
            pcch_nb = 42
            dl_ccch_nb = 43
            dl_dcch_nb = 44
            ul_ccch_nb = 45
            ul_dcch_nb = 46
            els_sib1_signature = 47
            els_sysinfo_block_type1 = 48
            nhn_plmn_identity_list = 49
            els_dl_ccch = 50
            els_dl_dcch = 51
            els_ul_dcch = 52

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V15PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V15PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V15PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V15PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V15PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V15PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V15PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V15PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V15PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V15PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V15PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V15PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V15PduType.PduType.sc_mcch_r13
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V15PduType.PduType.bcch_bch_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V15PduType.PduType.bcch_dl_sch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V15PduType.PduType.pcch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V15PduType.PduType.dl_ccch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V15PduType.PduType.dl_dcch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V15PduType.PduType.ul_ccch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V15PduType.PduType.ul_dcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V15PduType.PduType.els_dl_ccch
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V15PduType.PduType.els_dl_dcch
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V15PduType.PduType.els_ul_dcch
                                                                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V15PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V15PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V15PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V15PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V15PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V16PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            sc_mcch_r13 = 10
            rrcconnection_reconfiguration = 11
            rrcconnrelease_v8m0_ies = 12
            rrcconnection_reconfiguration_complete = 13
            rrcconnrelease_v9e0_ies = 14
            sysinfo_block_type1 = 15
            sysinfo_block_type1_v8h0_ies = 16
            uecapabilityenquiry = 17
            uecapabilityinformation = 18
            ueinforesponse_v9e0_ies = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type3_v10j0_ies = 21
            sysinfo_block_type5_v8h0_ies = 22
            sysinfo_block_type6_v8h0_ies = 23
            tdd_configsl_r12 = 24
            ellipsoid_point = 25
            ellipsoid_point_altitude = 26
            ellipsoid_point_altitude_uncertainty_ellipsoid = 27
            ellipsoid_arc = 28
            ellipsoid_point_uncertainty_circle = 29
            ellipsoid_point_uncertainty_ellipse = 30
            horizontal_velocity = 31
            polygon = 32
            measurement_ref_time = 33
            rsrp_rangsl3_r12 = 34
            ue_eutra_cap = 35
            ue_eutra_cap_v9a0_ies = 36
            ue_eutra_cap_v10j0_ies = 37
            sl_txpoolid_r13 = 38
            var_short_mac_input = 39
            bcch_bch_nb = 40
            bcch_dl_sch_nb = 41
            pcch_nb = 42
            dl_ccch_nb = 43
            dl_dcch_nb = 44
            ul_ccch_nb = 45
            ul_dcch_nb = 46
            els_sib1_signature = 47
            els_sysinfo_block_type1 = 48
            els_dl_dcch = 49
            els_ul_dcch = 50

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V16PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V16PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V16PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V16PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V16PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V16PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V16PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V16PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V16PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V16PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V16PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V16PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V16PduType.PduType.sc_mcch_r13
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V16PduType.PduType.bcch_bch_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V16PduType.PduType.bcch_dl_sch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V16PduType.PduType.pcch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V16PduType.PduType.dl_ccch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V16PduType.PduType.dl_dcch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V16PduType.PduType.ul_ccch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V16PduType.PduType.ul_dcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V16PduType.PduType.els_dl_dcch
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V16PduType.PduType.els_ul_dcch
                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V16PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V16PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V16PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V16PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V16PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V17PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            rrcconnection_reconfiguration = 9
            rrcconnrelease_v8m0_ies = 10
            rrcconnection_reconfiguration_complete = 11
            rrcconnrelease_v9e0_ies = 12
            sysinfo_block_type1 = 13
            sysinfo_block_type1_v8h0_ies = 14
            uecapabilityenquiry = 15
            uecapabilityinformation = 16
            ueinforesponse_v9e0_ies = 17
            sysinfo_block_type2_v8h0_ies = 18
            sysinfo_block_type5_v8h0_ies = 19
            sysinfo_block_type6_v8h0_ies = 20
            csi_im_configid_r12 = 21
            ellipsoid_point = 22
            ellipsoid_point_altitude = 23
            ellipsoid_point_altitude_uncertainty_ellipsoid = 24
            ellipsoid_arc = 25
            ellipsoid_point_uncertainty_circle = 26
            ellipsoid_point_uncertainty_ellipse = 27
            horizontal_velocity = 28
            polygon = 29
            measurement_ref_time = 30
            ue_eutra_cap = 31
            ue_eutra_cap_v9a0_ies = 32
            var_short_mac_input = 33
            els_sib1_signature = 34
            els_sysinfo_block_type1 = 35
            nhn_plmn_identity_list = 36
            els_dl_ccch = 37
            els_dl_dcch = 38
            els_ul_dcch = 39

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V17PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V17PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V17PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V17PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V17PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V17PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V17PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V17PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V17PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V17PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V17PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V17PduType.PduType.els_dl_ccch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V17PduType.PduType.els_dl_dcch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V17PduType.PduType.els_ul_dcch
                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V17PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V17PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V17PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V18PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            pcch_type = 5
            dl_ccch = 6
            dl_ccch_type = 7
            dl_dcch = 8
            dl_dcch_type = 9
            ul_ccch = 10
            ul_ccch_type = 11
            ul_dcch = 12
            ul_dcch_type = 13
            rrcconnection_reconfiguration = 14
            rrcconnection_reconfiguration_v8m0_ies = 15
            rrcconnection_reconfiguration_complete = 16
            rrcconnrelease_v9e0_ies = 17
            sysinfo = 18
            sysinfo_block_type1 = 19
            sysinfo_block_type1_v8h0_ies = 20
            uecapabilityenquiry = 21
            uecapabilityinformation = 22
            ueinforesponse_v9e0_ies = 23
            sysinfo_block_type2_v8h0_ies = 24
            sysinfo_block_type5_v8h0_ies = 25
            sysinfo_block_type6_v8h0_ies = 26
            csi_im_configid_r12 = 27
            ellipsoid_point = 28
            ellipsoid_point_altitude = 29
            ellipsoid_point_altitude_uncertainty_ellipsoid = 30
            ellipsoid_arc = 31
            ellipsoid_point_uncertainty_circle = 32
            ellipsoid_point_uncertainty_ellipse = 33
            horizontal_velocity = 34
            polygon = 35
            measurement_ref_time = 36
            ue_eutra_cap = 37
            ue_eutra_cap_v9a0_ies = 38
            ue_radio_paging_r12 = 39
            var_short_mac_input = 40
            els_sib1_signature = 41
            els_sysinfo_block_type1 = 42
            nhn_plmn_identity_list = 43
            els_dl_ccch = 44
            els_dl_dcch = 45
            els_ul_dcch = 46
            bcch_bch_mf = 47
            bcch_dl_sch_mf = 48
            pcch_mf = 49
            dl_ccch_mf = 50
            dl_dcch_mf = 51
            ul_ccch_mf = 52
            ul_dcch_mf = 53
            sysinfo_block_typemf1 = 54

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V18PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V18PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V18PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V18PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V18PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V18PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V18PduType.PduType.pcch_type
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V18PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V18PduType.PduType.dl_ccch_type
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V18PduType.PduType.dl_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V18PduType.PduType.dl_dcch_type
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V18PduType.PduType.ul_ccch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V18PduType.PduType.ul_ccch_type
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V18PduType.PduType.ul_dcch
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V18PduType.PduType.ul_dcch_type
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V18PduType.PduType.els_dl_ccch
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V18PduType.PduType.els_dl_dcch
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V18PduType.PduType.els_ul_dcch
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V18PduType.PduType.bcch_bch_mf
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V18PduType.PduType.bcch_dl_sch_mf
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V18PduType.PduType.pcch_mf
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V18PduType.PduType.dl_ccch_mf
                                                                                            else (
                                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                                if self.pdu_type
                                                                                                == LteRrcOtaPacket.V18PduType.PduType.dl_dcch_mf
                                                                                                else (
                                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                                                                    if self.pdu_type
                                                                                                    == LteRrcOtaPacket.V18PduType.PduType.ul_ccch_mf
                                                                                                    else (
                                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                                        if self.pdu_type
                                                                                                        == LteRrcOtaPacket.V18PduType.PduType.ul_dcch_mf
                                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V18PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.ul_ccch_type
                )
                or (
                    self.pdu_type == LteRrcOtaPacket.V18PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.ul_dcch_type
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.els_ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.ul_ccch_mf
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V18PduType.PduType.ul_dcch_mf
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V19PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_mbms = 2
            bcch_dl_sch = 3
            bcch_dl_sch_br = 4
            bcch_dl_sch_mbms = 5
            mcch = 6
            pcch = 7
            dl_ccch = 8
            dl_dcch = 9
            ul_ccch = 10
            ul_dcch = 11
            sc_mcch_r13 = 12
            rrcconnection_reconfiguration = 13
            rrcconnection_reconfiguration_v8m0_ies = 14
            rrcconnection_reconfiguration_complete = 15
            rrcconnrelease_v9e0_ies = 16
            scgfail_info_v12d0 = 17
            sysinfo_block_type1 = 18
            sysinfo_block_type1_v8h0_ies = 19
            uecapabilityenquiry = 20
            uecapabilityinformation = 21
            ueinforesponse_v9e0_ies = 22
            sysinfo_block_type2_v8h0_ies = 23
            sysinfo_block_type3_v10j0_ies = 24
            sysinfo_block_type5_v8h0_ies = 25
            sysinfo_block_type6_v8h0_ies = 26
            csi_rs_configid_r14xy = 27
            pusch_config_dedscell_r14xy = 28
            tdd_config_sl_r12 = 29
            ellipsoid_point = 30
            ellipsoid_point_altitude = 31
            ellipsoid_point_altitude_uncertainty_ellipsoid = 32
            ellipsoid_arc = 33
            ellipsoid_point_uncertainty_circle = 34
            ellipsoid_point_uncertainty_ellipse = 35
            horizontal_velocity = 36
            polygon = 37
            measurement_ref_time = 38
            rsrp_rangesl3_r12 = 39
            ue_eutra_cap = 40
            ue_eutra_cap_v9a0_ies = 41
            ue_eutra_cap_v10j0_ies = 42
            var_short_mac_input = 43
            sl_offset_ind_sync_r14 = 44
            bcch_bch_nb = 45
            bcch_dl_sch_nb = 46
            pcch_nb = 47
            dl_ccch_nb = 48
            dl_dcch_nb = 49
            ul_ccch_nb = 50
            sc_mcch_nb = 51
            ul_dcch_nb = 52
            els_sib1_signature = 53
            els_sysinfo_block_type1 = 54
            els_dl_dcch = 55
            els_ul_dcch = 56

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V19PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V19PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V19PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V19PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V19PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V19PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_mbms
                            if self.pdu_type
                            == LteRrcOtaPacket.V19PduType.PduType.bcch_dl_sch_mbms
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V19PduType.PduType.mcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V19PduType.PduType.pcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V19PduType.PduType.dl_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V19PduType.PduType.dl_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V19PduType.PduType.ul_ccch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V19PduType.PduType.ul_dcch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V19PduType.PduType.sc_mcch_r13
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V19PduType.PduType.bcch_bch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V19PduType.PduType.bcch_dl_sch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V19PduType.PduType.pcch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V19PduType.PduType.dl_ccch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V19PduType.PduType.dl_dcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V19PduType.PduType.ul_ccch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V19PduType.PduType.sc_mcch_nb
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V19PduType.PduType.ul_dcch_nb
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V19PduType.PduType.els_dl_dcch
                                                                                            else (
                                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                                if self.pdu_type
                                                                                                == LteRrcOtaPacket.V19PduType.PduType.els_ul_dcch
                                                                                                else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V19PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V19PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V19PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V19PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V19PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V1PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_dl_sch = 2
            pcch = 3
            dl_ccch = 4
            dl_dcch = 5
            ul_ccch = 6
            ul_dcch = 7

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V1PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V1PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V1PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                if self.pdu_type
                == LteRrcOtaPacket.V1PduType.PduType.bcch_dl_sch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                    if self.pdu_type == LteRrcOtaPacket.V1PduType.PduType.pcch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                        if self.pdu_type
                        == LteRrcOtaPacket.V1PduType.PduType.dl_ccch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V1PduType.PduType.dl_dcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V1PduType.PduType.ul_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V1PduType.PduType.ul_dcch
                                    else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V1PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V1PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V20PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            rrcconnection_reconfiguration = 10
            rrcconnection_reconfiguration_v8m0_ies = 11
            rrcconnection_reconfiguration_complete = 12
            rrcconnrelease_v9e0_ies = 13
            sysinfo_block_type1 = 14
            sysinfo_block_type1_v8h0_ies = 15
            uecapabilityenquiry = 16
            uecapabilityinformation = 17
            ueinforesponse_v9e0_ies = 18
            sysinfo_block_type2 = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type3_v10j0_ies = 21
            sysinfo_block_type5_v8h0_ies = 22
            sysinfo_block_type6_v8h0_ies = 23
            rsrp_rangesl3_r12 = 24
            rsrp_rangesl4_r13 = 25
            wlan_status_r13 = 26
            wlan_status_v1430 = 27
            ue_eutra_cap = 28
            ue_eutra_cap_v9a0_ies = 29
            ue_eutra_cap_v10j0_ies = 30
            v2x_band_width_class_r14 = 31
            supported_band_infolist_r12 = 32
            freq_band_indicatorlist_eutra_r12 = 33
            var_short_mac_input = 34
            pci_arfcn_r13 = 35
            sl_anchor_carrier_freqlist_v2x_r14 = 36
            sl_comm_tx_pool_list_r12 = 37
            sl_comm_tx_pool_list_ext_r13 = 38
            sl_comm_rx_pool_list_r12 = 39
            sl_disc_sysinfo_report_r13 = 40
            sl_gap_request_r13 = 41
            sl_offset_indicator_sync_r14 = 42
            sl_sync_config_list_r12 = 43
            sl_sync_config_listnfreq_r13 = 44
            ellipsoid_point = 45
            ellipsoid_point_altitude = 46
            ellipsoid_point_altitude_uncertainty_ellipsoid = 47
            ellipsoid_arc = 48
            ellipsoid_point_uncertainty_circle = 49
            ellipsoid_point_uncertainty_ellipse = 50
            horizontal_velocity = 51
            polygon = 52
            measurement_ref_time = 53
            bcch_bch_nb = 54
            bcch_dl_sch_nb = 55
            pcch_nb = 56
            dl_ccch_nb = 57
            dl_dcch_nb = 58
            ul_ccch_nb = 59
            sc_mcch_nb = 60
            ul_dcch_nb = 61
            els_sib1_signature = 62
            els_sysinfo_block_type1 = 63
            els_dl_dcch = 64
            els_ul_dcch = 65

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V20PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V20PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V20PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V20PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V20PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V20PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V20PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V20PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V20PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V20PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V20PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V20PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V20PduType.PduType.bcch_bch_nb
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V20PduType.PduType.bcch_dl_sch_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V20PduType.PduType.pcch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V20PduType.PduType.dl_ccch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V20PduType.PduType.dl_dcch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V20PduType.PduType.ul_ccch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V20PduType.PduType.sc_mcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V20PduType.PduType.ul_dcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V20PduType.PduType.els_dl_dcch
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V20PduType.PduType.els_ul_dcch
                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V20PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V20PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V20PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V20PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V20PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V21PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            pcch_type = 5
            dl_ccch = 6
            dl_ccch_type = 7
            dl_dcch = 8
            dl_dcch_type = 9
            ul_ccch = 10
            ul_ccch_type = 11
            ul_dcch = 12
            ul_dcch_type = 13
            rrcconnection_reconfiguration = 14
            rrcconnection_reconfiguration_v8m0_ies = 15
            rrcconnection_reconfiguration_complete = 16
            rrcconnrelease_v9e0_ies = 17
            sysinfo = 18
            sysinfo_block_type1 = 19
            sysinfo_block_type1_v8h0_ies = 20
            uecapabilityenquiry = 21
            uecapabilityinformation = 22
            ueinforesponse_v9e0_ies = 23
            sysinfo_block_type2_v8h0_ies = 24
            sysinfo_block_type5_v8h0_ies = 25
            sysinfo_block_type6_v8h0_ies = 26
            csi_im_configid_r12 = 27
            ellipsoid_point = 28
            ellipsoid_point_altitude = 29
            ellipsoid_point_altitude_uncertainty_ellipsoid = 30
            ellipsoid_arc = 31
            ellipsoid_point_uncertainty_circle = 32
            ellipsoid_point_uncertainty_ellipse = 33
            horizontal_velocity = 34
            polygon = 35
            measurement_ref_time = 36
            meas_objid_v1310 = 37
            ue_eutra_cap = 38
            ue_eutra_cap_v9a0_ies = 39
            ue_radio_paging_r12 = 40
            var_short_mac_input = 41
            els_sib1_signature = 42
            els_sysinfo_block_type1 = 43
            nhn_plmn_identity_list = 44
            els_dl_ccch = 45
            els_dl_dcch = 46
            els_ul_dcch = 47
            bcch_bch_mf = 48
            bcch_dl_sch_mf = 49
            pcch_mf = 50
            dl_ccch_mf = 51
            dl_dcch_mf = 52
            ul_ccch_mf = 53
            ul_dcch_mf = 54
            sysinfo_block_typemf1 = 55

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V21PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V21PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V21PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V21PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V21PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V21PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V21PduType.PduType.pcch_type
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V21PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V21PduType.PduType.dl_ccch_type
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V21PduType.PduType.dl_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V21PduType.PduType.dl_dcch_type
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V21PduType.PduType.ul_ccch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V21PduType.PduType.ul_ccch_type
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V21PduType.PduType.ul_dcch
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V21PduType.PduType.ul_dcch_type
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V21PduType.PduType.els_dl_ccch
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V21PduType.PduType.els_dl_dcch
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V21PduType.PduType.els_ul_dcch
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V21PduType.PduType.bcch_bch_mf
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V21PduType.PduType.bcch_dl_sch_mf
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V21PduType.PduType.pcch_mf
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V21PduType.PduType.dl_ccch_mf
                                                                                            else (
                                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                                if self.pdu_type
                                                                                                == LteRrcOtaPacket.V21PduType.PduType.dl_dcch_mf
                                                                                                else (
                                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                                                                    if self.pdu_type
                                                                                                    == LteRrcOtaPacket.V21PduType.PduType.ul_ccch_mf
                                                                                                    else (
                                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                                        if self.pdu_type
                                                                                                        == LteRrcOtaPacket.V21PduType.PduType.ul_dcch_mf
                                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V21PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.ul_ccch_type
                )
                or (
                    self.pdu_type == LteRrcOtaPacket.V21PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.ul_dcch_type
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.els_ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.ul_ccch_mf
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V21PduType.PduType.ul_dcch_mf
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V22PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            rrcconnection_reconfiguration = 9
            rrcconnection_reconfiguration_v8m0_ies = 10
            rrcconnection_reconfiguration_complete = 11
            rrcconnrelease_v9e0_ies = 12
            sysinfo_block_type1 = 13
            sysinfo_block_type1_v8h0_ies = 14
            uecapabilityenquiry = 15
            uecapabilityinformation = 16
            ueinforesponse_v9e0_ies = 17
            sysinfo_block_type2_v8h0_ies = 18
            sysinfo_block_type5_v8h0_ies = 19
            sysinfo_block_type6_v8h0_ies = 20
            tdd_configsl_r12 = 21
            ellipsoid_point = 22
            ellipsoid_point_altitude = 23
            ellipsoid_point_altitude_uncertainty_ellipsoid = 24
            ellipsoid_arc = 25
            ellipsoid_point_uncertainty_circle = 26
            ellipsoid_point_uncertainty_ellipse = 27
            horizontal_velocity = 28
            polygon = 29
            measurement_ref_time = 30
            rsrp_rangsl3_r12 = 31
            ue_eutra_cap = 32
            ue_eutra_cap_v9a0_ies = 33
            var_short_mac_input = 34
            els_sib1_signature = 35
            els_sysinfo_block_type1 = 36
            els_dl_dcch = 37
            els_ul_dcch = 38

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V22PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V22PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V22PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V22PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V22PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V22PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V22PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V22PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V22PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V22PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V22PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V22PduType.PduType.els_dl_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V22PduType.PduType.els_ul_dcch
                                                    else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V22PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V22PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V22PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V23PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            master_information_block_mbms_r14 = 10
            rrcconnection_reconfiguration = 11
            rrcconnection_reconfiguration_v8m0_ies = 12
            rrcconnection_reconfiguration_complete = 13
            rrcconnection_release_v9e0_ies = 14
            scgfailure_information_v12d0_ies = 15
            scptmconfiguration_r13 = 16
            scptmconfiguration_br_r14 = 17
            system_information_mbms_r14 = 18
            system_information_block_type1 = 19
            system_information_block_type1_v8h0_ies = 20
            system_information_block_type1_mbms_r14 = 21
            uecapability_enquiry = 22
            uecapability_information = 23
            ueinformation_response_v9e0_ies = 24
            system_information_block_type2 = 25
            system_information_block_type2_v8h0_ies = 26
            system_information_block_type3_v10j0_ies = 27
            system_information_block_type5_v8h0_ies = 28
            system_information_block_type6_v8h0_ies = 29
            tdd_config_sl_r12 = 30
            rsrp_range_sl3_r12 = 31
            ue_eutra_capability = 32
            ue_eutra_capability_v9a0_ies = 33
            ue_eutra_capability_v10j0_ies = 34
            sl_offset_indicator_sync_r14 = 35
            var_short_mac_input = 36
            ellipsoid_point = 37
            ellipsoid_point_with_altitude = 38
            ellipsoid_point_with_altitude_and_uncertainty_ellipsoid = 39
            ellipsoid_arc = 40
            ellipsoid_point_with_uncertainty_circle = 41
            ellipsoid_point_with_uncertainty_ellipse = 42
            horizontal_velocity = 43
            polygon = 44
            measurement_reference_time = 45
            bcch_bch_nb = 46
            bcch_dl_sch_nb = 47
            pcch_nb = 48
            dl_ccch_nb = 49
            dl_dcch_nb = 50
            ul_ccch_nb = 51
            sc_mcch_nb = 52
            ul_dcch_nb = 53
            els_sib1_signature = 54
            els_system_information_block_type1 = 55
            els_dl_dcch = 56
            els_ul_dcch = 57

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V23PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V23PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V23PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V23PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V23PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V23PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V23PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V23PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V23PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V23PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V23PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V23PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V23PduType.PduType.bcch_bch_nb
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V23PduType.PduType.bcch_dl_sch_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V23PduType.PduType.pcch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V23PduType.PduType.dl_ccch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V23PduType.PduType.dl_dcch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V23PduType.PduType.ul_ccch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V23PduType.PduType.sc_mcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V23PduType.PduType.ul_dcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V23PduType.PduType.els_dl_dcch
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V23PduType.PduType.els_ul_dcch
                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V23PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V23PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V23PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V23PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V23PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V24PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            master_information_block_mbms_r14 = 10
            rrcconnection_reconfiguration = 11
            rrcconnection_reconfiguration_v8m0_ies = 12
            rrcconnection_reconfiguration_complete = 13
            rrcconnection_release_v9e0_ies = 14
            scgfailure_information_v12d0_ies = 15
            scptmconfiguration_r13 = 16
            scptmconfiguration_br_r14 = 17
            system_information_mbms_r14 = 18
            system_information_block_type1 = 19
            system_information_block_type1_v8h0_ies = 20
            system_information_block_type1_mbms_r14 = 21
            uecapability_enquiry = 22
            uecapability_information = 23
            ueinformation_response_v9e0_ies = 24
            system_information_block_type2 = 25
            system_information_block_type2_v8h0_ies = 26
            system_information_block_type2_v10m0_ies = 27
            system_information_block_type3_v10j0_ies = 28
            system_information_block_type5_v8h0_ies = 29
            system_information_block_type6_v8h0_ies = 30
            tdd_config_sl_r12 = 31
            rsrp_range_sl3_r12 = 32
            ue_eutra_capability = 33
            ue_eutra_capability_v9a0_ies = 34
            ue_eutra_capability_v10j0_ies = 35
            sl_offset_indicator_sync_r14 = 36
            var_short_mac_input = 37
            ellipsoid_point = 38
            ellipsoid_point_with_altitude = 39
            ellipsoid_point_with_altitude_and_uncertainty_ellipsoid = 40
            ellipsoid_arc = 41
            ellipsoid_point_with_uncertainty_circle = 42
            ellipsoid_point_with_uncertainty_ellipse = 43
            horizontal_velocity = 44
            polygon = 45
            measurement_reference_time = 46
            bcch_bch_nb = 47
            bcch_dl_sch_nb = 48
            pcch_nb = 49
            dl_ccch_nb = 50
            dl_dcch_nb = 51
            ul_ccch_nb = 52
            sc_mcch_nb = 53
            ul_dcch_nb = 54
            els_sib1_signature = 55
            els_system_information_block_type1 = 56
            els_dl_dcch = 57
            els_ul_dcch = 58

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V24PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V24PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V24PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V24PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V24PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V24PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V24PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V24PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V24PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V24PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V24PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V24PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V24PduType.PduType.bcch_bch_nb
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V24PduType.PduType.bcch_dl_sch_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V24PduType.PduType.pcch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V24PduType.PduType.dl_ccch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V24PduType.PduType.dl_dcch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V24PduType.PduType.ul_ccch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V24PduType.PduType.sc_mcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V24PduType.PduType.ul_dcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V24PduType.PduType.els_dl_dcch
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V24PduType.PduType.els_ul_dcch
                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V24PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V24PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V24PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V24PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V24PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V25PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            bcch_dl_sch_br = 3
            mcch = 4
            pcch = 5
            dl_ccch = 6
            dl_dcch = 7
            ul_ccch = 8
            ul_dcch = 9
            master_information_block_mbms_r14 = 10
            rrcconnection_reconfiguration = 11
            rrcconnection_reconfiguration_v8m0_ies = 12
            rrcconnection_reconfiguration_complete = 13
            rrcconnection_release_v9e0_ies = 14
            scgfailure_information_v12d0_ies = 15
            scptmconfiguration_r13 = 16
            scptmconfiguration_br_r14 = 17
            system_information_mbms_r14 = 18
            system_information_block_type1 = 19
            system_information_block_type1_v8h0_ies = 20
            system_information_block_type1_mbms_r14 = 21
            uecapability_enquiry = 22
            uecapability_information = 23
            ueinformation_response_v9e0_ies = 24
            system_information_block_type2 = 25
            system_information_block_type2_v8h0_ies = 26
            system_information_block_type2_v10m0_ies = 27
            system_information_block_type3_v10j0_ies = 28
            system_information_block_type5_v8h0_ies = 29
            system_information_block_type6_v8h0_ies = 30
            sps_config_dl_stti_r15 = 31
            tdd_config_sl_r12 = 32
            rsrp_range_sl3_r12 = 33
            ue_eutra_capability = 34
            ue_eutra_capability_v9a0_ies = 35
            ue_eutra_capability_v10j0_ies = 36
            var_short_mac_input = 37
            ellipsoid_point = 38
            ellipsoid_point_with_altitude = 39
            ellipsoid_point_with_altitude_and_uncertainty_ellipsoid = 40
            ellipsoid_arc = 41
            ellipsoid_point_with_uncertainty_circle = 42
            ellipsoid_point_with_uncertainty_ellipse = 43
            horizontal_velocity = 44
            polygon = 45
            measurement_reference_time = 46
            bcch_bch_nb = 47
            bcch_bch_tdd_nb = 48
            bcch_dl_sch_nb = 49
            pcch_nb = 50
            dl_ccch_nb = 51
            dl_dcch_nb = 52
            ul_ccch_nb = 53
            sc_mcch_nb = 54
            ul_dcch_nb = 55
            ue_capability_nb_ext_r14_ies = 56
            els_sib1_signature = 57
            els_system_information_block_type1 = 58
            els_dl_dcch = 59
            els_ul_dcch = 60

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V25PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V25PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V25PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V25PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V25PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                        if self.pdu_type
                        == LteRrcOtaPacket.V25PduType.PduType.bcch_dl_sch_br
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V25PduType.PduType.mcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                if self.pdu_type
                                == LteRrcOtaPacket.V25PduType.PduType.pcch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V25PduType.PduType.dl_ccch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V25PduType.PduType.dl_dcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V25PduType.PduType.ul_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V25PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V25PduType.PduType.bcch_bch_nb
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_tdd_nb
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V25PduType.PduType.bcch_bch_tdd_nb
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V25PduType.PduType.bcch_dl_sch_nb
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V25PduType.PduType.pcch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V25PduType.PduType.dl_ccch_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V25PduType.PduType.dl_dcch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V25PduType.PduType.ul_ccch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V25PduType.PduType.sc_mcch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V25PduType.PduType.ul_dcch_nb
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V25PduType.PduType.els_dl_dcch
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V25PduType.PduType.els_ul_dcch
                                                                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V25PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V25PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V25PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V25PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V25PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V26PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_bch_mbms = 2
            bcch_dl_sch = 3
            bcch_dl_sch_br = 4
            bcch_dl_sch_mbms = 5
            mcch = 6
            pcch = 7
            dl_ccch = 8
            dl_dcch = 9
            ul_ccch = 10
            ul_dcch = 11
            sc_mcch_r13 = 12
            rrcconnection_reconfiguration = 13
            rrcconnection_reconfiguration_v8m0_ies = 14
            rrcconnection_reconfiguration_complete = 15
            rrcconnection_release_v9e0_ies = 16
            scgfailure_information_v12d0_ies = 17
            system_information_block_type1 = 18
            system_information_block_type1_v8h0_ies = 19
            uecapability_enquiry = 20
            uecapability_information = 21
            ueinformation_response_v9e0_ies = 22
            system_information_block_type2 = 23
            system_information_block_type2_v8h0_ies = 24
            system_information_block_type2_v10m0_ies = 25
            system_information_block_type3_v10j0_ies = 26
            system_information_block_type5_v8h0_ies = 27
            system_information_block_type6_v8h0_ies = 28
            tdd_config_sl_r12 = 29
            rsrp_range_sl3_r12 = 30
            ue_eutra_capability = 31
            ue_eutra_capability_v9a0_ies = 32
            ue_eutra_capability_v10j0_ies = 33
            var_short_mac_input = 34
            ellipsoid_point = 35
            ellipsoid_point_with_altitude = 36
            ellipsoid_point_with_altitude_and_uncertainty_ellipsoid = 37
            ellipsoid_arc = 38
            ellipsoid_point_with_uncertainty_circle = 39
            ellipsoid_point_with_uncertainty_ellipse = 40
            horizontal_velocity = 41
            polygon = 42
            measurement_reference_time = 43
            bcch_bch_nb = 44
            bcch_bch_tdd_nb = 45
            bcch_dl_sch_nb = 46
            pcch_nb = 47
            dl_ccch_nb = 48
            dl_dcch_nb = 49
            ul_ccch_nb = 50
            sc_mcch_nb = 51
            ul_dcch_nb = 52
            ue_capability_nb_ext_r14_ies = 53
            els_sib1_signature = 54
            els_system_information_block_type1 = 55
            els_dl_dcch = 56
            els_ul_dcch = 57

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V26PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V26PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V26PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V26PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_mbms
                    if self.pdu_type
                    == LteRrcOtaPacket.V26PduType.PduType.bcch_bch_mbms
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                        if self.pdu_type
                        == LteRrcOtaPacket.V26PduType.PduType.bcch_dl_sch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                            if self.pdu_type
                            == LteRrcOtaPacket.V26PduType.PduType.bcch_dl_sch_br
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_mbms
                                if self.pdu_type
                                == LteRrcOtaPacket.V26PduType.PduType.bcch_dl_sch_mbms
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V26PduType.PduType.mcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V26PduType.PduType.pcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V26PduType.PduType.dl_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V26PduType.PduType.dl_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V26PduType.PduType.ul_ccch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V26PduType.PduType.ul_dcch
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V26PduType.PduType.sc_mcch_r13
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V26PduType.PduType.bcch_bch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_tdd_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V26PduType.PduType.bcch_bch_tdd_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V26PduType.PduType.bcch_dl_sch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V26PduType.PduType.pcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V26PduType.PduType.dl_ccch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V26PduType.PduType.dl_dcch_nb
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V26PduType.PduType.ul_ccch_nb
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V26PduType.PduType.sc_mcch_nb
                                                                                            else (
                                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                                if self.pdu_type
                                                                                                == LteRrcOtaPacket.V26PduType.PduType.ul_dcch_nb
                                                                                                else (
                                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                                    if self.pdu_type
                                                                                                    == LteRrcOtaPacket.V26PduType.PduType.els_dl_dcch
                                                                                                    else (
                                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                                        if self.pdu_type
                                                                                                        == LteRrcOtaPacket.V26PduType.PduType.els_ul_dcch
                                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V26PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V26PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V26PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V26PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V26PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V27PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_bch_mbms = 2
            bcch_dl_sch = 3
            bcch_dl_sch_br = 4
            bcch_dl_sch_mbms = 5
            mcch = 6
            pcch = 7
            dl_ccch = 8
            dl_dcch = 9
            ul_ccch = 10
            ul_dcch = 11
            sc_mcch_r13 = 12
            rrcconnection_reconfiguration = 13
            rrcconnection_reconfiguration_v8m0_ies = 14
            rrcconnection_reconfiguration_complete = 15
            rrcconnection_release_v9e0_ies = 16
            scgfailure_information_v12d0b_ies = 17
            system_information_block_type1 = 18
            system_information_block_type1_v8h0_ies = 19
            uecapability_enquiry = 20
            uecapability_information = 21
            ueinformation_response_v9e0_ies = 22
            type_ffs = 23
            system_information_block_type2 = 24
            system_information_block_type2_v8h0_ies = 25
            system_information_block_type2_v10m0_ies = 26
            system_information_block_type3_v10j0_ies = 27
            system_information_block_type5_v8h0_ies = 28
            system_information_block_type6_v8h0_ies = 29
            tdd_config_sl_r12 = 30
            meas_result_scg_failure_mrdc_r15 = 31
            rsrp_range_sl3_r12 = 32
            ue_eutra_capability = 33
            ue_eutra_capability_v9a0_ies = 34
            ue_eutra_capability_v10j0_ies = 35
            ue_eutra_capability_v13e0b_ies = 36
            var_short_mac_input = 37
            var_short_resume_mac_input_r13 = 38
            ellipsoid_point = 39
            ellipsoid_point_with_altitude = 40
            ellipsoid_point_with_altitude_and_uncertainty_ellipsoid = 41
            ellipsoid_arc = 42
            ellipsoid_point_with_uncertainty_circle = 43
            ellipsoid_point_with_uncertainty_ellipse = 44
            horizontal_velocity = 45
            polygon = 46
            measurement_reference_time = 47
            bcch_bch_nb = 48
            bcch_bch_tdd_nb = 49
            bcch_dl_sch_nb = 50
            pcch_nb = 51
            dl_ccch_nb = 52
            dl_dcch_nb = 53
            ul_ccch_nb = 54
            sc_mcch_nb = 55
            ul_dcch_nb = 56
            ue_capability_nb_ext_r14_ies = 57
            els_sib1_signature = 58
            els_system_information_block_type1 = 59
            els_dl_dcch = 60
            els_ul_dcch = 61

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V27PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V27PduType.PduType,
                self._io.read_bits_int_be(7),
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V27PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V27PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_mbms
                    if self.pdu_type
                    == LteRrcOtaPacket.V27PduType.PduType.bcch_bch_mbms
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                        if self.pdu_type
                        == LteRrcOtaPacket.V27PduType.PduType.bcch_dl_sch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_br
                            if self.pdu_type
                            == LteRrcOtaPacket.V27PduType.PduType.bcch_dl_sch_br
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_mbms
                                if self.pdu_type
                                == LteRrcOtaPacket.V27PduType.PduType.bcch_dl_sch_mbms
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V27PduType.PduType.mcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V27PduType.PduType.pcch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V27PduType.PduType.dl_ccch
                                            else (
                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                if self.pdu_type
                                                == LteRrcOtaPacket.V27PduType.PduType.dl_dcch
                                                else (
                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                                    if self.pdu_type
                                                    == LteRrcOtaPacket.V27PduType.PduType.ul_ccch
                                                    else (
                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                        if self.pdu_type
                                                        == LteRrcOtaPacket.V27PduType.PduType.ul_dcch
                                                        else (
                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch
                                                            if self.pdu_type
                                                            == LteRrcOtaPacket.V27PduType.PduType.sc_mcch_r13
                                                            else (
                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_nb
                                                                if self.pdu_type
                                                                == LteRrcOtaPacket.V27PduType.PduType.bcch_bch_nb
                                                                else (
                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch_tdd_nb
                                                                    if self.pdu_type
                                                                    == LteRrcOtaPacket.V27PduType.PduType.bcch_bch_tdd_nb
                                                                    else (
                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch_nb
                                                                        if self.pdu_type
                                                                        == LteRrcOtaPacket.V27PduType.PduType.bcch_dl_sch_nb
                                                                        else (
                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch_nb
                                                                            if self.pdu_type
                                                                            == LteRrcOtaPacket.V27PduType.PduType.pcch_nb
                                                                            else (
                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch_nb
                                                                                if self.pdu_type
                                                                                == LteRrcOtaPacket.V27PduType.PduType.dl_ccch_nb
                                                                                else (
                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch_nb
                                                                                    if self.pdu_type
                                                                                    == LteRrcOtaPacket.V27PduType.PduType.dl_dcch_nb
                                                                                    else (
                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch_nb
                                                                                        if self.pdu_type
                                                                                        == LteRrcOtaPacket.V27PduType.PduType.ul_ccch_nb
                                                                                        else (
                                                                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.sc_mcch_nb
                                                                                            if self.pdu_type
                                                                                            == LteRrcOtaPacket.V27PduType.PduType.sc_mcch_nb
                                                                                            else (
                                                                                                gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch_nb
                                                                                                if self.pdu_type
                                                                                                == LteRrcOtaPacket.V27PduType.PduType.ul_dcch_nb
                                                                                                else (
                                                                                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                                                                                    if self.pdu_type
                                                                                                    == LteRrcOtaPacket.V27PduType.PduType.els_dl_dcch
                                                                                                    else (
                                                                                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                                                                                        if self.pdu_type
                                                                                                        == LteRrcOtaPacket.V27PduType.PduType.els_ul_dcch
                                                                                                        else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == LteRrcOtaPacket.V27PduType.PduType.ul_ccch)
                or (
                    self.pdu_type == LteRrcOtaPacket.V27PduType.PduType.ul_dcch
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V27PduType.PduType.ul_ccch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V27PduType.PduType.ul_dcch_nb
                )
                or (
                    self.pdu_type
                    == LteRrcOtaPacket.V27PduType.PduType.els_ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V2PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            ue_eutra_cap = 9
            var_short_mac_input = 10
            ue_eutra_cap_v9a0_ies = 11
            sysinfo_block_type1 = 12

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V2PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V2PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V2PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V2PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V2PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V2PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V2PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V2PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V2PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V2PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V2PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V2PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V2PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V3PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            sysinfo_block_type1_v8h0_ies = 9
            sysinfo_block_type2_v8h0_ies = 10
            sysinfo_block_type5_v8h0_ies = 11
            sysinfo_block_type6_v8h0_ies = 12
            ue_eutra_cap = 13
            ue_eutra_cap_v9a0_ies = 14
            var_short_mac_input = 15

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V3PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V3PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V3PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V3PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V3PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V3PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V3PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V3PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V3PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V3PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V3PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V3PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V3PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V4PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            sysinfo_block_type1 = 9
            sysinfo_block_type1_v8h0_ies = 10
            sysinfo_block_type2_v8h0_ies = 11
            sysinfo_block_type5_v8h0_ies = 12
            sysinfo_block_type6_v8h0_ies = 13
            ue_eutra_cap = 14
            ue_eutra_cap_v9a0_ies = 15
            var_short_mac_input = 16

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V4PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V4PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V4PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V4PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V4PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V4PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V4PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V4PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V4PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V4PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V4PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V4PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V4PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V6PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            sysinfo_block_type1_v8h0_ies = 9
            sysinfo_block_type2_v8h0_ies = 10
            sysinfo_block_type5_v8h0_ies = 11
            sysinfo_block_type6_v8h0_ies = 12
            carrier_freqlist_mbms_r11 = 13
            ue_eutra_cap = 14
            ue_eutra_cap_v9a0_ies = 15
            var_short_mac_input = 16

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V6PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V6PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V6PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V6PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V6PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V6PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V6PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V6PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V6PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V6PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V6PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V6PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V6PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V7PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            sysinfo_block_type1 = 9
            sysinfo_block_type1_v8h0_ies = 10
            sysinfo_block_type2_v8h0_ies = 11
            sysinfo_block_type5_v8h0_ies = 12
            sysinfo_block_type6_v8h0_ies = 13
            ue_eutra_cap = 14
            ue_eutra_cap_v9a0_ies = 15
            var_short_mac_input = 16

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V7PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V7PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V7PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V7PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V7PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V7PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V7PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V7PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V7PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V7PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V7PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V7PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V7PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V8PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            mcch = 3
            pcch = 4
            dl_ccch = 5
            dl_dcch = 6
            ul_ccch = 7
            ul_dcch = 8
            connectionrelease_v9e0_ie = 9
            sysinfo_block_type1 = 10
            sysinfo_block_type1_v8h0_ies = 11
            ueinforesponse_v9e0_ie = 12
            sysinfo_block_type2_v8h0_ies = 13
            sysinfo_block_type5_v8h0_ies = 14
            sysinfo_block_type6_v8h0_ies = 15
            ue_eutra_cap = 16
            ue_eutra_cap_v9a0_ies = 17

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V8PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V8PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V8PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V8PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V8PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V8PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V8PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V8PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V8PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V8PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V8PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V8PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V8PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V9PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            ellipsoid_point = 1
            ellipsoid_point_uncertainty_circle = 2
            ellipsoid_point_uncertainty_ellipse = 3
            ellipsoid_point_altitude = 4
            ellipsoid_point_altitude_uncertainty_ellipsoid = 5
            ellipsoid_arc = 6
            horizontal_velocity = 7
            bcch_bch = 8
            bcch_dl_sch = 9
            mcch = 10
            pcch = 11
            dl_ccch = 12
            dl_dcch = 13
            ul_ccch = 14
            ul_dcch = 15
            rrcconnrelease_v9e0_ies = 16
            sysinfo_block_type1 = 17
            sysinfo_block_type1_v8h0_ies = 18
            ueinforesponse_v9e0_ies = 19
            sysinfo_block_type2_v8h0_ies = 20
            sysinfo_block_type5_v8h0_ies = 21
            sysinfo_block_type6_v8h0_ies = 22
            ue_eutra_cap = 23
            ue_eutra_cap_v9a0_ies = 24

        def __init__(self, _io=None, _parent=None, _root=None):
            super(LteRrcOtaPacket.V9PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                LteRrcOtaPacket.V9PduType.PduType, self._io.read_bits_int_be(7)
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LteRrcOtaPacket.V9PduType, self)._write__seq(io)
            self._io.write_bits_int_be(7, int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_bch
                if self.pdu_type == LteRrcOtaPacket.V9PduType.PduType.bcch_bch
                else (
                    gsmtap_v2.GsmtapV2.LteRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == LteRrcOtaPacket.V9PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v2.GsmtapV2.LteRrcSubtype.mcch
                        if self.pdu_type
                        == LteRrcOtaPacket.V9PduType.PduType.mcch
                        else (
                            gsmtap_v2.GsmtapV2.LteRrcSubtype.pcch
                            if self.pdu_type
                            == LteRrcOtaPacket.V9PduType.PduType.pcch
                            else (
                                gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_ccch
                                if self.pdu_type
                                == LteRrcOtaPacket.V9PduType.PduType.dl_ccch
                                else (
                                    gsmtap_v2.GsmtapV2.LteRrcSubtype.dl_dcch
                                    if self.pdu_type
                                    == LteRrcOtaPacket.V9PduType.PduType.dl_dcch
                                    else (
                                        gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == LteRrcOtaPacket.V9PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v2.GsmtapV2.LteRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == LteRrcOtaPacket.V9PduType.PduType.ul_dcch
                                            else gsmtap_v2.GsmtapV2.LteRrcSubtype.unknown
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                self.pdu_type == LteRrcOtaPacket.V9PduType.PduType.ul_ccch
            ) or (self.pdu_type == LteRrcOtaPacket.V9PduType.PduType.ul_dcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink
