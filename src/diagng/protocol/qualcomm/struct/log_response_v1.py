# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import log_request_v1


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class LogResponseV1(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(LogResponseV1, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(LogResponseV1, self)._write__seq(io)

    def _check(self):
        self._dirty = False

    class Disable(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogResponseV1.Disable, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LogResponseV1.Disable, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class GetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogResponseV1.GetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = log_request_v1.LogRequestV1.LogMask(self._io)
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(LogResponseV1.GetMask, self)._write__seq(io)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False

    class RetrieveIdRanges(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogResponseV1.RetrieveIdRanges, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.last_item = []
            for i in range(4):
                self.last_item.append(self._io.read_u2le())

            self._dirty = False

        def _fetch_instances(self):
            pass
            for i in range(len(self.last_item)):
                pass

        def _write__seq(self, io=None):
            super(LogResponseV1.RetrieveIdRanges, self)._write__seq(io)
            for i in range(len(self.last_item)):
                pass
                self._io.write_u2le(self.last_item[i])

        def _check(self):
            if len(self.last_item) != 4:
                raise kaitaistruct.ConsistencyError(
                    'last_item', 4, len(self.last_item)
                )
            for i in range(len(self.last_item)):
                pass

            self._dirty = False

    class RetrieveValidMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogResponseV1.RetrieveValidMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = log_request_v1.LogRequestV1.LogMask(self._io)
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(LogResponseV1.RetrieveValidMask, self)._write__seq(io)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False

    class SetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogResponseV1.SetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = log_request_v1.LogRequestV1.LogMask(self._io)
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(LogResponseV1.SetMask, self)._write__seq(io)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False
