import pygame
from config import *
from ui.surface_handle import *
from core.selection import Selection

class About(Selection): # inherit from selection class
    def __init__(self, screen, current_screen):
        super().__init__(screen, current_screen) # inherit parents function
        
        # theme
        self.subtextcolour = pygame.Color(SUBTEXT)

        # text
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24) # font
       
    def draw(self, width, height, mouse_released):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        self.y_offset = 60 # how far off border of screen text should be (top)
        self.x_offset = 20 # how far off border of screen text should be (left)

        draw_text(self.screen, "how to play", 20, 20, self.subtextcolour, 24)
        self.how_to_play_text = wrap_text(
            "just start typing and the timer will start! the game will end once you have completed the sentence.",
             24, width - 50) # about how to play the game
        self.extra_modes_text = wrap_text(
            "in survival mode you play against 3 lives. if you lose all of them, you have failed the test. in timed mode, you type until the timer has finished.",
             24, width - 50)
        self.about_text = wrap_text(
            "this is my computer science nea, which is a minimalstic python typeracer mainly inspired by monkeytype. i have no plans to update its been submitted.",
             24, width - 50)

        for line in self.how_to_play_text: # go through each line in the text
            draw_text(self.screen, line, self.x_offset, self.y_offset, self.maintext, 24) # display text
            self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaccng between lines

        if width >= 1450: # prevents overlapping of text
            draw_text(self.screen, "extra modes", 20, 120, self.subtextcolour, 24)
            for line in self.extra_modes_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + 60, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaccng between lines
            draw_text(self.screen, "about", 20, 260, self.subtextcolour, 24)
            for line in self.about_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + 130, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaccng between lines
        else:
            draw_text(self.screen, "extra modes", 20, 150, self.subtextcolour, 24)
            for line in self.extra_modes_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + 50, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaccng between lines
            draw_text(self.screen, "about", 20, 320, self.subtextcolour, 24)
            for line in self.about_text: # go through each line in the text
                draw_text(self.screen, line, self.x_offset, self.y_offset + 100, self.maintext, 24) # display text
                self.y_offset += self.font.get_linesize() + 10 # add 10px of vertical spaccng between lines

        self.home_button.rect.topleft = (centre(self.home_button.image, width, height, 0, 250)) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # resturn current screen state