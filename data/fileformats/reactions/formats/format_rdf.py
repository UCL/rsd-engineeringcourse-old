from system import System
from reaction import Reaction
from species import Species  
from base_formatter import BaseFormatter


import rdflib

rdflib.plugin.register(
        'sparql', rdflib.query.Processor,
        'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register(
        'sparql', rdflib.query.Result,
        'rdfextras.sparql.query', 'SPARQLQueryResult')

class Formatter(BaseFormatter):
    def __init__(self,handling_extension,**options):
        BaseFormatter.__init__(self,handling_extension,**options)
        self.rea=rdflib.Namespace(
        "http://raw.github.com/UCL-RC-softdev/training/master/data/fileformats/reactions/schemas/ontology#"
        )
        
    handles=["rdf","ttl"]
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
        self.createGraph()

        base=rdflib.BNode()
        self.graph.add((base,rdflib.RDF["type"],self.rea["system"]))
        
        # PUT YOUR SOLUTION HERE
        
        
        self.graph.serialize(file,format=self.format_required())
    
    def format_required(self):
        format_name_table=dict(
            rdf="xml",
            ttl="turtle"
        )
        return format_name_table[self.handling_extension]  
