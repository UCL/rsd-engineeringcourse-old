from lxml import etree
from lxml.builder import E as builder

from system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter


class Formatter(BaseFormatter):

    def loadDOM(self,file):
        self.tree = etree.parse(file)
        self.root = self.tree.getroot()
        
    def writeDOM(self,file):
        self.tree = etree.ElementTree(self.root)
        file.write(etree.tostring(self.tree,pretty_print=True,xml_declaration=True,encoding='UTF-8'))  
        
    def queryXpath(self,query,start=None):
        if not start:
            start=self.tree
        return start.xpath(query)

    handles= ["xml"]

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

    def writeBuilder(self,file,system):
        
        reactions=[
            builder.reaction(rate=str(reaction.rate),
            *([builder.product(label=product.label) for product in reaction.products]+
            [builder.reactant(label=reactant.label) for reactant in reaction.reactants])
            ) for reaction in system.reactions
        ]
        
        self.root=builder.system(*reactions) # here, root is defined as a <system/> element

        self.writeDOM(file)
        
    def writeMako(self,file,system):
        pass
        
    def write(self,file,system):
        if self.options.get("use_lxml"):
            self.writeBuilder(file,system)
        else:
            self.writeMako(file,system)

        
 
