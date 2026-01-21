#!/bin/bash
# Installer Chromium
apt-get update
apt-get install -y chromium

# Lancer le bot
python bot.py
