import pygame # imports pygame modules
from config import *
from ui.text_box import *

class Game():
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30)
        self.running = True # main game loop
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # sets size of the window
        self.clock = pygame.time.Clock() # creates time using time pygame clock module

        # basic colours
        self.black = BLACK

        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.maintextcolour = pygame.Color(MAINTEXT)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.errorcolour = pygame.Color(ERROR)
        self.suberror = pygame.Color(SUBERROR)

        pygame.display.set_caption("Another Type Racing Game") # sets name of window (new)

        self.text = Text(self.screen) # create text object and passes screen to Text
    
    def run(self):
        while self.running:
            self.clock.tick(FPS) # sets the frames to 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False # sets main game loop to false
                elif event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                    self.text.text_handle(event)


            # get current width & height
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()

            # prevents user from resizing window under 800x600
            if self.width < 800: # if width is less than 800 (min width)
                self.screen = pygame.display.set_mode((WIDTH, self.height), pygame.RESIZABLE) # set width back to 800 and
                # keep current height
            elif self.height < 600: # if height is less than 600 (min height)
                self.screen = pygame.display.set_mode((self.width, HEIGHT), pygame.RESIZABLE)
                # set height back to 600, keep current width


            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text(self.width, self.height) # draws to screen and passed through current width to draw_text
            pygame.display.flip() # continuously updates the screen

        pygame.quit()
        # exit() # closes program
