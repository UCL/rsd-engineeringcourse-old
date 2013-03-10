import base_system1 as base
from ..formats.format_hdf5 import Formatter


class TestHDF5():

    def setUp(self):
        self.formatter=Formatter("hdf5")
        self.extension="hdf5"