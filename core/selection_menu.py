import pygame
from config import *
from ui.button import *
from ui.surface_handle import *
from core.game import *

class Selection(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.__number_of_words = 0

        # THEME
        self.maincolour = pygame.Color(MAIN)
        self.maintext = pygame.Color(MAINTEXT)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)

        # images of buttons
      
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()

        # list
        self.game_mode_list = ["Normal", "Survival", "Timed"] # game modes
        self.words_list = ["15 words", "25 words"] # no. of words
        self.time_list = ["15s", "30s", "60s"] # time selections for timed mode
        self.game_current_index = 0 # current index of the game mode list
        self.words_current_index = 0 # current index of the no. of words list
        self.time_current_index = 0 # current index of time selections
        
        # BUTTONSs
        self.gamemode_select_button = Button(0, 0, self.rounded_button_img, # gamemode button
         self.rounded_button_hover_img, 0.55, self.game_mode_list[self.game_current_index], 25, self.maintext, self.maintext)
        self.words_select_button = Button(0, 0, self.rounded_button_img, # no. of words
         self.rounded_button_hover_img, 0.55, self.words_list[self.words_current_index], 25, self.maintext, self.maintext)
        self.time_select_button = Button(0, 0, self.rounded_button_small_img, # time selection
         self.rounded_button_small_hover_img, 0.55, self.time_list[self.time_current_index], 25, self.maintext, self.maintext)
        self.start_button = Button(0, 0, self.green_button_img, # start button
         self.green_button_hover_img, 0.55, "Start", 25, self.maintext, self.maintext)

    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clean entities
        
        # text
        draw_text_centre(self.screen, "Game mode", width, height, -100, -80, self.maintext, 24) # displays "Game mode"
        if self.game_current_index == 0 or self.game_current_index == 1: # only displays when button is set on normal or survival
            draw_text_centre(self.screen, "Test length", width, height, -100, 40, self.maintext, 24) # displays "Test length"

        """ buttons """
        # gamemode button
        self.gamemode_select_button.rect.topleft = centre(self.gamemode_select_button.image, width, height, 100, -80) # centre the button
        if self.gamemode_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.game_current_index = (self.game_current_index + 1) % len(self.game_mode_list) # go to the next value,
            self.gamemode_select_button.set_text(self.game_mode_list[self.game_current_index]) # update the button text with
            # the next game mode
        
        # seconds button
        if self.game_current_index == 2: # only displays when button is set on timed
            self.time_select_button.rect.topleft = centre(self.time_select_button.image, width, height, 230, -80) # centre the button
            if self.time_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
                self.time_current_index = (self.time_current_index + 1) % len(self.time_list) # go to the next value,
                self.time_select_button.set_text(self.time_list[self.time_current_index]) # update the button text with
                # the next time selection

        # words button
        if self.game_current_index == 0 or self.game_current_index == 1: # only displays when button is set on normal or survival
            self.words_select_button.rect.topleft = centre(self.words_select_button.image, width, height, 100, 40) # centre the button
            if self.words_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
                self.words_current_index = (self.words_current_index + 1) % len(self.words_list) # go to the next value,
                # once current_index = 3, the current index will become 0 again
                self.words_select_button.set_text(self.words_list[self.words_current_index]) # update the button text with
                # the next no. of words

        # home button
        self.home_button.rect.topleft = centre(self.home_button.image, width, height, 0, 250) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # return current screen state
        
        # start button
        self.start_button.rect.topleft = centre(self.start_button.image, width, height, 0, 160) # start button
        if self.start_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "game" # set current screen to game
            return self.current_screen # return current screen state

    def getGameMode(self):
        self.__game_mode = self.game_mode_list[self.game_current_index] # get game mode name
        return self.__game_mode # return name
    
    def getSeconds(self):
        self.__time_select = self.time_list[self.time_current_index][:2] # get seconds
        return self.__time_select
    
    def getNumberOfWords(self):
        if self.game_current_index == 0 or self.game_current_index == 1:
            self.__number_of_words = self.words_list[self.words_current_index][:2] # get the first 2 letters
        elif self.game_current_index == 2:
            self.__number_of_words = "45"
        return self.__number_of_words # return number of words