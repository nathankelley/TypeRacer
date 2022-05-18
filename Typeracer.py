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

    # We'll start the render, call our draw functions, and finish the render :)
    # rendered. make sure to have set_window() active prior to these commands otherwise they will be useless
    arcade.start_render()
    draw_background()
    arcade.finish_render()

    # Xander's Code for Key Input Retrieval
    # This should run outside of all other loops except for the main gameplay loop
    # The key 'Recieving input' is a simple check variable we can toggle between true and false for while the user is actively playing, as it will 
    #   decide if the keyboard inputs should be taken. I feel that we should have a point-and-click menu, something that benefits from this check.

    # This is the user input string that will be checked against the block of text that the user is racing to type // the 'block_of_text' on line 42&44-49 is a big placeholder 
    input_string = []
    block_of_text = "Superlative Stonks, to the moon go crazy! This is a test variable."

    # This is the comparison between the input string and the saved block of text
    for i in block_of_text:
        if block_of_text[i] == input_string[i]:
            pass
        else:
            print("Xander Test Comparison Block String Incomplete")

    # This is the function to recieve keypress input, more notes on how I plan to duplicate it for the rest of the table inside.
    def on_key_press(self, key, modifier):

        # Each of these if statements work to assess what key is pressed and edit the string appropriately 

        # Special Characters
        if key == arcade.key.COMMA:
            input_string.append(",")
        if key == arcade.key.PERIOD:
            input_string.append(".")
        if key == arcade.key.SPACE:
            input_string.append(" ")
        if key == arcade.key.SEMICOLON:
            input_string.append(";")
        if key == arcade.key.COLON:
            input_string.append(":")
        if key == arcade.key.DOUBLEQUOTE:
            input_string.append("\"")
        if key == arcade.key.EXCLAMATION:
            input_string.append("!")
        if key == arcade.key.QUESTION:
            input_string.append("?")
        if key == arcade.key.MINUS:
            input_string.append("-")

        # Character with special effect (remove)
        if key == arcade.key.BACKSPACE:
            input_string.pop()
            # This will remove the last item from the text

        # Alpha Characters (to be finished)
        if key == arcade.key.A:
            input_string.append("a")
        if key == arcade.key.B:
            input_string.append("b")

        # Neumeric Characters
        if key == arcade.key.KEY_0:
            input_string.append("0")
        if key == arcade.key.KEY_1:
            input_string.append("1")
        if key == arcade.key.KEY_2:
            input_string.append("2")
        if key == arcade.key.KEY_3:
            input_string.append("3")
        if key == arcade.key.KEY_4:
            input_string.append("4")
        if key == arcade.key.KEY_5:
            input_string.append("5")
        if key == arcade.key.KEY_6:
            input_string.append("6")
        if key == arcade.key.KEY_7:
            input_string.append("7")
        if key == arcade.key.KEY_8:
            input_string.append("8")
        if key == arcade.key.KEY_9:
            input_string.append("9")


    # This line will keep the window up until someone closes it
    arcade.run

else: 
    RUN_PROGRAM = False
