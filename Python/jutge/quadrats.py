'''DIBUIXANT ELEMENTS
La llibreria arcade disposa d'unes primitives (funcions de dibuix) que ens permeten dibuixar:'''
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 300, 300, 0, arcade.csscolor.DARK_BLUE)
arcade.draw_lrtb_rectangle_filled(300, 600, 300, 0, arcade.csscolor.PINK)
arcade.draw_lrtb_rectangle_filled(0, 300, 600, 300, arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(300, 600, 600, 300, arcade.csscolor.YELLOW)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()