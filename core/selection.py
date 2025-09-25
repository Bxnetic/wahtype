import pygame
from config import *
from ui.button import *

class gameSelection:
    def __init__(self, screen):
        # screen
        self.screen = screen
        # colours
        self.white = pygame.Color(WHITE)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)
        # images of buttons
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        # list
        self.list = ["Normal", "Timed", "Survival"]
        self.current_index = 0
        # initiate buttons
        self.gamemode_select_button = Button(0, 0, self.rounded_button_img, 
         self.rounded_button_hover_img, 0.55, self.list[self.current_index], 25, self.white, self.white) # button that displays "Play"

    def draw(self, width, height):
        def centre(surface, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
                int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface
        
        self.screen.fill(self.bgcolour) # clean entities
        self.gamemode_select_button.rect.topleft = (centre(self.gamemode_select_button.image, 0, 0)) # centre the button
        if self.gamemode_select_button.draw(self.screen): # if the play button is clicked
            print(self.current_index)
            print(self.list[self.current_index])
            self.current_index = (self.current_index + 1) % len(self.list)
            self.gamemode_select_button.setText(self.list[self.current_index])
    