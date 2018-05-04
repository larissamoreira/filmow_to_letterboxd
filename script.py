#imports
import requests
from bs4 import BeautifulSoup
import pandas

#variables
user = 'nnothumann' #change this user for yours.
csv_file = "./movies.csv"
movies_originals = []

#functions
def read_links(soup):
    links = []
    for link in soup.find_all("a"):
        if link.get('data-movie-pk') != None:
            links.append(link.get('href'))

    return links

def get_original_title(links):
    global movies_originals
    for link in links:
        html_doc = requests.get('https://filmow.com%s' % link)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        for link in soup.find_all("h2", class_="movie-original-title"):
            movies_originals.append(link.get_text())

def read_movies(user):
    i = 1 
    while requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i)):
        html_doc = requests.get('https://filmow.com/usuario/%s/filmes/ja-vi/?pagina=%d' % (user, i))
        print("reading page %d" % i)
        i = i + 1
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        links = read_links(soup)
        get_original_title(links)

#call functions
read_movies(user)

# writing csv
df = pandas.DataFrame(data={"Title": movies_originals})
df.to_csv(csv_file, sep=',',index=False)