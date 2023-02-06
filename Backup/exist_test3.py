import urllib
import urllib.request
import json
import html_to_json
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
        #print("#####")
        #print(o.keys())
        if letter in o.keys():
            isKey=True
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,True)
        
        else:
            for k,v in o.items():
                t=IsExist(letter,v)
                if t[existIdx]==True:
                    isKey=t[0] or t[1]
                    hasElemInSameLayer=LenCount(v,2)
                    return (isKey,hasElemInSameLayer,True)
            
            hasElemInSameLayer=False
            return (isKey,hasElemInSameLayer,False)
            
    elif isinstance(o,list):
        #print("@@@@@@")
        # print(o)
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
        #print("!!!!!!!!!!!!!")
        #print("letter="+str(letter)+",type(letter)="+str(type(letter))+",o="+str(o)+",type(o)="+str(type(o)))
        """
        s1=o.split("'")
        for x in s1:
            if isinstance(x,str):
                s2=x.split(' ')
                if letter in s2:
                    isKey=False
                    hasElemInSameLayer=False
                    return (isKey,hasElemInSameLayer,True)
        
        isKey=False
        hasElemInSameLayer=False
        return (isKey,hasElemInSameLayer,False)
        """
        
        json.loads()
        
def printExistence(letter,o):
    existIdx=2
    result=IsExist(letter, o)
    if result[existIdx]:
        print(str(letter)+" does exist in o.")
        print(result)
        
    else:
        print(str(letter)+" does NOT exist in o.")
        print(result)
        
url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
output_json=html_to_json.convert(s)
dictionary=dict(output_json)
o=dictionary
print(o)
print(type(o))
#printExistence('label',o)
printExistence('"title"',o)
#printExistence('menu',o)
#printExistence('"simpleText"',o)
