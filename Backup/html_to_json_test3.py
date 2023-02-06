import urllib
import urllib.request
import json
import html_to_json

def print_dict(output_dict,currCnt):
    for v in output_dict:
        print("v")
        print(output_dict[v])
        print(v)
        if type(output_dict[v])==type(dict):
            print("dict!!!")
            print_dict(output_dict[v])
        elif type(output_dict[v])==type(list):
            print("dict!!!")
            print_dict(output_dict[v])
        else:
            print("output_dict[v]")
            print(type(output_dict[v]))
            print(output_dict[v])    
        
        
url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
output_json=html_to_json.convert(s)
print("~~~~~~~~~~~~~~~~~~~~~~~")
print(output_json)
