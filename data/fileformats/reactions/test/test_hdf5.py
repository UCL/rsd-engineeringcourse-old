import base_system1 as base
from ..formats.format_hdf5 import Formatter


class TestHDF5(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter()
        self.extension="hdf5"