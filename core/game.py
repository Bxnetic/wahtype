import pygame # imports pygame modules
from config import *
from ui.text_box import *

class Game():
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        self.running = True # main game loop
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # sets size of the window
        self.clock = pygame.time.Clock() # creates time using time pygame clock module
    
    def run(self):
        while self.running:
            self.clock.tick(FPS) # sets the frames to 60
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False # sets main game loop to false
                elif event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                    text.text_handle(event)

        pygame.quit()
        # exit() # closes program
