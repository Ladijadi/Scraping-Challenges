import requests

api_url = 'https://quotes.toscrape.com/api/quotes?page='

page = 1
quotes = []
has_next_page = True

while has_next_page:
    # Requête GET pour chaque page
    response = requests.get(api_url + str(page))
    data = response.json()  # On obtient la réponse en JSON

    quotes.extend(data['quotes'])

    has_next_page = data['has_next']
    page += 1  # Passe à la page suivante

# Affiche le nombre total de citations
total_quotes = len(quotes)
print(f"Nombre total de citations : {total_quotes}")
