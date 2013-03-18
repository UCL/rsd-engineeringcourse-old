import species
class Reaction:
    def __init__(self,reactants,products,rate):
        self.reactants=reactants
        self.products=products
        self.rate=rate
    def __str__(self):
        return "+ ".join(sorted(str(x) for x in self.reactants))+" -> " + "+ ".join(sorted(str(x) for x in self.products))+" ("+str(self.rate)+")"
    def __eq__(self,other):
        return str(self)==str(other) 