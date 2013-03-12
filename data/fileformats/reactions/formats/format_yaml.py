from reaction_system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter
import yaml

class Formatter(BaseFormatter):
    handles= ["yaml", "yml"]
    def parse(self,file):
        system=System()
        
        model = yaml.load(file)
                   
        # Add reactions according to the yaml model

        return system

    def write(self,file,system):
        # Make a model of the system just as dicts and lists:
        model=None # Put your solution here

        # Dump as yaml

        yaml.dump(model,file)