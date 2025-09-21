import pygame
from config import *

class gameSelection:
    def __init__(self, screen):
        # screen
        self.screen = screen
        # colours
        self.white = pygame.Color(WHITE)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)

    def draw(self, width, height):
        self.screen.fill(self.bgcolour)
        