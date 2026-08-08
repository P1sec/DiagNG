#!/usr/bin/env python3

from kaitaistruct import ReadWriteKaitaiStruct


def pretty_print_struct(struct: ReadWriteKaitaiStruct, indent: int = 0) -> str:
    output = ''
    for key, value in vars(struct).items():
        if not key.startswith('_'):
            output += ' ' * indent
            pretty_value = repr(value).replace('<diagng.protocol.', '<', 1)
            output += f'{key}: {pretty_value}\n'
            if isinstance(value, ReadWriteKaitaiStruct):
                output += pretty_print_struct(value, indent + 2)

    return output
