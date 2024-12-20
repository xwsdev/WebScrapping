import requests
from bs4 import BeautifulSoup

# URL de la première page (à adapter selon le site que vous scrappez)
base_url = "https://exemple.com/page="  # Remplacez par l'URL réelle

# Fonction pour scrapper une seule page
def scrape_page(page_number):
    url = base_url + str(page_number)
    print(f"Scraping de la page {page_number}: {url}")
    
    # Envoyer une requête GET pour récupérer le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête a réussi (code HTTP 200)
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page {page_number}, statut HTTP: {response.status_code}")
        return None

    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemple : Récupérer tous les titres d'articles dans des balises <h2> avec la classe 'article-title'
    titles = soup.find_all('h2', class_='article-title')

    # Si des titres sont trouvés, les afficher
    if titles:
        for idx, title in enumerate(titles, 1):
            print(f"Page {page_number} - Article {idx}: {title.get_text(strip=True)}")
    else:
        print(f"Aucun titre trouvé sur la page {page_number}.")
    
    return soup  # Retourner le soup pour les prochaines pages si nécessaire

# Fonction pour gérer la pagination
def scrape_all_pages(start_page, end_page):
    for page in range(start_page, end_page + 1):
        scrape_page(page)

# Exemple d'utilisation : scrapper de la page 1 à la page 5
scrape_all_pages(1, 5)
