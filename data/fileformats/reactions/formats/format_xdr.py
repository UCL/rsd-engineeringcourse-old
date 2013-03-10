from system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter
import xdrlib 



class Formatter(BaseFormatter):
    handles=["xdr"]
    magic=0x3415
    version=0x0001
    def parse(self,file):
        
        unpacker=xdrlib.Unpacker(file.read())
        magic=unpacker.unpack_uint()
        version=unpacker.unpack_uint()
        assert magic==Formatter.magic
        assert version==Formatter.version
        system=System() 
        
        # Your XDR solution here
        
 
        return system
    def write(self,file,system):
        packer=xdrlib.Packer() 
        packer.pack_uint(Formatter.magic)
        packer.pack_uint(Formatter.version)

        # Your XDR solution here

        file.write(packer.get_buffer())
             