import base_system1 as base
from ..formats.format_rdf import Formatter

class TestCSV(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter()
        self.extension="rdf"