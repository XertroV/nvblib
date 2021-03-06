__author__ = 'xertrov'

from pycoin.encoding import a2b_base58

from . import Instruction, OP_TRANSFER, OP_ENABLE_TFER, OP_DISABLE_TFER, validate_address

from ..constants import ENDIAN



class EnableTransfer(Instruction):
    """PREFIX[3] OP_ENABLE_TFER[1] address[25]"""
    OP_CODE = OP_ENABLE_TFER

    def __init__(self, address):
        super().__init__()
        self.address = address if type(address) is bytes else a2b_base58(address)

        self._extra_bytes = self.address
        self._args = [self.address]

        validate_address(self.address)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        return cls(bs[4:])


class TransferIdentity(Instruction):
    """PREFIX[3] OP_TRANSFER[1]"""
    OP_CODE = OP_TRANSFER

    def __init__(self):
        super().__init__()

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)  # technically we aren't validating the length here, do we need to?
        return cls()


class DisableTransfer(Instruction):
    """PREFIX[3] OP_DISABLE_TFER[1]"""
    OP_CODE = OP_DISABLE_TFER

    def __init__(self):
        super().__init__()

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)  # technically we aren't validating the length here, do we need to?
        return cls()