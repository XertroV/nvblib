__author__ = 'XertroV'

from . import Instruction, OP_CAST, validate_resolution, validate_prefix

from ..constants import ENDIAN

class CastVote(Instruction):
    """PREFIX[3] OP_CAST[1] vote_number[1] resolution[<10]"""

    def __init__(self, vote_number, resolution):
        super().__init__()
        self.op_code = OP_CAST
        self.vote_number = int(vote_number).to_bytes(1, ENDIAN)
        self.resolution = bytes(resolution.upper().encode())
        self._extra_bytes = self.vote_number + self.resolution

        validate_resolution(self.resolution)

    @classmethod
    def from_bytes(cls, bs):
        validate_prefix(bs)