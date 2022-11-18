from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(url, 'html.parser')

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)

for sibiling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibiling)