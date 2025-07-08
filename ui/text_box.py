import pygame # imports pygame modules
from config import *

class Text():
    def __init__(self, screen):
        pygame.init()
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types

        # basic colours
        self.white = WHITE 
        self.black = BLACK
        self.screen = screen

        # font
        self.font = pygame.font.Font(None, 32)

    def text_handle(self, event):
        if self.done:
            return # ignore input if typing is done

        if event.key == pygame.K_BACKSPACE and len(self.usertext) > 0: # if user presses backspace, removes last character 
            self.usertext = self.usertext[:-1]
            print(self.usertext)
        elif event.key == pygame.K_RETURN: # if user presses enter / return, then typing is done
            self.done = True
            # self.usertext = "" # resets the current string if enter / return is pressed
        else:
            self.usertext += event.unicode # adds user's letter to the usertext string
            print(self.usertext)

    def draw_text(self):
        self.screen.fill(self.black) # sets the display background to black

        test = self.font.render(self.usertext + "|", True, self.white) # renders the text "hello world!"
        self.screen.blit(test, (20, 20)) # displays the text on screen