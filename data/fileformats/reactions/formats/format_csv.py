import CSV

from system import System
from reaction import Reaction
from species import Species


class Formatter:
    def handles(self):
        return ["csv"]
    def parse(self,file):
        reader=csv.reader(file)
        system=System()
    def write(self,file,system):
        pass
