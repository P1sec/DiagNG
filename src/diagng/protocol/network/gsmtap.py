# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.network import gsmtap_v2
from diagng.protocol.network import gsmtap_v3


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class Gsmtap(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Gsmtap, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.version = self._io.read_u1()
        if not self.version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.version, self._io, '/seq/0'
            )
        if not self.version <= 3:
            raise kaitaistruct.ValidationGreaterThanError(
                3, self.version, self._io, '/seq/0'
            )
        _on = self.version
        if _on == 2:
            pass
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = gsmtap_v2.GsmtapV2(_io__raw_content)
            self.content._read()
        elif _on == 3:
            pass
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = gsmtap_v3.GsmtapV3(_io__raw_content)
            self.content._read()
        else:
            pass
            self.content = self._io.read_bytes_full()
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.version
        if _on == 2:
            pass
            self.content._fetch_instances()
        elif _on == 3:
            pass
            self.content._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(Gsmtap, self)._write__seq(io)
        self._io.write_u1(self.version)
        _on = self.version
        if _on == 2:
            pass
            _io__raw_content = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_content)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_content=_io__raw_content):
                self._raw_content = _io__raw_content.to_byte_array()
                parent.write_bytes(self._raw_content)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(content)', 0, parent.size() - parent.pos()
                    )

            _io__raw_content.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.content._write__seq(_io__raw_content)
        elif _on == 3:
            pass
            _io__raw_content = KaitaiStream(
                BytesIO(bytearray(self._io.size() - self._io.pos()))
            )
            self._io.add_child_stream(_io__raw_content)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self._io.size() - self._io.pos()))

            def handler(parent, _io__raw_content=_io__raw_content):
                self._raw_content = _io__raw_content.to_byte_array()
                parent.write_bytes(self._raw_content)
                if not parent.is_eof():
                    raise kaitaistruct.ConsistencyError(
                        'raw(content)', 0, parent.size() - parent.pos()
                    )

            _io__raw_content.write_back_handler = (
                KaitaiStream.WriteBackHandler(_pos2, handler)
            )
            self.content._write__seq(_io__raw_content)
        else:
            pass
            self._io.write_bytes(self.content)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'content', 0, self._io.size() - self._io.pos()
                )

    def _check(self):
        if not self.version >= 1:
            raise kaitaistruct.ValidationLessThanError(
                1, self.version, None, '/seq/0'
            )
        if not self.version <= 3:
            raise kaitaistruct.ValidationGreaterThanError(
                3, self.version, None, '/seq/0'
            )
        _on = self.version
        if _on == 2:
            pass
        elif _on == 3:
            pass
        else:
            pass
        self._dirty = False
