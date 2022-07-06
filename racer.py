import arcade
import menu
from random import randint

timer_running = False
input_string = []
#this is a ~~surprise tool~~ global variable that is needed for processing and passing the users input



control_text = "This is the control text! I live on line 7. Try typing this sentance out and see what happens!"

with open('texts/text.txt') as txt:
    control_text = txt.read()
    txt.close()

# this pulls the text from the file

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RacingLane:
    def __init__(self, x, y, image_path ):
        self.center = Point(x, y)
        self.length = 600
        self.texture = arcade.load_texture(image_path)  
        self.width = 50
    def draw(self): 
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.length, self.width, self.texture)   
                
class MovingObject:
    def __init__(self, image_path):
        self.center = Point(0,0) 
        self.lane = None
        self.percentage = 0
        self.texture = arcade.load_texture(image_path)
    def set_lane(self, lane):
        self.lane = lane
        self.center.y = self.lane.center.y
        self.percentage = 0 
    
    def update(self):
        self.center.x = (self.lane.center.x - self.lane.length/2) + (self.lane.length * self.percentage)
                 
    def draw(self): 
        arcade.draw_texture_rectangle(self.center.x, self.center.y, 50, 50, self.texture, -90) 

class Text_Box:
    def __init__(self,x, y, width, text):
        self.width = width
        self.center = Point(x, y)
        self.text = arcade.Text(text, self.center.x, self.center.y, arcade.color.BLACK_BEAN, font_size=15, width=self.width-20, anchor_x="center", anchor_y="center", multiline=True)
        
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.width, self.text.content_height+20, arcade.color.WHITE)  
        self.text.draw() 

