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
        
class Menu(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window', fullscreen: bool = False, resizable: bool = False, update_rate: float = 1 / 60):
        super().__init__(width, height, title, fullscreen, resizable, update_rate)
        
    def draw_title(self):
        arcade.draw_text(SCREEN_TITLE, self.width/2, self.height-150, arcade.color.BLACK_BEAN, font_size=100, anchor_x="center")
            
    
    def on_draw(self):
        draw_background()
        self.draw_title()
    
    def on_key_press(self, key: int, modifiers: int):
        print(chr(key))
        
if __name__ == "__main__":
    menu = Menu(SCREEN_WIDTH,SCREEN_HEIGHT, SCREEN_TITLE)        
    
    arcade.run()
          
        
      
        