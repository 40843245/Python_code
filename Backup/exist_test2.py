import json

def LenCount(o,cnt):
    if isinstance(o,dict) or isinstance(o,tuple) or isinstance(o,set) or isinstance(o,list):
        if len(o)>=int(cnt):
            return True
        else:
            return False
    return False

def IsExist(letter,o):
    existIdx=2
    isKey=False
    if isinstance(o,dict):        
        if letter in o:
            isKey=True
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,True)
        else:
            for k,v in o.items():
                if IsExist(letter,v)[existIdx]==True:
                    isKey=False
                    hasElemInSameLayer=LenCount(v,2)
                    return (isKey,hasElemInSameLayer,True)
            
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,False)
            
    elif isinstance(o,list):
        for v in o:
            if IsExist(letter,v)[existIdx]==True:
                isKey=False
                hasElemInSameLayer=LenCount(v,2)
                return (isKey,hasElemInSameLayer,True)
        
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
    
    elif isinstance(o,set):
        for v in o:
            if IsExist(letter,v)[existIdx]==True:
                isKey=False
                hasElemInSameLayer=LenCount(v,2)
                return (isKey,hasElemInSameLayer,True)
            
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
    
    elif isinstance(o,tuple):
        for v in o:
            if IsExist(letter,v)[existIdx]==True:
                hasElemInSameLayer=LenCount(v,2)
                return (isKey,hasElemInSameLayer,True)
        isKey=False
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
    
    else:
        if letter==o:
            isKey=False
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,True)
        else:
            isKey=False
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,False)
        
        
def printExistence(letter,o):
    existIdx=2
    result=IsExist(letter, o)
    if result[existIdx]:
        print(str(letter)+" does exist in o.")
        print(result)
        
    else:
        print(str(letter)+" does NOT exist in o.")
        print(result)
        
o={"a":1,"b":2,"c":[{"d":4,"e":5,"f":{"g":6}},(7,8,9),({"h":10},"i")],"aa":[{"j":11}]}
jsonData=json.dumps(o,indent=4)
print(jsonData)

printExistence('a',o)
printExistence('b',o)
printExistence('c',o)
printExistence('d',o)
printExistence('e',o)
printExistence('f',o)
printExistence(1,o)
printExistence(2,o)
printExistence(3,o)
printExistence(4,o)
printExistence(5,o)
printExistence(6,o)
printExistence('h',o)
printExistence(7,o)
printExistence(8,o)
printExistence(9,o)
printExistence(10,o)
printExistence('i',o)
printExistence('j',o)
printExistence(11,o)
printExistence('k',o)
printExistence('l',o)
printExistence('m',o)
