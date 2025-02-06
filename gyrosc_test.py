from pythonosc import osc_server, dispatcher

def print_osc_message(address, *args):
    print(f"Received OSC message: {address} {args}")

if __name__ == "__main__":
    ip = "0.0.0.0"  # Listens on all available interfaces
    port = 7400  # Ensure this matches the port set in GyrOSC

    disp = dispatcher.Dispatcher()
    disp.set_default_handler(print_osc_message)

    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    print(f"Listening for OSC messages on {ip}:{port}...")
    server.serve_forever()
