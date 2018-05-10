#imports
import requests
from bs4 import BeautifulSoup
import pandas
import re

#variables
movies_originals = []
csv_file = "./filmes.csv"

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
        print("getting original title from link %s" % link)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        for link in soup.find_all("h2", class_="movie-original-title"):
            if re.match("[^\x00-\x7F]", link.get_text()):
                for link in soup.find_all('div', class_="movie-other-titles"):
                    for item in link.find_all('li'):
                        if item.em.get_text() == "Estados Unidos da América":
                            movies_originals.append(item.strong.get_text())
            else:
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

def get_info():
    user = input("Digite o seu nome de usuário no filmow: ")
    print("OK! A busca será feita no usuário " + user + ". Seu csv será salvo no diretório atual com o nome filmes.csv")
    
    return user

def main():
    user = get_info()
    read_movies(user)
    #writing csv
    df = pandas.DataFrame(data={"Title": movies_originals})
    df.to_csv(csv_file, sep=',',index=False)

if __name__ == "__main__":
    main()
