__author__ = 'XertroV'

from pycoin.key import Key

from . import Instruction, validate_hash160, OP_DELEGATE

from ..constants import ENDIAN

class DelegateVote(Instruction):
    """PREFIX[3] OP_DELEGATE[1] categories[1] address[20]
    numbers in [] indicate # bytes"""

    def __init__(self, address, categories):
        super().__init__()
        self.op_code = OP_DELEGATE
        self.hash160 = bytes(Key.from_text(address).hash160())
        self.categories = int(categories).to_bytes(1, ENDIAN)
        self._extra_bytes = self.categories + self.hash160

        validate_hash160(self.hash160)