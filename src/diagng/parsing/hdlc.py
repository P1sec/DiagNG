#!/usr/bin/env python3

"""
WIP 2026-07-03

QCDM pseudo-HDLC muxer/demuxer

- COMMAND CODE: 1 byte: command code
- PAYLOAD: n bytes: packet payload (which escapes: 0x7d -> 0x7d 0x5d, 0x7e -> 0x7d 0x5e)
- CHECKSUM: 2 bytes (⚠️ can be escaped too): CCITT CRC-16 checksum (with Python: `crcmod.mkCrcFun(0x11021, initCrc=0, xorOut=0xffff)`)
- TRAILER: 1 byte: 0x7e
"""

from crcmod import mkCrcFun

CRC16_CCITT = mkCrcFun(0x11021, initCrc=0, xorOut=0xFFFF)


class BadTrailerException(ValueError):
    pass


class InvalidCRCException(ValueError):
    pass


TRAILER_CHAR = b'\x7e'


def hdlc_encode(data: bytes) -> bytes:
    data += CRC16_CCITT(data).to_bytes(2, 'little')
    data = data.replace(b'\x7d', b'\x7d\x5d')
    data = data.replace(b'\x7e', b'\x7d\x5e')
    return data + TRAILER_CHAR


def hdlc_decode(data: bytes) -> bytes:
    assert data.endswith(TRAILER_CHAR)
    assert data.count(TRAILER_CHAR) == 1
    data = data.replace(b'\x7d\x5e', b'\x7e')
    data = data.replace(b'\x7d\x5d', b'\x7d')
    assert len(data) >= 4
    crc = CRC16_CCITT(data[:-3]).to_bytes(2, 'little')
    assert data[-3:-1] == crc
    return data[:-3]


class HdlcDecoder:
    def decode(self, data: bytes):
        return hdlc_decode(data)
