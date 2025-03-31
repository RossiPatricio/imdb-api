import requests
from bs4 import BeautifulSoup
from duck_search import *

def scrap_imdb(search):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    
    url = search
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
 
    title = soup.title.text.replace(' - IMDb', '').strip() 
    director = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
    resume = soup.find('span', class_='sc-42125d72-0 gKbnVu').text
    names = soup.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    crew= []
    for name in names[1:6]:
        crew.append(name.text)

    return (
        f"TITLE: {title}\n"
        f"DIRECTOR: {director}\n"
        f"SYNOPSIS: {resume}\n"
        f"{crew}\n"
        f"[{url}]"
    )
