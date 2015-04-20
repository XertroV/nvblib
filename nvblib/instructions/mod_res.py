__author__ = 'XertroV'

from . import Instruction, OP_MOD_RES, validate_resolution, validate_url, len_to_one_byte

from ..constants import ENDIAN


class ModResolution(Instruction):
    """PREFIX[3] OP_MOD_RES[1] categories[1] end_timestamp[4] res_len[1] resolution[<15] url_len[1] url[<15]"""

    def __init__(self, categories, end_timestamp, resolution, url):
        super().__init__()
        self.op_code = OP_MOD_RES
        self.categories = int(categories).to_bytes(1, ENDIAN)
        self.end_timestamp = int(end_timestamp).to_bytes(4, ENDIAN)
        self.resolution = bytes(resolution.encode())
        self.url = bytes(url.encode())

        self._extra_bytes = self.categories + self.end_timestamp + \
            len_to_one_byte(self.resolution) + self.resolution + \
            len_to_one_byte(self.url) + self.url

        validate_url(self.url)
        validate_resolution(self.resolution)