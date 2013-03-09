import unittest
from ..system import System
import tempfile
import StringIO
import fixtures

class BaseSystem1Test(unittest.TestCase):

    def output_expectation(self):
        return fixtures.file_for(self.extension,'system1out').read()

    def parse_input(self):
        return self.formatter.parse(fixtures.file_for(self.extension,'system1')) 
        
    def write_temp(self,system):
        output=StringIO.StringIO() 
        self.formatter.write(output,system)
        return output.getvalue()

    def test_parse_system1(self):
        system=self.parse_input()
        self.assertItemsEqual(system.species,["A", "B", "C","D","E"])
        self.assertEqual(len(system.reactions),4)

    def test_write_system1(self): 
        system=System()
        system.add(["A", "B"],["C"],0.1,0.3)
        system.add(["C"],["D", "E"],0.3,0.2)
        self.assertEqual(self.write_temp(system),self.output_expectation())
        
    def test_read_write(self):
        system=self.parse_input()
        self.assertEqual(self.write_temp(system),self.output_expectation())