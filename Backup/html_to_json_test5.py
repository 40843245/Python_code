
import urllib
import urllib.request
import json
import html_to_json

target_list=[]

def SetGlboalList():
    global target_list
    target_list=[]
    
def print_whiteline(letter):
    for idx in range(0,2,1):
        s=''
        for jdx in range(0,20,1):
            s+=letter
        print(s)
    return None

def print_dict(output_dict,currCnt):
    
    global target_list
    for v in output_dict:
        if type(v)==type(list()):
            print(str(currCnt)+":"+"v is a list!!!")
            print_dict(v,currCnt+1)
            continue
        elif type(v)==type(dict()):
            print(str(currCnt)+":"+"v is a dict!!!")
            print_dict(v,currCnt+1)
            continue
        
        print_whiteline('@')
        
        if type(output_dict)==type(list()):
            for val in output_dict:
                if type(val)==type(dict()):
                    print(str(currCnt)+":"+"val is a dict!!!")
                    print_dict(val,currCnt+1)
                elif type(val)==type(list()):
                    print(str(currCnt)+":"+"val is a list!!!")
                    print_dict(val,currCnt+1)

                else:
                    print("val")
                    print(type(val))
                    print(val)          
        else:        
             if type(output_dict[v])==type(dict()):
                 print(str(currCnt)+":"+"output_dict[v] is a dict!!!")
                 print_dict(output_dict[v],currCnt+1)
             elif type(output_dict[v])==type(list()):
                 print(str(currCnt)+":"+"output_dict[v] is a list!!!")
                 print_dict(output_dict[v],currCnt+1)

             else:
                 print(str(currCnt)+":"+"output_dict[v]")
                 print(type(output_dict[v]))
                 print(output_dict[v])  
    
    return target_list
        
SetGlboalList()
url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
output_json=html_to_json.convert(s)
print("~~~~~~~~~~~~~~~~~~~~~~~")
target_list=print_dict(output_json,0)
print(target_list)