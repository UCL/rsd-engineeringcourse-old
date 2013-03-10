import unittest
from ..system import System
import tempfile
import StringIO
import fixtures
from ..formats.formatter_factory import FormatterFactory

class BaseSystem1Test(unittest.TestCase):
    def initialise_formatters(self,extension,fixture_extension=None,**args):
        self.extension=extension
        self.fixture_extension=fixture_extension
        if self.fixture_extension is None:
            self.fixture_extension=extension
        self.formatter_factory=FormatterFactory()
        self.formatter=self.formatter_factory.formatter_for(self.extension,**args)
        self.fixture_formatter=self.formatter_factory.formatter_for(self.fixture_extension,**args)
        
    def parse_input(self):
        return self.fixture_formatter.parse(fixtures.file_for(self.fixture_extension,'system1')) 
        
    def write_temp(self,system):
        output=StringIO.StringIO() 
        self.formatter.write(output,system)
        return output.getvalue()
        
    def write_then_read(self,system):
        return self.formatter.parse(StringIO.StringIO(self.write_temp(system)))

    def test_parse_system1(self):
        system=self.parse_input()
        self.assertItemsEqual(system.species,["A", "B", "C","D","E"])
        self.assertEqual(len(system.reactions),4) 
        self.assertItemsEqual([x.rate for x in system.reactions],[0.3,0.2,0.3,0.1])

    def test_write_read(self): 
        system=System()
        system.add(["A", "B"],["C"],0.1,0.3)
        system.add(["C"],["D", "E"],0.3,0.2)
        system2=self.write_then_read(system)
        self.assertItemsEqual(system2.species,["A", "B", "C","D","E"])
        self.assertEqual(len(system2.reactions),4)
        self.assertItemsEqual([x.rate for x in system2.reactions],[0.3,0.2,0.3,0.1])
        
    def test_read_write_read(self):
        system=self.parse_input()
        system2=self.write_then_read(system)
        self.assertItemsEqual(system2.species,["A", "B", "C","D","E"])
        self.assertEqual(len(system2.reactions),4)
        self.assertItemsEqual([x.rate for x in system2.reactions],[0.3,0.2,0.3,0.1])