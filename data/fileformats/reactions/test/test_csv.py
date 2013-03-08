import unittest
from ..system import System
from ..formats.format_csv import Formatter
import tempfile
import StringIO
import fixtures


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.formatter=Formatter()

    def test_parse_system1(self):
        system=self.formatter.parse(fixtures.file_for('csv','system1'))  
        self.assertItemsEqual(system.species,["A", "B", "C","D","E"])
        self.assertEqual(len(system.reactions),4)

    def test_write_system1(self): 
        system=System()
        system.add(["A", "B"],["C"],0.1,0.3)
        system.add(["C"],["D", "E"],0.3,0.2)
        output=StringIO.StringIO()
        self.formatter.write(output,system)
        expectation=fixtures.file_for('csv','system1out').read()
        self.assertEqual(output.getvalue(),expectation)
        
    def test_read_write(self):
        system=self.formatter.parse(fixtures.file_for('csv','system1'))
        output=StringIO.StringIO()
        self.formatter.write(output,system)
        expectation=fixtures.file_for('csv','system1out').read()
        self.assertEqual(output.getvalue(),expectation)        