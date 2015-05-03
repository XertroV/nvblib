__author__ = 'XertroV'

from pycoin.encoding import a2b_base58

from . import Instruction, OP_EMPOWER, validate_address

from ..constants import ENDIAN


class EmpowerVote(Instruction):
    """ PREFIX[3] OP_EMPOWER[1] votes[4] address_bytes[25]
    """
    OP_CODE = OP_EMPOWER

    def __init__(self, votes, address):
        super().__init__()
        self.address = address if type(address) == bytes else a2b_base58(address)
        self.votes = int(votes).to_bytes(4, ENDIAN)
        self._extra_bytes = self.votes + self.address

        validate_address(self.address)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        votes = int.from_bytes(bs[4:8], ENDIAN)
        address = bs[8:]
        assert len(address) == 25
        return cls(votes, address)