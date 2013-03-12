from lxml import etree
from lxml.builder import E as builder
import mako.template as mk 

from ..reaction_system import System
from ..reaction import Reaction
from ..species import Species
from base_formatter import BaseFormatter

import os


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
        
    def makoTemplate(self):
        here = os.path.dirname(__file__) 
        return mk.Template(open(os.path.join(here,'xml.mko')).read(),output_encoding='UTF-8')

    handles= ["xml"]

    def parse(self,file):
        self.loadDOM(file)
        system=System() 
        
        # put your solution here
        
        return system

    def writeBuilder(self,file,system):
        
        rest="None" #Replace this with your solution for the rest of the XML model
        
        self.root=builder.system(rest) # here, root is defined as a <system/> element

        self.writeDOM(file)
        
    def writeMako(self,file,system): 
        file.write(self.makoTemplate().render(system=system))
        
    def write(self,file,system):
        if self.options.get("use_lxml"):
            self.writeBuilder(file,system)
        else:
            self.writeMako(file,system)

        
 
