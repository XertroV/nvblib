__author__ = 'XertroV'

from .instructions.create import CreateNetwork
from .instructions.cast import CastVote
from .instructions.delegate import DelegateVote
from .instructions.empower import EmpowerVote
from .instructions.mod_res import ModResolution
from .instructions.comment import CommentNulldata
from .instructions import OP_TRANSFER, OP_DELEGATE, OP_CREATE, OP_CAST, OP_EMPOWER, OP_MOD_RES, OP_NULL

instruction_map = {
    'create': CreateNetwork,
    'cast': CastVote,
    'delegate': DelegateVote,
    'mod_res': ModResolution,
    'empower': EmpowerVote,
    'comment': CommentNulldata,
    'transfer': None,
}

op_code_map = {
    OP_CREATE: CreateNetwork,
    OP_CAST: CastVote,
    OP_DELEGATE: DelegateVote,
    OP_MOD_RES: ModResolution,
    OP_EMPOWER: EmpowerVote,
    OP_TRANSFER: None,
}

def instruction_lookup(instruction_str):
    return instruction_map.get(instruction_str)

def op_code_lookup(op_code_byte):
    return op_code_map[op_code_byte]

def get_op(script_bytes):
    return script_bytes[3]