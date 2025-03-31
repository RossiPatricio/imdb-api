import requests
from bs4 import BeautifulSoup
import urllib.parse

def duck_search(termino):
    url = f"https://duckduckgo.com/html/?q={termino}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    resultados = []
    for link in soup.select(".result__title a"):
        enlace = link["href"]
        resultados.append(enlace)

    return resultados[:1]

def get_url(search):
    input = f'imdb {search}'
    result = duck_search(input)
    if result:
        enlace = result[0]
        # Verificamos si es un enlace de redirección de DuckDuckGo
        parsed = urllib.parse.urlparse(enlace)
        if parsed.path.startswith("/l/"):
            # Extraemos el parámetro 'uddg' que contiene la URL codificada
            params = urllib.parse.parse_qs(parsed.query)
            url = params.get("uddg", [None])[0]
            return url

def duck_Search(user):
    ls = user.split(' ')
    search = '+'.join(ls)
    url = f'https://duckduckgo.com/?t=h_&q={search}'
    return url
