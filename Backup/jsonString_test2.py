import json

# JSON string:
# Multi-line string
x = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"],
    "Food": "var function() { t=' "label" : " target " ';}"
	}"""

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(type(y))

for k,v in y.items():
    print("-----------------")
    print(k)
    print(v)
    print("-!-!-!-")
    l=(str(v).split("'"))
    for li in l:
        print(li)
    
