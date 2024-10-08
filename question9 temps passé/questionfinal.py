import requests
from bs4 import BeautifulSoup
import time

# URL pour les citations aléatoires
url = "https://quotes.toscrape.com/random"

# Variables pour mesurer le temps
total_start_time = time.time()

# Nombre de citations à extraire
num_quotes = 100
all_quotes = set() 

while len(all_quotes) < num_quotes:
    # Envoyer la requête GET pour chaque citation
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erreur lors de la requête. Code de statut: {response.status_code}")
        continue

    # Parser le contenu avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    quote = soup.find('span', class_='text')
    author = soup.find('small', class_='author')

    if quote and author:
        all_quotes.add((quote.text, author.text))
        print(f"Citations collectées : {len(all_quotes)}")
    else:
        print("Erreur : impossible de trouver la citation ou l'auteur.")

# Temps total de scraping
total_end_time = time.time()
total_time = total_end_time - total_start_time

print(f"Nombre total de citations extraites : {len(all_quotes)}")
print(f"Temps total de scraping : {total_time:.2f} secondes")