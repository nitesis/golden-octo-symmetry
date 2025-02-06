from pythonosc import osc_server, dispatcher
from p5 import *
import threading

# Global variables for visualization
x_pos, y_pos = 300, 300
gyro_x, gyro_y = 0, 0  # Variables to store GyrOSC data

# OSC message handler
def osc_handler(address, *args):
    global gyro_x, gyro_y
    if address == "/gyro":
        gyro_x, gyro_y = args[0], args[1]  # Use first two values for movement

# Start OSC server in a separate thread
def start_osc_server():
    ip, port = "0.0.0.0", 7400  # Ensure this port matches GyrOSC settings
    disp = dispatcher.Dispatcher()
    disp.map("/gyro", osc_handler)  # Listen for gyroscope data

    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    print(f"Listening for OSC messages on {ip}:{port}...")
    server.serve_forever()

# Start the OSC server thread
threading.Thread(target=start_osc_server, daemon=True).start()

# p5 Visualization
def setup():
    size(600, 600)
    no_stroke()

def draw():
    global x_pos, y_pos, gyro_x, gyro_y
    background(255)

    # Update position based on gyro data
    x_pos += gyro_x * 10  # Adjust sensitivity
    y_pos += gyro_y * 10  

    # Keep within bounds
    x_pos = constrain(x_pos, 0, width)
    y_pos = constrain(y_pos, 0, height)

    fill(0, 0, 255)
    ellipse(x_pos, y_pos, 50, 50)

# Run the p5 sketch
if __name__ == "__main__":
    run()
