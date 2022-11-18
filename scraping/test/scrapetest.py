from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


try:
  url = urlopen("https://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It worked!")

    
# bs = BeautifulSoup(url.read(), 'html.parser')

# print(bs.h1)


# import urllib.request

# html = urllib.request.urlopen("https://pythonscraping.com/pages/page1.html")

# text = html.read().decode("utf8")

# print(text)
