from osc_client import OSCClient
from visualization import Visualization
import threading
from p5 import run_sketch  # Importiere p5 für die Visualisierung
import osc
import p5

print("Pakete erfolgreich geladen!")


def start_osc_server():
    # Initialisiere den OSC-Client (mit der IP-Adresse und dem Port des OSC-Servers)
    osc_client = OSCClient(ip="192.168.1.100", port=8000)
    
    # Starte den OSC-Server in einem separaten Thread
    osc_thread = threading.Thread(target=osc_client.start)
    osc_thread.daemon = True  # Der Thread wird beendet, wenn das Hauptprogramm beendet wird
    osc_thread.start()

    return osc_client

def setup_visualization(osc_client):
    # Initialisiere die Visualisierung und übergebe den OSC-Client
    visualization = Visualization(osc_client)
    return visualization

def run():
    # Starte den OSC-Server und erhalte den OSC-Client
    osc_client = start_osc_server()

    # Initialisiere die Visualisierung mit dem OSC-Client
    visualization = setup_visualization(osc_client)
    
    # Starte die p5-Visualisierung
    run_sketch(visualization)

if __name__ == "__main__":
    run()
