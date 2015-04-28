__author__ = 'XertroV'

from . import Instruction, OP_CAST, validate_resolution

from ..constants import ENDIAN

class CastVote(Instruction):
    """PREFIX[3] OP_CAST[1] vote_number[1] resolution[<10]"""
    OP_CODE = OP_CAST

    def __init__(self, vote_number, resolution):
        super().__init__()
        self.vote_number = int(vote_number).to_bytes(1, ENDIAN)
        self.resolution = resolution.upper() if type(resolution) is bytes else resolution.upper().encode()
        self._extra_bytes = self.vote_number + self.resolution

        validate_resolution(self.resolution)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        vote_number = bs[4]
        resolution = bs[5:]

        validate_resolution(resolution)

        return cls(vote_number, str(resolution))

