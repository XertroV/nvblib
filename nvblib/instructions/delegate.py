__author__ = 'XertroV'

from pycoin.encoding import a2b_base58

from . import Instruction, validate_address, OP_DELEGATE, _to_bytes

from ..constants import ENDIAN

class DelegateVote(Instruction):
    """PREFIX[3] OP_DELEGATE[1] categories[1] address_bytes[25]
    numbers in [] indicate # bytes"""
    OP_CODE = OP_DELEGATE

    def __init__(self, address, categories):
        super().__init__()
        self.address = _to_bytes(lambda a: a2b_base58(a), address)
        self.categories = _to_bytes(lambda c: int(c).to_bytes(1, ENDIAN), categories)
        self._extra_bytes = self.categories + self.address

        validate_address(self.address)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        categories = bs[4]
        address = bs[5:]
        return cls(address, categories)


