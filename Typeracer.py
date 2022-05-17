## Library imports go Here
import arcade


## Constants: This will be for the screen that the program opens a new window of
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "Typeracer"

def draw_background():
    # This draws the background to fill the screen

    # arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT,arcade.color.WHITE_SMOKE)
        arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 3),
                                      arcade.color.SKY_BLUE)

    # Draw the ground in the bottom third
        arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)

def draw_actors():
    # When we create items to draw onto the background, lets put them into an array/list
    # and then we can draw the whole list here!

    arcade.draw_actors()

# We'll start the render, call our draw functions, and finish the render :)
# rendered. make sure to have set_window() active prior to these commands otherwise they will be useless
arcade.start_render()
draw_background()
arcade.finish_render()




# This line will keep the window up until someone closes it
arcade.run