class Racer_Window(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMARANTH_PINK)        
        
        self.total_time = 0.0
        self.timer_running = False
        
        moving_object_3 = MovingObject(":resources:images/space_shooter/playerShip1_blue.png")
        racing_lane_3 = RacingLane(self.width/2, self.height - 100, ":resources:images/backgrounds/abstract_1.jpg")
        moving_object_3.set_lane(racing_lane_3)
        
        self.text_box = Text_Box(self.width/2, self.height/2, self.width - 20, control_text)
        self.user_box = Text_Box(self.width/2, self.height/2 - 100, self.width - 20, "")
        self.wpm_box = Text_Box(self.width/2, self.height/2 - 200, self.width/8, "")

        self.moving_objects = [moving_object_3]
        self.racing_lanes = [racing_lane_3]
        
        # set up the text file for the user
        
    def on_update(self, delta_time):
        # constantly updating the user text box to reflect what they are typing
        self.user_box.text = self.text = arcade.Text("".join(input_string), self.user_box.center.x, self.user_box.center.y, arcade.color.BLACK_BEAN, font_size=15, width=self.width-20, anchor_x="center", anchor_y="center", multiline=True)
        self.user_box.draw()

        # this is the code that on update will compate the user input to the text box to see what % of the passage they have typed
        # if you change the global variable control_text please update this input as well, thanks!
        ship_move_percent = self.compare_strings(input_string,control_text)

        # basic implementation of ship percentage bar
        for moving_object in self.moving_objects:
                moving_object.update()
                if moving_object.percentage < 1 : 
                    # if the object isnt at 100% then we do the following:
                    moving_object.percentage = ship_move_percent

        # basic implementation of wpm calculation
        # counting the " " (space) characters in the correct-text tells us how many words the user has written.
        # first we need a basic accumulation of time (using the delta_time input for the on_update class!)
        minutes = 0
        wpm = 0
        if (self.timer_running):
            self.total_time += delta_time
            minutes = int(self.total_time) / 60

        # now we find how many words the user has written:
        words = self.calculate_words(input_string, control_text)
        if minutes != 0:
            wpm = round(words / minutes)
            # uncomment the below command text for a real-time update of your wpm printed in the terminal for debugging purposes
            # print(wpm) 
            self.wpm_box.draw()
        
        # Once we find a good spot to draw() the wpm on the screen we'll write the code to update it's value here:
        self.wpm_box.text = arcade.Text("".join("wpm: "+ str(wpm)), self.wpm_box.center.x, self.wpm_box.center.y, arcade.color.BLACK_BEAN, font_size=10, width=60, anchor_x="center", anchor_y="center")
        

        if (("".join(input_string)) == control_text):
            menu.GameOverView().on_draw()
            print("The texts were identical, program exiting because no 'you win' is implemented yet. See line 83 (as of 6/7/2022)")
            
            
    def on_draw(self):
        arcade.start_render()
        for racing_lane in self.racing_lanes:
            racing_lane.draw()
        for moving_object in self.moving_objects:
                moving_object.draw()  
        self.text_box.draw()     
        self.user_box.draw()    
        self.wpm_box.draw()    

    
        
    
    def compare_strings(self, string1, string2):
        # pass user input as string1, and use the text box as string2
        counter = 0
        for i in string1:
            if i == string2[counter]:
                counter += 1
            else:
                # once we've hit a wrong letter we stop the increments
                break
        percent = counter / len(string2)
        return percent

    def calculate_words(self, string1, string2):
        counter = 0
        spaces = 0
        for i in string1:
            if i == string2[counter]:
                counter += 1
                if i == " ":
                    spaces += 1
            else:
                # once we've hit a wrong letter we stop the increments
                break
        # The space is added after the word is completed, so returning the number of spaces from the correct string list will
        # guarantee that we have the number of total words completed.    
        return spaces
        


    def on_key_press(self, key, modifiers):

        # As soon as the first key is pressed, we start counting for wpm:
        self.timer_running = True

        # Each of these if statements work to assess what key is pressed and edit the string appropriately 

        # Special Characters
        if key == arcade.key.COMMA:
            input_string.append(",")
        elif key == arcade.key.PERIOD:
            input_string.append(".")
        elif key == arcade.key.SPACE:
            input_string.append(" ")
        elif key == arcade.key.SEMICOLON:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append(":")
            else:
                input_string.append(";")
        elif key == arcade.key.BACKSLASH:
            input_string.append("\\")
        elif key == arcade.key.SLASH:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("?")
            else:
                input_string.append("/")
        elif key == arcade.key.MINUS:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("_")
            else:
                input_string.append("-")
        elif key == arcade.key.QUOTELEFT:
            #PYTHON ARCADE PACKAGE IS UNABLE TO DETECT QUOTATION INPUT
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("\"")
            else:
                input_string.append("\'")


        # this is a helpful key for testing purposes, TK remove once polished.
        elif key == arcade.key.ENTER:
            print("".join(input_string))
        


        # Character with special effect (remove)
        elif key == arcade.key.BACKSPACE:
            input_string.pop()
            # This will remove the last item from the text

        # Alpha Characters (finished)
        elif key == arcade.key.A:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("A")
            else:
                input_string.append("a")
        elif key == arcade.key.B:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("B")
            else:
                input_string.append("b")
        elif key == arcade.key.C:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("C")
            else:
                input_string.append("c")
        elif key == arcade.key.D:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("D")
            else:
                input_string.append("d")
        elif key == arcade.key.E:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("E")
            else:
                input_string.append("e")
        elif key == arcade.key.F:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("F")
            else:
                input_string.append("f")
        elif key == arcade.key.G:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("G")
            else:
                input_string.append("g")
        elif key == arcade.key.H:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("H")
            else:
                input_string.append("h")
        elif key == arcade.key.I:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("I")
            else:
                input_string.append("i")
        elif key == arcade.key.J:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("J")
            else:
                input_string.append("j")
        elif key == arcade.key.K:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("K")
            else:
                input_string.append("k")
        elif key == arcade.key.L:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("L")
            else:
                input_string.append("l")
        elif key == arcade.key.M:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("M")
            else:
                input_string.append("m")
        elif key == arcade.key.N:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("N")
            else:
                input_string.append("n")
        elif key == arcade.key.O:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("O")
            else:
                input_string.append("o")
        elif key == arcade.key.P:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("P")
            else:
                input_string.append("p")
        elif key == arcade.key.Q:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("Q")
            else:
                input_string.append("q")
        elif key == arcade.key.R:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("R")
            else:
                input_string.append("r")
        elif key == arcade.key.S:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("S")
            else:
               input_string.append("s")
        elif key == arcade.key.T:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("T")
            else:
               input_string.append("t")
        elif key == arcade.key.U:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("U")
            else:
                input_string.append("u")
        elif key == arcade.key.V:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("V")
            else:
                input_string.append("v")
        elif key == arcade.key.W:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("W")
            else:
               input_string.append("w")
        elif key == arcade.key.X:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("X")
            else:
                input_string.append("x")
        elif key == arcade.key.Y:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("Y")
            else:
               input_string.append("y")
        elif key == arcade.key.Z:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("Z")
            else:
               input_string.append("z")

        # Neumeric Characters (finished)
        elif key == arcade.key.KEY_0:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append(")")
            else:
                input_string.append("0")
        elif key == arcade.key.KEY_1:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("!")
            else:
                input_string.append("1")
        elif key == arcade.key.KEY_2:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("@")
            else:
                input_string.append("2")
        elif key == arcade.key.KEY_3:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("#")
            else:
                input_string.append("3")
        elif key == arcade.key.KEY_4:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("$")
            else:
                input_string.append("4")
        elif key == arcade.key.KEY_5:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("%")
            else:
                input_string.append("5")
        elif key == arcade.key.KEY_6:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("^")
            else:
                input_string.append("6")
        elif key == arcade.key.KEY_7:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("&")
            else:
                input_string.append("7")
        elif key == arcade.key.KEY_8:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("*")
            else:
                input_string.append("8")
        elif key == arcade.key.KEY_9:
            if modifiers & arcade.key.MOD_SHIFT:
                input_string.append("(")
            else:
                input_string.append("9")

if __name__== "__main__":
    racer_window = Racer_Window()
    arcade.run()           
            
         
                    