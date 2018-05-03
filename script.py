#reading all watched movies

import requests
from bs4 import BeautifulSoup

user = 'nnothumann' #change this user for yours.
movies = []

i = 1
while requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i)):
    html_doc = requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i))
    i = i + 1
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    for link in soup.find_all("span", class_="title"):
        movies.append(link.get_text())

print(movies)