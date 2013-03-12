# We could do some lovely metaprogramming here, but let's keep it simple
# since this is teaching code

import format_csv
import format_json
import format_null
import format_rdf
import format_xdr
import format_xml
import format_yaml

import importlib
class FormatterFactory:
     
    def __init__(self):
        self.extensions=['csv','json','null','rdf','xdr','xml','yaml']
        
        self.formatters={}
        self.formatters['csv']=format_csv.Formatter
        self.formatters['json']=format_json.Formatter
        self.formatters['null']=format_null.Formatter
        self.formatters['rdf']=format_rdf.Formatter
        self.formatters['xdr']=format_xdr.Formatter
        self.formatters['xml']=format_xml.Formatter
        self.formatters['yaml']=format_yaml.Formatter
        
        for extension in self.extensions:
            for extra_extension in self.formatters[extension].handles:
                if extension==extra_extension:
                    continue
                self.formatters[extra_extension]=self.formatters[extension]
                
    def formatter_for(self,extension,**options):
        return self.formatters[extension](extension,**options)
         