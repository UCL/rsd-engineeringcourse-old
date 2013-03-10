import base_system1 as base
from ..formats.format_rdf import Formatter

class TestRDFXML(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter("rdf")
        self.extension="rdf"
        
class TestRDFTurtle(base.BaseSystem1Test):

    def setUp(self):
        self.formatter=Formatter("ttl")
        self.extension="ttl"