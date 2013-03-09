from system import System
from reaction import Reaction
from species import Species  

import rdflib

rdflib.plugin.register(
        'sparql', rdflib.query.Processor,
        'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register(
        'sparql', rdflib.query.Result,
        'rdfextras.sparql.query', 'SPARQLQueryResult')

class Formatter:
    def __init__(self):
        self.rea=rdflib.Namespace("http://raw.github.com/UCL-RC-softdev/training/master/data/fileformats/reactions/schemas/ontology#")
        
    def handles(self):
        return ["rdf"]
    def loadGraph(self,file):
        self.graph = rdflib.graph.Graph()
        self.graph.parse(file)
        
    def createGraph(self):
        self.graph=rdflib.graph.Graph()     
        # Bind prefix, namespace pairs.
        self.graph.bind("rea", "http://raw.github.com/UCL-RC-softdev/training/master/data/fileformats/reactions/schemas/ontology#")
        self.graph.bind("xsd", "http://www.w3.org/2001/XMLSchema#")
        
    def querySparql(self,query):
        return self.graph.query(query,initNs=dict(rea=self.rea)).result
        
    def parse(self,file):
        self.loadGraph(file)
        system=System() 

        # PUT YOUR PARSER SOLUTION HERE


        return system
    def write(self,file,system):
        pass
        
        # PUT YOUR SOLUTION HERE
          
