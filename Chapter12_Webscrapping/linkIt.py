
# linkIt.py - Open all links on the current page

from bs4 import BeautifulSoup
import requests, webbrowser
import re, sys, pyperclip

address = pyperclip.paste()
print("Adress = ", address)

req = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.text)

links = []
for link in soup.findAll("a"):
    links.append(link.get("href"))

opened_links = 0
for link in links:
    if link is None:
        continue
    if opened_links < 5 and link.startswith("http"):
        webbrowser.open(str(link))
        opened_links += 1
.    # print(link)
