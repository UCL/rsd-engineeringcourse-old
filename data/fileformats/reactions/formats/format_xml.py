import system
import reaction
import species

class Formatter:
    def handles(self):
        return ["xml"]
    def parse(self,file):
        return system.System()
    def write(self,file,system):
        pass   