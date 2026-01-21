from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# 🔹 Options Chrome pour Render
options = Options()
options.add_argument("--headless")  # mode sans interface graphique
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 🔹 Récupérer le chemin du binaire Chromium depuis l'environnement
chrome_bin = os.environ.get("CHROME_BIN", "/usr/bin/chromium")
options.binary_location = chrome_bin

# 🔹 Créer le driver Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Exemple simple : aller sur Google
driver.get("https://www.google.com")
print("Titre de la page :", driver.title)

# Attendre un peu pour debug
time.sleep(5)

driver.quit()
