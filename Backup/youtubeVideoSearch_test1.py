from bs4 import BeautifulSoup
import requests



def print_msg(msg):
    print("name!!!")
    print(msg)
    print("type!!!")
    print(type(msg))
    print("dir!!!")
    print(dir(msg))
    return None

def func(soup):
    for entry in soup.find_all("entry"):
        for link in entry.find_all("link"):
            print(link["href"])    
            
            
            
            
            
url='https://www.youtube.com/@barbarabarbosa3998'
#url='https://www.youtube.com/watch?v=qeqAdK1as-A&list=RDqeqAdK1as-A&start_radio=1'
#url="https://www.youtube.com/feeds/videos.xml?user=LinusTechTips"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
print("-------------------------------------------")
# print_msg(html)
print("-------------------------------------------")
print_msg(soup)


        
        

    