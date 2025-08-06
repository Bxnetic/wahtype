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
        self.screen = screen

    def end_stats(self, wpm, time):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        final_wpm = self.font.render(f"{wpm}", True, self.maincolour)
        self.screen.blit(final_wpm, (20, 20))

        final_time = self.font.render(f"{time}", True, self.maincolour)
        self.screen.blit(final_time, (40, 80))
