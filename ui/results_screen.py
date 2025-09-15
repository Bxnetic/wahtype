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

    def end_stats(self, wpm, time, accuracy, width, height):
        self.screen.fill(self.bgcolour) # clear all the entities on screen

        def centre(text, paddingWidth, paddingHeight):
            return (
                (width / 2) - (text.get_width()) / 2 + paddingWidth, (height / 2)
                 - (text.get_height() / 2 + paddingHeight)
            ) # display text on the top
            
        def draw_text(text, x, y, color, size):
            font = pygame.font.Font("fonts\\ari-w9500-bold.ttf", size) # font
            current_text = font.render(text, True, color) # render the text
            current_text_rect = current_text.get_rect(
                topleft=(centre(current_text, x, y))) # display text in the centre
            self.screen.blit(current_text, current_text_rect) # display the text on screen

        """ wpm """
        draw_text("wpm", 0, 50, self.subtextcolour, 24) # display "wpm"
        draw_text(f"{wpm}", 0, 0, self.maincolour, 70) # display wpm

        """ time """
        draw_text("time", -200, 50, self.subtextcolour, 24) # display "time"
        draw_text(f"{time}", -200, 0, self.maincolour, 70) # display final time

        """ accuracy """
        draw_text("accuracy", 200, 50, self.subtextcolour, 24) # display "accuracy"
        draw_text(f"{accuracy}%", 200, 0, self.maincolour, 70) # display accuracy