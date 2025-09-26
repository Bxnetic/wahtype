import pygame
from config import *
from ui.button import *
from core.game import *

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
        self.game_mode_list = ["Normal", "Timed", "Survival"] # game modes
        self.character_list = ["15", "25"] # no. of characters
        self.game_current_index = 0 # current index of the game mode list
        self.character_current_index = 0 # current index of the no. of character list
        # initiate buttons
        self.gamemode_select_button = Button(0, 0, self.rounded_button_img, 
         self.rounded_button_hover_img, 0.55, self.game_mode_list[self.game_current_index], 25, self.white, self.white)
        self.character_select_button = Button(0, 0, self.rounded_button_img, 
         self.rounded_button_hover_img, 0.55, self.character_list[self.character_current_index], 25, self.white, self.white)
        # button that displays game mode

    def draw(self, width, height):
        def centre(surface, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
                int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface
        
        self.screen.fill(self.bgcolour) # clean entities

        self.gamemode_select_button.rect.topleft = (centre(self.gamemode_select_button.image, 0, -80)) # centre the button
        if self.gamemode_select_button.draw(self.screen): # if the game mode button is clicked
            print(self.game_current_index) # debug 
            print(self.game_mode_list[self.game_current_index]) # debug
            self.game_current_index = (self.game_current_index + 1) % len(self.game_mode_list) # go to the next value self.game_mode_list
            # once current_index = 3, the current index will become 0 again
            self.gamemode_select_button.setText(self.game_mode_list[self.game_current_index]) # update the button text with
            # the next game mode
        self.character_select_button.rect.topleft = (centre(self.character_select_button.image, 0, 40)) # centre the button
        if self.character_select_button.draw(self.screen): # if the game mode button is clicked
            print(self.character_current_index) # debug 
            print(self.character_list[self.character_current_index]) # debug
            self.character_current_index = (self.character_current_index + 1) % len(self.character_list) # go to the next value self.game_mode_list
            # once current_index = 3, the current index will become 0 again
            self.character_select_button.setText(self.character_list[self.character_current_index]) # update the button text with
            # the next game mode
            