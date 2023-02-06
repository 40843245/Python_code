import urllib
import urllib.request
import json

url="https://www.youtube.com/@ThunderBird777"
html=urllib.request.urlopen(url)
s=html.read().decode()
dicts=json.loads(s)
print(dicts)
print(type(dicts))

