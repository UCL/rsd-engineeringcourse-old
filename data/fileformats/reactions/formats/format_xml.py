from lxml import etree
from lxml.builder import E as builder

from system import System
from reaction import Reaction
from species import Species

class Formatter:
    def __init__(self):
        pass

    def loadDOM(self,file):
        self.tree = etree.parse(file)
        self.root = self.tree.getroot()
        
    def writeDOM(self,file):
        self.tree = etree.ElementTree(self.root)
        file.write(etree.tostring(self.tree,pretty_print=True,xml_declaration=True,encoding='UTF-8'))  
        
    def queryXpath(self,query):
        return self.tree.xpath(query)

    def handles(self):
        return ["xml"]

    def parse(self,file):
        self.loadDOM(file)
        system=System() 
        
        # put your solution here
        
        return system

    def write(self,file,system):
        
        rest="None" #Replace this with your solution for the rest of the XML model
        
        self.root=builder.system(rest) # here, root is defined as a <system/> element

        self.writeDOM(file)

        
 