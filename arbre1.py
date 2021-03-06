"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
lkllll
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()