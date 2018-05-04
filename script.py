#reading all watched movies

#imports
import requests
from bs4 import BeautifulSoup

#variables
user = 'nnothumann' #change this user for yours.
links = []
moviesoriginals = []

#functions
def readLinks(soup):
    for link in soup.find_all("a"):
        if link.get('data-movie-pk') != None:
            links.append(link.get('href'))

    return links

def getOriginalTitle(links):
    global moviesoriginals
    for link in links:
        html_doc = requests.get('https://filmow.com%s' % link)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        for link in soup.find_all("h2", class_="movie-original-title"):
            moviesoriginals.append(link.get_text())

def readAllMovies(user):
    i = 1
    while requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i)):
        html_doc = requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i))
        print("Lendo pagina %d\n" % i)
        i = i + 1
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        links = readLinks(soup)
        getOriginalTitle(links)

#call functions
readAllMovies(user)
print(moviesoriginals)
    