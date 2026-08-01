# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from diagng.protocol.qualcomm.struct import gsm_rr_signaling_message
from diagng.protocol.qualcomm.struct import wcdma_signaling_message
from diagng.protocol.qualcomm.struct import diag_logging
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception(
        'Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s'
        % (kaitaistruct.__version__)
    )


class DiagLogF(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        super(DiagLogF, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.pending_msgs = self._io.read_u1()
        self.log_outer_length = self._io.read_u2le()
        self.inner_log = DiagLogF.InnerLog(self._io, self, self._root)
        self.inner_log._read()
        self._dirty = False

    def _fetch_instances(self):
        pass
        self.inner_log._fetch_instances()

    def _write__seq(self, io=None):
        super(DiagLogF, self)._write__seq(io)
        self._io.write_u1(self.pending_msgs)
        self._io.write_u2le(self.log_outer_length)
        self.inner_log._write__seq(self._io)

    def _check(self):
        if self.inner_log._root != self._root:
            raise kaitaistruct.ConsistencyError(
                'inner_log', self._root, self.inner_log._root
            )
        if self.inner_log._parent != self:
            raise kaitaistruct.ConsistencyError(
                'inner_log', self, self.inner_log._parent
            )
        self._dirty = False

    class InnerLog(ReadWriteKaitaiStruct):
        class RefTs(IntEnum):
            epoch_1980 = 315964800
            min_ts_unix = 946681200
            max_ts_unix = 4102441200
            min_ts_16bitmantissa = 33067703992320000
            max_ts_16bitmantissa = 198520413880320000

        def __init__(self, _io=None, _parent=None, _root=None):
            super(DiagLogF.InnerLog, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.log_inner_length = self._io.read_u2le()
            self.log_code = KaitaiStream.resolve_enum(
                diag_logging.DiagLogging.LogCode, self._io.read_u2le()
            )
            self.log_time = self._io.read_u8le()
            _on = self.log_code
            if (
                _on
                == diag_logging.DiagLogging.LogCode.gsm_rr_signaling_message
            ):
                pass
                self._raw_content = self._io.read_bytes(
                    self.log_inner_length - 12
                )
                _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
                self.content = gsm_rr_signaling_message.GsmRrSignalingMessage(
                    _io__raw_content
                )
                self.content._read()
            elif (
                _on == diag_logging.DiagLogging.LogCode.wcdma_signaling_message
            ):
                pass
                self._raw_content = self._io.read_bytes(
                    self.log_inner_length - 12
                )
                _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
                self.content = wcdma_signaling_message.WcdmaSignalingMessage(
                    _io__raw_content
                )
                self.content._read()
            else:
                pass
                self.content = self._io.read_bytes(self.log_inner_length - 12)
            self._dirty = False

        def _fetch_instances(self):
            pass
            _on = self.log_code
            if (
                _on
                == diag_logging.DiagLogging.LogCode.gsm_rr_signaling_message
            ):
                pass
                self.content._fetch_instances()
            elif (
                _on == diag_logging.DiagLogging.LogCode.wcdma_signaling_message
            ):
                pass
                self.content._fetch_instances()
            else:
                pass

        def _write__seq(self, io=None):
            super(DiagLogF.InnerLog, self)._write__seq(io)
            self._io.write_u2le(self.log_inner_length)
            self._io.write_u2le(int(self.log_code))
            self._io.write_u8le(self.log_time)
            _on = self.log_code
            if (
                _on
                == diag_logging.DiagLogging.LogCode.gsm_rr_signaling_message
            ):
                pass
                _io__raw_content = KaitaiStream(
                    BytesIO(bytearray(self.log_inner_length - 12))
                )
                self._io.add_child_stream(_io__raw_content)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.log_inner_length - 12))

                def handler(parent, _io__raw_content=_io__raw_content):
                    self._raw_content = _io__raw_content.to_byte_array()
                    if len(self._raw_content) != self.log_inner_length - 12:
                        raise kaitaistruct.ConsistencyError(
                            'raw(content)',
                            self.log_inner_length - 12,
                            len(self._raw_content),
                        )
                    parent.write_bytes(self._raw_content)

                _io__raw_content.write_back_handler = (
                    KaitaiStream.WriteBackHandler(_pos2, handler)
                )
                self.content._write__seq(_io__raw_content)
            elif (
                _on == diag_logging.DiagLogging.LogCode.wcdma_signaling_message
            ):
                pass
                _io__raw_content = KaitaiStream(
                    BytesIO(bytearray(self.log_inner_length - 12))
                )
                self._io.add_child_stream(_io__raw_content)
                _pos2 = self._io.pos()
                self._io.seek(self._io.pos() + (self.log_inner_length - 12))

                def handler(parent, _io__raw_content=_io__raw_content):
                    self._raw_content = _io__raw_content.to_byte_array()
                    if len(self._raw_content) != self.log_inner_length - 12:
                        raise kaitaistruct.ConsistencyError(
                            'raw(content)',
                            self.log_inner_length - 12,
                            len(self._raw_content),
                        )
                    parent.write_bytes(self._raw_content)

                _io__raw_content.write_back_handler = (
                    KaitaiStream.WriteBackHandler(_pos2, handler)
                )
                self.content._write__seq(_io__raw_content)
            else:
                pass
                self._io.write_bytes(self.content)

        def _check(self):
            _on = self.log_code
            if (
                _on
                == diag_logging.DiagLogging.LogCode.gsm_rr_signaling_message
            ):
                pass
            elif (
                _on == diag_logging.DiagLogging.LogCode.wcdma_signaling_message
            ):
                pass
            else:
                pass
                if len(self.content) != self.log_inner_length - 12:
                    raise kaitaistruct.ConsistencyError(
                        'content',
                        self.log_inner_length - 12,
                        len(self.content),
                    )
            self._dirty = False

        @property
        def unix_ts(self):
            if hasattr(self, '_m_unix_ts'):
                return self._m_unix_ts

            self._m_unix_ts = (
                self.log_time
                if (
                    (self.log_time > 946681200)
                    and (self.log_time < 4102441200)
                )
                else (315964800 + (self.log_time >> 16) // 800)
                + ((self.log_time & 65535) // 49152) // 800
            )
            return getattr(self, '_m_unix_ts', None)

        def _invalidate_unix_ts(self):
            del self._m_unix_ts
