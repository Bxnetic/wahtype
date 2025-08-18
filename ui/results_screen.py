import pygame
from config import *
from data.stats_tracker import *

class Results:
    def __init__(self, screen):

        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.maintextcolour = pygame.Color(MAINTEXT)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.errorcolour = pygame.Color(ERROR)
        self.suberror = pygame.Color(SUBERROR)

        # fonts
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_big = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 70)
        self.screen = screen

    def test_ended(self):
        return True

    def end_stats(self, wpm, time, accuracy, width, height):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        """ wpm """
        wpm_text = self.font.render("wpm", True, self.subtextcolour) # text that says "wpm"
        wpm_text_rect = wpm_text.get_rect(topleft=((width / 2) - (wpm_text.get_width()) / 2,
         (height / 2) - (wpm_text.get_height() / 2 + 50))) # rect of wpm text
        self.screen.blit(wpm_text, wpm_text_rect) # display text on screen

        final_wpm = self.font_big.render(f"{wpm}", True, self.maincolour) # text displays final wpm
        final_wpm_rect = final_wpm.get_rect(topleft=((width / 2) - (final_wpm.get_width()) / 2,
         (height / 2) - (final_wpm.get_height() / 2))) # rect of final wpm
        self.screen.blit(final_wpm, final_wpm_rect) # display text on screen 

        """ time """
        time_text = self.font.render("time", True, self.subtextcolour)
        time_text_rect = time_text.get_rect(topleft=((width / 2) - (time_text.get_width()) / 2 - 200,
         (height / 2) - (time_text.get_height() / 2 + 50)))
        self.screen.blit(time_text, time_text_rect) # display text on screen

        final_time = self.font_big.render(f"{time}", True, self.maincolour) # text displays final wpm
        final_time_rect = final_time.get_rect(topleft=((width / 2) - (final_time.get_width()) / 2 - 200,
         (height / 2) - (final_time.get_height() / 2))) # rect of final wpm
        self.screen.blit(final_time, final_time_rect) # display text on screen 

        """ accuracy """
        accuracy_text = self.font.render("accuracy", True, self.subtextcolour)
        accuracy_text_rect = accuracy_text.get_rect(topleft=((width / 2) - (accuracy_text.get_width()) / 2 + 200,
         (height / 2) - (accuracy_text.get_height() / 2 + 50)))
        self.screen.blit(accuracy_text, accuracy_text_rect) # display text on screen

        accuracy_value = self.font_big.render(f"{accuracy}%", True, self.maincolour) # text displays final wpm
        accuracy_rect = accuracy_value.get_rect(topleft=((width / 2) - (accuracy_value.get_width()) / 2 + 200,
         (height / 2) - (accuracy_value.get_height() / 2))) # rect of final wpm
        self.screen.blit(accuracy_value, accuracy_rect) # display text on screen