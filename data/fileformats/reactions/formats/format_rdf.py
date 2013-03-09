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
            """%reaction)
            try:
                system.add(reactants,products,float(str(rate[0][0])))
            except:
                system.add(reactants,products,float(str(rate[0])))

        return system
    def write(self,file,system):
        self.createGraph()
        base=rdflib.BNode()
        self.graph.add((base,rdflib.RDF["type"],self.rea["system"]))
        # each species needs its own node ID
        for species in system.species.values():
            species.node=rdflib.BNode()

        for number,reaction in enumerate(system.reactions):
            reaction_node=rdflib.BNode()
            self.graph.add((base,self.rea["hasReaction"],reaction_node))
            self.graph.add((reaction_node,rdflib.RDFS["label"],rdflib.Literal(str(number))))
            self.graph.add((reaction_node,rdflib.RDF["type"],self.rea["reaction"])) 
            self.graph.add((reaction_node,self.rea["rate"],rdflib.Literal(reaction.rate)))
            for reactant in reaction.reactants:
                self.graph.add((reaction_node,self.rea["reactant"],reactant.node))
                self.graph.add((reactant.node,rdflib.RDF["type"],self.rea["species"]))
                self.graph.add((reactant.node,rdflib.RDFS["label"],rdflib.Literal(reactant.label)))
            for product in reaction.products:
                self.graph.add((reaction_node,self.rea["product"],product.node))
                self.graph.add((product.node,rdflib.RDF["type"],self.rea["species"]))
                self.graph.add((product.node,rdflib.RDFS["label"],rdflib.Literal(product.label)))
                            
        self.graph.serialize(file)
          