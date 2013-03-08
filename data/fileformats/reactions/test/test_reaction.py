import unittest
from ..reaction import Reaction
class TestRenderEngagements(unittest.TestCase):
    def setUp(self):
        pass
    def test_init(self): 
        atobandc=Reaction(["A"],["B","C"],0.1)
        self.assertEqual(atobandc.reactants[0].label,"A")
        self.assertEqual(atobandc.products[0].label,"B")
        self.assertEqual(atobandc.products[1].label,"C")
        self.assertEqual(atobandc.rate,0.1)