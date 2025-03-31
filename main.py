from scraping_imdb import *
from duck_search import *

archivo = r'C:\Users\PRossi\code\movie-info\movies.txt'

def movie_info(search):
    url = get_url(search)
    content = scrap_imdb(url)
    return content


with open(archivo, 'r') as file_object:
    content = file_object.readlines()
    for line in content:
        print(F'{movie_info(line)}\n')
