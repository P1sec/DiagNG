#!/usr/bin/env python3
from diagng.protocol.qualcomm.struct.dlf_file import DlfFile

from os.path import dirname, realpath
from kaitaistruct import KaitaiStream

SCRIPT_DIR = dirname(realpath(__file__))
INPUT_FILE = realpath(SCRIPT_DIR + '/dlf/barberaz_5g.dlf')

def test__parse_barberaz_5g_file():
    stream = KaitaiStream(open(INPUT_FILE, 'rb'))
    resp = DlfFile(stream)
    resp._read()
