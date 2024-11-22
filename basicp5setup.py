from p5 import *
from pythonosc import dispatcher, osc_server
import threading

# Variables for circle position
x_pos, y_pos = 250, 250

def setup():
    """Setup the canvas and OSC server."""
    size(500, 500)
    no_stroke()
    # Start OSC server in a separate thread
    threading.Thread(target=start_osc_server, daemon=True).start()

def draw():
    """Draw the circle and text."""
    global x_pos, y_pos
    background(0, 0, 255)  # Blue background
    fill(0, 255, 0)        # Green circle
    ellipse(x_pos, y_pos, 100, 100)
    fill(0)                # Black text
    text("I'm p5.py", (x_pos - 25, y_pos))

def osc_message_handler(address, *args):
    """Handle incoming OSC messages."""
    global x_pos, y_pos
    print(f"Received OSC: {address}, {args}")
    if address == '/gyro':
        x_pos, y_pos = args[0], args[1]

def start_osc_server():
    """Start the OSC server."""
    dispatcher_map = dispatcher.Dispatcher()
    dispatcher_map.map("/test", osc_message_handler)

    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 12345), dispatcher_map)
    print("OSC server started on port 12345")
    server.serve_forever()

if __name__ == "__main__":
    run()
