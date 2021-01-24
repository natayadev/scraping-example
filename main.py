from bs4 import BeautifulSoup
import requests

url = "https://www.primeraedicion.com.ar/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
contents = soup.find_all('ul', "wpp-list")

print("LO MÁS LEÍDO HOY")
print("Fuente: Primera Edición")
print("")

for title in contents:
    sub = title.find_all('a', 'wpp-post-title')
    print(sub[0].contents)
    print("Link: " + sub[0].attrs.get('href'))
    print("")