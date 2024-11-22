from particle import ParticleSystem
from p5 import *

class Visualization:
    def __init__(self, osc_client=None):
        self.osc_client = osc_client  # Optional, wenn du OSC verwenden möchtest
        self.particle_system = ParticleSystem()

        if self.particle_system is None:
            print("particle_system is not initialized correctly.")

        if self.osc_client is None:
            print("osc_client is not initialized correctly.")   

    def setup(self):
        print("Setting up canvas")
        size(600, 600)  # Setze die Größe des Fensters
        no_stroke()  # Keine Konturen für die Partikel

    def draw(self):
        print("Drawing frame")  # Verify draw calls
        background(0)  # Hintergrund auf schwarz setzen
        self.particle_system.update()  # Partikel-Visualisierung

    def handle_iphone_data(self, data):
    
        # Verarbeitet iPhone-Daten, die von OSC kommen, und beeinflusst die Partikel.
        # Beispielsweise können die iPhone-Daten die Position der Partikel ändern.
        print(f"Received iPhone data: {data}")
        x, y = data
        self.particle_system.create_particle(x, y)


        