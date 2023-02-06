def object_getattribute(obj, name):
    ## message in help function
    """
    Emulate PyObject_GenericGetAttr() in Objects/object.c
    1111111111111111111111111111
    aaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    
class DirtyWord:
    def __init__(self,l=None):
        self.dirty_word=l if l!= None else []
    def Is_DirtyWord(self,word):
        tf=True if word in self.dirty_word else False
        print(tf)
        
o=DirtyWord()
result=object_getattribute(o,"Is_DirtyWord")
print(result)
x=help(object_getattribute)
print(x)
print(type(x))