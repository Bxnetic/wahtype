import pygame # imports pygame modules

class Text():
    def __init__(self):
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types

    def text_handle(self, event):
        if self.done:
            return # ignore input if typing is done

        if event.key == pygame.K_BACKSPACE:
            self.usertext = self.usertext[:-1]
            print(self.usertext)
        elif event.key == pygame.K_RETURN:
            self.done = True
        else:
            self.usertext += event.unicode
            print(self.usertext)

text = Text()