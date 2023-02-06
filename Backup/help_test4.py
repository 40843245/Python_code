def object_getattribute(obj, name):
    ## message in help function

    null = object()
    
    """
    Emulate PyObject_GenericGetAttr() in Objects/object.c
    """
    
    objtype = type(obj)
    
    

x=help(object_getattribute)
print(x)
print(type(x))