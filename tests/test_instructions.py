__author__ = 'xertrov'

import unittest
import random

from pycoin.encoding import a2b_base58

from nvblib.instructions import cast, comment, create, delegate, empower, mod_res, transfer
from nvblib.constants import ENDIAN

class Tests(unittest.TestCase):

    def test_cast(self):
        vote_num = random.randint(0,255)
        r = b'RSLTN-1'
        test_bytes = b'NVB' + cast.CastVote.OP_CODE + vote_num.to_bytes(1, ENDIAN) + r
        v1 = cast.CastVote(vote_num, r)
        v2 = cast.CastVote.from_bytes(test_bytes)
        assert v1.resolution == v2.resolution
        assert v1.vote_number == v2.vote_number

        self.assertRaises(AssertionError, cast.CastVote.from_bytes, [b'\x00' + test_bytes])

    def test_transfer(self):
        enable_transfer_encoded = b'NVB' + transfer.EnableTransfer.OP_CODE + b'\x00\x0c\x9b\nJ\xf3[\xc1(\x1a\xf3\xd5\x13z\x1c\x90\xdc\x11\x17\xb3\x10\x82y\xe0\xf3'
        assert enable_transfer_encoded == transfer.EnableTransfer(a2b_base58('129eqgh8CNi7LibSmJtbDEnZFTmKA6H3HU')).to_bytes()