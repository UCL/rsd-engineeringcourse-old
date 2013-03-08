import species
class Reaction:
    def __init__(self,reactants,products,rate):
        self.reactants=[species.Species(reactant) for reactant in reactants]
        self.products=[species.Species(product) for product in products]
        self.rate=rate