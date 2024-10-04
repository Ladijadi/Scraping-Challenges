import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/js/page/10/'

# Requête GET pour la page
response = requests.get(url)

# Vérification de la réponse
if response.status_code == 200:
    # Analyser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver la première citation
    first_quote = soup.find('div', class_='quote')
    
    if first_quote:
        quote_text = first_quote.find('span', class_='text').get_text()
        quote_author = first_quote.find('small', class_='author').get_text()
        print(f'La première citation est : "{quote_text}" - {quote_author}')
    else:
        print("Aucune citation trouvée.")
else:
    print("Erreur lors de la récupération de la page.")
