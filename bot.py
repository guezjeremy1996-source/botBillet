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
options.binary_location = "/usr/bin/chromium"  # chemin vers Chromium sur Render

# 🔹 Créer le driver Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Exemple simple : aller sur Google
driver.get("https://www.google.com")
print(driver.title)

# Attendre un peu pour voir le résultat (utile pour debug)
time.sleep(5)

driver.quit()
