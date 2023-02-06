def find_name_in_mro(cls, name, default):
    ## message in help function
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def object_getattribute(obj, name):
    ## message in help function
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__')
            or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)
    
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