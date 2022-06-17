import arcade
import arcade.gui


## Constants: This will be for the screen that the program opens a new window of
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "Typeracer"
GAME_OVER_TITLE = "GAME OVER"
RESTART_BUTTON_TEXT = "Restart"
EXIT_BUTTON_TEXT = "Exit"

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
    
    #Draw a street for the car  
        arcade.draw_lrtb_rectangle_filled(0, 
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT / 3 - 10,
                                          SCREEN_HEIGHT / 4,
                                          arcade.color.BLACK)
        
        arcade.draw_lrtb_rectangle_filled(0,
                                          SCREEN_WIDTH,
                                          SCREEN_HEIGHT / 3 - 50,
                                          SCREEN_HEIGHT / 3 - 55,
                                          arcade.color.WHITE)    
        
   
    
class Menu(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False, update_rate: float = 1 / 60):
        super().__init__(width, height, title, fullscreen, resizable, update_rate)
        
    #FOR THE UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
    # Box for buttons
        self.v_box = arcade.gui.UIBoxLayout()
    
    # Draw buttons     
        start_button = arcade.gui.UIFlatButton(text = "START", width = 200)
        self.v_box.add(start_button.with_space_around(bottom = 20))
        quit_button = QuitButton(text = "QUIT", width = 200)
        self.v_box.add(quit_button)
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "center_x",
                anchor_y = "center_y",
                child = self.v_box
            )
        )
        
    def draw_title(self):
        arcade.draw_text(SCREEN_TITLE, self.width/2, self.height-150, arcade.color.BLACK_BEAN, font_size=100, font_name="Caveat", anchor_x="center")
    
    def on_draw(self):
        draw_background()
        self.manager.draw()
        self.draw_title()
    
    def on_key_press(self, key: int, modifiers: int):
        print(chr(key))
        
        
############### QUIT BUTTON ###############
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()    


############### GAME OVER VIEW ###############
class GameOverView(arcade.View, Menu):
    def __init__(self):
        super().__init__()
        
    #FOR THE UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
    # Box for buttons
        self.v_box = arcade.gui.UIBoxLayout()
        
    # Draw exit and restart button
        restart_button = QuitButton(text = RESTART_BUTTON_TEXT, width = 200)
        self.v_box.add(restart_button)    
        exit_button = arcade.gui.UIFlatButton(text = EXIT_BUTTON_TEXT, width = 200)
        self.v_box.add(exit_button.with_space_around(bottom = 20))
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "center_x",
                anchor_y = "center_y",
                child = self.v_box
            )
        )
        
    def draw_title(self):
        arcade.draw_text(GAME_OVER_TITLE, self.width/2, self.height-150, arcade.color.BLACK_BEAN, font_size=100, font_name="Caveat", anchor_x="center")
    
    def on_draw(self):
        self.clear()
        draw_background()
        self.manager.draw()
        self.draw_title()   
    
    def on_key_press(self, key: int, modifiers: int):
        print(chr(key))
        
        
        
if __name__ == "__main__":
    menu = Menu(SCREEN_WIDTH,SCREEN_HEIGHT, SCREEN_TITLE)        
    
    arcade.run()