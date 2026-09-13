# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_response
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagCmdExtF(ReadWriteKaitaiStruct):
    class ProcType(IntEnum):
        modem = 0
        app = 1
        common_dual = 2
        qdsp6 = 3
        riva = 4
        slpi = 5
        wdsp = 6
        cdsp = 7
        no_proc = 255

    class TimeOffsetType(IntEnum):
        no_custom_offset = 0
        sync_offset_type = 1
        no_offset = 255

    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagCmdExtF, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.version = self._io.read_u1()
        if not self.version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.version, self._io, '/seq/0'
            )
        _on = self.version
        if _on == 1:
            pass
            self.header = DiagCmdExtF.V1Header(self._io, self, self._root)
            self.header._read()
        elif _on == 2:
            pass
            self.header = DiagCmdExtF.V2Header(self._io, self, self._root)
            self.header._read()
        self.payload = diag_response.DiagResponse(self._io)
        self.payload._read()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.version
        if _on == 1:
            pass
            self.header._fetch_instances()
        elif _on == 2:
            pass
            self.header._fetch_instances()
        self.payload._fetch_instances()

    def _write__seq(self, io=None):
        super(DiagCmdExtF, self)._write__seq(io)
        self._io.write_u1(self.version)
        _on = self.version
        if _on == 1:
            pass
            self.header._write__seq(self._io)
        elif _on == 2:
            pass
            self.header._write__seq(self._io)
        self.payload._write__seq(self._io)

    def _check(self):
        if not self.version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.version, None, '/seq/0'
            )
        _on = self.version
        if _on == 1:
            pass
            if self.header._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'header', self._root, self.header._root
                )
            if self.header._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'header', self, self.header._parent
                )
        elif _on == 2:
            pass
            if self.header._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'header', self._root, self.header._root
                )
            if self.header._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'header', self, self.header._parent
                )
        self._dirty = False

    class V1Header(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagCmdExtF.V1Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.proc_id = KaitaiStream.resolve_enum(
                DiagCmdExtF.ProcType, self._io.read_u2le()
            )
            self.subscription_id = self._io.read_u4le()
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(DiagCmdExtF.V1Header, self)._write__seq(io)
            self._io.write_u2le(int(self.proc_id))
            self._io.write_u4le(self.subscription_id)

        def _check(self):
            self._dirty = False

    class V2Header(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagCmdExtF.V2Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.proc_id = KaitaiStream.resolve_enum(
                DiagCmdExtF.ProcType, self._io.read_u2le()
            )
            self.len_name = self._io.read_u1()
            self.time_offset_type = KaitaiStream.resolve_enum(
                DiagCmdExtF.TimeOffsetType, self._io.read_u1()
            )
            self.time_offset = self._io.read_u8le()
            self.ulog_name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(24), 0, False)
            ).decode('ASCII')
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(DiagCmdExtF.V2Header, self)._write__seq(io)
            self._io.write_u2le(int(self.proc_id))
            self._io.write_u1(self.len_name)
            self._io.write_u1(int(self.time_offset_type))
            self._io.write_u8le(self.time_offset)
            self._io.write_bytes_limit(
                (self.ulog_name).encode('ASCII'), 24, 0, 0
            )

        def _check(self):
            if len((self.ulog_name).encode('ASCII')) > 24:
                raise kaitaistruct.ConsistencyError(
                    'ulog_name', 24, len((self.ulog_name).encode('ASCII'))
                )
            if (
                KaitaiStream.byte_array_index_of(
                    (self.ulog_name).encode('ASCII'), 0
                )
                != -1
            ):
                raise kaitaistruct.ConsistencyError(
                    'ulog_name',
                    -1,
                    KaitaiStream.byte_array_index_of(
                        (self.ulog_name).encode('ASCII'), 0
                    ),
                )
            self._dirty = False
