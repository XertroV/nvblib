__author__ = 'XertroV'

from ..constants import ENDIAN, MSG_PREFIX

OP_NULL = b'\x00'

OP_CREATE = b'\x01'
OP_MOD_RES = b'\x02'
OP_EMPOWER = b'\x03'

OP_CAST = b'\x10'
OP_DELEGATE = b'\x11'

OP_TRANSFER = b'\x20'


def validate_resolution(r):
    assert type(r) == bytes
    assert len(r) < 15


def validate_url(u):
    assert type(u) == bytes
    assert len(u) < 15


def validate_hash160(h):
    assert type(h) == bytes
    assert len(h) == 20


def validate_name(n):
    assert len(n) < 30
    assert type(n) == bytes


def validate_prefix(bs):
    assert bs[:3] == MSG_PREFIX


def validate_comment(c):
    assert type(c) == bytes
    assert len(c) <= 40


def len_to_one_byte(i):
    return len(i).to_bytes(1, ENDIAN)


class Instruction:
    PREFIX = MSG_PREFIX
    OP_CODE = OP_NULL

    def __init__(self):
        self.op_code = self.OP_CODE
        self._extra_bytes = b''

    def _encode_with_extra_bytes(self, *bs):
        return self.PREFIX + self.op_code + b''.join(bs)

    def to_bytes(self):
        return self.PREFIX + self.op_code + self._extra_bytes

    @classmethod
    def validate_header(cls, bs):
        validate_prefix(bs)
        assert bs[3] == cls.OP_CODE[0]

    @classmethod
    def from_bytes(cls, bs):
        raise NotImplemented