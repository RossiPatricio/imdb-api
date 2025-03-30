from scraping_imdb import *
from ducksearch import *

user_input = input('Search: ')
response = duck_search(user_input)
content = scrap_imdb(response)
print(content)
