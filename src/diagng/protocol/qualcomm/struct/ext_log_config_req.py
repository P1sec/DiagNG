# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_log_config_f_req
from diagng.protocol.qualcomm.struct import diag_logging
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class ExtLogConfigReq(ReadWriteKaitaiStruct):
    class PresetId(IntEnum):
        qxdm_preset_1 = 1
        qxdm_preset_2 = 2

    class StreamId(IntEnum):
        qxdm = 1
        dci = 2

    def __init__(self, _io=None, _parent=None, _root=None):
        super(ExtLogConfigReq, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.cmd_version = self._io.read_u1()
        if not self.cmd_version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.cmd_version, self._io, '/seq/0'
            )
        if not self.cmd_version <= 2:
            raise kaitaistruct.ValidationGreaterThanError(
                2, self.cmd_version, self._io, '/seq/0'
            )
        self.operation = KaitaiStream.resolve_enum(
            diag_log_config_f_req.DiagLogConfigFReq.Operation,
            self._io.read_u1(),
        )
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = ExtLogConfigReq.Disable(
                _io__raw_payload, self, self._root
            )
            self.payload._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = ExtLogConfigReq.GetMask(
                _io__raw_payload, self, self._root
            )
            self.payload._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = ExtLogConfigReq.RetrieveIdRanges(
                _io__raw_payload, self, self._root
            )
            self.payload._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            self._raw_payload = self._io.read_bytes_full()
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = ExtLogConfigReq.SetMask(
                _io__raw_payload, self, self._root
            )
            self.payload._read()
        else:
            pass
            self.payload = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
            pass
            self.payload._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            self.payload._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            self.payload._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            self.payload._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(ExtLogConfigReq, self)._write__seq(io)
        self._io.write_u1(self.cmd_version)
        self._io.write_u1(int(self.operation))
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
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
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
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
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
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
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
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
        else:
            pass
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'payload', 0, self._io.size() - self._io.pos()
                )

    def _check(self):
        if not self.cmd_version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.cmd_version, None, '/seq/0'
            )
        if not self.cmd_version <= 2:
            raise kaitaistruct.ValidationGreaterThanError(
                2, self.cmd_version, None, '/seq/0'
            )
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'payload', self._root, self.payload._root
                )
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'payload', self, self.payload._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'payload', self._root, self.payload._root
                )
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'payload', self, self.payload._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'payload', self._root, self.payload._root
                )
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'payload', self, self.payload._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'payload', self._root, self.payload._root
                )
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'payload', self, self.payload._parent
                )
        else:
            pass
        self._dirty = False

    class Disable(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.Disable, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = ExtLogConfigReq.StreamOrPresetId(
                self._io, self, self._root
            )
            self.stream_or_preset_id._read()
            self.reserved = self._io.read_bytes(1)
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.stream_or_preset_id._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.Disable, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_bytes(self.reserved)

        def _check(self):
            if self.stream_or_preset_id._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self._root,
                    self.stream_or_preset_id._root,
                )
            if self.stream_or_preset_id._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self,
                    self.stream_or_preset_id._parent,
                )
            if len(self.reserved) != 1:
                raise kaitaistruct.ConsistencyError(
                    'reserved', 1, len(self.reserved)
                )
            self._dirty = False

    class GetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.GetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = ExtLogConfigReq.StreamOrPresetId(
                self._io, self, self._root
            )
            self.stream_or_preset_id._read()
            self.reserved = self._io.read_bytes(1)
            self.equipment_id = KaitaiStream.resolve_enum(
                diag_logging.DiagLogging.EquipmentId, self._io.read_u4le()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.stream_or_preset_id._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.GetMask, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_bytes(self.reserved)
            self._io.write_u4le(int(self.equipment_id))

        def _check(self):
            if self.stream_or_preset_id._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self._root,
                    self.stream_or_preset_id._root,
                )
            if self.stream_or_preset_id._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self,
                    self.stream_or_preset_id._parent,
                )
            if len(self.reserved) != 1:
                raise kaitaistruct.ConsistencyError(
                    'reserved', 1, len(self.reserved)
                )
            self._dirty = False

    class PresetId(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.PresetId, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.preset = KaitaiStream.resolve_enum(
                ExtLogConfigReq.PresetId, self._io.read_u8le()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.PresetId, self)._write__seq(io)
            self._io.write_u8le(int(self.preset))

        def _check(self):
            self._dirty = False

    class RetrieveIdRanges(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.RetrieveIdRanges, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.RetrieveIdRanges, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class RetrieveValidMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.RetrieveValidMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.equipment_id = KaitaiStream.resolve_enum(
                diag_logging.DiagLogging.EquipmentId, self._io.read_u4le()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.RetrieveValidMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))

        def _check(self):
            self._dirty = False

    class SetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.SetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = ExtLogConfigReq.StreamOrPresetId(
                self._io, self, self._root
            )
            self.stream_or_preset_id._read()
            self.reserved = self._io.read_bytes(1)
            self.log_mask = diag_log_config_f_req.DiagLogConfigFReq.LogMask(
                self._io
            )
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.stream_or_preset_id._fetch_instances()
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.SetMask, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_bytes(self.reserved)
            self.log_mask._write__seq(self._io)

        def _check(self):
            if self.stream_or_preset_id._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self._root,
                    self.stream_or_preset_id._root,
                )
            if self.stream_or_preset_id._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'stream_or_preset_id',
                    self,
                    self.stream_or_preset_id._parent,
                )
            if len(self.reserved) != 1:
                raise kaitaistruct.ConsistencyError(
                    'reserved', 1, len(self.reserved)
                )
            self._dirty = False

    class StreamId(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.StreamId, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream = KaitaiStream.resolve_enum(
                ExtLogConfigReq.StreamId, self._io.read_u8le()
            )
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.StreamId, self)._write__seq(io)
            self._io.write_u8le(int(self.stream))

        def _check(self):
            self._dirty = False

    class StreamOrPresetId(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigReq.StreamOrPresetId, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            _on = self._root.cmd_version
            if _on == 1:
                pass
                self.id = ExtLogConfigReq.StreamId(self._io, self, self._root)
                self.id._read()
            elif _on == 2:
                pass
                self.id = ExtLogConfigReq.PresetId(self._io, self, self._root)
                self.id._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            _on = self._root.cmd_version
            if _on == 1:
                pass
                self.id._fetch_instances()
            elif _on == 2:
                pass
                self.id._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigReq.StreamOrPresetId, self)._write__seq(io)
            _on = self._root.cmd_version
            if _on == 1:
                pass
                self.id._write__seq(self._io)
            elif _on == 2:
                pass
                self.id._write__seq(self._io)

        def _check(self):
            _on = self._root.cmd_version
            if _on == 1:
                pass
                if self.id._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'id', self._root, self.id._root
                    )
                if self.id._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'id', self, self.id._parent
                    )
            elif _on == 2:
                pass
                if self.id._root != self._root:
                    raise kaitaistruct.ConsistencyError(
                        'id', self._root, self.id._root
                    )
                if self.id._parent != self:
                    raise kaitaistruct.ConsistencyError(
                        'id', self, self.id._parent
                    )
            self._dirty = False
