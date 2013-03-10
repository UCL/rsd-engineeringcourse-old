import base_system1 as base
from ..formats.format_xdr import Formatter


class TestXDR():

    def setUp(self):
        self.formatter=Formatter("xdr")
        self.extension="xdr"