# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagLogF(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagLogF, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.pending_msgs = self._io.read_u1()
        self.log_outer_length = self._io.read_u2le()
        self.inner_log = DiagLogF.InnerLog(self._io, self, self._root)
        self.inner_log._read()
        self._dirty = False

    def _fetch_instances(self):
        pass
        self.inner_log._fetch_instances()

    def _write__seq(self, io=None):
        super(DiagLogF, self)._write__seq(io)
        self._io.write_u1(self.pending_msgs)
        self._io.write_u2le(self.log_outer_length)
        self.inner_log._write__seq(self._io)

    def _check(self):
        if self.inner_log._root != self._root:
            raise kaitaistruct.ConsistencyError(
                'inner_log', self._root, self.inner_log._root
            )
        if self.inner_log._parent != self:
            raise kaitaistruct.ConsistencyError(
                'inner_log', self, self.inner_log._parent
            )
        self._dirty = False

    class InnerLog(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogF.InnerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_inner_length = self._io.read_u2le()
            self.log_code = self._io.read_u2le()
            self.log_time = self._io.read_u8le()
            self.payload = self._io.read_bytes(self.log_inner_length - 12)
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(DiagLogF.InnerLog, self)._write__seq(io)
            self._io.write_u2le(self.log_inner_length)
            self._io.write_u2le(self.log_code)
            self._io.write_u8le(self.log_time)
            self._io.write_bytes(self.payload)

        def _check(self):
            if len(self.payload) != self.log_inner_length - 12:
                raise kaitaistruct.ConsistencyError(
                    'payload', self.log_inner_length - 12, len(self.payload)
                )
            self._dirty = False
