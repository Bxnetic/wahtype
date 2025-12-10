import pygame
from config import *
from ui.surface_handle import *
from core.selection import Selection

class About(Selection): # inherit from selection class
    def __init__(self, screen, current_screen):
        super().__init__(screen, current_screen) # inherit parents function
        
        # THEME
        self.subtextcolour = pygame.Color(SUBTEXT)

        # TEXT
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24) # font
       
    def draw(self, width, height, mouse_released):
        # subprogram that positons the text depending on the width and height of window
        def position_text(extra_width, extra_height, about_width, about_height, extra_y_value, about_y_value):
            draw_text(self.screen, "extra modes", extra_width, extra_height, self.maincolour, 24) # display "extra modes"
            for line in self.extra_modes_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + extra_y_value, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaceing between lines
            draw_text(self.screen, "about", about_width, about_height, self.maincolour, 24) # display "about"
            for line in self.about_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + about_y_value, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaceing between lines

        self.screen.fill(self.bgcolour) # clear all the entities on screen

        self.y_offset = 60 # how far off border of screen text should be (top)
        self.x_offset = 20 # how far off border of screen text should be (left)

        draw_text(self.screen, "how to play", 20, 20, self.maincolour, 24) # display "how to play"
        self.how_to_play_text = wrap_text(
            "just start typing and the timer will start! the game will end once you have completed the sentence.",
             24, width - 50) # about how to play the game
        self.extra_modes_text = wrap_text(
            "in survival mode you play against 3 lives. if you lose all of them, you have failed the test. in timed mode, you type until the timer has finished.",
             24, width - 50) # about how to extra modes work
        self.about_text = wrap_text(
            "this is my computer science nea, which is a minimalstic python typeracer mainly inspired by monkeytype. i have no plans to update once its been submitted.",
             24, width - 50) # explanation of this project

        for line in self.how_to_play_text: # go through each line in the text
            draw_text(self.screen, line, self.x_offset, self.y_offset, self.maintext, 24) # display text
            self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaceing between lines

        if width >= 1450: # prevents overlapping of text
            position_text(20, 120, 20, 270, 60, 130) # place text at these positions
        elif width >= 1115: # prevents overlapping of text
            position_text(20, 150, 20, 280, 50, 100) # place text at these positions
        if width <= 1115: # prevents overlapping of text
            position_text(20, 150, 20, 320, 50, 100) # place text at these positions

        draw_text(self.screen, "github.com/Bxnetic", width - 250, height - 60, self.maintext, 20) # credit

        self.home_button.rect.topleft = (centre(self.home_button.image, width, height, 0, 250)) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # resturn current screen state