import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Konfiguration laden
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

config = load_config()

# HTTPS-Listener
@app.route('/api', methods=['POST'])
def handle_request():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # Gruppen als Set extrahieren
    groups = set(data.get("group", []))

    # Priority als Set extrahieren, auch wenn es nur ein einzelner Wert ist
    priority = data.get("priority", None)
    if isinstance(priority, int):
        priority = {priority}  # In ein Set umwandeln, falls es ein einzelner Wert ist
    elif isinstance(priority, list):
        priority = set(priority)  # In ein Set umwandeln, falls es eine Liste ist
    else:
        priority = set()  # Leeres Set, falls kein gültiger Wert gefunden wird

    # URLs für Gruppenbedingungen auswählen
    urls_to_call = []
    for rule in config["groups"]:
        required_groups = set(rule["required_groups"])
        if required_groups.issubset(groups):
            urls_to_call.extend(rule["urls"])
            break  # Keine weiteren Regeln prüfen, sobald eine Bedingung erfüllt ist

    # URLs für Priority-Wert auswählen
    for rule in config.get("priority", []):
        required_priority = set(rule["required_priority"])
        if required_priority.issubset(priority):
            urls_to_call.extend(rule["urls"])
            break  # Nur die erste passende Priority-Bedingung verwenden

    # URLs aufrufen und Ergebnisse speichern
    results = {}
    for url in urls_to_call:
        if url:  # Nur nicht-leere URLs aufrufen
            try:
                response = requests.get(url)
                results[url] = response.status_code if response.status_code == 200 else f"Failed with {response.status_code}"
            except requests.RequestException as e:
                results[url] = f"Error: {str(e)}"

    return jsonify({"results": results}), 200

if __name__ == "__main__":
    app.run(ssl_context=(config["server"]["ssl_certificate"], config["server"]["ssl_key"]),
            host=config["server"]["host"], port=config["server"]["port"])
