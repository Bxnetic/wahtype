import pygame
from config import *
from data.stats_tracker import *

class Results:
    def __init__(self, screen):
        # screen
        self.screen = screen
        
        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.subtextcolour = pygame.Color(SUBTEXT)

        # fonts
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_big = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 70)

    def test_ended(self):
        return True

    def end_stats(self, wpm, time, accuracy, width, height):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        def center_top(text, paddingWidth, paddingHeight):
            return (width / 2) - (text.get_width()) / 2 + paddingWidth, (height / 2) - (text.get_height() / 2 + paddingHeight)

        def center_bottom(text, paddingWidth, paddingHeight):
            return (width / 2) - (text.get_width()) / 2 + paddingWidth, (height / 2) - (text.get_height() / 2 + paddingHeight)

        """ wpm """
        wpm_text = self.font.render("wpm", True, self.subtextcolour) # text that says "wpm"
        wpm_text_rect = wpm_text.get_rect(topleft=(center_top(wpm_text, 0, 50))) # rect of wpm text
        self.screen.blit(wpm_text, wpm_text_rect) # display text on screen

        final_wpm = self.font_big.render(f"{wpm}", True, self.maincolour) # text displays final wpm
        final_wpm_rect = final_wpm.get_rect(topleft=(center_bottom(final_wpm, 0, 0))) # rect of final wpm
        self.screen.blit(final_wpm, final_wpm_rect) # display text on screen 

        """ time """
        time_text = self.font.render("time", True, self.subtextcolour)
        time_text_rect = time_text.get_rect(topleft=(center_top(time_text, -200, 50)))
        self.screen.blit(time_text, time_text_rect) # display text on screen

        final_time = self.font_big.render(f"{time}", True, self.maincolour) # text displays final wpm
        final_time_rect = final_time.get_rect(topleft=(center_bottom(final_time, -200, 0))) # rect of final wpm
        self.screen.blit(final_time, final_time_rect) # display text on screen 

        """ accuracy """
        accuracy_text = self.font.render("accuracy", True, self.subtextcolour)
        accuracy_text_rect = accuracy_text.get_rect(topleft=(center_top(accuracy_text, 200, 50)))
        self.screen.blit(accuracy_text, accuracy_text_rect) # display text on screen

        accuracy_value = self.font_big.render(f"{accuracy}%", True, self.maincolour) # text displays final wpm
        accuracy_rect = accuracy_value.get_rect(topleft=(center_bottom(accuracy_value, 200, 0))) # rect of final wpm
        self.screen.blit(accuracy_value, accuracy_rect) # display text on screen