import csv

from system import System
from reaction import Reaction
from species import Species
from base_formatter import BaseFormatter

class Formatter(BaseFormatter):    
    handles=["csv"]
    def parse(self,file):
        system=System()
        reader=csv.reader(file)
        for row in reader:
            reverse=row.pop()
            if reverse!="":
                reverse=float(reverse)
            else:
                reverse=None
            forward=float(row.pop()) 
            products=[]
            reactants=[] 
            current=row.pop()
            while current != "-":
                products.append(current)
                current=row.pop()
            reactants=row
            system.add(reactants,list(reversed(products)),forward,reverse)
        return system

    def write(self,file,system):
        writer=csv.writer(file,lineterminator='\n')
        for reaction in system.reactions:
            writer.writerow(reaction.reactants+["-"]+reaction.products+[reaction.rate,""]) 
