import base_system1 as base

class TestXML(base.BaseSystem1Test):

    def setUp(self):
        self.initialise_formatters("xml",use_lxml=True)
        
class TestXMLMako(base.BaseSystem1Test):

    def setUp(self):
        self.initialise_formatters("xml") 