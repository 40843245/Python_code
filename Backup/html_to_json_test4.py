import urllib
import urllib.request
import json
import html_to_json

def print_whiteline(letter):
    for idx in range(0,2,1):
        s=''
        for jdx in range(0,20,1):
            s+=letter
        print(s)
    return None

def print_dict(output_dict,currCnt):
    for v in output_dict:
        if type(v)==type(list()):
            print("v is a list!!!")
            print_dict(v)
            continue
        elif type(v)==type(dict()):
            print("v is a dict!!!")
            print_dict(v)
            continue
        
        print_whiteline('-')
        
        print(v)
        print(type(v))
        print(output_dict)
        print(type(output_dict))
        print_whiteline('@')
        
        if type(output_dict)==type(list()):
            for val in output_dict:
                if type(val)==type(dict()):
                    print("val is a dict!!!")
                    print_dict(val)
                elif type(val)==type(list()):
                    print("val is a list!!!")
                    print_dict(val)

                else:
                    print("val")
                    print(type(val))
                    print(val)          
        else:        
             if type(output_dict[v])==type(dict()):
                 print("output_dict[v] is a dict!!!")
                 print_dict(output_dict[v])
             elif type(output_dict[v])==type(list()):
                 print("output_dict[v] is a list!!!")
                 print_dict(output_dict[v])

             else:
                 print("output_dict[v]")
                 print(type(output_dict[v]))
                 print(output_dict[v])  
    
    return None
        
url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
output_json=html_to_json.convert(s)
print("~~~~~~~~~~~~~~~~~~~~~~~")
print(output_json)
#print_dict(output_json)
