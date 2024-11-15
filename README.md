# Divera2Loxone
Small Python REST Application running on Linux (tested with Ubuntu 22.04) creating an Endpoint ```/api``` for evaluating DIVERA 24/7 JSON Files and triggering URLs based on a simple logic. Originally this REST API was created to trigger Virtual Inputs on a Loxone Miniserver. But it can be used universally to trigger every URL via HTTP/GET. 
In this Version, only the fields ```groups``` and ```priority``` are recognized. You can simply add more fields by editing the config.json and the main Code on ```div2lox.py```

Format of the DIVERA24/7 JSON File: 
https://help.divera247.com/pages/viewpage.action?pageId=44171381

**You might consider running this Service behind a nginx reverse proxy due to security reasons.** 

# Install this little Service
Copy the Folder Div2Lox on a location on your Filesystem where you want to run the Service, e.g. ```/opt/div2lox/```

## 1. System Update and Python with the dependencies

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-venv python3-pip -y

pip3 install flask requests
```

## 2. Customize Path und Enviromnents to your personal needs
Check paths, ports, SSL Certificates etc. in the ```config.json``` and customize them to your needs. 

## 3. Create Systemd Daemon
Copy ```div2lox.service``` to ```/etc/systemd/system``` and customize User, Group and the paths to your needs. 

## 4. Reload Daemons und start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable div2lox.service
sudo systemctl start div2lox.service
```
## 5. Test your Service
You can simply test your Endpoint with cURL on your commandline:
```bash
curl -k -X POST https://yourhostorip:yourport/api \
-H "Content-Type: application/json" \
-d '{
  "group": ["12345", "123456"],
  "priority": 1
}'
```

## 5. Make Changes
After every change on your ```config.json``` or your main ```div2lox.py``` you will need to restart your service using:
```bash
sudo systemctl restart div2lox.service
```
