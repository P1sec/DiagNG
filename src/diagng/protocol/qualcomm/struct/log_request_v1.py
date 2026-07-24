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


class LogRequestV1(ReadWriteKaitaiStruct):
    class Operation(IntEnum):
        disable_op = 0
        retrieve_id_ranges_op = 1
        retrieve_valid_mask_op = 2
        set_mask_op = 3
        get_mask_op = 4

    def __init__(self, _io=None, _parent=None, _root=None):
        super(LogRequestV1, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(LogRequestV1, self)._write__seq(io)

    def _check(self):
        self._dirty = False

    class Disable(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.Disable, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LogRequestV1.Disable, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class GetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.GetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LogRequestV1.GetMask, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class LogMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.LogMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.equipment_id = KaitaiStream.resolve_enum(
                diag_logging.DiagLogging.EquipmentId, self._io.read_u4le()
            )
            self.num_logs_on_bit_field = self._io.read_u4le()
            self.logs_on_bit_field = []
            for i in range(self.num_logs_on_bit_field):
                self.logs_on_bit_field.append(
                    self._io.read_bits_int_le(1) != 0
                )

            self._dirty = False

        def _fetch_instances(self):
            pass
            for i in range(len(self.logs_on_bit_field)):
                pass

        def _write__seq(self, io=None):
            super(LogRequestV1.LogMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))
            self._io.write_u4le(self.num_logs_on_bit_field)
            for i in range(len(self.logs_on_bit_field)):
                pass
                self._io.write_bits_int_le(1, int(self.logs_on_bit_field[i]))

        def _check(self):
            if len(self.logs_on_bit_field) != self.num_logs_on_bit_field:
                raise kaitaistruct.ConsistencyError(
                    'logs_on_bit_field',
                    self.num_logs_on_bit_field,
                    len(self.logs_on_bit_field),
                )
            for i in range(len(self.logs_on_bit_field)):
                pass

            self._dirty = False

    class RetrieveIdRanges(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.RetrieveIdRanges, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass
            self._dirty = False

        def _fetch_instances(self):
            pass

        def _write__seq(self, io=None):
            super(LogRequestV1.RetrieveIdRanges, self)._write__seq(io)

        def _check(self):
            self._dirty = False

    class RetrieveValidMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.RetrieveValidMask, self).__init__(_io)
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
            super(LogRequestV1.RetrieveValidMask, self)._write__seq(io)
            self._io.write_u4le(int(self.equipment_id))

        def _check(self):
            self._dirty = False

    class SetMask(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(LogRequestV1.SetMask, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_mask = LogRequestV1.LogMask(self._io, self, self._root)
            self.log_mask._read()
            self._dirty = False

        def _fetch_instances(self):
            pass
            self.log_mask._fetch_instances()

        def _write__seq(self, io=None):
            super(LogRequestV1.SetMask, self)._write__seq(io)
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
