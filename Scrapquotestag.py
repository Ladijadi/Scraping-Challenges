from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter
import time

# Initialisation du driver Selenium (utilisation de Google Chrome)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Décommenter pour exécuter en mode sans tête
driver = webdriver.Chrome(options=options)

# URL de la page à scraper
URL = "https://quotes.toscrape.com/tableful/"

try:
    # Accéder à la page
    driver.get(URL)

    # Attendre que le corps de la page soit complètement chargé
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Ajouter un délai fixe pour s'assurer que tout est bien chargé
    time.sleep(5)

    # Attendre que les éléments contenant les citations soient présents
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
    )

    # Récupérer le contenu HTML de la page
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")

    # Extraire toutes les citations et leurs tags
    quotes = soup.find_all("div", class_="quote")
    tags = []

    for quote in quotes:
        # Récupérer tous les tags associés à chaque citation
        quote_tags = quote.find_all("a", class_="tag")
        tags.extend([tag.get_text() for tag in quote_tags])

    # Compter la fréquence des tags
    tag_counter = Counter(tags)

    # Afficher le tag le plus fréquent
    most_common_tag = tag_counter.most_common(1)
    if most_common_tag:
        print(f"Le tag le plus répétitif est : {most_common_tag[0][0]} avec {most_common_tag[0][1]} occurrences.")
    else:
        print("Aucun tag trouvé.")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")

finally:
    # Fermer le driver après l'exécution
    driver.quit()
