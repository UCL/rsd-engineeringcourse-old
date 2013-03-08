import unittest
from ..system import System
class TestSystem(unittest.TestCase):
    def setUp(self):
        self.system=System()
    def test_one_reaction(self):
        self.system.add(["A"],["B","C"],0.1)
        self.assertItemsEqual(self.system.species,["A","B","C"])
        self.assertEqual(len(self.system.reactions),1)
    def test_reversible(self):
        self.system.add(["A"],["B","C"],0.1,0.3)
        self.assertItemsEqual(self.system.species,["A","B","C"])
        self.assertEqual(len(self.system.reactions),2)
    def test_two_reversible_reactions(self):
        self.system.add(["A","B"],["C"],0.1,0.3)
        self.system.add(["C"],["D","E"],0.1,0.3)
        self.assertItemsEqual(self.system.species,["A","B","C","D","E"])
        self.assertEqual(len(self.system.reactions),4) 