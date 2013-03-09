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
        reactions=[x[0] for x in self.querySparql("""\
        SELECT ?label
        WHERE {
            ?reaction rdf:type rea:reaction .
            ?reaction rdfs:label ?label
        }
        """)] 

                
        for reaction in reactions:
            
            reactants=[x[0] for x in self.querySparql("""\
            SELECT ?label
            WHERE {
                ?reaction rdfs:label "%s" .
                ?reaction rea:reactant ?reactant .
                ?reactant rdfs:label ?label .
            }
            """%reaction)]
            
            products=[x[0] for x in self.querySparql("""\
            SELECT ?label
            WHERE {
                ?reaction rdfs:label "%s" .
                ?reaction rea:product ?product .
                ?product rdfs:label ?label
            }
            """%reaction)]
            rate=self.querySparql("""\
            SELECT ?rate
            WHERE {
                ?reaction rdfs:label "%s" .
                ?reaction rea:rate ?rate .
            }
            """%reaction)[0]
              
            system.add(reactants,products,rate)


        return system
    def write(self,file,system):
        pass  