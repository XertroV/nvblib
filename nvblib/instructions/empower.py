__author__ = 'XertroV'

from pycoin.key import Key

from . import Instruction, OP_EMPOWER, validate_hash160

from ..constants import ENDIAN


class EmpowerVote(Instruction):
    """ PREFIX[3] OP_EMPOWER[1] votes[4] hash160[20]
    """
    OP_CODE = OP_EMPOWER

    def __init__(self, votes, address):
        super().__init__()
        self.hash160 = bytes(Key.from_text(address).hash160())
        self.votes = int(votes).to_bytes(4, ENDIAN)
        self._extra_bytes = self.votes + self.hash160

        validate_hash160(self.hash160)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        votes = int.from_bytes(bs[4:8], ENDIAN)
        address = bs[8:]
        return cls(votes, address)