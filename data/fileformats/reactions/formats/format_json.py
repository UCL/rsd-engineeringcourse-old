from reaction_system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter
import json

class Formatter(BaseFormatter):
    handles=["json"]
    def parse(self,file):
        system=System()
        
        model = json.load(file)

        # Add reactions according to the json model
        
        return system

    def write(self,file,system):
        # Make a model of the system just as dicts and lists:
        model=None # Put your solution here

        # Dump as json

        json.dump(model,file) 