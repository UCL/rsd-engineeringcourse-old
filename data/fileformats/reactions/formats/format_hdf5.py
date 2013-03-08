import system
import reaction
import species

class Formatter:
    def handles(self):
        return ["hdf5"]
    def parse(self,filename):
        pass
    def write(self,filename):
        pass