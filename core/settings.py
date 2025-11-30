import pygame
from config import *
from ui.button import *
from data.stats_tracker import Stats
from core.audio_handle import Audio

class Settings:
    def __init__(self, screen, current_screen):
        # screen
        self.screen = screen
        self.current_screen = current_screen

        # colours
        self.maincolour = pygame.Color(MAIN)
        self.maintext = pygame.Color(MAINTEXT)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)

        # images & buttons
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()

        # list
        self.music_list = ["On", "Off"] # turn music on or off
        self.sound_fx_list = ["On", "Off"] # turn sound fx on or off
        self.music_current_index = 0 # current index of the game mode list
        self.sound_fx_current_index = 0 # current index of the no. of words list
        self.music_selection = self.music_list[self.music_current_index] # get music_selection name
        self.sound_fx_selection = self.sound_fx_list[self.sound_fx_current_index] # get music_selection name
        
        # initiate button
        self.home_button = Button(0, 0, self.home_img, # home button
         self.home_img_hover, 0.2, "", 0, self.maincolour, self.maincolour)
        self.music_button = Button(0, 0, self.rounded_button_img, # music select button
         self.rounded_button_hover_img, 0.55, self.music_list[self.music_current_index], 25, self.maintext, self.maintext)
        self.sound_fx_button = Button(0, 0, self.rounded_button_img, # music select button
         self.rounded_button_hover_img, 0.55, self.music_list[self.music_current_index], 25, self.maintext, self.maintext)
        
        # classes
        self.audio = Audio() # create audio object
    
    # checks buttons conditions in settings menu only
    def check_buttons(self):
        self.music_selection = self.music_list[self.music_current_index] # get music_selection name
        self.sound_fx_selection = self.sound_fx_list[self.sound_fx_current_index] # get music_selection name
        self.audio.update_settings(self.music_selection, self.sound_fx_selection) # update user's settings

        if self.music_selection == "Off": # if button is set to off
            print("True") # debug
            self.audio.pause_music() # pause music
        if self.music_selection == "On": # if button is set to on
            self.audio.resume_music() # resume music
    
    # displays menu
    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clear all the entities on screen
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
        
        draw_text("Music", -100, -80, self.maintext, 24) # displays "Music"
        draw_text("Sound FX", -100, 40, self.maintext, 24) # displays "Sound FX"

        # music select button
        self.music_button.rect.topleft = (centre(self.music_button.image, 100, -80)) # centre the button
        if self.music_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.music_current_index = (self.music_current_index + 1) % len(self.music_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.music_button.setText(self.music_list[self.music_current_index]) # update the button text with
            # the next game mode

        # sound fx button
        self.sound_fx_button.rect.topleft = (centre(self.sound_fx_button.image, 100, 40)) # centre the button
        if self.sound_fx_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.sound_fx_current_index = (self.sound_fx_current_index + 1) % len(self.sound_fx_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.sound_fx_button.setText(self.sound_fx_list[self.sound_fx_current_index]) # update the button text with
            # the next no. of words

        # home button
        self.home_button.rect.topleft = (centre(self.home_button.image, 0, 250)) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # return current screen state
    