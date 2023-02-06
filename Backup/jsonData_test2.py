import json

def IsExist(letter,dictionary):
    if letter in dictionary:
        print(str(letter)+" is in the dictionary"+str(dictionary))
    else:
        print(str(letter)+" is NOT in the dictionary"+str(dictionary))
        
        
        
        
o={"a":1,"b":2,"c":[{"d":4,"e":5,"f":{"g":6}}]}
jsonData=json.dumps(o,indent=4)
print(jsonData)
IsExist('a',o)
IsExist('b',o)
IsExist('c',o)
IsExist('d',o)
IsExist('e',o)
IsExist('f',o)
IsExist(1,o)
IsExist(2,o)
IsExist(3,o)
IsExist(4,o)
IsExist(5,o)
IsExist(6,o)
IsExist('h',o)
