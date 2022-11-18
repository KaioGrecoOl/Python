from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(url, 'html.parser')

print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)

# for sibiling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibiling)