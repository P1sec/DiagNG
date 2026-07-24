# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import log_response_v1
from diagng.protocol.qualcomm.struct import log_request_v1
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagLogConfigFReq(ReadWriteKaitaiStruct):
    class Status(IntEnum):
        success = 0

    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagLogConfigFReq, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.padding = self._io.read_bytes(3)
        self.operation = KaitaiStream.resolve_enum(
            log_request_v1.LogRequestV1.Operation, self._io.read_u4le()
        )
        self.status = KaitaiStream.resolve_enum(
            DiagLogConfigFReq.Status, self._io.read_u4le()
        )
        _on = self.operation
        if _on == log_request_v1.LogRequestV1.Operation.disable_op:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = log_response_v1.LogResponseV1.Disable(
                _io__raw_payload
            )
            self.payload._read()
        elif _on == log_request_v1.LogRequestV1.Operation.get_mask_op:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = log_response_v1.LogResponseV1.GetMask(
                _io__raw_payload
            )
            self.payload._read()
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_id_ranges_op
        ):
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = log_response_v1.LogResponseV1.RetrieveIdRanges(
                _io__raw_payload
            )
            self.payload._read()
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_valid_mask_op
        ):
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = log_response_v1.LogResponseV1.RetrieveValidMask(
                _io__raw_payload
            )
            self.payload._read()
        elif _on == log_request_v1.LogRequestV1.Operation.set_mask_op:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = log_response_v1.LogResponseV1.SetMask(
                _io__raw_payload
            )
            self.payload._read()
        else:
            pass
            self.payload = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.operation
        if _on == log_request_v1.LogRequestV1.Operation.disable_op:
            pass
            self.payload._fetch_instances()
        elif _on == log_request_v1.LogRequestV1.Operation.get_mask_op:
            pass
            self.payload._fetch_instances()
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_id_ranges_op
        ):
            pass
            self.payload._fetch_instances()
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_valid_mask_op
        ):
            pass
            self.payload._fetch_instances()
        elif _on == log_request_v1.LogRequestV1.Operation.set_mask_op:
            pass
            self.payload._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(DiagLogConfigFReq, self)._write__seq(io)
        self._io.write_bytes(self.padding)
        self._io.write_u4le(int(self.operation))
        self._io.write_u4le(int(self.status))
        _on = self.operation
        if _on == log_request_v1.LogRequestV1.Operation.disable_op:
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
        elif _on == log_request_v1.LogRequestV1.Operation.get_mask_op:
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
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_id_ranges_op
        ):
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
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_valid_mask_op
        ):
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
        elif _on == log_request_v1.LogRequestV1.Operation.set_mask_op:
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
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'payload', 0, self._io.size() - self._io.pos()
                )

    def _check(self):
        if len(self.padding) != 3:
            raise kaitaistruct.ConsistencyError(
                'padding', 3, len(self.padding)
            )
        _on = self.operation
        if _on == log_request_v1.LogRequestV1.Operation.disable_op:
            pass
        elif _on == log_request_v1.LogRequestV1.Operation.get_mask_op:
            pass
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_id_ranges_op
        ):
            pass
        elif (
            _on == log_request_v1.LogRequestV1.Operation.retrieve_valid_mask_op
        ):
            pass
        elif _on == log_request_v1.LogRequestV1.Operation.set_mask_op:
            pass
        else:
            pass
        self._dirty = False
