from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL de la page initiale contenant les citations
URL = "https://quotes.toscrape.com/js/page/10/"

# Séparation de l'URL pour extraire la base de l'URL et le numéro de la page
parts = URL.split('/')
URL_base = '/'.join(parts[:-2]) + '/'
page_number = int(parts[-2])

# Initialisation du driver Selenium (utilisation de Google Chrome dans ce cas)
driver = webdriver.Chrome()

# Variable pour stocker la première citation trouvée
first_quote = None

try:
    # Variable pour suivre si l'on doit continuer à parcourir les pages précédentes
    previousElement = ""

    # Boucle tant qu'il existe une page précédente à parcourir
    while previousElement is not None:
        # Construire l'URL pour la page en cours
        url = URL_base + str(page_number)
        driver.get(url)  # Charger la page dans le navigateur

        # Attendre que l'élément contenant les citations soit chargé
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
        )

        # Récupérer le contenu HTML de la page
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, "html.parser")

        # Vérifier s'il y a un bouton "Previous" pour parcourir les pages précédentes
        previousElement = soup.find("li", class_="previous")

        # Extraire toutes les citations de la page actuelle
        quotes = soup.find_all("div", class_="quote")

        # Si des citations sont présentes sur cette page, prendre la première
        if len(quotes) > 0:
            quote = quotes[0]
            # Stocker les informations de la première citation trouvée
            first_quote = {
                "text": quote.find("span", class_="text").text.strip(),  # Texte de la citation
                "author": quote.find("small", class_="author").text.strip(),  # Auteur
                "tags": [tag.get_text() for tag in quote.find_all("a", class_="tag")]  # Liste des tags
            }

        # Décrémenter le numéro de la page pour passer à la page précédente
        page_number -= 1

finally:
    # Fermer le navigateur après avoir terminé le parcours
    driver.close()

    # Afficher la première citation trouvée si elle existe
    if first_quote:
        print("La première citation est :")
        print(f"Citation : {first_quote['text']}")
        print(f"Auteur : {first_quote['author']}")
        print(f"Tags : {first_quote['tags']}")
    else:
        print("Aucune citation trouvée.")
