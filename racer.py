import arcade
from random import randint

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

class Racer_Window(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMARANTH_PINK)
        
        moving_object_1 = MovingObject(":resources:images/enemies/ladybug.png")
        racing_lane_1 = RacingLane(self.width/2, self.height/2 - 100, ":resources:images/topdown_tanks/tileGrass1.png")
        moving_object_1.set_lane(racing_lane_1)
        
        moving_object_2 = MovingObject(":resources:images/animated_characters/robot/robot_idle.png")
        racing_lane_2 = RacingLane(self.width/2, self.height/2, ":resources:images/topdown_tanks/tileGrass_roadEast.png")
        moving_object_2.set_lane(racing_lane_2)
        
        moving_object_3 = MovingObject(":resources:images/space_shooter/playerShip1_blue.png")
        racing_lane_3 = RacingLane(self.width/2, self.height/2 + 100, ":resources:images/backgrounds/abstract_1.jpg")
        moving_object_3.set_lane(racing_lane_3)
        
        self.moving_objects = [moving_object_1, moving_object_2, moving_object_3]
        self.racing_lanes = [racing_lane_1, racing_lane_2, racing_lane_3]
        
        
    def on_update(self, delta_time):
        for moving_object in self.moving_objects:
                moving_object.update()
                if moving_object.percentage < 1 : 
                    num = randint(1, 10)
                    if num == 1:
                        moving_object.percentage += .01 
            
    def on_draw(self):
        arcade.start_render()
        for racing_lane in self.racing_lanes:
            racing_lane.draw()
        for moving_object in self.moving_objects:
                moving_object.draw()    
            
if __name__== "__main__":
    racer_window = Racer_Window()
    arcade.run()           
            
         
                    