# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from diagng.parsing.struct.qualcomm import diag_verno_f_req
from diagng.parsing.struct.qualcomm import diag_unknown
from diagng.parsing.struct.qualcomm import diag_cmd_code


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagRequest(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(DiagRequest, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.cmd_code = KaitaiStream.resolve_enum(
            diag_cmd_code.DiagCmdCode.DiagCmd, self._io.read_u1()
        )
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_verno_f_req.DiagVernoFReq(_io__raw_payload)
        else:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_unknown.DiagUnknown(_io__raw_payload)

    def _fetch_instances(self):
        pass
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
            self.payload._fetch_instances()
        else:
            pass
            self.payload._fetch_instances()
