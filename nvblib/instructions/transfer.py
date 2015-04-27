__author__ = 'xertrov'

from . import Instruction, OP_TRANSFER, validate_hash160

from ..constants import ENDIAN


class ModResolution(Instruction):
    """PREFIX[3] OP_TRANSFER[1] hash160[20]"""

    def __init__(self, hash160):
        super().__init__()
        self.op_code = OP_TRANSFER
        self.hash160 = hash160

        self._extra_bytes = self.hash160

        validate_hash160(self.hash160)