# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_log_config_f_req
from diagng.protocol.qualcomm.struct import ext_log_config_req


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class ExtLogConfigRsp(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(ExtLogConfigRsp, self).__init__(_io)
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
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = ExtLogConfigRsp.Disable(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = ExtLogConfigRsp.GetMask(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = ExtLogConfigRsp.RetrieveIdRanges(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = ExtLogConfigRsp.SetMask(
                _io__raw_action, self, self._root
            )
            self.action._read()
        else:
            pass
            self.action = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
            pass
            self.action._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            self.action._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            self.action._fetch_instances()
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            self.action._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(ExtLogConfigRsp, self)._write__seq(io)
        self._io.write_u1(self.cmd_version)
        self._io.write_u1(int(self.operation))
        _on = self.operation
        if _on == diag_log_config_f_req.DiagLogConfigFReq.Operation.disable_op:
            pass
            _io__raw_action = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_action)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_action=_io__raw_action):
                self._raw_action = _io__raw_action.to_byte_array()
                parent.write_bytes(self._raw_action)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(action)', 0, parent.size() - parent.pos()
                    )

            _io__raw_action.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.action._write__seq(_io__raw_action)
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            _io__raw_action = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_action)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_action=_io__raw_action):
                self._raw_action = _io__raw_action.to_byte_array()
                parent.write_bytes(self._raw_action)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(action)', 0, parent.size() - parent.pos()
                    )

            _io__raw_action.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.action._write__seq(_io__raw_action)
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            _io__raw_action = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_action)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_action=_io__raw_action):
                self._raw_action = _io__raw_action.to_byte_array()
                parent.write_bytes(self._raw_action)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(action)', 0, parent.size() - parent.pos()
                    )

            _io__raw_action.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.action._write__seq(_io__raw_action)
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            _io__raw_action = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_action)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_action=_io__raw_action):
                self._raw_action = _io__raw_action.to_byte_array()
                parent.write_bytes(self._raw_action)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(action)', 0, parent.size() - parent.pos()
                    )

            _io__raw_action.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.action._write__seq(_io__raw_action)
        else:
            pass
            self._io.write_bytes(self.action)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'action', 0, self._io.size() - self._io.pos()
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
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.get_mask_op
        ):
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.retrieve_id_ranges_op
        ):
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif (
            _on
            == diag_log_config_f_req.DiagLogConfigFReq.Operation.set_mask_op
        ):
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        else:
            pass
        self._dirty = False

    class Disable(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigRsp.Disable, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = (
                ext_log_config_req.ExtLogConfigReq.StreamOrPresetId(self._io)
            )
            self.stream_or_preset_id._read()
            self.status = self._io.read_u8le()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.stream_or_preset_id._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigRsp.Disable, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_u8le(self.status)

        def _check(self):
            self._dirty = False

    class GetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigRsp.GetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = (
                ext_log_config_req.ExtLogConfigReq.StreamOrPresetId(self._io)
            )
            self.stream_or_preset_id._read()
            self.status = self._io.read_u8le()
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
            super(ExtLogConfigRsp.GetMask, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_u8le(self.status)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False

    class RetrieveIdRanges(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigRsp.RetrieveIdRanges, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.status = self._io.read_u8le()
            self.reserved = self._io.read_u8le()
            self.last_item = []
            for i in range(16):
                self.last_item.append(self._io.read_u4le())

            self._dirty = False

        def _fetch_instances(self):
            pass
            for i in range(len(self.last_item)):
                pass

        def _write__seq(self, io=None):
            super(ExtLogConfigRsp.RetrieveIdRanges, self)._write__seq(io)
            self._io.write_u8le(self.status)
            self._io.write_u8le(self.reserved)
            for i in range(len(self.last_item)):
                pass
                self._io.write_u4le(self.last_item[i])

        def _check(self):
            if len(self.last_item) != 16:
                raise kaitaistruct.ConsistencyError(
                    'last_item', 16, len(self.last_item)
                )
            for i in range(len(self.last_item)):
                pass

            self._dirty = False

    class RetrieveValidMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigRsp.RetrieveValidMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = diag_log_config_f_req.DiagLogConfigFReq.LogMask(
                self._io
            )
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(ExtLogConfigRsp.RetrieveValidMask, self)._write__seq(io)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False

    class SetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(ExtLogConfigRsp.SetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.stream_or_preset_id = (
                ext_log_config_req.ExtLogConfigReq.StreamOrPresetId(self._io)
            )
            self.stream_or_preset_id._read()
            self.status = self._io.read_u8le()
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
            super(ExtLogConfigRsp.SetMask, self)._write__seq(io)
            self.stream_or_preset_id._write__seq(self._io)
            self._io.write_u8le(self.status)
            self.log_mask._write__seq(self._io)

        def _check(self):
            self._dirty = False
