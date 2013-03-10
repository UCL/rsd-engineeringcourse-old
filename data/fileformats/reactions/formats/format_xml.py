from lxml import etree

from system import System
from reaction import Reaction
from species import Species

class Formatter:
    def __init__(self):
        pass

    def loadDOM(self,file):
        self.tree = etree.parse(file)
        self.root = self.tree.getroot()
        
    def createDOM(self):
        self.root=etree.XML('''\
<?xml version="1.0"?>
<system>
</system>
''')

        self.tree = etree.ElementTree(self.root)
        
    def queryXpath(self,query,start=None):
        if not start:
            start=self.tree
        return start.xpath(query)

    def handles(self):
        return ["xml"]

    def parse(self,file):
        self.loadDOM(file)
        system=System() 
        
        # put your solution here
        
        reactions=self.queryXpath("//reaction")
        for reaction in reactions:
            products=self.queryXpath("product/@label",reaction)
            reactants=self.queryXpath("reactant/@label",reaction)
            rate=float(self.queryXpath("@rate",reaction)[0])
            
            system.add(reactants,products,rate)
        
        return system

    def write(self,file,system):
        self.createDOM()
        
        # put your solution here
        
        file.write(etree.tostring(self.tree,pretty_print=True,xml_declaration=True,encoding='UTF-8'))   