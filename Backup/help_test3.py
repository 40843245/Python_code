def object_getattribute(obj, name):
    ## message in help function

    null = object()
    objtype = type(obj)
    """
    Emulate PyObject_GenericGetAttr() in Objects/object.c
    """
    

x=help(object_getattribute)
print(x)
print(type(x))