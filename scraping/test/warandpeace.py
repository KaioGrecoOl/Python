from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(url.read(), 'html.parser')

nameList = bs.findAll("span", {"class": {"green", "red"}})

for name in nameList:
  print(name.get_text())
