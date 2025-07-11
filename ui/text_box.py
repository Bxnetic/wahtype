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
        else:
            if event.unicode and event.unicode.isprintable():
                self.usertext += event.unicode # adds user's letter to the usertext string


    def wrap_text(self, text, font, max_width):
        words = text.split(" ") # split the words in the sentence
        lines = [] # lines array
        current_line = "" # current line that's being constructed

        for word in words: 
            temp_line = current_line + word + " " # adds next word to the temporary line
            if font.size(temp_line)[0] <= max_width: # checks if the size of the line (width) can fit the window (before it gets cut off)
                current_line = temp_line # if the line still fits the window, then add the word
            else:
                lines.append(current_line) # if not then wrap the line   
                current_line = word + " " # start new line
            
        if current_line: # if there is a final line left then
            lines.append(current_line) # add it to the line array so it can appear on screen

        return lines

    def get_sentence(self):
        return "Hello"


    def draw_text(self):
        
        max_width = WIDTH - 40 # add 20px padding to edge
        y_offset = 20 # height of the lin
        
        target_text = self.get_sentence()

        target_text_lines = self.wrap_text(target_text, self.font, max_width)

        # break words down into each character
        user_chars = list(self.usertext)

        char_index = 0 # index of current character across all lines
        
        for line in target_text_lines: # loop through each line in the target sentence
            x_offset = 20 # left padding for each line
            for char in line: # go through each character in the line
                if char_index < len(user_chars): # checks if the user has typed the amount of characters
                    
                    user_char = user_chars[char_index] # gets current character typed at same position as target character, to compare them

                    if user_char == char: # if user's character matches target char then print character in green
                        color = self.maintextcolour
                    else:
                        color = self.errorcolour # if not, print character in red
                else:
                    color = self.subtextcolour # if neither, then display grey

                # display rendered character
                rendered_char = self.font.render(char, True, color)

                # draw the character at the (x, y) positions of the screen
                self.screen.blit(rendered_char, (x_offset, y_offset))

                # move x pos to the right, by the width of the character just drawn, so the characters dont overlap themselves
                x_offset += self.font.size(char)[0] # gets x pos of the character just rendered

                # increase the character index, so it goes to the next character
                char_index += 1

            # once line finishes, move the next line down vertically
            y_offset += self.font.get_linesize() + 10 # add 10px of vertical spacing
        
        if self.usertext == target_text:
            test = self.font.render("well done", True, self.maintextcolour)
            self.screen.blit(test, (100, 100))
        