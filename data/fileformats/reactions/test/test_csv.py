import base_system1 as base
from ..formats.format_csv import Formatter


class TestCSV(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter()
        self.extension="csv"