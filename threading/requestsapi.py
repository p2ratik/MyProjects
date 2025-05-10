import requests
from bs4 import BeautifulSoup

r = requests.get('https://api.github.com/events')

soup=BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)



# with open("Contents3.txt", "w", encoding="utf-8") as file:
#     file.write(r.text)
