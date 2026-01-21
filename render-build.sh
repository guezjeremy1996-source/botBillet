#!/bin/bash
# Mettre à jour les paquets
apt-get update

# Installer Chromium et les dépendances pour Render
apt-get install -y chromium chromium-driver

# Exporter le chemin du binaire Chromium pour Selenium
export CHROME_BIN=/usr/bin/chromium
export PATH=$PATH:/usr/lib/chromium

# Installer les dépendances Python
pip install -r requirements.txt

# Lancer le bot
python bot.py
