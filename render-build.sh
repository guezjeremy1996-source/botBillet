#!/bin/bash
# Mettre à jour les paquets
apt-get update

# Installer Chromium et ChromeDriver
apt-get install -y chromium-browser chromium-chromedriver

# Lancer le bot
python bot.py
