import requests
from bs4 import BeautifulSoup

# URL de la page de connexion
login_url = 'https://quotes.toscrape.com/login'  # Remplacez par l'URL réelle

# Créer une session
session = requests.Session()

# Récupérer le formulaire et le jeton CSRF
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Données du formulaire
payload = {
    'csrf_token': csrf_token,
    'username': 'votre_nom_utilisateur',
    'password': 'votre_mot_de_passe'
}

# Soumettre le formulaire
response = session.post(login_url, data=payload)

# Vérifier si la connexion a réussi
if 'Logout' in response.text:  # Vérifiez un élément de page qui apparaît après connexion
    print("Connexion réussie")
else:
    print("Échec de la connexion")
