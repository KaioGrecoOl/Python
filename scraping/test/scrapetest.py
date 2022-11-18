from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(url.read(), 'html.parser')

print(bs.h1)


# import urllib.request

# html = urllib.request.urlopen("https://pythonscraping.com/pages/page1.html")

# text = html.read().decode("utf8")

# print(text)
