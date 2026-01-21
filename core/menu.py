import pygame
from config import *
from ui.button import *

class Menu:
    def __init__(self, screen):
        # screen
        self.screen = screen

        # THEME
        self.white = pygame.Color(WHITE)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.maintext = pygame.Color(MAINTEXT)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.error = pygame.Color(ERROR)

        # IMAGES
        self.game_img = pygame.image.load("images\\game_logo.png").convert_alpha()
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        self.rounded_button_small_img = pygame.image.load("images\\rounded_button_small.png").convert_alpha()
        self.rounded_button_small_hover_img = pygame.image.load("images\\rounded_button_small_hover.png").convert_alpha()
        self.green_button_img = pygame.image.load("images\\rounded_button_green.png").convert_alpha()
        self.green_button_hover_img = pygame.image.load("images\\rounded_button_green_hover.png").convert_alpha()
        self.blank_img = pygame.image.load("images\\blank.png")
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()

        # BUTTONS
        self.play_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Play", 25, self.white, self.white) # button that displays "Play"
        self.stats_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Stats", 25, self.white, self.white) # button that displays "Stats"
        self.settings_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Settings", 25, self.white, self.white) # button that displays "Settings"
        self.quit_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Quit", 25, self.white, self.white) # button that displays "Quit"
        self.about_button = Button(0, 0, self.blank_img, 
            self.blank_img, 1, "how to play", 20, self.white, self.submaincolour) # button that displays "v1 • bxnetic"
        self.home_button = Button(10000, 10000, self.home_img, # home button (displays off screen)
            self.home_img_hover, 0.2, "", 0, self.maintext, self.maintext) 
        self.start_button = Button(10000, 10000, self.green_button_img, # start button (displays off screen)
            self.green_button_hover_img, 0.55, "Start", 25, self.maintext, self.maintext)

    def draw(self, width, height, mouse_released):
        def centre(surface, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
             int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface

        self.screen.fill(self.bgcolour) # clear all the entities on screen
        # game icon
        self.game_img_rect = self.game_img.get_rect(
            topleft=(centre(self.game_img, 0, -200))) # game icon rect
        self.screen.blit(self.game_img, self.game_img_rect) # display game image on screen
        # buttons
        self.play_button.rect.topleft = (centre(self.play_button.image, 0, -40)) # centre the button
        if self.play_button.draw(self.screen, mouse_released): # if the play button is clicked
            return "selection"
        self.stats_button.rect.topleft = (centre(self.stats_button.image, 0, 40)) # centre the button
        if self.stats_button.draw(self.screen, mouse_released): # if the scores button is clicked
            return "stats"
        self.settings_button.rect.topleft = (centre(self.settings_button.image, 0, 120)) # centre the button
        if self.settings_button.draw(self.screen, mouse_released): # if the settings button is clicked
            return "settings"
        self.quit_button.rect.topleft = (centre(self.quit_button.image, 0, 200)) # centre the button
        if self.quit_button.draw(self.screen, mouse_released): # if the quit button is clicked
            return "quit"
        self.about_button.rect.topleft = (centre(self.blank_img, 0, 280)) # centre the button
        if self.about_button.draw(self.screen, mouse_released): # if the quit button is clicked
            return "about"
        if self.home_button.draw(self.screen, mouse_released):
            return "menu"
        if self.start_button.draw(self.screen, mouse_released):
            return "game"