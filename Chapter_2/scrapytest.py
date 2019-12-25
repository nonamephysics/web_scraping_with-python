from urllib.request import urlopen 
from bs4 import BeautifulSoup 
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html") 
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"}) 
for name in nameList: 
    print(name.get_text())


#findAll(tag, attributes, recursive, text, limit, keywords) 
#find(tag, attributes, recursive, text, keywords) 

    
print (bsObj.findAll({"h1","h2","h3","h4","h5","h6"}))
print (bsObj.findAll("span", {"class":"green", "class":"red"})) 

nameList = bsObj.findAll(text="the prince") 
print(len(nameList))