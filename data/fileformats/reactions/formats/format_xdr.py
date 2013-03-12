from reaction_system import System
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
        
        reaction_count=unpacker.unpack_uint()
        for reaction_index in range(reaction_count):
            rate=unpacker.unpack_double()
            reactant_count=unpacker.unpack_uint()
            reactants=[""]*reactant_count
            for reactant_index in range(reactant_count):
                reactants[reactant_index]=unpacker.unpack_string()
            product_count=unpacker.unpack_uint()
            products=[""]*product_count
            for product_index in range(product_count):
                products[product_index]=unpacker.unpack_string()

            system.add(reactants,products,rate)
        
 
        return system
    def write(self,file,system):
        packer=xdrlib.Packer() 
        packer.pack_uint(Formatter.magic)
        packer.pack_uint(Formatter.version)
        packer.pack_uint(len(system.reactions))
        for reaction in system.reactions:
            packer.pack_double(reaction.rate)
            packer.pack_uint(len(reaction.reactants))
            for reactant in reaction.reactants:
                packer.pack_string(reactant.label)
            packer.pack_uint(len(reaction.products))
            for product in reaction.products:
                packer.pack_string(product.label)
        file.write(packer.get_buffer())
             