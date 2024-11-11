from p5 import run, setup, draw
from visualization import Visualization
from osc_client import OSCClient

def main():
    # OSCClient für die Kommunikation mit dem iPhone
    osc_client = OSCClient(ip="192.168.1.100", port=8000)  # IP-Adresse des iPhones

    # Visualisierungsklasse initialisieren
    visualization = Visualization(osc_client)

    # Setup und Draw Methoden für p5
    def p5_setup():
        visualization.setup()

    def p5_draw():
        visualization.draw()

    run()

if __name__ == "__main__":
    main()