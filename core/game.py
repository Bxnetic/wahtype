import pygame # imports pygame modules
from config import *
from ui.text_box import *

class Game():
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30)
        self.running = True # main game loop
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # sets size of the window
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

            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text() # draws to screen
            pygame.display.flip() # continuously updates the screen

        pygame.quit()
        # exit() # closes program
