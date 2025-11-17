import pygame
from config import *
from ui.button import *

class StatsMenu:
    def __init__(self, screen, current_screen):
        # screen
        self.screen = screen
        self.current_screen = current_screen

        # colours
        self.maincolour = pygame.Color(MAIN)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.bgcolour = pygame.Color(BACKGROUND)

        # images & buttons
        self.rounded_button_img  = pygame.image.load("images\\rounded_button.png").convert_alpha()
        self.rounded_button_hover_img = pygame.image.load("images\\rounded_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()
        
        # initiate button
        self.home_button = Button(0, 0, self.home_img, # home button
         self.home_img_hover, 0.2, "", 0, self.maincolour, self.maincolour) 

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

        # normal
        draw_text("Normal", 0, -250, self.subtextcolour, 24) # display "normal"
        draw_text("15 words", -100, -200, self.subtextcolour, 24) # display "15 words"
        draw_text(f"0", -100, -150, self.maincolour, 70) # display wpm
        draw_text(f"0%", -100, -100, self.maincolour, 24) # display accuracy
        draw_text("25 words", 100, -200, self.subtextcolour, 24) # display "25 words"
        draw_text(f"0", 100, -150, self.maincolour, 70) # display wpm
        draw_text(f"0%", 100, -100, self.maincolour, 24) # display accuracy

        # survival
        # draw_text("Survival", 0, 0, self.subtextcolour, 24) # display "wpm"
        # draw_text(f"0", 0, -130, self.maincolour, 70) # display wpm

        # # accuracy
        # draw_text("Timed", 200, -200, self.subtextcolour, 24) # display "accuracy"
        # draw_text(f"0%", 200, -130, self.maincolour, 70) # display accuracy

        # home button
        self.home_button.rect.topleft = (centre(self.home_button.image, 0, 250)) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # return current screen state