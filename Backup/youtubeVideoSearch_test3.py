from bs4 import BeautifulSoup
import urllib
import re 

def print_msg(msg):
    print("name!!!")
    for x in msg:
        print(x)
    print("type!!!")
    print(type(msg))
    print("dir!!!")
    for x in dir(msg):
        print(x)
    
#url='https://www.youtube.com/playlist?list=PLYjSYQBFeM-zQeZFpWeZ_4tnhc3GQWNj8'
url='https://www.youtube.com/@ThunderBird777'

page=urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())


href_tags = soup.find_all(href=True)
print("----------------------------------------------------------")
print_msg(href_tags)

"""
ff = open("C:/exp/file.txt", "w")
print("----------------------------------------------------------")
print_msg(ff)

for i in href_tags:
    ff.write(str(i))
ff.close()


for i in href_tags:
    if re.findall('watch',str(i))=='watch':
        ff.write(str(i))
ff.close()
"""