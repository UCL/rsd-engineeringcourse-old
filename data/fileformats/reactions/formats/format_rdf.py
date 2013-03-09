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
    def handles(self):
        return ["rdf"]
    def loadGraph(self,file):
        self.graph = rdflib.graph.Graph()
        self.graph.parse(file)
    def querySparql(self,query):
        return self.graph.query(
        query,initNs=dict(
                rea=
                rdflib.Namespace(
                "http://raw.github.com/UCL-RC-softdev/training/master/data/fileformats/reactions/schemas/ontology#")
                )
        ).result
    def parse(self,file):
        self.loadGraph(file)
        system=System() 

        # PUT YOUR PARSER SOLUTION HERE

        return system
    def write(self,file,system):
        pass  