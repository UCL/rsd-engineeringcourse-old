import species
import reaction

class System:
    def __init__(self):
        self.reactions =[ ]
        self.species ={} 

    def get_species(self,species):
        return self.species[ str(species) ]

    def add_species(self,species): 
        if not str(species) in self.species:
            self.species[str(species)] = species
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