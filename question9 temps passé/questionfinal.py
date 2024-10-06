import requests
from bs4 import BeautifulSoup

# URL pour les citations aléatoires
url = "https://quotes.toscrape.com/random"

# Envoyer la requête GET pour chaque citation
response = requests.get(url)

# Parser le contenu avec BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extraire la citation et l'auteur
quote = soup.find('span', class_='text').text
author = soup.find('small', class_='author').text

print(f"Citation : {quote}\nAuteur : {author}")
