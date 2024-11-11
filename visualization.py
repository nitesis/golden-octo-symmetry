from particle import ParticleSystem
from p5 import *

class Visualization:
    def __init__(self, osc_client=None):
        self.osc_client = osc_client  # Optional, wenn du OSC verwenden möchtest
        self.particle_system = ParticleSystem()

    def setup(self):
        size(600, 600)  # Setze die Größe des Fensters
        no_stroke()  # Keine Konturen für die Partikel

    def draw(self):
        background(0)  # Hintergrund auf schwarz setzen

        # Partikel-Visualisierung
        self.particle_system.update()

    def handle_iphone_data(self, data):
        """
        Verarbeitet iPhone-Daten, die von OSC kommen, und beeinflusst die Partikel.
        Beispielsweise können die iPhone-Daten die Position der Partikel ändern.
        """
        print(f"Received iPhone data: {data}")
        x, y = data
        self.particle_system.create_particle(x, y)

    def handle_mouse_event(self, x, y):
        """
        Diese Funktion wird aufgerufen, wenn die Maus sich bewegt.
        Sie erzeugt neue Partikel basierend auf der Mausposition.
        """
        self.particle_system.create_particle(x, y)