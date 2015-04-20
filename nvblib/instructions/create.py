__author__ = 'XertroV'

from . import Instruction, OP_CREATE, validate_name, validate_prefix

class CreateNetwork(Instruction):
    """PREFIX[3] OP_CREATE[1] name[<30]"""

    def __init__(self, name):
        super().__init__()
        self.op_code = OP_CREATE
        self.name = bytes(name.encode() if type(name) is str else name)
        self._extra_bytes = self.name

        validate_name(self.name)

    @classmethod
    def from_bytes(cls, bs):
        validate_prefix(bs)
        assert bs[3] == OP_CREATE
        name = bs[4:]
        validate_name(name)
        return cls(name)