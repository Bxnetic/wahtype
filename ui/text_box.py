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
        
        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.maincolour = pygame.Color(MAIN)
        self.submaincolour = pygame.Color(SUBMAIN)
        self.maintextcolour = pygame.Color(MAINTEXT)
        self.subtextcolour = pygame.Color(SUBTEXT)
        self.errorcolour = pygame.Color(ERROR)
        self.suberror = pygame.Color(SUBERROR)

        # screen
        self.screen = screen

        # font
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)

    def text_handle(self, event):
        if self.done:
            return # ignore input if typing is done

        if event.key == pygame.K_BACKSPACE: # if user presses backspace, removes last character 
            if len(self.usertext) > 0: 
                self.usertext = self.usertext[:-1]
            print(self.usertext)
        elif event.key == pygame.K_RETURN: # if user presses enter / return, then typing is done
            self.done = True
            # self.usertext = "" # resets the current string if enter / return is pressed
        else:
            self.usertext += event.unicode # adds user's letter to the usertext string
            print(self.usertext)

    def draw_text(self):

        usertext = self.font.render(self.usertext, True, self.maintextcolour) # renders the text "hello world!"
        userstext_rect = usertext.get_rect(topleft = (20, 20))
        sentence = self.font.render("hello horse beautiful yes test when they are", True, self.subtextcolour)
        sentence_rect = sentence.get_rect(topleft = (20, 20))

        self.screen.blit(usertext, userstext_rect) # displays the text on screen
        self.screen.blit(sentence, sentence_rect) # displays the text on screen