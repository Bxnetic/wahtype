import pygame # imports pygame modules
from config import *

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

        pygame.quit()
        # exit() # closes program
