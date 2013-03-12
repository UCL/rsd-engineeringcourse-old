import species as sp
import reaction

class System:
    def __init__(self):
        self.reactions =[ ]
        self.species ={} 

    def get_species(self,species):
        return self.species[ str(species) ]

    def add_species(self,species): 
        if not str(species) in self.species:
            self.species[str(species)] = sp.Species(species)
        return self.get_species(species)

    def add(self,reactants,products,forward,reverse=None):
        for reactant in reactants:
            self.add_species(reactant)
        for product in products:
            self.add_species(product) 
        system_reactants = [self.get_species(reactant) for reactant in reactants]
        system_products = [self.get_species(product) for product in products]
        
        self.reactions.append(reaction.Reaction(system_reactants, system_products, forward))
        if reverse:
            self.reactions.append(reaction.Reaction(system_products, system_reactants, reverse))

    def __str__(self):
        return "; ".join(sorted(str(x) for x in sorted(self.reactions)))
        
    def __eq__(self,other):
        return str(self)==str(other)  