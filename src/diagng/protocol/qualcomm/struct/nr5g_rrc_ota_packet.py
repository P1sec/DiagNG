# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
from diagng.protocol.network import gsmtap_v3


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class Nr5gRrcOtaPacket(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Nr5gRrcOtaPacket, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.packet_version = self._io.read_u4le()
        self.rrc_rel = self._io.read_u1()
        self.rrc_ver_major = self._io.read_bits_int_be(4)
        self.rrc_ver_minor = self._io.read_bits_int_be(4)
        self.bearer_id = self._io.read_u1()
        self.phy_cellid = self._io.read_u2le()
        if self.packet_version >= 16:
            pass
            self.nr_global_cellid = self._io.read_u8le()

        self.frequency = self._io.read_u4le()
        _on = self.packet_version
        if _on == 1:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU2(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 10:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 11:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 2:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU2(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 3:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 4:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 5:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 6:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 7:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 8:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        elif _on == 9:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU4(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        else:
            pass
            self.sfn_subfn = Nr5gRrcOtaPacket.SfnSubfnU3(
                self._io, self, self._root
            )
            self.sfn_subfn._read()
        _on = self.packet_version
        if _on == 1:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V1PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 10:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V10PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 11:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V11PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 12:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V11PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 13:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V13PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 14:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V14PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 15:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V15PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 16:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V16PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 17:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V17PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 18:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V17PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 19:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V17PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 2:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V2PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 20:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V20PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 23:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V20PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 24:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V20PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 25:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V17PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 26:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V26PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 28:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V26PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 3:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V3PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 4:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V4PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 5:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V5PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 6:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V6PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 7:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V7PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 8:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V8PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        elif _on == 9:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V9PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        else:
            pass
            self.pdu_type = Nr5gRrcOtaPacket.V20PduType(
                self._io, self, self._root
            )
            self.pdu_type._read()
        self.sib_mask = self._io.read_u4le()
        self.len_message = self._io.read_u2le()
        if self.packet_version >= 19:
            pass
            self.unknown_1 = self._io.read_u1()

        if self.packet_version >= 23:
            pass
            self.unknown_2 = self._io.read_u2le()

        if self.packet_version >= 23:
            pass
            self.segment_id = self._io.read_u1()

        self.message = self._io.read_bytes(self.len_message)
        self._dirty = False

    def _fetch_instances(self):
        pass
        if self.packet_version >= 16:
            pass

        _on = self.packet_version
        if _on == 1:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 10:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 11:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 2:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 3:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 4:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 5:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 6:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 7:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 8:
            pass
            self.sfn_subfn._fetch_instances()
        elif _on == 9:
            pass
            self.sfn_subfn._fetch_instances()
        else:
            pass
            self.sfn_subfn._fetch_instances()
        _on = self.packet_version
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
        elif _on == 28:
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
        if self.packet_version >= 19:
            pass

        if self.packet_version >= 23:
            pass

        if self.packet_version >= 23:
            pass

    def _write__seq(self, io=None):
        super(Nr5gRrcOtaPacket, self)._write__seq(io)
        self._io.write_u4le(self.packet_version)
        self._io.write_u1(self.rrc_rel)
        self._io.write_bits_int_be(4, self.rrc_ver_major)
        self._io.write_bits_int_be(4, self.rrc_ver_minor)
        self._io.write_u1(self.bearer_id)
        self._io.write_u2le(self.phy_cellid)
        if self.packet_version >= 16:
            pass
            self._io.write_u8le(self.nr_global_cellid)

        self._io.write_u4le(self.frequency)
        _on = self.packet_version
        if _on == 1:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 10:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 11:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 2:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 3:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 4:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 5:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 6:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 7:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 8:
            pass
            self.sfn_subfn._write__seq(self._io)
        elif _on == 9:
            pass
            self.sfn_subfn._write__seq(self._io)
        else:
            pass
            self.sfn_subfn._write__seq(self._io)
        _on = self.packet_version
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
        elif _on == 28:
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
        self._io.write_u4le(self.sib_mask)
        self._io.write_u2le(self.len_message)
        if self.packet_version >= 19:
            pass
            self._io.write_u1(self.unknown_1)

        if self.packet_version >= 23:
            pass
            self._io.write_u2le(self.unknown_2)

        if self.packet_version >= 23:
            pass
            self._io.write_u1(self.segment_id)

        self._io.write_bytes(self.message)

    def _check(self):
        if self.packet_version >= 16:
            pass

        _on = self.packet_version
        if _on == 1:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 10:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 11:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 2:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 3:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 4:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 5:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 6:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 7:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 8:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        elif _on == 9:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        else:
            pass
            if self.sfn_subfn._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self._root, self.sfn_subfn._root
                )
            if self.sfn_subfn._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'sfn_subfn', self, self.sfn_subfn._parent
                )
        _on = self.packet_version
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
        elif _on == 28:
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
        if self.packet_version >= 19:
            pass

        if self.packet_version >= 23:
            pass

        if self.packet_version >= 23:
            pass

        if len(self.message) != self.len_message:
            raise kaitaistruct.ConsistencyError(
                'message', self.len_message, len(self.message)
            )
        self._dirty = False

    class SfnSubfnU2(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU2, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.sub_fn = self._io.read_bits_int_be(4)
            self.sys_fn = self._io.read_bits_int_be(10)
            self.reserved = self._io.read_bits_int_be(2)
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU2, self)._write__seq(io)
            self._io.write_bits_int_be(4, self.sub_fn)
            self._io.write_bits_int_be(10, self.sys_fn)
            self._io.write_bits_int_be(2, self.reserved)

        def _check(self):
            self._dirty = False

    class SfnSubfnU3(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU3, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.slot_n = self._io.read_bits_int_be(3)
            self.sub_fn = self._io.read_bits_int_be(6)
            self.sys_fn = self._io.read_bits_int_be(9)
            self.reserved_2 = self._io.read_bits_int_be(6)
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU3, self)._write__seq(io)
            self._io.write_bits_int_be(3, self.slot_n)
            self._io.write_bits_int_be(6, self.sub_fn)
            self._io.write_bits_int_be(9, self.sys_fn)
            self._io.write_bits_int_be(6, self.reserved_2)

        def _check(self):
            self._dirty = False

    class SfnSubfnU4(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU4, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_bits_int_be(3)
            self.sub_fn = self._io.read_bits_int_be(6)
            self.sys_fn = self._io.read_bits_int_be(10)
            self.reserved_2 = self._io.read_bits_int_be(13)
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.SfnSubfnU4, self)._write__seq(io)
            self._io.write_bits_int_be(3, self.reserved)
            self._io.write_bits_int_be(6, self.sub_fn)
            self._io.write_bits_int_be(10, self.sys_fn)
            self._io.write_bits_int_be(13, self.reserved_2)

        def _check(self):
            self._dirty = False

    class V10PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            sysinfo = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            cell_group_config = 22
            meas_result_celllist_eutra = 23
            meas_result_scg_fail = 24
            radio_bearer_config = 25
            freq_band_list = 26
            ue_cap_req_filter_nr = 27
            ue_mrdc_capability = 28
            ue_nr_capability = 29
            var_resume_mac_input = 30
            var_short_mac_input = 31

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V10PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V10PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V10PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V10PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V10PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V10PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V10PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V10PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V10PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V10PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V10PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V10PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V10PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V10PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V10PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V10PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V10PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V10PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V10PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V10PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V10PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V10PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V10PduType.PduType.ue_mrdc_capability
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V10PduType.PduType.ue_nr_capability
                                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V10PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V10PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V10PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V11PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            sysinfo = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            sib12_ie_r16 = 22
            pos_sysinfo_r16 = 23
            cell_group_config = 24
            meas_result_celllist_eutra = 25
            meas_result_scg_fail = 26
            radio_bearer_config = 27
            freq_band_list = 28
            ue_cap_req_filter_nr = 29
            ue_mrdc_capability = 30
            ue_nr_capability = 31
            var_resume_mac_input = 32
            var_rlf_rpt_r16 = 33
            var_short_mac_input = 34

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V11PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V11PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V11PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V11PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V11PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V11PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V11PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V11PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V11PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V11PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V11PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V11PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V11PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V11PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V11PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V11PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V11PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V11PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V11PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V11PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V11PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V11PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V11PduType.PduType.sib12_ie_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V11PduType.PduType.ue_mrdc_capability
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V11PduType.PduType.ue_nr_capability
                                                                                                    else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V11PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V11PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V11PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V13PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            sysinfo = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            sib12_ie_r16 = 22
            pos_sysinfo_r16 = 23
            cell_group_config = 24
            meas_result_celllist_eutra = 25
            meas_result_scg_fail = 26
            radio_bearer_config = 27
            freq_band_list = 28
            ue_cap_req_filter_nr = 29
            ue_mrdc_capability = 30
            ue_nr_capability = 31
            ue_nr_capability_v15c0 = 32
            var_resume_mac_input = 33
            var_rlf_rpt_r16 = 34
            var_short_mac_input = 35

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V13PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V13PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V13PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V13PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V13PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V13PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V13PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V13PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V13PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V13PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V13PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V13PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V13PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V13PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V13PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V13PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V13PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V13PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V13PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V13PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V13PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V13PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V13PduType.PduType.sib12_ie_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V13PduType.PduType.ue_mrdc_capability
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V13PduType.PduType.ue_nr_capability
                                                                                                    else (
                                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                        if self.pdu_type
                                                                                                        == Nr5gRrcOtaPacket.V13PduType.PduType.ue_nr_capability_v15c0
                                                                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V13PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V13PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V13PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V14PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            systeminformation = 12
            overheatingassistance = 13
            uecapenquiry_v1560_ie = 14
            sib2 = 15
            sib3 = 16
            sib4 = 17
            sib5 = 18
            sib6 = 19
            sib7 = 20
            sib8 = 21
            sib9 = 22
            sib12_ie_r16 = 23
            pos_sysinfo_r16 = 24
            cell_group_config = 25
            meas_result_celllist_eutra = 26
            meas_result_scg_fail = 27
            radio_bearer_config = 28
            freq_band_list = 29
            ue_cap_req_filter_nr = 30
            ue_mrdc_capability = 31
            ue_nr_capability = 32
            ue_nr_capability_v15c0 = 33
            var_resume_mac_input = 34
            var_rlf_rpt_r16 = 35
            var_short_mac_input = 36

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V14PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V14PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V14PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V14PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V14PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V14PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V14PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V14PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V14PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V14PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V14PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V14PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V14PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V14PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V14PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V14PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V14PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V14PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V14PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V14PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V14PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V14PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V14PduType.PduType.sib12_ie_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V14PduType.PduType.ue_mrdc_capability
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V14PduType.PduType.ue_nr_capability
                                                                                                    else (
                                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                        if self.pdu_type
                                                                                                        == Nr5gRrcOtaPacket.V14PduType.PduType.ue_nr_capability_v15c0
                                                                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V14PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V14PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V14PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V15PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            systeminformation = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            sib12_ie_r16 = 22
            pos_sysinfo_r16 = 23
            cell_group_config = 24
            meas_result_celllist_eutra = 25
            meas_result_scg_fail = 26
            radio_bearer_config = 27
            freq_band_list = 28
            ue_cap_req_filter_nr = 29
            ue_mrdc_capability = 30
            ue_nr_capability = 31
            ue_nr_capability_v15c0 = 32
            var_resume_mac_input = 33
            var_rlf_rpt_r16 = 34
            var_short_mac_input = 35
            locationcoordinates = 36
            velocity = 37
            locationerror = 38
            locationerror_r13 = 39
            displacementtimestamp_r15 = 40

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V15PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V15PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V15PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V15PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V15PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V15PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V15PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V15PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V15PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V15PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V15PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V15PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V15PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V15PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V15PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V15PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V15PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V15PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V15PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V15PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V15PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V15PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V15PduType.PduType.sib12_ie_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V15PduType.PduType.ue_mrdc_capability
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V15PduType.PduType.ue_nr_capability
                                                                                                    else (
                                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                        if self.pdu_type
                                                                                                        == Nr5gRrcOtaPacket.V15PduType.PduType.ue_nr_capability_v15c0
                                                                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V15PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V15PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V15PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V16PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            systeminformation = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            sib12_ie_r16 = 22
            pos_sysinfo_r16 = 23
            cell_group_config = 24
            meas_result_celllist_eutra = 25
            meas_result_scg_fail = 26
            radio_bearer_config = 27
            freq_band_list = 28
            ue_cap_req_filter_nr = 29
            ue_mrdc_capability = 30
            ue_nr_capability = 31
            ue_nr_capability_v15c0 = 32
            var_resume_mac_input = 33
            var_rlf_rpt_r16 = 34
            var_short_mac_input = 35
            locationcoordinates = 36
            velocity = 37
            locationerror = 38
            locationerror_r13 = 39
            displacementtimestamp_r15 = 40

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V16PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V16PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V16PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V16PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V16PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V16PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V16PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V16PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V16PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V16PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V16PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V16PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V16PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V16PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V16PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V16PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V16PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V16PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V16PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V16PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V16PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V16PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V16PduType.PduType.sib12_ie_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V16PduType.PduType.ue_mrdc_capability
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V16PduType.PduType.ue_nr_capability
                                                                                                    else (
                                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                        if self.pdu_type
                                                                                                        == Nr5gRrcOtaPacket.V16PduType.PduType.ue_nr_capability_v15c0
                                                                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V16PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V16PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V16PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V17PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            systeminformation = 12
            overheatingassistance = 13
            uecapenquiry_v1560_ie = 14
            sib2 = 15
            sib3 = 16
            sib4 = 17
            sib5 = 18
            sib6 = 19
            sib7 = 20
            sib8 = 21
            sib9 = 22
            sib10_r16 = 23
            sib12_ie_r16 = 24
            pos_sysinfo_r16 = 25
            cell_group_config = 26
            meas_result_celllist_eutra = 27
            meas_result_scg_fail = 28
            radio_bearer_config = 29
            freq_band_list = 30
            ue_cap_req_filter_nr = 31
            ue_mrdc_capability = 32
            ue_nr_capability = 33
            ue_nr_capability_v15c0 = 34
            var_resume_mac_input = 35
            var_rlf_rpt_r16 = 36
            var_short_mac_input = 37
            locationcoordinates = 38
            velocity = 39
            locationerror = 40
            locationsource_r13 = 41
            displacementtimestamp_r15 = 42

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V17PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V17PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V17PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V17PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V17PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V17PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V17PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V17PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V17PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V17PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V17PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V17PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V17PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V17PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V17PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V17PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V17PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V17PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V17PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V17PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V17PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V17PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib10_r16
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V17PduType.PduType.sib10_r16
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib12_r16
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V17PduType.PduType.sib12_ie_r16
                                                                                                else (
                                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                                    if self.pdu_type
                                                                                                    == Nr5gRrcOtaPacket.V17PduType.PduType.ue_mrdc_capability
                                                                                                    else (
                                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                        if self.pdu_type
                                                                                                        == Nr5gRrcOtaPacket.V17PduType.PduType.ue_nr_capability
                                                                                                        else (
                                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                            if self.pdu_type
                                                                                                            == Nr5gRrcOtaPacket.V17PduType.PduType.ue_nr_capability_v15c0
                                                                                                            else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
            )
            return getattr(self, '_m_gsmtap_subtype', None)

        def _invalidate_gsmtap_subtype(self):
            del self._m_gsmtap_subtype

        @property
        def is_uplink(self):
            if hasattr(self, '_m_is_uplink'):
                return self._m_is_uplink

            self._m_is_uplink = (
                (self.pdu_type == Nr5gRrcOtaPacket.V17PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V17PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V17PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V1PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            xbcch_bch = 1
            dl_xccch = 2
            dl_xdcch = 3
            ul_xccch = 4
            ul_xdcch = 5
            beam_id = 6
            plmn_id_list = 7
            ue_5gra_cap = 8
            var_short_mac = 9
            default_config = 10

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V1PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V1PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V1PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V1PduType.PduType.xbcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V1PduType.PduType.dl_xccch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V1PduType.PduType.dl_xdcch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V1PduType.PduType.ul_xccch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V1PduType.PduType.ul_xdcch
                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                self.pdu_type == Nr5gRrcOtaPacket.V1PduType.PduType.ul_xccch
            ) or (self.pdu_type == Nr5gRrcOtaPacket.V1PduType.PduType.ul_xdcch)
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V20PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            mcch = 5
            pcch = 6
            ul_ccch = 7
            ul_ccch1 = 8
            ul_dcch = 9
            rrc_reconfig = 10
            rrc_reconfig_complete = 11

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V20PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V20PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V20PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V20PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V20PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V20PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V20PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.mcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V20PduType.PduType.mcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V20PduType.PduType.pcch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V20PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V20PduType.PduType.ul_ccch1
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V20PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V20PduType.PduType.rrc_reconfig
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V20PduType.PduType.rrc_reconfig_complete
                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V20PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V20PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V20PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V26PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            mcch = 5
            pcch = 6
            ul_ccch = 7
            ul_ccch1 = 8
            ul_dcch = 9
            rrc_reconfig = 11
            rrc_reconfig_complete = 12

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V26PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V26PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V26PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type
                == Nr5gRrcOtaPacket.V26PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V26PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V26PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V26PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.mcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V26PduType.PduType.mcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V26PduType.PduType.pcch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V26PduType.PduType.ul_ccch
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V26PduType.PduType.ul_ccch1
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V26PduType.PduType.ul_dcch
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V26PduType.PduType.rrc_reconfig
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V26PduType.PduType.rrc_reconfig_complete
                                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V26PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V26PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V26PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V2PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            dl_dcch = 2
            ul_dcch = 3
            reconfig = 4
            reconfig_complete = 5
            sb1 = 6
            beam_fail_recovery_config = 7
            meas_result_scg_fail = 8
            radio_bearer_config = 9
            subcarrier_spacing_rach = 10
            band_param_comb_list_ul = 11
            ue_capability_rat_container_list = 12
            ue_mrdc_capability = 13
            ue_nr_capability = 14
            supported_band_comb = 15
            candidate_rs_index_info_list = 16
            cellid = 17
            meas_obj_eutra = 18
            meas_result_list_eutra = 19
            meas_result_sstd = 20
            phy_cellnr = 21
            phys_cellid_eutra = 22
            short_mac_i = 23
            ue_capability_info = 24
            mbsfn_subframe_config_list = 25

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V2PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V2PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V2PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V2PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V2PduType.PduType.dl_dcch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V2PduType.PduType.ul_dcch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V2PduType.PduType.reconfig
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V2PduType.PduType.reconfig_complete
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V2PduType.PduType.ue_mrdc_capability
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V2PduType.PduType.ue_nr_capability
                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                self.pdu_type == Nr5gRrcOtaPacket.V2PduType.PduType.ul_dcch
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V3PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            dl_dcch = 2
            ul_dcch = 3
            reconfig = 4
            reconfig_complete = 5
            sb1 = 6
            cell_group_config = 7
            gscn_value_nr = 8
            meas_result_scg_failure = 9
            meas_result_celllist_sftd = 10
            radio_bearer_config = 11
            freq_band_list = 12
            ue_capability_rat_containerlist = 13
            ue_mrdc_capability = 14
            ue_nr_capability = 15
            cellid = 16
            short_mac_i = 17

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V3PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V3PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V3PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V3PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V3PduType.PduType.dl_dcch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V3PduType.PduType.ul_dcch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V3PduType.PduType.reconfig
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V3PduType.PduType.reconfig_complete
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V3PduType.PduType.ue_mrdc_capability
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V3PduType.PduType.ue_nr_capability
                                        else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                self.pdu_type == Nr5gRrcOtaPacket.V3PduType.PduType.ul_dcch
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V4PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            mob_from_nr_cmd = 9
            reconfig = 10
            reconfig_complete = 11
            sib1 = 12
            systeminfo = 13
            amf_id = 14
            cell_group_config = 15
            meas_result_scg_failure = 16
            meas_result_celllist_sftd = 17
            radio_bearer_config = 18
            ue_capability_req_filter_nr = 19
            ue_mrdc_capability = 20
            ue_nr_capability = 21

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V4PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V4PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V4PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V4PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V4PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V4PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V4PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V4PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V4PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V4PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V4PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V4PduType.PduType.reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V4PduType.PduType.reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V4PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V4PduType.PduType.ue_mrdc_capability
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V4PduType.PduType.ue_nr_capability
                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V4PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V4PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V4PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V5PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            reconfig = 9
            reconfig_complete = 10
            sib1 = 11
            systeminfo = 12
            sib2 = 13
            sib3 = 14
            sib4 = 15
            sib5 = 16
            sib6 = 17
            sib7 = 18

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V5PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V5PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V5PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V5PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V5PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V5PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V5PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V5PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V5PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V5PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V5PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V5PduType.PduType.reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V5PduType.PduType.reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V5PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V5PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V5PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V5PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V5PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V5PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V5PduType.PduType.sib7
                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V5PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V5PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V5PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V6PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            reconfig = 9
            reconfig_complete = 10
            sib1 = 11
            systeminfo = 12
            sib2 = 13
            sib3 = 14
            sib4 = 15
            sib5 = 16
            sib6 = 17
            sib7 = 18
            sib8 = 19
            sib9 = 20
            cell_group_config = 21
            meas_result_celllist_sftd = 22
            meas_result_scg_failure = 23
            radio_bearer_config = 24
            ue_capability_req_filter_nr = 25
            ue_mrdc_capability = 26
            ue_nr_capability = 27
            var_resume_mac_input = 28
            var_short_mac_input = 29

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V6PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V6PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V6PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V6PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V6PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V6PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V6PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V6PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V6PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V6PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V6PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V6PduType.PduType.reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V6PduType.PduType.reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V6PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V6PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V6PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V6PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V6PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V6PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V6PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V6PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V6PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V6PduType.PduType.ue_mrdc_capability
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V6PduType.PduType.ue_nr_capability
                                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V6PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V6PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V6PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V7PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            reconfig = 9
            reconfig_complete = 10
            sib1 = 11
            systeminfo = 12
            sib2 = 13
            sib3 = 14
            sib4 = 15
            sib5 = 16
            sib6 = 17
            sib7 = 18
            sib8 = 19
            sib9 = 20
            cell_group_config = 21
            meas_result_celllist_sftd = 22
            meas_result_scg_failure = 23
            radio_bearer_config = 24
            freq_band_list = 25
            ue_capability_req_filter_nr = 26
            ue_mrdc_capability = 27
            ue_nr_capability = 28
            var_resume_mac_input = 29
            var_short_mac_input = 30

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V7PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V7PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V7PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V7PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V7PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V7PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V7PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V7PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V7PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V7PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V7PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V7PduType.PduType.reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V7PduType.PduType.reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V7PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V7PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V7PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V7PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V7PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V7PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V7PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V7PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V7PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V7PduType.PduType.ue_mrdc_capability
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V7PduType.PduType.ue_nr_capability
                                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V7PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V7PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V7PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V8PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            sysinfo = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            cell_group_config = 22
            meas_result_celllist_sftd_nr = 23
            meas_result_celllist_eutra = 24
            meas_result_scg_fail = 25
            radio_bearer_config = 26
            freq_band_list = 27
            ue_cap_req_filter_nr = 28
            ue_mrdc_capability = 29
            ue_nr_capability = 30
            var_resume_mac_input = 31
            var_short_mac_input = 32

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V8PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V8PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V8PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V8PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V8PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V8PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V8PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V8PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V8PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V8PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V8PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V8PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V8PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V8PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V8PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V8PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V8PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V8PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V8PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V8PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V8PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V8PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V8PduType.PduType.ue_mrdc_capability
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V8PduType.PduType.ue_nr_capability
                                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V8PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V8PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V8PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink

    class V9PduType(ReadWriteKaitaiStruct):
        class PduType(IntEnum):
            bcch_bch = 1
            bcch_dl_sch = 2
            dl_ccch = 3
            dl_dcch = 4
            pcch = 5
            ul_ccch = 6
            ul_ccch1 = 7
            ul_dcch = 8
            rrc_reconfig = 9
            rrc_reconfig_complete = 10
            sib1 = 11
            sysinfo = 12
            uecapenquiry_v1560_ie = 13
            sib2 = 14
            sib3 = 15
            sib4 = 16
            sib5 = 17
            sib6 = 18
            sib7 = 19
            sib8 = 20
            sib9 = 21
            cell_group_config = 22
            meas_result_celllist_eutra = 23
            meas_result_scg_fail = 24
            radio_bearer_config = 25
            freq_band_list = 26
            ue_cap_req_filter_nr = 27
            ue_mrdc_capability = 28
            ue_nr_capability = 29
            var_resume_mac_input = 30

        def __init__(self, _io=None, _parent=None, _root=None):
            super(Nr5gRrcOtaPacket.V9PduType, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pdu_type = KaitaiStream.resolve_enum(
                Nr5gRrcOtaPacket.V9PduType.PduType, self._io.read_u1()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(Nr5gRrcOtaPacket.V9PduType, self)._write__seq(io)
            self._io.write_u1(int(self.pdu_type))

        def _check(self):
            self._dirty = False

        @property
        def gsmtap_subtype(self):
            if hasattr(self, '_m_gsmtap_subtype'):
                return self._m_gsmtap_subtype

            self._m_gsmtap_subtype = (
                gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_bch
                if self.pdu_type == Nr5gRrcOtaPacket.V9PduType.PduType.bcch_bch
                else (
                    gsmtap_v3.GsmtapV3.NrRrcSubtype.bcch_dl_sch
                    if self.pdu_type
                    == Nr5gRrcOtaPacket.V9PduType.PduType.bcch_dl_sch
                    else (
                        gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_ccch
                        if self.pdu_type
                        == Nr5gRrcOtaPacket.V9PduType.PduType.dl_ccch
                        else (
                            gsmtap_v3.GsmtapV3.NrRrcSubtype.dl_dcch
                            if self.pdu_type
                            == Nr5gRrcOtaPacket.V9PduType.PduType.dl_dcch
                            else (
                                gsmtap_v3.GsmtapV3.NrRrcSubtype.pcch
                                if self.pdu_type
                                == Nr5gRrcOtaPacket.V9PduType.PduType.pcch
                                else (
                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch
                                    if self.pdu_type
                                    == Nr5gRrcOtaPacket.V9PduType.PduType.ul_ccch
                                    else (
                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_ccch1
                                        if self.pdu_type
                                        == Nr5gRrcOtaPacket.V9PduType.PduType.ul_ccch1
                                        else (
                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ul_dcch
                                            if self.pdu_type
                                            == Nr5gRrcOtaPacket.V9PduType.PduType.ul_dcch
                                            else (
                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration
                                                if self.pdu_type
                                                == Nr5gRrcOtaPacket.V9PduType.PduType.rrc_reconfig
                                                else (
                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.rrc_reconfiguration_complete
                                                    if self.pdu_type
                                                    == Nr5gRrcOtaPacket.V9PduType.PduType.rrc_reconfig_complete
                                                    else (
                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib1
                                                        if self.pdu_type
                                                        == Nr5gRrcOtaPacket.V9PduType.PduType.sib1
                                                        else (
                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib2
                                                            if self.pdu_type
                                                            == Nr5gRrcOtaPacket.V9PduType.PduType.sib2
                                                            else (
                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib3
                                                                if self.pdu_type
                                                                == Nr5gRrcOtaPacket.V9PduType.PduType.sib3
                                                                else (
                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib4
                                                                    if self.pdu_type
                                                                    == Nr5gRrcOtaPacket.V9PduType.PduType.sib4
                                                                    else (
                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib5
                                                                        if self.pdu_type
                                                                        == Nr5gRrcOtaPacket.V9PduType.PduType.sib5
                                                                        else (
                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.sib6
                                                                            if self.pdu_type
                                                                            == Nr5gRrcOtaPacket.V9PduType.PduType.sib6
                                                                            else (
                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.sib7
                                                                                if self.pdu_type
                                                                                == Nr5gRrcOtaPacket.V9PduType.PduType.sib7
                                                                                else (
                                                                                    gsmtap_v3.GsmtapV3.NrRrcSubtype.sib8
                                                                                    if self.pdu_type
                                                                                    == Nr5gRrcOtaPacket.V9PduType.PduType.sib8
                                                                                    else (
                                                                                        gsmtap_v3.GsmtapV3.NrRrcSubtype.sib9
                                                                                        if self.pdu_type
                                                                                        == Nr5gRrcOtaPacket.V9PduType.PduType.sib9
                                                                                        else (
                                                                                            gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_mrdc_capability
                                                                                            if self.pdu_type
                                                                                            == Nr5gRrcOtaPacket.V9PduType.PduType.ue_mrdc_capability
                                                                                            else (
                                                                                                gsmtap_v3.GsmtapV3.NrRrcSubtype.ue_nr_capability
                                                                                                if self.pdu_type
                                                                                                == Nr5gRrcOtaPacket.V9PduType.PduType.ue_nr_capability
                                                                                                else gsmtap_v3.GsmtapV3.NrRrcSubtype.unknown
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
                (self.pdu_type == Nr5gRrcOtaPacket.V9PduType.PduType.ul_ccch)
                or (
                    self.pdu_type
                    == Nr5gRrcOtaPacket.V9PduType.PduType.ul_ccch1
                )
                or (
                    self.pdu_type == Nr5gRrcOtaPacket.V9PduType.PduType.ul_dcch
                )
            )
            return getattr(self, '_m_is_uplink', None)

        def _invalidate_is_uplink(self):
            del self._m_is_uplink
