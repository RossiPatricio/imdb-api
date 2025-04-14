from scraping_imdb import *
from duck_search import *

archivo = r'C:\Users\PRossi\code\march\movie-info\movies.txt'

def movie_info(element):
    url = get_url(element)
    content = scrap_imdb(url)
    return content

lista_de_diccionarios= []
with open(archivo, 'r') as file_object:
    content = file_object.readlines()
    for line in content:
        data = movie_info(line)
        lista_de_diccionarios.append(data)

for movie in lista_de_diccionarios:
    print(movie)
