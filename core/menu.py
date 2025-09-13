import pygame
from config import *
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
        self.bgcolour = pygame.Color(BACKGROUND)
        # images & buttons
        self.game_img = pygame.image.load("images\\game_logo.png").convert_alpha()
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        # initiate button
        self.play_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Play", 25, self.white) # button that displays "Play"
        self.leaderboard_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Leaderboard", 25, self.white) # button that displays "Leaderboard"
        self.settings_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Settings", 25, self.white) # button that displays "Settings"
        self.quit_button = Button(0, 0, self.rounded_button_img, 
            self.rounded_button_hover_img, 0.55, "Quit", 25, self.white) # button that displays "Quit"
    
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
        self.game_img_rect = self.game_img.get_rect(
            topleft=(centre(self.game_img, 0, -200))) # game icon rect
        self.play_button.rect.topleft = (centre(self.play_button.image, 0, -40)) # centre the button
        if self.play_button.draw(self.screen): # if the play_button is clicked
            self.setGameState(False) # set game to unpaused
        self.leaderboard_button.rect.topleft = (centre(self.leaderboard_button.image, 0, 40)) # centre the button
        if self.leaderboard_button.draw(self.screen): # if the play_button is clicked
            pass
        self.settings_button.rect.topleft = (centre(self.settings_button.image, 0, 120)) # centre the button
        if self.settings_button.draw(self.screen): # if the play_button is clicked
            pass
        self.quit_button.rect.topleft = (centre(self.quit_button.image, 0, 200)) # centre the button
        if self.quit_button.draw(self.screen): # if the play_button is clicked
            self.setRun(False) # set run / game loop to false, closing the program
        self.screen.blit(self.game_img, self.game_img_rect) # display game image on screen

        
