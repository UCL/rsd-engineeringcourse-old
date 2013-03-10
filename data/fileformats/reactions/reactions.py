import sys
import os
import argparse

from system import *
import formats.formatter_factory

class Reactions:
    def __init__(self,clargs):
        self.parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
        self.parser.add_argument("--in", help="Input file")
        self.parser.add_argument("--out", help="Output file")
        self.parser.add_argument("--bigfile",type=int)
        self.formatter_factory = formats.formatter_factory.FormatterFactory()
        options,extra = self.parser.parse_known_args(clargs)
        
        self.infile=vars(options).get('in') #Because "in" is a reserved word
        self.outfile=options.out
         

        self.in_type_string=os.path.splitext(self.infile)[-1][1:]
        self.out_type_string=os.path.splitext(self.outfile)[-1][1:]
        self.in_formatter=self.formatter_factory.formatter_for(self.in_type_string)
        self.out_formatter=self.formatter_factory.formatter_for(self.out_type_string)
        
    def act(self):
        self.system=self.in_formatter.parse(open(self.infile)) 
        self.out_formatter.write(open(self.outfile,'w'),self.system) 
        
def main():
    Reactions(sys.argv).act()

if __name__ == '__main__':
    main()      