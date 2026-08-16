# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_log_config_f_rsp
from diagng.protocol.qualcomm.struct import diag_verno_f_rsp
from diagng.protocol.qualcomm.struct import diag_log_f
from diagng.protocol.qualcomm.struct import diag_cmd_code
from diagng.protocol.qualcomm.struct import diag_unknown


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagResponse(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagResponse, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.cmd_code = KaitaiStream.resolve_enum(
            diag_cmd_code.DiagCmdCode.DiagCmd, self._io.read_u1()
        )
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_config_f:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_log_config_f_rsp.DiagLogConfigFRsp(
                _io__raw_payload
            )
            self.payload._read()
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_f:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_log_f.DiagLogF(_io__raw_payload)
            self.payload._read()
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_verno_f_rsp.DiagVernoFRsp(_io__raw_payload)
            self.payload._read()
        else:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = diag_unknown.DiagUnknown(_io__raw_payload)
            self.payload._read()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_config_f:
            pass
            self.payload._fetch_instances()
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_f:
            pass
            self.payload._fetch_instances()
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
            self.payload._fetch_instances()
        else:
            pass
            self.payload._fetch_instances()

    def _write__seq(self, io=None):
        super(DiagResponse, self)._write__seq(io)
        self._io.write_u1(int(self.cmd_code))
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_config_f:
            pass
            _io__raw_payload = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_payload)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_payload=_io__raw_payload):
                self._raw_payload = _io__raw_payload.to_byte_array()
                parent.write_bytes(self._raw_payload)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(payload)', 0, parent.size() - parent.pos()
                    )

            _io__raw_payload.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.payload._write__seq(_io__raw_payload)
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_f:
            pass
            _io__raw_payload = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_payload)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_payload=_io__raw_payload):
                self._raw_payload = _io__raw_payload.to_byte_array()
                parent.write_bytes(self._raw_payload)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(payload)', 0, parent.size() - parent.pos()
                    )

            _io__raw_payload.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.payload._write__seq(_io__raw_payload)
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
            _io__raw_payload = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_payload)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_payload=_io__raw_payload):
                self._raw_payload = _io__raw_payload.to_byte_array()
                parent.write_bytes(self._raw_payload)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(payload)', 0, parent.size() - parent.pos()
                    )

            _io__raw_payload.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.payload._write__seq(_io__raw_payload)
        else:
            pass
            _io__raw_payload = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_payload)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_payload=_io__raw_payload):
                self._raw_payload = _io__raw_payload.to_byte_array()
                parent.write_bytes(self._raw_payload)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(payload)', 0, parent.size() - parent.pos()
                    )

            _io__raw_payload.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.payload._write__seq(_io__raw_payload)

    def _check(self):
        _on = self.cmd_code
        if _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_config_f:
            pass
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.log_f:
            pass
        elif _on == diag_cmd_code.DiagCmdCode.DiagCmd.verno_f:
            pass
        else:
            pass
        self._dirty = False
