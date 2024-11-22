from osc_client import OSCClient
from visualization import Visualization
import threading
from p5 import *  # Importiere p5 für die Visualisierung

print("Pakete erfolgreich geladen!")

visualization = None  # Global instance of Visualization to link with p5

def setup():
    global visualization
    if visualization is not None:
        visualization.setup()

def draw():
    global visualization
    if visualization is not None:
        visualization.draw()

def start_osc_server():
    # Initialisiere den OSC-Client (mit der IP-Adresse und dem Port des OSC-Servers)
    osc_client = OSCClient(ip="127.0.0.1", port=12345)

    if osc_client is None:
        print("Failed to initialize OSC client.")
    
    # Starte den OSC-Server in einem separaten Thread
    osc_thread = threading.Thread(target=osc_client.start)
    osc_thread.daemon = True  # Der Thread wird beendet, wenn das Hauptprogramm beendet wird
    osc_thread.start()

    return osc_client

def setup_visualization(osc_client):
    # Initialisiere die Visualisierung und übergebe den OSC-Client
    visualization = Visualization(osc_client)

    if visualization is None:
        print("Visualization setup failed.")

    return visualization

def run_visualization():
    # Starte den OSC-Server und erhalte den OSC-Client
    osc_client = start_osc_server()

    # Initialisiere die Visualisierung mit dem OSC-Client
    visualization = setup_visualization(osc_client)
    
    # Starte die p5-Visualisierung
    run() 

if __name__ == "__main__":
    run_visualization()
