# A Python script to read saved data from a CSV file and send it to Processing via OSC

import csv
import time
from pythonosc.udp_client import SimpleUDPClient

# OSC-Client einrichten
ip = "127.0.0.1"  # Localhost
port = 12000      # Port muss mit dem in Processing übereinstimmen
client = SimpleUDPClient(ip, port)

# CSV-Datei laden
csv_file = "/Users/vibe/Documents/A_CAS AICP/03_AI for Movement_Sensing_Realtime Interaction/Project_03/Beschleunigung ohne g 2024-11-18 20-19-21/Raw Data.csv"  # Stelle sicher, dass die Datei existiert

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Überspringt die Kopfzeile, falls vorhanden
    for row in reader:
        try:
            value = float(row[0])  # Nimmt an, dass die Werte in der ersten Spalte stehen
            print(f"Sende Wert: {value}")
            client.send_message("/data", value)
            time.sleep(0.1)  # Kurz warten, um eine realistische Datenrate zu simulieren
        except ValueError:
            print(f"Fehler beim Konvertieren: {row}")
