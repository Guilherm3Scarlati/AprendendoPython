import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7ao+do+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

# titulo = site.find("title")
# print(titulo)

cotacaoDolar = site.find("span", class_="SwHCTb")
print(cotacaoDolar.get_text())
print(cotacaoDolar["data-value"])