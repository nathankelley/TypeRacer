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

# We'll start the render, call our draw functions, and finish the render :)
# rendered. make sure to have set_window() active prior to these commands otherwise they will be useless
arcade.start_render()
draw_background()
arcade.finish_render()

# Xander's Code for Key Input Retrieval
# This should run outside of all other loops except for the main gameplay loop
# The key 'Recieving input' is a simple check variable we can toggle between true and false for while the user is actively playing, as it will 
#   decide if the keyboard inputs should be taken. I feel that we should have a point-and-click menu, something that benefits from this check.

# This is the user input string that will be checked against the block of text that the user is racing to type
input_string = []

# This is the function to recieve keypress input, more notes on how I plan to duplicate it for the rest of the table inside.
def on_key_press(self, key, modifier):

    if key == arcade.key.A:

        print("A has been pressed")
        # A temporary test to show that on press works
        # once we have the spacing finalized I'll create a table to recieve input for each key

        input_string.append("a")



# This line will keep the window up until someone closes it
arcade.run

