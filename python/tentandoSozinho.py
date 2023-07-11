import requests
from bs4 import BeautifulSoup

link = "https://www.gov.br/pt-br"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())

titulo = site.find("title")
print(titulo)

tituloPost = site.find("p", class_="tile-subtitle")
print(tituloPost.get_text())
print(tituloPost["$0"])