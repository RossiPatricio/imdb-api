import requests
from bs4 import BeautifulSoup
import urllib.parse

def duckduck(termino):
    url = f"https://duckduckgo.com/html/?q={termino}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    resultados = []

    for link in soup.select(".result__title a"):
        enlace = link["href"]
        resultados.append(enlace)

    return resultados[:1]

def duck_search(search):
    input = f'imdb {search}'
    result = duckduck(input)
    if result:
        enlace = result[0]
        # Verificamos si es un enlace de redirección de DuckDuckGo
        parsed = urllib.parse.urlparse(enlace)
        if parsed.path.startswith("/l/"):
            # Extraemos el parámetro 'uddg' que contiene la URL codificada
            params = urllib.parse.parse_qs(parsed.query)
            rott_url = params.get("uddg", [None])[0]
            return rott_url
