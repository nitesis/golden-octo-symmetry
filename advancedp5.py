from pythonosc import dispatcher, osc_server
from p5 import *
import threading

# Global variables for circle position
circle_x = 300
circle_y = 300

# p5 setup function
def setup():
    size(600, 600)
    no_stroke()
    start_osc_server()  # Start OSC server in setup

# p5 draw function
def draw():
    global circle_x, circle_y
    background(240)
    fill(circle_x % 255, 100, 200)
    circle_size = 20 + circle_y / 10
    circle((circle_x, circle_y), circle_size)
    print(f"x_pos: {circle_x}, y_pos: {circle_y}")  # Debugging

# OSC message handler
def handle_osc_message(address, *args):
    global circle_x, circle_y
    if address == '/gyro':
        circle_x, circle_y = args[0], args[1]
        print(f"Received OSC message with x: {circle_x}, y: {circle_y}")

# Set up the OSC server
def start_osc_server(ip="127.0.0.1", port=12345):
    disp = dispatcher.Dispatcher()
    disp.map("/gyro", handle_osc_message)  # Map OSC messages at /circle to the handler
    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    print(f"OSC Server is running on {ip}:{port}")
    # Start the server in a separate thread so it doesn't block the p5 window
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()



# Run the p5 application
run()
