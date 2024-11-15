# Divera2Loxone
Small Python REST Application for evaluating DIVERA 24/7 JSON Files and triggering URLs based on a simple logic. Originally this REST API was created to trigger Virtual Inputs on a Loxone Miniserver. But it can be used universally to trigger every URL via HTTP/GET. 
In this Version, only the fields ```groups``` and ```priority``` are recognized. You can simply add more Fields by editing the config.json and the main Code on div2lox.py

Format of the DIVERA24/7 JSON File: 
https://help.divera247.com/pages/viewpage.action?pageId=44171381

# Install this little Service

## 1. System Update and Python with the dependencies

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-venv python3-pip -y

pip3 install flask requests
```

## 2. Customize Path und Enviromnents to your personal needs

## 3. Create Systemd Daemon

## 4. Reload Daemons und start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable div2lox.service
sudo systemctl start div2lox.service
```
