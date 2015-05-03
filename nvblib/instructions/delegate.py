__author__ = 'XertroV'

from pycoin.encoding import a2b_base58

from . import Instruction, validate_address, validate_prefix, OP_DELEGATE

from ..constants import ENDIAN

class DelegateVote(Instruction):
    """PREFIX[3] OP_DELEGATE[1] categories[1] address_bytes[25]
    numbers in [] indicate # bytes"""
    OP_CODE = OP_DELEGATE

    def __init__(self, address, categories):
        super().__init__()
        self.address = address if type(address) == bytes else a2b_base58(address)
        self.categories = int(categories).to_bytes(1, ENDIAN)
        self._extra_bytes = self.categories + self.address

        validate_address(self.address)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        categories = bs[4]
        address = bs[5:]
        return cls(address, categories)


