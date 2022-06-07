import arcade
from random import randint

input_string = []
#this is a ~~surprise tool~~ global variable that is needed for processing and passing the users input

control_text = "this is the control text"
#swap this variable and all instances of it out for whatever changing text variable is implemented, this
#variable is what the program checks the user input against to determine if they completed the typing

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
        
        
        moving_object_3 = MovingObject(":resources:images/space_shooter/playerShip1_blue.png")
        racing_lane_3 = RacingLane(self.width/2, self.height - 100, ":resources:images/backgrounds/abstract_1.jpg")
        moving_object_3.set_lane(racing_lane_3)
        
        self.text_box = Text_Box(self.width/2, self.height/2, self.width - 20, control_text)
        self.user_box = Text_Box(self.width/2, self.height/2 - 100, self.width - 20, "")

        self.moving_objects = [moving_object_3]
        self.racing_lanes = [racing_lane_3]
        
        
    def on_update(self, delta_time):
        for moving_object in self.moving_objects:
                moving_object.update()
                if moving_object.percentage < 1 : 
                    num = randint(1, 10)
                    if num == 1:
                        moving_object.percentage += .01 
        
        # constantly updating the user text box to reflect what they are typing
        self.user_box.text = self.text = arcade.Text("".join(input_string), self.user_box.center.x, self.user_box.center.y, arcade.color.BLACK_BEAN, font_size=15, width=self.width-20, anchor_x="center", anchor_y="center", multiline=True)
        self.user_box.draw()

        if (("".join(input_string)) == control_text):
            print("The texts were identical, program exiting because no 'you win' is implemented yet. See line 83 (as of 6/7/2022)")
            exit()
            
            
    def on_draw(self):
        arcade.start_render()
        for racing_lane in self.racing_lanes:
            racing_lane.draw()
        for moving_object in self.moving_objects:
                moving_object.draw()  
        self.text_box.draw()     
        self.user_box.draw()
    
    def on_key_press(self, key, modifier):

        # Each of these if statements work to assess what key is pressed and edit the string appropriately 

        # Special Characters
        if key == arcade.key.COMMA:
            input_string.append(",")
        elif key == arcade.key.PERIOD:
            input_string.append(".")
        elif key == arcade.key.SPACE:
            input_string.append(" ")
        elif key == arcade.key.SEMICOLON:
            input_string.append(";")
        elif key == arcade.key.COLON:
            input_string.append(":")
        elif key == arcade.key.DOUBLEQUOTE:
            input_string.append("\"")
        elif key == arcade.key.EXCLAMATION:
            input_string.append("!")
        elif key == arcade.key.QUESTION:
            input_string.append("?")
        elif key == arcade.key.MINUS:
            input_string.append("-")
        elif key ==arcade.key.ENTER:
            print(''.join(input_string))

        # Character with special effect (remove)
        elif key == arcade.key.BACKSPACE:
            input_string.pop()
            # This will remove the last item from the text

        # Alpha Characters (to be finished)
        elif key == arcade.key.A:
            input_string.append("a")
        elif key == arcade.key.B:
            input_string.append("b")
        elif key == arcade.key.C:
            input_string.append("c")
        elif key == arcade.key.D:
            input_string.append("d")
        elif key == arcade.key.E:
            input_string.append("e")
        elif key == arcade.key.F:
            input_string.append("f")
        elif key == arcade.key.G:
            input_string.append("g")
        elif key == arcade.key.H:
            input_string.append("h")
        elif key == arcade.key.I:
            input_string.append("i")
        elif key == arcade.key.J:
            input_string.append("j")
        elif key == arcade.key.K:
            input_string.append("k")
        elif key == arcade.key.L:
            input_string.append("l")
        elif key == arcade.key.M:
            input_string.append("m")
        elif key == arcade.key.N:
            input_string.append("n")
        elif key == arcade.key.O:
            input_string.append("o")
        elif key == arcade.key.P:
            input_string.append("p")
        elif key == arcade.key.Q:
            input_string.append("q")
        elif key == arcade.key.R:
            input_string.append("r")
        elif key == arcade.key.S:
            input_string.append("s")
        elif key == arcade.key.T:
            input_string.append("t")
        elif key == arcade.key.U:
            input_string.append("u")
        elif key == arcade.key.V:
            input_string.append("v")
        elif key == arcade.key.W:
            input_string.append("w")
        elif key == arcade.key.X:
            input_string.append("x")
        elif key == arcade.key.Y:
            input_string.append("y")
        elif key == arcade.key.Z:
            input_string.append("z")

        # Neumeric Characters
        elif key == arcade.key.KEY_0:
            input_string.append("0")
        elif key == arcade.key.KEY_1:
            input_string.append("1")
        elif key == arcade.key.KEY_2:
            input_string.append("2")
        elif key == arcade.key.KEY_3:
            input_string.append("3")
        elif key == arcade.key.KEY_4:
            input_string.append("4")
        elif key == arcade.key.KEY_5:
            input_string.append("5")
        elif key == arcade.key.KEY_6:
            input_string.append("6")
        elif key == arcade.key.KEY_7:
            input_string.append("7")
        elif key == arcade.key.KEY_8:
            input_string.append("8")
        elif key == arcade.key.KEY_9:
            input_string.append("9")
        else:
            print("key input not recognized")

if __name__== "__main__":
    racer_window = Racer_Window()
    arcade.run()           
            
         
                    