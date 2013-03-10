import base_system1 as base
from ..formats.format_json import Formatter


class TestJSON(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter("json")
        self.extension="json"