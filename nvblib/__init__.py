__author__ = 'XertroV'

from .instructions.create import CreateNetwork
from .instructions.cast import CastVote
from .instructions.delegate import DelegateVote
from .instructions.empower import EmpowerVote
from .instructions.mod_res import ModResolution
from .instructions.comment import CommentNulldata

instruction_map = {
    'create': CreateNetwork,
    'cast': CastVote,
    'delegate': DelegateVote,
    'mod_res': ModResolution,
    'empower': EmpowerVote,
    'comment': CommentNulldata,
}

def instruction_lookup(i):
    return instruction_map.get(i)