import pygame
from config import *

class Menu:
    def __init__(self, screen):
        # screen
        self.screen = screen
        
        # colours
        self.white = pygame.Color(WHITE)
        self.bgcolour = pygame.Color(BACKGROUND)
        # images & buttons
        self.game_img = pygame.image.load("images\\game_logo.png").convert_alpha()

    def draw_text(self, text, x, y, color, size):
            font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font

            current_text = font.render(text, True, color) # render the text
            current_text_rect = current_text.get_rect(centre=(x, y))
            self.screen.blit(current_text, current_text_rect) # display the text on screen

    def draw(self, width, height):
        def centre(surface, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
             int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface

        self.screen.fill(self.bgcolour) # clear all the entities on screen
        self.game_img_rect = self.game_img.get_rect(topleft=(centre(self.game_img, 0, -200)))
        self.screen.blit(self.game_img, self.game_img_rect)

        
