from pythonosc import dispatcher, osc_server
import threading
from p5 import *

# Variables to hold the received coordinates
x_pos, y_pos = 300, 300  # Start in the center

# Function to handle OSC data, update x and y positions
def handle_osc_data(address, *args):
    print(f"Received data from {address}: {args}")
    global x_pos, y_pos
    # x_pos, y_pos = args  # Update position with received coordinates

    if len(args) >= 2:
        x_pos, y_pos = args[:2]  # Nimmt nur die ersten zwei Argumente
    else:
        print("Insufficient arguments received.")
    
    try:
        print(f"Received OSC message at {address} with arguments: {args}")
    except Exception as e:
        print(f"Error in handling OSC data: {e}")

# OSC client setup
def start_osc_server(ip="192.168.1.129", port=12345):
    disp = dispatcher.Dispatcher()
    disp.map("/hand", handle_osc_data)  # Expecting data on the "/hand" address

    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    print(f"OSC Server running on {ip}:{port}")
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True  # Stops server on main thread exit
    server_thread.start()

def setup():
    size(600, 600)
    no_stroke()
    # start_osc_server()  # Start the OSC server when the sketch begins

# p5 draw function
def draw():
    background(255)  # White background
    fill(0, 0, 255)  # Blue fill for the circle
    print(f"x_pos: {x_pos}, y_pos: {y_pos}")  # Debugging
    # Test mit festen Werten
    ellipse(x_pos, y_pos, 50, 50)
    no_loop()  # This stops the draw loop after one frame

  
# Start the p5 sketch
if __name__ == "__main__":
    run()
