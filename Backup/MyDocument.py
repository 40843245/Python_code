import docx
from docx import document
from docx import parts

#class MyDocuments():
class MyDocuments(document.Document,parts.DocumentPart):
    def __init__(self,name):
        self._name=name
    
    

x=MyDocuments("Jay")
