__author__ = 'xertrov'

import unittest
import random

from nvblib.instructions import cast, comment, create, delegate, empower, mod_res, transfer
from nvblib.constants import ENDIAN

class Tests(unittest.TestCase):

    def test_cast(self):
        vote_num = random.randint(0,255)
        r = b'RSLTN-1'
        test_bytes = b'NVB' + cast.CastVote.OP_CODE + vote_num.to_bytes(1, ENDIAN) + r
        v1 = cast.CastVote(vote_num, str(r))
        v2 = cast.CastVote.from_bytes(test_bytes)
        assert v1.resolution == v2.resolution
        assert v1.vote_number == v2.vote_number

        self.assertRaises(AssertionError, cast.CastVote.from_bytes, [b'\x00' + test_bytes])