import unittest
from ..species import Species
class TestSpecies(unittest.TestCase):
    def setUp(self):
        pass
    def test_init_string(self):
        a=Species("a")
        self.assertEqual(a.label,"a")
    def test_init_species(self):
        a=Species(Species("a"))
        self.assertEqual(a.label,"a") 