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

    def draw_text(self, text, x, y, color, size):
            font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font

            current_text = font.render(text, True, color) # render the text
            current_text_rect = current_text.get_rect(center=(x, y))
            self.screen.blit(current_text, current_text_rect) # display the text on screen

    def draw(self):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        self.draw_text("text", 20, 20, self.maincolour, 20)
