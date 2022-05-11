## Library imports go Here
import arcade


## Constants: This will be for the screen that the program opens a new window of
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Typeracer"

def draw_background():
    # This draws the background to fill the screen

    arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT,arcade.color.WHITE_SMOKE)

def draw_actors():
    # When we create items to draw onto the background, lets put them into an array/list
    # and then we can draw the whole list here!

    arcade.draw_actors()

# this line takes all the things we've asked arcade to draw, and prints them-
# imagine the draw commands prior to this have been a queue and now they are being
# rendered
arcade.finish_render()




# This line will keep the window up until someone closes it
arcade.run

