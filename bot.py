import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ================= CONFIG =================

URL = "https://billets.stadefrance.com/selection/event/date?productId=10229597069844"
CHECK_INTERVAL = 5  # secondes

# 🔹 Tokens Pushover depuis les variables d'environnement
PUSHOVER_USER_KEY = os.environ["PUSHOVER_USER_KEY"]
PUSHOVER_APP_TOKEN = os.environ["PUSHOVER_APP_TOKEN"]

# ================= NOTIF =================

def send_push_notification(message):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message,
        "url": URL,
        "url_title": "Ouvrir la billetterie"
    }
    requests.post(url, data=data)

# ================= SELENIUM HEADLESS =================

options = Options()
options.add_argument("--headless")  # mode invisible
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.binary_location = "/usr/bin/chromium-browser"  # 🔹 chemin correct sur Render

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

print("Surveillance 24/7 démarrée...")
driver.get(URL)

while True:
    try:
        time.sleep(3)
        body_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        if "non disponible" not in body_text:
            print("🎫 BILLETS DISPONIBLES !!!")
            send_push_notification("🎫 Billets disponibles !")
            break
        else:
            print("Toujours indisponible...")

        time.sleep(CHECK_INTERVAL)
        driver.refresh()

    except Exception as e:
        print("Erreur :", e)
        time.sleep(CHECK_INTERVAL)

driver.quit()
