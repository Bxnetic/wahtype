import pygame
from config import *
from core.selection import modeSelection
from ui.button import *

class Menu:
    def __init__(self, screen):
        # screen
        self.screen = screen
        # run / game loop
        self.game_paused = True
        self.running = True
        # colours
        self.white = pygame.Color(WHITE)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)
        # images & buttons
        self.game_img = pygame.image.load("images\\game_logo.png").convert_alpha()
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        self.blank_img = pygame.image.load("images\\blank.png")
        # initiate button
        self.play_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Play", 25, self.white, self.white) # button that displays "Play"
        self.scores_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Scores", 25, self.white, self.white) # button that displays "Scores"
        self.settings_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Settings", 25, self.white, self.white) # button that displays "Settings"
        self.quit_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Quit", 25, self.white, self.white) # button that displays "Quit"
        self.about_button = Button(0, 0, self.blank_img, 
            self.blank_img, 1, "v1 • bxnetic", 20, self.white, self.submaincolour) # button that displays "v1 • bxnetic"
        # classes
        self.modeSelection = modeSelection(self.screen)
    
    # set and get methods
    def setRun(self, state): # set run / game loop state
        self.running = state
    def getRun(self): # get current run / game loop state
        return self.running
    def setGameState(self, state): # set game state
        self.game_paused = state
    def getGameState(self): # get current game state
        return self.game_paused

    def draw(self, width, height):
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
        if self.play_button.draw(self.screen): # if the play button is clicked
            self.modeSelection.draw
            # self.setGameState(False) # set game to unpaused
        self.scores_button.rect.topleft = (centre(self.scores_button.image, 0, 40)) # centre the button
        if self.scores_button.draw(self.screen): # if the scores button is clicked
            pass
        self.settings_button.rect.topleft = (centre(self.settings_button.image, 0, 120)) # centre the button
        if self.settings_button.draw(self.screen): # if the settings button is clicked
            pass
        self.quit_button.rect.topleft = (centre(self.quit_button.image, 0, 200)) # centre the button
        if self.quit_button.draw(self.screen): # if the quit button is clicked
            self.setRun(False) # set run / game loop to false, closing the program
        self.about_button.rect.topleft = (centre(self.blank_img, 0, 280)) # centre the button
        if self.about_button.draw(self.screen): # if the quit button is clicked
            pass