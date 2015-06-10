__author__ = 'XertroV'

from pycoin.key import Key
from pycoin.encoding import b2a_base58, a2b_hashed_base58

from ..constants import ENDIAN, MSG_PREFIX

OP_NULL = b'\x00'

OP_CREATE = b'\x01'
OP_MOD_RES = b'\x02'
OP_EMPOWER = b'\x03'

OP_CAST = b'\x10'
OP_DELEGATE = b'\x11'

OP_TRANSFER = b'\x20'
OP_ENABLE_TFER = b'\x21'
OP_DISABLE_TFER = b'\x22'

op_str_map = {
    OP_NULL: 'OP_NULL',
    OP_CREATE: 'OP_CREATE',
    OP_MOD_RES: 'OP_MOD_RES',
    OP_EMPOWER: 'OP_EMPOWER',
    OP_CAST: 'OP_CAST',
    OP_DELEGATE: 'OP_DELEGATE',
    OP_TRANSFER: 'OP_TRANSFER',
    OP_ENABLE_TFER: 'OP_ENABLE_TFER',
    OP_DISABLE_TFER: 'OP_DISABLE_TFER',
}

_to_bytes = lambda f, s: s if type(s) is bytes else f(s)

def _assert(condition, msg):
    if not condition:
        raise AssertionError(str(msg))


def validate_resolution(r):
    res_max_len = 9
    _assert(type(r) == bytes, 'Resolution: type must be bytes')
    _assert(len(r) < res_max_len, 'Resolution: len > %d, %s' % (res_max_len, r))


def validate_url(u):
    url_max_len = 20
    _assert(type(u) == bytes, 'Url: type must be bytes')
    _assert(len(u) <= url_max_len, 'Url: len > %d, %s' % (url_max_len, u))


def validate_address(address_bytes):
    _assert(type(address_bytes) == bytes, 'Address: type must be bytes')
    _assert(len(address_bytes) == 25, 'Address: len != 25')
    v_hash160 = a2b_hashed_base58(b2a_base58(address_bytes))
    _assert(v_hash160 == address_bytes[0:21], 'Address: version + hash160 does not match')


def validate_name(n):
    _assert(len(n) < 30, 'Name: len >= 30')
    _assert(type(n) == bytes, 'Name: type must be bytes')


def validate_prefix(bs):
    _assert(bs[:3] == MSG_PREFIX, 'msg prefix wrong')


def validate_comment(c):
    _assert(type(c) == bytes, 'Comment: type must be bytes')
    _assert(len(c) <= 80, 'Comment: len > 40')


def len_to_one_byte(i):
    return len(i).to_bytes(1, ENDIAN)


class Instruction:
    PREFIX = MSG_PREFIX
    OP_CODE = OP_NULL

    def __init__(self):
        self.op_code = self.OP_CODE
        self._extra_bytes = b''
        self._args = []

    def _encode_with_extra_bytes(self, *bs):
        return self.PREFIX + self.op_code + b''.join(bs)

    def to_bytes(self):
        return self.PREFIX + self.op_code + self._extra_bytes

    def address_pretty(self):
        return b2a_base58(self.address)

    @classmethod
    def validate_header(cls, bs):
        validate_prefix(bs)
        _assert(bs[3] == cls.OP_CODE[0], 'Op_code must match')

    @classmethod
    def from_bytes(cls, bs):
        raise NotImplemented()

    def decode(self):
        ''' Decode this instruction to something like: OP_CAST 255 v.Num RES '''
        return op_str_map[self.OP_CODE] + ' ' + ' '.join(map(str, self._args))