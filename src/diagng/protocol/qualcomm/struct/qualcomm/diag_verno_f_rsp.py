# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagVernoFRsp(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagVernoFRsp, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.compile_date = (
            KaitaiStream.bytes_terminate(
                KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32),
                0,
                False,
            )
        ).decode('ASCII')
        self.compile_time = (
            KaitaiStream.bytes_terminate(
                KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32),
                0,
                False,
            )
        ).decode('ASCII')
        self.release_date = (
            KaitaiStream.bytes_terminate(
                KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32),
                0,
                False,
            )
        ).decode('ASCII')
        self.release_time = (
            KaitaiStream.bytes_terminate(
                KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32),
                0,
                False,
            )
        ).decode('ASCII')
        self.version_directory = (
            KaitaiStream.bytes_terminate(
                KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32),
                0,
                False,
            )
        ).decode('ASCII')
        self.station_class_mark = self._io.read_u1()
        self.mobile_cai_revision = self._io.read_u1()
        self.mobile_model = self._io.read_u1()
        self.mobile_firmware_revision = self._io.read_u1()
        self.slot_cycle_index = self._io.read_u2le()
        self.hardware_major_version = self._io.read_u1()
        self.hardware_minor_version = self._io.read_u1()
        self._dirty = False

    def _fetch_instances(self):
        pass

    def _write__seq(self, io=None):
        super(DiagVernoFRsp, self)._write__seq(io)
        self._io.write_bytes_limit(
            (self.compile_date).encode('ASCII'), 11, 0, 32
        )
        self._io.write_bytes_limit(
            (self.compile_time).encode('ASCII'), 8, 0, 32
        )
        self._io.write_bytes_limit(
            (self.release_date).encode('ASCII'), 11, 0, 32
        )
        self._io.write_bytes_limit(
            (self.release_time).encode('ASCII'), 8, 0, 32
        )
        self._io.write_bytes_limit(
            (self.version_directory).encode('ASCII'), 8, 0, 32
        )
        self._io.write_u1(self.station_class_mark)
        self._io.write_u1(self.mobile_cai_revision)
        self._io.write_u1(self.mobile_model)
        self._io.write_u1(self.mobile_firmware_revision)
        self._io.write_u2le(self.slot_cycle_index)
        self._io.write_u1(self.hardware_major_version)
        self._io.write_u1(self.hardware_minor_version)

    def _check(self):
        if len((self.compile_date).encode('ASCII')) > 11:
            raise kaitaistruct.ConsistencyError(
                'compile_date', 11, len((self.compile_date).encode('ASCII'))
            )
        if (
            KaitaiStream.byte_array_index_of(
                (self.compile_date).encode('ASCII'), 0
            )
            != -1
        ):
            raise kaitaistruct.ConsistencyError(
                'compile_date',
                -1,
                KaitaiStream.byte_array_index_of(
                    (self.compile_date).encode('ASCII'), 0
                ),
            )
        if len((self.compile_date).encode('ASCII')) == 11:
            pass
            if (len((self.compile_date).encode('ASCII')) != 0) and (
                KaitaiStream.byte_array_index(
                    (self.compile_date).encode('ASCII'), -1
                )
                == 32
            ):
                raise kaitaistruct.ConsistencyError(
                    'compile_date',
                    32,
                    KaitaiStream.byte_array_index(
                        (self.compile_date).encode('ASCII'), -1
                    ),
                )

        if len((self.compile_time).encode('ASCII')) > 8:
            raise kaitaistruct.ConsistencyError(
                'compile_time', 8, len((self.compile_time).encode('ASCII'))
            )
        if (
            KaitaiStream.byte_array_index_of(
                (self.compile_time).encode('ASCII'), 0
            )
            != -1
        ):
            raise kaitaistruct.ConsistencyError(
                'compile_time',
                -1,
                KaitaiStream.byte_array_index_of(
                    (self.compile_time).encode('ASCII'), 0
                ),
            )
        if len((self.compile_time).encode('ASCII')) == 8:
            pass
            if (len((self.compile_time).encode('ASCII')) != 0) and (
                KaitaiStream.byte_array_index(
                    (self.compile_time).encode('ASCII'), -1
                )
                == 32
            ):
                raise kaitaistruct.ConsistencyError(
                    'compile_time',
                    32,
                    KaitaiStream.byte_array_index(
                        (self.compile_time).encode('ASCII'), -1
                    ),
                )

        if len((self.release_date).encode('ASCII')) > 11:
            raise kaitaistruct.ConsistencyError(
                'release_date', 11, len((self.release_date).encode('ASCII'))
            )
        if (
            KaitaiStream.byte_array_index_of(
                (self.release_date).encode('ASCII'), 0
            )
            != -1
        ):
            raise kaitaistruct.ConsistencyError(
                'release_date',
                -1,
                KaitaiStream.byte_array_index_of(
                    (self.release_date).encode('ASCII'), 0
                ),
            )
        if len((self.release_date).encode('ASCII')) == 11:
            pass
            if (len((self.release_date).encode('ASCII')) != 0) and (
                KaitaiStream.byte_array_index(
                    (self.release_date).encode('ASCII'), -1
                )
                == 32
            ):
                raise kaitaistruct.ConsistencyError(
                    'release_date',
                    32,
                    KaitaiStream.byte_array_index(
                        (self.release_date).encode('ASCII'), -1
                    ),
                )

        if len((self.release_time).encode('ASCII')) > 8:
            raise kaitaistruct.ConsistencyError(
                'release_time', 8, len((self.release_time).encode('ASCII'))
            )
        if (
            KaitaiStream.byte_array_index_of(
                (self.release_time).encode('ASCII'), 0
            )
            != -1
        ):
            raise kaitaistruct.ConsistencyError(
                'release_time',
                -1,
                KaitaiStream.byte_array_index_of(
                    (self.release_time).encode('ASCII'), 0
                ),
            )
        if len((self.release_time).encode('ASCII')) == 8:
            pass
            if (len((self.release_time).encode('ASCII')) != 0) and (
                KaitaiStream.byte_array_index(
                    (self.release_time).encode('ASCII'), -1
                )
                == 32
            ):
                raise kaitaistruct.ConsistencyError(
                    'release_time',
                    32,
                    KaitaiStream.byte_array_index(
                        (self.release_time).encode('ASCII'), -1
                    ),
                )

        if len((self.version_directory).encode('ASCII')) > 8:
            raise kaitaistruct.ConsistencyError(
                'version_directory',
                8,
                len((self.version_directory).encode('ASCII')),
            )
        if (
            KaitaiStream.byte_array_index_of(
                (self.version_directory).encode('ASCII'), 0
            )
            != -1
        ):
            raise kaitaistruct.ConsistencyError(
                'version_directory',
                -1,
                KaitaiStream.byte_array_index_of(
                    (self.version_directory).encode('ASCII'), 0
                ),
            )
        if len((self.version_directory).encode('ASCII')) == 8:
            pass
            if (len((self.version_directory).encode('ASCII')) != 0) and (
                KaitaiStream.byte_array_index(
                    (self.version_directory).encode('ASCII'), -1
                )
                == 32
            ):
                raise kaitaistruct.ConsistencyError(
                    'version_directory',
                    32,
                    KaitaiStream.byte_array_index(
                        (self.version_directory).encode('ASCII'), -1
                    ),
                )

        self._dirty = False
