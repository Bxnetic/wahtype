import pygame
from config import *

class Menu:
    def __init__(self, screen):
        # screen
        self.screen = screen
        
        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.subtextcolour = pygame.Color(SUBTEXT)

        # fonts
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_big = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 70)

    def draw(self):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        test = self.font.render("test", True, self.maincolour)
        self.screen.blit(test, (0, 0))
