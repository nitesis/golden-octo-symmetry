from p5 import *

# Set up the canvas and initialize any variables
def setup():
    size(600, 600)  # Create a 600x600 canvas
    no_stroke()  # Disable outline for shapes

# This function will be called repeatedly to draw on the canvas
def draw():
    background(240)  # Light grey background
    # The circle changes color based on the mouse's x-position
    fill(255, 100, 200)
    # The circle changes size based on the mouse's y-position
    circle_size = 20
    # Draw the circle at the mouse's position
    circle((100, 100), circle_size)

# Run the p5 application
run()