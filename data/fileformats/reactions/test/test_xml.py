import base_system1 as base
from ..formats.format_xml import Formatter


class TestXML(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter("xml")
        self.extension="xml"