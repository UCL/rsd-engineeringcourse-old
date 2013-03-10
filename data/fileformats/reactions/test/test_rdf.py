import base_system1 as base

class TestRDFXML(base.BaseSystem1Test):

    def setUp(self):
        self.initialise_formatters("rdf")
        
class TestRDFTurtle(base.BaseSystem1Test):

    def setUp(self):
        self.initialise_formatters("ttl")