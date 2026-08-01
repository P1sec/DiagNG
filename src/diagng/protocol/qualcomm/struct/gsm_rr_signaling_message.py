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


class GsmRrSignalingMessage(ReadWriteKaitaiStruct):
    class ChannelType(IntEnum):
        dcch = 0
        bcch = 1
        l2_rach = 2
        ccch = 3
        sacch = 4
        sdcch = 5
        facch_f = 6
        facch_h = 7
        l2_rach_with_no_delay = 8

    class MessageType(IntEnum):
        todo_xx = 0

    def __init__(self, _io=None, _parent=None, _root=None):
        super(GsmRrSignalingMessage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.is_downlink = self._io.read_bits_int_be(1) != 0
        self.channel_type = KaitaiStream.resolve_enum(
            GsmRrSignalingMessage.ChannelType, self._io.read_bits_int_be(7)
        )
        self.message_type = KaitaiStream.resolve_enum(
            GsmRrSignalingMessage.MessageType, self._io.read_u1()
        )
        self.len_message = self._io.read_u1()
        self.message = self._io.read_bytes(self.len_message)
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(GsmRrSignalingMessage, self)._write__seq(io)
        self._io.write_bits_int_be(1, int(self.is_downlink))
        self._io.write_bits_int_be(7, int(self.channel_type))
        self._io.write_u1(int(self.message_type))
        self._io.write_u1(self.len_message)
        self._io.write_bytes(self.message)

    def _check(self):
        if len(self.message) != self.len_message:
            raise kaitaistruct.ConsistencyError(
                'message', self.len_message, len(self.message)
            )
        self._dirty = False
