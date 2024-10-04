import requests
from bs4 import BeautifulSoup

# URL de la première page
BASE_URL = "http://quotes.toscrape.com/"

def get_total_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # On cherche la balise avec la classe 'next' pour voir s'il y a des pages suivantes
    next_button = soup.find('li', class_='next')
    
    # Si on trouve un bouton "Next", c'est qu'il y a plus de pages
    page_number = 1
    while next_button:
        next_page_url = BASE_URL + next_button.find('a')['href']
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_button = soup.find('li', class_='next')
        page_number += 1
    
    return page_number

# Affiche le nombre total de pages
total_pages = get_total_pages(BASE_URL)
print(f"Nombre total de pages : {total_pages}")
