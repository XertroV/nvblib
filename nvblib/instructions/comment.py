from . import Instruction, validate_comment

class CommentNulldata(Instruction):
    PREFIX = b''

    def __init__(self, comment):
        self.op_code = b''
        self.comment = comment.encode()
        self._extra_bytes = self.comment

        validate_comment(self.comment)
