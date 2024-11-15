# Divera2Loxone
Small Python REST Application for evaluating DIVERA 24/7 JSON Files and triggering URLs based on a simple logic

# Installation und Einrichtung der Flask-Anwendung

Diese Anleitung beschreibt die Schritte zur Installation und Konfiguration einer Flask-Anwendung, die HTTPS nutzt und auf einem Linux-Server wie Ubuntu läuft.

## 1. Python installieren und Python Abhängigkeiten

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y

pip3 install flask requests
```

## 2. Anpassen der Pfade und Umgebungen an das eigene System

## 3. Systemd Dienst erstellen 

## 4. Dienste neu laden, aktivieren und starten

```bash
sudo systemctl daemon-reload
sudo systemctl start ampelctl.service
sudo systemctl enable ampelctl.service
```
