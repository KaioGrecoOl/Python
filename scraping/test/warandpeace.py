from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(url.read(), 'html.parser')

print(bs.text)
