from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import requests

# 🔹 Lire les clés Pushover depuis les variables d'environnement
PUSHOVER_APP_TOKEN = os.getenv("PUSHOVER_APP_TOKEN")
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")

# Vérifier que les clés sont bien présentes
if not PUSHOVER_APP_TOKEN or not PUSHOVER_USER_KEY:
    raise Exception("PUSHOVER_APP_TOKEN ou PUSHOVER_USER_KEY manquant !")

# 🔹 Options Chrome pour Render
options = Options()
options.add_argument("--headless")  # mode sans interface graphique
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium"  # chemin vers Chromium sur Render

# 🔹 Créer le driver Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Exemple simple : aller sur Google
driver.get("https://www.google.com")
print(driver.title)

# 🔹 Exemple d'envoi d'une notification Pushover
def send_pushover(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": PUSHOVER_APP_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message
        }
    )

send_pushover("Bot démarré avec succès !")

# Attendre un peu pour debug
time.sleep(5)
driver.quit()
