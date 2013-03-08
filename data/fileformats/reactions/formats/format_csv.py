import system
import reaction
import species 
import CSV

class Formatter:
    def handles(self):
        return ["csv"]
    def parse(self,file):
        reader=csv.reader(file)
        system=system.System()
    def write(self,file,system):
        pass
