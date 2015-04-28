__author__ = 'xertrov'

from . import Instruction, OP_TRANSFER, validate_hash160

from ..constants import ENDIAN


class ModResolution(Instruction):
    """PREFIX[3] OP_TRANSFER[1] hash160[20]"""
    OP_CODE = OP_TRANSFER

    def __init__(self, hash160):
        super().__init__()
        self.hash160 = hash160 if type(hash160) is bytes else hash160.encode()

        self._extra_bytes = self.hash160

        validate_hash160(self.hash160)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        return cls(bs[4:])