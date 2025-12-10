from config import *
from core.selection import Selection
from data.stats_tracker import Stats
from ui.button import *
from ui.surface_handle import *
from core.audio_handle import Audio

class Settings(Selection): # inherit from selection class
    def __init__(self, screen, current_screen, music_index, sound_fx_index):
        super().__init__(screen, current_screen) # inherit parents function
        
        # THEME
        self.error = pygame.Color(ERROR)

        # LIST
        self.music_list = ["On", "Off"] # turn music on or off
        self.sound_fx_list = ["On", "Off"] # turn sound fx on or off
        self.delete_scores_list = ["Delete Scores", "Are you sure?"] # delete scores or not
        self.music_current_index = int(music_index) # current index of the game mode list
        self.sound_fx_current_index = int(sound_fx_index) # current index of the no. of words list
        self.delete_scores_current_index = 0 # current index of delete scores list
        self.music_selection = self.music_list[self.music_current_index] # get music_selection name
        self.sound_fx_selection = self.sound_fx_list[self.sound_fx_current_index] # get music_selection name
        self.delete_scores_selection = self.delete_scores_list[self.delete_scores_current_index] # get delete_scores name
        
        # BUTTONS
        self.music_button = Button(0, 0, self.rounded_button_img, # music select button
         self.rounded_button_hover_img, 0.55, self.music_list[self.music_current_index], 25, self.maintext, self.maintext)
        self.sound_fx_button = Button(0, 0, self.rounded_button_img, # sound fx select button
         self.rounded_button_hover_img, 0.55, self.music_list[self.sound_fx_current_index], 25, self.maintext, self.maintext)
        self.delete_scores_button = Button(0, 0, self.rounded_button_img, # delete scores button
         self.rounded_button_hover_img, 0.55, self.delete_scores_list[self.delete_scores_current_index], 22, self.maintext, self.error)
        
        # CLASSES
        self.audio = Audio() # create audio object
        self.stats = Stats() # create stats object
    
    # CHECK BUTTONS CONDITIONS
    def check_buttons(self):
        self.music_selection = self.music_list[self.music_current_index] # get music_selection name
        self.sound_fx_selection = self.sound_fx_list[self.sound_fx_current_index] # get sound_fx name
        self.audio.update_settings(self.music_selection, self.sound_fx_selection) # update user's settings

        if self.music_selection == "Off": # if button is set to off
            self.audio.pause_music() # pause music
        if self.music_selection == "On": # if button is set to on
            self.audio.resume_music() # resume music
    
    # DISPLAYS MENU
    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clear all the entities on screen
        
        draw_text_centre(self.screen, "Music", width, height, -100, -80, self.maintext, 24) # displays "Music"
        draw_text_centre(self.screen, "Sound FX", width, height, -100, 40, self.maintext, 24) # displays "Sound FX"

        # music select button
        self.music_button.rect.topleft = centre(self.music_button.image, width, height, 100, -80) # centre the button
        if self.music_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.music_current_index = (self.music_current_index + 1) % len(self.music_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.music_button.setText(self.music_list[self.music_current_index]) # update the button text with next game mode

        # sound fx button
        self.sound_fx_button.rect.topleft = centre(self.sound_fx_button.image, width, height, 100, 40) # centre the button
        if self.sound_fx_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.sound_fx_current_index = (self.sound_fx_current_index + 1) % len(self.sound_fx_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.sound_fx_button.setText(self.sound_fx_list[self.sound_fx_current_index]) # update the button text with next value

        # delete scores button
        self.delete_scores_button.rect.topleft = centre(self.delete_scores_button.image, width, height, 250, 250) # centre the button
        if self.delete_scores_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.delete_scores_current_index = (self.delete_scores_current_index + 1) % len(self.delete_scores_list) # go to the next value,
            # once current_index = 3, the current index will become 0 again
            self.delete_scores_button.setText(self.delete_scores_list[self.delete_scores_current_index]) # update the button text with next value

            if self.delete_scores_current_index == 0 and mouse_released == True: # button is displaying "are you sure?"
                self.stats.delete_scores() # delete scores when user presses button
                print("Scores deleted!") # debug
                
        # home button
        self.home_button.rect.topleft = centre(self.home_button.image, width, height, 0, 250) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # return current screen state
    