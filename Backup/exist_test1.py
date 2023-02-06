import json

def LenCount(o,cnt):
    if len(o)>=int(cnt):
        return True
    else:
        return False

def IsExist(letter,o):
    isKey=False
    if isinstance(o,dict):        
        if letter in o:
            isKey=True
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,True)
        else:
            for k,v in o.items():
                if IsExist(letter,v)[2]==True:
                    isKey=False
                    hasElemInSameLayer=LenCount(o,2)
                    return (isKey,hasElemInSameLayer,True)
            
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,False)
            
    elif isinstance(o,list):
        for v in o:
            if IsExist(letter,v)[2]==True:
                isKey=False
                hasElemInSameLayer=LenCount(o,2)
                return (isKey,hasElemInSameLayer,True)
        
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
    
    elif isinstance(o,set):
        for v in o:
            if IsExist(letter,v)[2]==True:
                isKey=False
                hasElemInSameLayer=LenCount(o,2)
                return (isKey,hasElemInSameLayer,True)
            
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
    
    elif isinstance(o,tuple):
        for v in o:
            if IsExist(letter,v)[2]==True:
                hasElemInSameLayer=LenCount(o,2)
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
    if IsExist(letter, o)[2]:
        print(str(letter)+" does exist in "+str(o))
    else:
        print(str(letter)+" does NOT exist in "+str(o))
        
o={"a":1,"b":2,"c":[{"d":4,"e":5,"f":{"g":6}},(7,8,9),({"h":10},"i")]}
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
