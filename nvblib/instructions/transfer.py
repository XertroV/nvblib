__author__ = 'xertrov'

from pycoin.encoding import a2b_base58

from . import Instruction, OP_TRANSFER, validate_address

from ..constants import ENDIAN


class ModResolution(Instruction):
    """PREFIX[3] OP_TRANSFER[1] address[25]"""
    OP_CODE = OP_TRANSFER

    def __init__(self, address):
        super().__init__()
        self.address = address if type(address) is bytes else a2b_base58(address)

        self._extra_bytes = self.address

        validate_address(self.address)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        return cls(bs[4:])