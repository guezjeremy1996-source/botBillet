#!/bin/bash
# Mettre à jour les paquets
apt-get update

# Installer Chromium et le driver
apt-get install -y chromium chromium-driver

# Définir la variable d'environnement pour Selenium
export CHROME_BIN=/usr/bin/chromium

# Installer les dépendances Python
pip install -r requirements.txt

# Lancer le bot
python bot.py
