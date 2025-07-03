import pygame # imports pygame modules
from config import BLACK, WHITE

class Text():
    def __init__(self):
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types
        self.white = WHITE
        self.black = BLACK

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
        return

text = Text() # creates an object called "text"