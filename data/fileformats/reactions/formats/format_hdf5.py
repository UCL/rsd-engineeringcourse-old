import system
import reaction
import species

class Formatter:
    def handles(self):
        return ["hdf5"]
    def parse(self,file):
        return system.System()
    def write(self,file,system):
        pass  