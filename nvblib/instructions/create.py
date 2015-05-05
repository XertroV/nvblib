__author__ = 'XertroV'

from . import Instruction, OP_CREATE, validate_name, _to_bytes

class CreateNetwork(Instruction):
    """PREFIX[3] OP_CREATE[1] name[<30]"""
    OP_CODE = OP_CREATE

    def __init__(self, name):
        super().__init__()
        self.name = _to_bytes(lambda n: n.encode(), name)
        self._extra_bytes = self.name
        self._args = [self.name]

        validate_name(self.name)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        name = bs[4:]
        validate_name(name)
        return cls(name)