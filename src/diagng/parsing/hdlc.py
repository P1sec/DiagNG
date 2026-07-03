#!/usr/bin/env python3

"""
    WIP 2026-07-03

    QCDM pseudo-HDLC muxer/demuxer

    - COMMAND CODE: 1 byte: command code
    - PAYLOAD: n bytes: packet payload (which escapes: 0x7d -> 0x7d 0x5d, 0x7e -> 0x7d 0x5e)
    - CHECKSUM: 2 bytes (⚠️ can be escaped too): CCITT CRC-16 checksum (with Python: `crcmod.mkCrcFun(0x11021, initCrc=0, xorOut=0xffff)`)
    - TRAILER: 1 byte: 0x7e
"""
