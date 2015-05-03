__author__ = 'XertroV'

from . import Instruction, OP_MOD_RES, validate_resolution, validate_url, len_to_one_byte, _to_bytes

from ..constants import ENDIAN


class ModResolution(Instruction):
    """PREFIX[3] OP_MOD_RES[1] categories[1] end_timestamp[4] res_len[1] resolution[<15] url_len[1] url[<15]"""
    OP_CODE = OP_MOD_RES

    def __init__(self, categories, end_timestamp, resolution, url):
        super().__init__()
        self.categories = _to_bytes(lambda c: int(c).to_bytes(1, ENDIAN), categories)
        self.end_timestamp = _to_bytes(lambda ts: int(ts).to_bytes(4, ENDIAN), end_timestamp)
        self.resolution = _to_bytes(lambda r: r.encode(), resolution)
        self.url = _to_bytes(lambda u: u.encode(), url)

        self._extra_bytes = self.categories + self.end_timestamp + \
            len_to_one_byte(self.resolution) + self.resolution + \
            len_to_one_byte(self.url) + self.url

        validate_url(self.url)
        validate_resolution(self.resolution)

    @classmethod
    def from_bytes(cls, bs):
        cls.validate_header(bs)
        categories = bs[4]
        end = int.from_bytes(bs[5:9], ENDIAN)
        res_len = bs[9]
        res = bs[10:10+res_len]
        url_len = bs[10+res_len]
        url = bs[10+res_len+1:]  # this is ugly...
        return cls(categories, end, res, url)