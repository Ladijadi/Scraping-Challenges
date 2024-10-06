import requests
from bs4 import BeautifulSoup

# URL de la page
url = 'https://quotes.toscrape.com/filter.aspx'
url_search = 'https://quotes.toscrape.com/search.aspx'
page = requests.get(url_search)

# Session pour gérer les cookies et la session
session = requests.Session()

# Récupération du contenu de la page
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup_search = BeautifulSoup(page.content, 'html.parser')

# Extraction des valeurs de champs cachés comme __VIEWSTATE
viewstate = soup_search.find('input', {'name': '__VIEWSTATE'})['value']

# Données pour soumettre le formulaire
data = {
    'author': 'Albert Einstein',  # Nom de l'auteur choisi
    'tag': 'music',       # Exemple de tag, si applicable
    '__VIEWSTATE': viewstate,
    'submit_button': 'Search'
}

# Envoi de la requête POST
response = session.post(url, data=data)

# Affichage du contenu de la réponse
soup_result = BeautifulSoup(response.text, 'html.parser')
result = soup_result.find("div", class_="results")

# Récuperation de la citation
if result is not None:
    content = result.find("span", class_="content").text.strip()
    author = result.find("span", class_="author").text.strip()
    tag = result.find("span", class_="tag").text.strip()

    # Affichage du résultat
    print("L'unique citation est : ")
    print(content)
    print(f"Auteur : {author}")
    print(f"Tags : {tag}")