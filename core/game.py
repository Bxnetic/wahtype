import pygame # imports pygame modules
from config import *
from ui.text_box import *
from ui.button import *

class Game:
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30) # allows user to hold key

        # screen, fps and run
        self.running = True # main game loop
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # sets size of the window
        self.clock = pygame.time.Clock() # creates time using time pygame clock module

        # images for all the buttons
        self.reset_img = pygame.image.load("images\\reset_button.png").convert_alpha()
        self.reset_img_hover = pygame.image.load("images\\reset_button_hover.png").convert_alpha()
        
        # initiate buttons
        self.reset_button = Button(0, 0, self.reset_img, 
             self.reset_img_hover, 0.2)

        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)

        # pygame window
        pygame.display.set_caption("Another Type Racing Game") # sets name of window (new)

        # classes
        self.text = Text(self.screen) # create text object and passes screen to Text

    def run(self):
        while self.running:
            self.clock.tick(FPS) # sets the frames to 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False # sets main game loop to false
                elif event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                    self.text.text_handle(event)

            """ size of window """
            # get current width & height of window
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()

            # prevents user from resizing window under 800x600
            if self.width < 800: # if width is less than 800 (min width)
                self.screen = pygame.display.set_mode((WIDTH, self.height), pygame.RESIZABLE) # set width back to 800 and
                # keep current height
            elif self.height < 600: # if height is less than 600 (min height)
                self.screen = pygame.display.set_mode((self.width, HEIGHT), pygame.RESIZABLE)
                # set height back to 600, keep current width

            """ game elements """
            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text(self.width, self.height) # draws to screen and passes current width to draw_text
              
            # buttons
            if self.text.done: # if the test has been completed
                self.reset_button.rect.topleft = (int((self.width / 2)) - int(self.reset_button.rect.width / 2),
                int((self.height / 2)) + 150) # move the button further down the screen
            else:
                 self.reset_button.rect.topleft = (int((self.width / 2)) - int(self.reset_button.rect.width / 2),
                int((self.height / 2)) + 50) # set the positioning of the button depending on the current width & height

            if self.reset_button.draw(self.screen): # if the button is clicked
                self.text.reset()

            pygame.display.flip() # continuously updates the screen

        pygame.quit() # closes program
