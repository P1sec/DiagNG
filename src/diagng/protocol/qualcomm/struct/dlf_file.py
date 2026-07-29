# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_log_f


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DlfFile(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DlfFile, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.logs = []
        i = 0
        while not self._io.is_eof():
            _t_logs = diag_log_f.DiagLogF.InnerLog(self._io)
            try:
                _t_logs._read()
            finally:
                self.logs.append(_t_logs)
            i += 1

        self._dirty = False

    def _fetch_instances(self):
        pass
        for i in range(len(self.logs)):
            pass
            self.logs[i]._fetch_instances()

    def _write__seq(self, io=None):
        super(DlfFile, self)._write__seq(io)
        for i in range(len(self.logs)):
            pass
            if self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'logs', 0, self._io.size() - self._io.pos()
                )
            self.logs[i]._write__seq(self._io)

        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(
                'logs', 0, self._io.size() - self._io.pos()
            )

    def _check(self):
        for i in range(len(self.logs)):
            pass

        self._dirty = False
