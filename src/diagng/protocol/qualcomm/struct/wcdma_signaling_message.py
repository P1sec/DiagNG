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


class WcdmaSignalingMessage(ReadWriteKaitaiStruct):
    class ChannelType(IntEnum):
        rrclog_sig_ul_ccch = 0
        rrclog_sig_ul_dcch = 1
        rrclog_sig_dl_ccch = 2
        rrclog_sig_dl_dcch = 3
        rrclog_sig_dl_bcch_bch = 4
        rrclog_sig_dl_bcch_fach = 5
        rrclog_sig_dl_pcch = 6
        rrclog_extension_sib = 9
        rrclog_sib_container = 10

    class PacketType(IntEnum):
        base = 0
        explicit_arfcn_psc = 8
        special = 15

    class RadioBearer(IntEnum):
        ccch = 0
        dcch_um = 1
        dcch_am = 2
        dcch_dt_high_pri = 3
        dcch_dt_low_pri = 4
        bcch_s = 40
        bcch_n = 41
        bcch_fach = 42
        pcch = 43
        ctch = 44

    class SpecialType(IntEnum):
        unknown_1 = 0
        unknown_2 = 14
        invalid_packet = 15

    def __init__(self, _io=None, _parent=None, _root=None):
        super(WcdmaSignalingMessage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.packet_type = KaitaiStream.resolve_enum(
            WcdmaSignalingMessage.PacketType, self._io.read_bits_int_be(4)
        )
        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass
            self.channel_type = KaitaiStream.resolve_enum(
                WcdmaSignalingMessage.ChannelType, self._io.read_bits_int_be(4)
            )

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass
            self.special_type = KaitaiStream.resolve_enum(
                WcdmaSignalingMessage.SpecialType, self._io.read_bits_int_be(4)
            )

        self.radio_bearer = KaitaiStream.resolve_enum(
            WcdmaSignalingMessage.RadioBearer, self._io.read_u1()
        )
        self.len_message = self._io.read_u2le()
        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass
            self.uarfcn = self._io.read_u2le()

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass
            self.psc = self._io.read_u2le()

        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass
            self.message = self._io.read_bytes(self.len_message)

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass
            self.payload = self._io.read_bytes_full()

        self._dirty = False

    def _fetch_instances(self):
        pass
        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass

        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass

    def _write__seq(self, io=None):
        super(WcdmaSignalingMessage, self)._write__seq(io)
        self._io.write_bits_int_be(4, int(self.packet_type))
        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass
            self._io.write_bits_int_be(4, int(self.channel_type))

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass
            self._io.write_bits_int_be(4, int(self.special_type))

        self._io.write_u1(int(self.radio_bearer))
        self._io.write_u2le(self.len_message)
        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass
            self._io.write_u2le(self.uarfcn)

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass
            self._io.write_u2le(self.psc)

        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass
            self._io.write_bytes(self.message)

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'payload', 0, self._io.size() - self._io.pos()
                )

    def _check(self):
        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass

        if (
            self.packet_type
            == WcdmaSignalingMessage.PacketType.explicit_arfcn_psc
        ):
            pass

        if self.packet_type != WcdmaSignalingMessage.PacketType.special:
            pass
            if len(self.message) != self.len_message:
                raise kaitaistruct.ConsistencyError(
                    'message', self.len_message, len(self.message)
                )

        if self.packet_type == WcdmaSignalingMessage.PacketType.special:
            pass

        self._dirty = False

    @property
    def is_uplink(self):
        if hasattr(self, '_m_is_uplink'):
            return self._m_is_uplink

        self._m_is_uplink = (
            self.channel_type
            == WcdmaSignalingMessage.ChannelType.rrclog_sig_ul_ccch
        ) or (
            self.channel_type
            == WcdmaSignalingMessage.ChannelType.rrclog_sig_ul_dcch
        )
        return getattr(self, '_m_is_uplink', None)

    def _invalidate_is_uplink(self):
        del self._m_is_uplink
