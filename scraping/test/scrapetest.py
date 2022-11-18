import urllib.request

html = urllib.request.urlopen("https://pythonscraping.com/pages/page1.html")

text = html.read().decode("utf8")

print(text)
