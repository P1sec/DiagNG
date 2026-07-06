# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.parsing.struct.qualcomm import diag_response
import diagng.parsing.hdlc


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagStream(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagStream, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self._raw_frames = []
        self.frames__inner_size = []
        self.frames__outer_size = []
        self._raw__raw_frames = []
        self.frames = []
        i = 0
        while not self._io.is_eof():
            self._raw__raw_frames.append(
                self._io.read_bytes_term(126, True, True, True)
            )
            _process = diagng.parsing.hdlc.HdlcDecoder()
            self._raw_frames.append(_process.decode(self._raw__raw_frames[-1]))
            self.frames__outer_size.append(len(self._raw__raw_frames[i]))
            self.frames__inner_size.append(len(self._raw_frames[i]))
            _io__raw_frames = KaitaiStream(BytesIO(self._raw_frames[-1]))
            _t_frames = diag_response.DiagResponse(_io__raw_frames)
            try:
                _t_frames._read()
            finally:
                self.frames.append(_t_frames)
            i += 1

        self._dirty = False

    def _fetch_instances(self):
        pass
        for i in range(len(self.frames)):
            pass
            self.frames[i]._fetch_instances()

    def _write__seq(self, io=None):
        super(DiagStream, self)._write__seq(io)
        self._raw_frames = []
        self._raw__raw_frames = []
        for i in range(len(self.frames)):
            pass
            if self._io.is_eof():
                raise kaitaistruct.ConsistencyError(
                    'frames', 0, self._io.size() - self._io.pos()
                )
            _io__raw_frames = KaitaiStream(
                BytesIO(bytearray(self.frames__inner_size[i]))
            )
            self._io.add_child_stream(_io__raw_frames)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.frames__outer_size[i]))
            _process_val = diagng.parsing.hdlc.HdlcDecoder()

            def handler(
                parent,
                _io__raw_frames=_io__raw_frames,
                i=i,
                _process_val=_process_val,
            ):
                self._raw_frames.append(_io__raw_frames.to_byte_array())
                self._raw__raw_frames.append(
                    _process_val.encode(self._raw_frames[i])
                )
                if len(self._raw__raw_frames[i]) == 0:
                    raise kaitaistruct.ConsistencyError(
                        'raw(frames)', 0, len(self._raw__raw_frames[i])
                    )
                if (
                    KaitaiStream.byte_array_index_of(
                        self._raw__raw_frames[i], 126
                    )
                    != len(self._raw__raw_frames[i]) - 1
                ):
                    raise kaitaistruct.ConsistencyError(
                        'raw(frames)',
                        len(self._raw__raw_frames[i]) - 1,
                        KaitaiStream.byte_array_index_of(
                            self._raw__raw_frames[i], 126
                        ),
                    )
                parent.write_bytes(self._raw__raw_frames[i])

            _io__raw_frames.write_back_handler = KaitaiStream.WriteBackHandler(
                _pos2, handler
            )
            self.frames[i]._write__seq(_io__raw_frames)

        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(
                'frames', 0, self._io.size() - self._io.pos()
            )

    def _check(self):
        for i in range(len(self.frames)):
            pass

        self._dirty = False
