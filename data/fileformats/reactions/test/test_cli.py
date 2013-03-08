import unittest 
import shlex

from ..reactions import Reactions

class TestRenderEngagements(unittest.TestCase):
    def setUp(self):
        pass
    def test_inoutext(self): 
        reactions=Reactions(shlex.split("--in something.csv --out somethingelse.rdf"))
        self.assertEqual(reactions.in_type_string,"csv")
        self.assertEqual(reactions.out_type_string,"rdf")
        self.assertEqual(reactions.infile,"something.csv")
        self.assertEqual(reactions.outfile,"somethingelse.rdf")
    def test_get_formatter(self):
        reactions=Reactions(shlex.split("--in something.csv --out somethingelse.rdf"))
        self.assertEqual(reactions.in_formatter.handles(),['csv'])
        self.assertEqual(reactions.out_formatter.handles(),['rdf'])