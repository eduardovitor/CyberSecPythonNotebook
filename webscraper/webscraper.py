from bs4 import BeautifulSoup
import requests

url = "https://www.climatempo.com.br/"

site = requests.get(url).content

soup = BeautifulSoup(site,"html.parser")

noticias = soup.findAll("h4",class_="-gray-dark-2 -font-base -bold")

for noticia in noticias:
    print(noticia.string)

print(soup.title.string)