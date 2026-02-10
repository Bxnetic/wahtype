import pygame
from config import *
from ui.button import *
from ui.surface_handle import *
from core.game import *

class Selection(Menu): # inherits from menu class
    def __init__(self, screen):
        super().__init__(screen) # inherit screen from menu class
        self.__number_of_words = 0 # user's selected no. of words

        # LIST
        self.__game_mode_list = ["Normal", "Survival", "Timed"] # game modes
        self.__words_list = ["15 words", "25 words"] # no. of words
        self.__time_list = ["15s", "30s", "60s"] # time selections for timed mode

        self.__game_current_index = 0 # current index of the game mode list
        self.__words_current_index = 0 # current index of the no. of words list
        self.__time_current_index = 0 # current index of time selections
        
        # BUTTONS
        self.gamemode_select_button = Button(0, 0, self.rounded_button_img, # gamemode button
         self.rounded_button_hover_img, 0.55, self.__game_mode_list[self.__game_current_index], 25, self.maintext, self.maintext)

        self.words_select_button = Button(0, 0, self.rounded_button_img, # no. of words
         self.rounded_button_hover_img, 0.55, self.__words_list[self.__words_current_index], 25, self.maintext, self.maintext)

        self.time_select_button = Button(0, 0, self.rounded_button_small_img, # time selection
         self.rounded_button_small_hover_img, 0.55, self.__time_list[self.__time_current_index], 25, self.maintext, self.maintext)

    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clean entities
        
        # text
        draw_text_centre(self.screen, "Game mode", width, height, -100, -80, self.maintext, 24) # displays "Game mode"
        if self.__game_current_index == 0 or self.__game_current_index == 1: # only displays when button is set on normal or survival
            draw_text_centre(self.screen, "Test length", width, height, -100, 40, self.maintext, 24) # displays "Test length"

        # gamemode button
        self.gamemode_select_button.rect.topleft = centre(self.gamemode_select_button.image, width, height, 100, -80) # centre the button
        if self.gamemode_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.__game_current_index = (self.__game_current_index + 1) % len(self.__game_mode_list) # go to the next value,
            self.gamemode_select_button.set_text(self.__game_mode_list[self.__game_current_index]) # update the button text with
            # the next game mode
        
        # seconds button
        if self.__game_current_index == 2: # only displays when button is set on timed
            self.time_select_button.rect.topleft = centre(self.time_select_button.image, width, height, 230, -80) # centre the button
            if self.time_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
                self.__time_current_index = (self.__time_current_index + 1) % len(self.__time_list) # go to the next value,
                self.time_select_button.set_text(self.__time_list[self.__time_current_index]) # update the button text with
                # the next time selection

        # words button
        if self.__game_current_index == 0 or self.__game_current_index == 1: # only displays when button is set on normal or survival
            self.words_select_button.rect.topleft = centre(self.words_select_button.image, width, height, 100, 40) # centre the button
            if self.words_select_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
                self.__words_current_index = (self.__words_current_index + 1) % len(self.__words_list) # go to the next value,
                # once current_index = 3, the current index will become 0 again
                self.words_select_button.set_text(self.__words_list[self.__words_current_index]) # update the button text with
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
        self.__game_mode = self.__game_mode_list[self.__game_current_index] # get game mode name
        return self.__game_mode # return name
    
    def getSeconds(self):
        self.__time_select = self.__time_list[self.__time_current_index][:2] # get seconds
        return self.__time_select
    
    def getNumberOfWords(self):
        if self.__game_current_index == 0 or self.__game_current_index == 1:
            self.__number_of_words = self.__words_list[self.__words_current_index][:2] # get the first 2 letters
        elif self.__game_current_index == 2:
            self.__number_of_words = "45"
        return self.__number_of_words # return number of words