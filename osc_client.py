from pythonosc import dispatcher, osc_server
import threading

class OSCClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = None
        self.data = None  # Diese Variable speichert die empfangenen Daten

    def start(self):
        """Startet den OSC-Server."""
        dispatcher = self.create_dispatcher()
        server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), dispatcher)
        print(f"OSC Server läuft auf {self.ip}:{self.port}")
        server.serve_forever()

    def create_dispatcher(self):
        """Erstellt den Dispatcher, der OSC-Nachrichten abfängt und verarbeitet."""
        dispatcher = dispatcher.Dispatcher()
        # Hier definieren wir die Adresse (z. B. "/iphone") und die zugehörige Funktion
        dispatcher.map("/iphone", self.handle_iphone_data)
        return dispatcher

    def handle_iphone_data(self, address, *args):
        """Verarbeitet die OSC-Nachricht und speichert die Daten."""
        # Angenommen, die iPhone-Daten sind als X und Y Position übertragen:
        self.data = args
        print(f"Empfangene iPhone-Daten: {args}")

    def get_data(self):
        """Gibt die zuletzt empfangenen iPhone-Daten zurück."""
        return self.data