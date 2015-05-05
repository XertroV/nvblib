__author__ = 'XertroV'

from . import Instruction, OP_CAST, validate_resolution, _to_bytes

from ..constants import ENDIAN

class CastVote(Instruction):
    """PREFIX[3] OP_CAST[1] vote_number[1] resolution[<10]"""
    OP_CODE = OP_CAST

    def __init__(self, vote_number, resolution):
        super().__init__()
        self.vote_number = _to_bytes(lambda v: int(v).to_bytes(1, ENDIAN), vote_number)
        self.resolution = _to_bytes(lambda r: r.upper() if type(r) is bytes else r.upper().encode(), resolution)
        self._extra_bytes = self.vote_number + self.resolution
        self._args = [self.vote_number, self.resolution]

        validate_resolution(self.resolution)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        vote_number = bs[4]
        resolution = bs[5:]

        validate_resolution(resolution)

        return cls(vote_number, resolution)

