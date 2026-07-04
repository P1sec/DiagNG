# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from diagng.parsing.struct.qualcomm import diag_cmd_code


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagMessage(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(DiagMessage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.cmd_code = KaitaiStream.resolve_enum(
            diag_cmd_code.DiagCmdCode.DiagCmd, self._io.read_u1()
        )
        self.payload = self._io.read_bytes_full()

    def _fetch_instances(self):
        pass
