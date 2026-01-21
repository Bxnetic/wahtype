import pygame
from config import *
from data.stats_tracker import *
from ui.surface_handle import *

class Results:
    def __init__(self, screen):
        # SCREEN
        self.screen = screen
        
        # THEME
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.error = pygame.Color(ERROR)

    def end_stats(self, wpm, time, accuracy, width, height, gameMode, testFailed, lives, chars, incorrect_chars):
        self.screen.fill(self.bgcolour) # clear all the entities on screen
        
        # wpm
        draw_text_centre(self.screen, "wpm", width, height, 0, -50, self.subtextcolour, 24) # display "wpm"
        draw_text_centre(self.screen, f"{wpm}", width, height, 0, 0, self.maincolour, 70) # display wpm

        # time
        draw_text_centre(self.screen, "time", width, height, -200, -50, self.subtextcolour, 24) # display "time"
        draw_text_centre(self.screen, f"{time}", width, height, -200, 0, self.maincolour, 70) # display final time

        # accuracy
        draw_text_centre(self.screen, "accuracy", width, height, 200, -50, self.subtextcolour, 24) # display "accuracy"
        draw_text_centre(self.screen, f"{accuracy}%", width, height, 200, 0, self.maincolour, 70) # display accuracy

        # game mode
        draw_text_centre(self.screen, "game mode", width, height, -200, 80, self.subtextcolour, 24) # display "game mode"
        draw_text_centre(self.screen, f"{gameMode}", width, height, -200, 110, self.maincolour, 24) # display name of game mode

        # characters
        draw_text_centre(self.screen, f"characters", width, height, 0, 80, self.subtextcolour, 24) # display lives
        draw_text_centre(self.screen, f"{chars}", width, height, 0, 110, self.maincolour, 24) # display number of lives
        # incorrect characters
        if gameMode == "Normal" or gameMode == "Timed":
            draw_text_centre(self.screen, f"incorrect", width, height, 200, 80, self.subtextcolour, 24) # display lives
            draw_text_centre(self.screen, f"{incorrect_chars}", width, height, 200, 110, self.maincolour, 24) # display number of lives

        # lives
        if gameMode == "Survival":
            draw_text_centre(self.screen, f"lives left", width, height, 200, 80, self.subtextcolour, 24) # display lives
            draw_text_centre(self.screen, f"{lives}", width, height, 200, 110, self.maincolour, 24) # display number of lives
            if testFailed:
                draw_text_centre(self.screen, "FAILED", width, height, 0, -150, self.error, 60) # display "FAILED" # display FAILED if the user fails test

            