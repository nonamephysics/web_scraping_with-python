from urllib.request import urlopen 
from bs4 import BeautifulSoup 
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html") 

#check thah content isnot empty
if html is None: 
    print("URL is not found") 
else:
    bsObj = BeautifulSoup(html.read()); 
print(bsObj.h1)


#try to look for some fake tag
try: 
    badContent = bsObj.nonExistingTag.anotherTag 
except AttributeError as e: 
    print("Tag was not found") 
else: 
    if badContent == None: 
            print ("Tag was not found") 
    else: 
            print(badContent)


#from urllib.request import urlopen 
#from urllib.error import HTTPError 
#from bs4 import BeautifulSoup 
# def getTitle(url): 
#    try: 
#        html = urlopen(url) 
#    except HTTPError as e: 
#        return None 
#    try: 
#        bsObj = BeautifulSoup(html.read()) 
#        title = bsObj.body.h1 
#    except AttributeError as e: 
#        return None 
#    return title 
#title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html") 
#if title == None: 
#    print("Title could not be found") 
#else: 
#    print(title)