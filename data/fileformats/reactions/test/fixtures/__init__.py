import os
here = os.path.dirname(__file__)

def file_for(extension,system):
    return open(os.path.join(here,"{system}.{extension}".format(**locals())))