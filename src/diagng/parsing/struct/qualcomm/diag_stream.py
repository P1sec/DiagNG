# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from diagng.parsing.struct.qualcomm import diag_response
import diagng.parsing.hdlc


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagStream(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(DiagStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self._raw_frames = []
        self._raw__raw_frames = []
        self.frames = []
        i = 0
        while not self._io.is_eof():
            self._raw__raw_frames.append(
                self._io.read_bytes_term(126, True, True, True)
            )
            _process = diagng.parsing.hdlc.HdlcDecoder()
            self._raw_frames.append(_process.decode(self._raw__raw_frames[-1]))
            _io__raw_frames = KaitaiStream(BytesIO(self._raw_frames[-1]))
            self.frames.append(diag_response.DiagResponse(_io__raw_frames))
            i += 1

    def _fetch_instances(self):
        pass
        for i in range(len(self.frames)):
            pass
            self.frames[i]._fetch_instances()
