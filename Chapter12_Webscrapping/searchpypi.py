
# searchpypi.py - Opens several search results on pypi

import requests, webbrowser, bs4, sys
print("Searching...")
res = requests.get("https://pypi.org/search/?q="+"".join(sys.argv[1:]))
# retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each element
linkElems = soup.select(".package-snippet")
numOpen = min(5, len(linkElems))
if not linkElems:
    print("No links found!")
    sys.exit()
for  i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)