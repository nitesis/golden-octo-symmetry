from pythonosc import dispatcher as osc_dispatcher, osc_server
from threading import *

class OSCClient:
    # Diese Methode initialisiert die Klasse mit der IP-Adresse und dem Port, auf denen der OSC-Server laufen soll.
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = None
        self.data = None  # Diese Variable speichert die empfangenen Daten

    # Startet den OSC-Server, der auf eingehende OSC-Nachrichten wartet.
    def start(self):
        dispatcher_instance = self.create_dispatcher() 
        server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), dispatcher_instance)
        print(f"OSC Server läuft auf {self.ip}:{self.port}")
        server.serve_forever()

    # Erstellt den Dispatcher, der die eingehenden OSC-Nachrichten an die entsprechenden Handler weiterleitet. 
    # In diesem Fall wird die Adresse "/iphone" mit der Methode handle_iphone_data verbunden.
    def create_dispatcher(self):
        dispatcher_instance = osc_dispatcher.Dispatcher() 
        # Hier definieren wir die Adresse (z. B. "/iphone") und die zugehörige Funktion
        dispatcher_instance.map("/iphone", self.handle_iphone_data)
        return dispatcher_instance

    # Diese Methode wird aufgerufen, wenn eine OSC-Nachricht an die Adresse "/iphone" gesendet wird. 
    # Sie speichert die empfangenen Daten (in diesem Fall die x- und y-Koordinaten) in der data-Variable.
    def handle_iphone_data(self, address, *args):
        # Verarbeitet die OSC-Nachricht und speichert die Daten.
        # Angenommen, die iPhone-Daten sind als X und Y Position übertragen:
        self.data = args
        print(f"Empfangene iPhone-Daten: {args}")

    # Gibt die zuletzt empfangenen Daten zurück. 
    # Dies kann in anderen Teilen des Programms verwendet werden, um mit den iPhone-Daten zu interagieren.
    def get_data(self):
        # Gibt die zuletzt empfangenen iPhone-Daten zurück.
        return self.data
