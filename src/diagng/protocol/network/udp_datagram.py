# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.network import gsmtap


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class UdpDatagram(ReadWriteKaitaiStruct):
    """UDP is a simple stateless transport layer (AKA OSI layer 4)
    protocol, one of the core Internet protocols. It provides source and
    destination ports, basic checksumming, but provides not guarantees
    of delivery, order of packets, or duplicate delivery.
    """

    def __init__(self, _io=None, _parent=None, _root=None):
        super(UdpDatagram, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.src_port = self._io.read_u2be()
        self.dst_port = self._io.read_u2be()
        self.length = self._io.read_u2be()
        self.checksum = self._io.read_u2be()
        _on = self.dst_port
        if _on == 4729:
            pass
            self._raw_body = self._io.read_bytes(self.length - 8)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = gsmtap.Gsmtap(_io__raw_body)
            self.body._read()
        else:
            pass
            self.body = self._io.read_bytes(self.length - 8)
        self._dirty = False

    def _fetch_instances(self):
        pass
        _on = self.dst_port
        if _on == 4729:
            pass
            self.body._fetch_instances()
        else:
            pass

    def _write__seq(self, io=None):
        super(UdpDatagram, self)._write__seq(io)
        self._io.write_u2be(self.src_port)
        self._io.write_u2be(self.dst_port)
        self._io.write_u2be(self.length)
        self._io.write_u2be(self.checksum)
        _on = self.dst_port
        if _on == 4729:
            pass
            _io__raw_body = KaitaiStream(BytesIO(bytearray(self.length - 8)))
            self._io.add_child_stream(_io__raw_body)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.length - 8))

            def handler(parent, _io__raw_body=_io__raw_body):
                self._raw_body = _io__raw_body.to_byte_array()
                if len(self._raw_body) != self.length - 8:
                    raise kaitaistruct.ConsistencyError(
                        'raw(body)', self.length - 8, len(self._raw_body)
                    )
                parent.write_bytes(self._raw_body)

            _io__raw_body.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.body._write__seq(_io__raw_body)
        else:
            pass
            self._io.write_bytes(self.body)

    def _check(self):
        _on = self.dst_port
        if _on == 4729:
            pass
        else:
            pass
            if len(self.body) != self.length - 8:
                raise kaitaistruct.ConsistencyError(
                    'body', self.length - 8, len(self.body)
                )
        self._dirty = False
