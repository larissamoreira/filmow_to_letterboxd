#reading movies (for now only in the first page)

import requests
from bs4 import BeautifulSoup

user = 'nnothumann' #change this user for yours.
html_doc = requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/' % user)
soup = BeautifulSoup(html_doc.text, 'html.parser')

movies = []
for link in soup.find_all("span", class_="title"):
    movies.append(link.get_text())

print(movies)