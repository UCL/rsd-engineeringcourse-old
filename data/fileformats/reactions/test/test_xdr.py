import base_system1 as base
from ..formats.format_xdr import Formatter


class TestXDR(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter()
        self.extension="xdr"