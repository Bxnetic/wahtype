import pygame
from config import *
from ui.button import *
from core.game import *

class gameSelection:
    def __init__(self, screen, current_screen):
        # screen
        self.screen = screen
        self.current_screen = current_screen
        # colours
        self.white = pygame.Color(WHITE)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)
        # images of buttons
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()
        # list
        self.game_mode_list = ["Normal", "Timed", "Survival"] # game modes
        self.words_list = ["15 words", "25 words"] # no. of words
        self.game_current_index = 0 # current index of the game mode list
        self.words_current_index = 0 # current index of the no. of words list
        # initiate buttons
        self.home_button = Button(0, 0, self.home_img,
         self.home_img_hover, 0.2, "", 0, self.white, self.white)
        self.gamemode_select_button = Button(0, 0, self.rounded_button_img, 
         self.rounded_button_hover_img, 0.55, self.game_mode_list[self.game_current_index], 25, self.white, self.white)
        self.words_select_button = Button(0, 0, self.rounded_button_img, 
         self.rounded_button_hover_img, 0.55, self.words_list[self.words_current_index], 25, self.white, self.white)
         
        # button that displays game mode

    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clean entities

        """ functions """
        def centre(surface, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
                int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface
        def draw_text(text, x, y, color, size):
            font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font
            current_text = font.render(text, True, color) # render the text
            current_text_rect = current_text.get_rect(
                topleft=(centre(current_text, x, y))) # display text in the centre
            self.screen.blit(current_text, current_text_rect) # display the text on screen
        
        # text
        draw_text("Game mode", -100, -80, self.white, 24) # displays "Game mode"
        draw_text("Test length", -100, 40, self.white, 24) # displays "Test length"

        """ buttons """
        # gamemode button
        self.gamemode_select_button.rect.topleft = (centre(self.gamemode_select_button.image, 100, -80)) # centre the button
        if self.gamemode_select_button.draw(self.screen, mouse_released): # if the game mode button is clicked
            self.game_current_index = (self.game_current_index + 1) % len(self.game_mode_list) # go to the next value,
            self.gamemode_select_button.setText(self.game_mode_list[self.game_current_index]) # update the button text with
            # the next game mode
        # words button
        self.words_select_button.rect.topleft = (centre(self.words_select_button.image, 100, 40)) # centre the button
        if self.words_select_button.draw(self.screen, mouse_released): # if the game mode button is clicked
            self.words_current_index = (self.words_current_index + 1) % len(self.words_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.words_select_button.setText(self.words_list[self.words_current_index]) # update the button text with
            # the next game mode
        # home button
        self.home_button.rect.topleft = (centre(self.home_button.image, 0, 200)) # home button
        if self.home_button.draw(self.screen, mouse_released):
            self.current_screen = "menu"
            return self.current_screen
        