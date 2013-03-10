from system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter


class Formatter(BaseFormatter):
    handles= ["yaml", "yml"]
    def parse(self,file):
        system=System()
        return system
    def write(self,file,system):
        pass