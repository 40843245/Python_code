import urllib
import urllib.request
import json
import html_to_json

# python 2
def gen_dict_extract(key, var):
    if hasattr(var,'items'): # hasattr(var,'items') for python 3
        for k, v in var.items(): # var.items() for python 3
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result
            else:
                if v==key:
                    yield v

url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
output_json=html_to_json.convert(s)
#print(output_json)
endText="No more elements"
x=gen_dict_extract('lang',output_json)
while True:

    it=next(x,endText)
    print(it)
    if it==endText:
        break
    print("-----------------")

