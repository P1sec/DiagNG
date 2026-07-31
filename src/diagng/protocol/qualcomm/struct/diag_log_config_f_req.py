# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import diag_logging
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagLogConfigFReq(ReadWriteKaitaiStruct):
    class Operation(IntEnum):
        disable_op = 0
        retrieve_id_ranges_op = 1
        retrieve_valid_mask_op = 2
        set_mask_op = 3
        get_mask_op = 4

    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagLogConfigFReq, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.padding = KaitaiStream.bytes_strip_right(
            self._io.read_bytes(3), 0
        )
        self.operation = KaitaiStream.resolve_enum(
            DiagLogConfigFReq.Operation, self._io.read_u4le()
        )
        _on = self.operation
        if _on == DiagLogConfigFReq.Operation.disable_op:
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = DiagLogConfigFReq.Disable(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif _on == DiagLogConfigFReq.Operation.get_mask_op:
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = DiagLogConfigFReq.GetMask(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif _on == DiagLogConfigFReq.Operation.retrieve_id_ranges_op:
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = DiagLogConfigFReq.RetrieveIdRanges(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif _on == DiagLogConfigFReq.Operation.retrieve_valid_mask_op:
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = DiagLogConfigFReq.RetrieveValidMask(
                _io__raw_action, self, self._root
            )
            self.action._read()
        elif _on == DiagLogConfigFReq.Operation.set_mask_op:
            pass
            self._raw_action = self._io.read_bytes_full()
            _io__raw_action = KaitaiStream(BytesIO(self._raw_action))
            self.action = DiagLogConfigFReq.SetMask(
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
        if _on == DiagLogConfigFReq.Operation.disable_op:
            pass
            self.action._fetch_instances()
        elif _on == DiagLogConfigFReq.Operation.get_mask_op:
            pass
            self.action._fetch_instances()
        elif _on == DiagLogConfigFReq.Operation.retrieve_id_ranges_op:
            pass
            self.action._fetch_instances()
        elif _on == DiagLogConfigFReq.Operation.retrieve_valid_mask_op:
            pass
            self.action._fetch_instances()
        elif _on == DiagLogConfigFReq.Operation.set_mask_op:
            pass
            self.action._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(DiagLogConfigFReq, self)._write__seq(io)
        self._io.write_bytes_limit(self.padding, 3, 0, 0)
        self._io.write_u4le(int(self.operation))
        _on = self.operation
        if _on == DiagLogConfigFReq.Operation.disable_op:
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
        elif _on == DiagLogConfigFReq.Operation.get_mask_op:
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
        elif _on == DiagLogConfigFReq.Operation.retrieve_id_ranges_op:
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
        elif _on == DiagLogConfigFReq.Operation.retrieve_valid_mask_op:
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
        elif _on == DiagLogConfigFReq.Operation.set_mask_op:
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
        if len(self.padding) > 3:
            raise kaitaistruct.ConsistencyError(
                'padding', 3, len(self.padding)
            )
        if (len(self.padding) != 0) and (
            KaitaiStream.byte_array_index(self.padding, -1) == 0
        ):
            raise kaitaistruct.ConsistencyError(
                'padding', 0, KaitaiStream.byte_array_index(self.padding, -1)
            )
        _on = self.operation
        if _on == DiagLogConfigFReq.Operation.disable_op:
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif _on == DiagLogConfigFReq.Operation.get_mask_op:
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif _on == DiagLogConfigFReq.Operation.retrieve_id_ranges_op:
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif _on == DiagLogConfigFReq.Operation.retrieve_valid_mask_op:
            pass
            if self.action._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'action', self._root, self.action._root
                )
            if self.action._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'action', self, self.action._parent
                )
        elif _on == DiagLogConfigFReq.Operation.set_mask_op:
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
            super(DiagLogConfigFReq.Disable, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(DiagLogConfigFReq.Disable, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class GetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogConfigFReq.GetMask, self).__init__(_io)
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
            super(DiagLogConfigFReq.GetMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))

        def _check(self):
            self._dirty = False

    class LogMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogConfigFReq.LogMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.equipment_id = KaitaiStream.resolve_enum(
                diag_logging.DiagLogging.EquipmentId, self._io.read_u4le()
            )
            self.num_logs_on_bitfield = self._io.read_u4le()
            self.logs_on_bitfield = []
            for i in range(self.num_logs_on_bitfield):
                self.logs_on_bitfield.append(self._io.read_bits_int_le(1) != 0)

            self._dirty = False

        def _fetch_instances(self):
            pass
            for i in range(len(self.logs_on_bitfield)):
                pass

        def _write__seq(self, io=None):
            super(DiagLogConfigFReq.LogMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))
            self._io.write_u4le(self.num_logs_on_bitfield)
            for i in range(len(self.logs_on_bitfield)):
                pass
                self._io.write_bits_int_le(1, int(self.logs_on_bitfield[i]))

        def _check(self):
            if len(self.logs_on_bitfield) != self.num_logs_on_bitfield:
                raise kaitaistruct.ConsistencyError(
                    'logs_on_bitfield',
                    self.num_logs_on_bitfield,
                    len(self.logs_on_bitfield),
                )
            for i in range(len(self.logs_on_bitfield)):
                pass

            self._dirty = False

    class RetrieveIdRanges(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogConfigFReq.RetrieveIdRanges, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(DiagLogConfigFReq.RetrieveIdRanges, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class RetrieveValidMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogConfigFReq.RetrieveValidMask, self).__init__(_io)
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
            super(DiagLogConfigFReq.RetrieveValidMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))

        def _check(self):
            self._dirty = False

    class SetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogConfigFReq.SetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = DiagLogConfigFReq.LogMask(
                self._io, self, self._root
            )
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(DiagLogConfigFReq.SetMask, self)._write__seq(io)
            self.log_mask._write__seq(self._io)

        def _check(self):
            if self.log_mask._root != self._root:
                raise kaitaistruct.ConsistencyError(
                    'log_mask', self._root, self.log_mask._root
                )
            if self.log_mask._parent != self:
                raise kaitaistruct.ConsistencyError(
                    'log_mask', self, self.log_mask._parent
                )
            self._dirty = False
