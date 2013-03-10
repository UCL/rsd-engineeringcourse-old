import base_system1 as base

class TestCSV(base.BaseSystem1Test):

    def setUp(self):
        self.initialise_formatters("csv")