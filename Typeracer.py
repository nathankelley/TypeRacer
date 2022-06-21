## Library imports go Here
import arcade

## Constants: This will be for the screen that the program opens a new window of
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "Typeracer"
RUN_PROGRAM = True

while RUN_PROGRAM:
    
    # get out of program when no longer playing
    if RUN_PROGRAM == False:
        print("Thanks for playing!")
        break
        

    def draw_background():
        # This draws the background to fill the screen

        arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT,arcade.color.WHITE_SMOKE)

    def draw_actors():
        # When we create items to draw onto the background, lets put them into an array/list
        # and then we can draw the whole list here!

        arcade.draw_actors()

    # This line will keep the window up until someone closes it
    arcade.run

else: 
    RUN_PROGRAM = False
