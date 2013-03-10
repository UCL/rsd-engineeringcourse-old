from system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter
import yaml

class Formatter(BaseFormatter):
    handles= ["yaml","yml"]
    def parse(self,file):
        system=System()
        
        model = yaml.load(file)
        for reaction in model:
            system.add(reaction.get("reactants"),reaction.get("products"),reaction["rate"])

        return system

    def write(self,file,system):
        # Make a model of the system just as dicts and lists:
        model=[dict(
            rate=reaction.rate,
            reactants=[reactant.label for reactant in reaction.reactants],
            products=[product.label for product in reaction.products]
        ) for reaction in system.reactions
        ]

        # Dump as json

        yaml.dump(model,file)
