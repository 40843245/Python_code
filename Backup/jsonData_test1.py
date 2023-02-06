import json

o={"a":1,"b":2,"c":[{"d":4,"e":5,"f":{"g":6}}]}

jsonData=json.dumps(o,indent=4)
print(jsonData)
