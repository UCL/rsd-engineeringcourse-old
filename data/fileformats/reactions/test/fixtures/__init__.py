import os
here = os.path.dirname(__file__)

def file_for(extension,system="system1"):
    return open(os.path.join(here,"{system}.{extension}".format(**locals())))