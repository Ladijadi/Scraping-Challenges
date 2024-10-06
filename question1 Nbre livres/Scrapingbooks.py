import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL de la page principale
BASE_URL = "https://books.toscrape.com/"

# Fonction pour obtenir le contenu HTML d'une page
def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

# Fonction pour extraire toutes les catégories de livres
def get_categories(soup):
    categories = {}
    category_list = soup.find('ul', class_='nav-list').find('ul').find_all('li')
    
    for category in category_list:
        category_name = category.get_text(strip=True)
        category_url = BASE_URL + category.find('a')['href']
        categories[category_name] = category_url
    
    return categories

# Fonction pour récupérer le nombre de livres et le prix moyen d'une catégorie
def get_books_info(category_url):
    soup = get_soup(category_url)
    books = soup.find_all('article', class_='product_pod')
    
    total_price = 0
    book_count = 0

    while True:
        for book in books:
            price = book.find('p', class_='price_color').get_text()
            price = float(re.sub(r'[^0-9.]', '', price))  # Suppression des symboles pour ne garder que le prix
            total_price += price
            book_count += 1

        # Passer à la page suivante si elle existe
        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = category_url.rsplit('/', 1)[0] + '/' + next_button.find('a')['href']
            soup = get_soup(next_url)
            books = soup.find_all('article', class_='product_pod')
        else:
            break

    # Calcul du prix moyen
    average_price = total_price / book_count if book_count > 0 else 0
    return book_count, average_price

# Scraping des catégories et des infos
def scrape_books():
    main_soup = get_soup(BASE_URL)
    categories = get_categories(main_soup)

# Liste pour stocker les résultats
    category_data = []

    for category, url in categories.items():
        book_count, average_price = get_books_info(url)
        # Ajouter les données à la liste
        category_data.append((category, book_count, average_price))
        
#Créer une DataFrame à partir des résultats
    df = pd.DataFrame(category_data, columns=['Categorie', 'Numbre de livres', 'Prix moyen'])

  # Afficher la DataFrame
    print(df)
# Exécution du script
scrape_books()