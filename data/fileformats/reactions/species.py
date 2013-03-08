class Species:
    def __init__(self,input):
        self.label=str(input)
    def __str__(self):
        return self.label
    def __eq__(self,other):
        return str(self)==str(other)