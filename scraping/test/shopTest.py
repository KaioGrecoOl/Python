from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(url, 'html.parser')
images = bs.find_all(lambda tag: len(tag.attrs) == 2)

for image in images: 
    print(image)


# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)

# for sibiling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibiling)