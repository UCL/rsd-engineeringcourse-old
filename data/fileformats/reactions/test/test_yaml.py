import base_system1 as base
from ..formats.format_yaml import Formatter


class TestYAML(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter()
        self.extension="yml"