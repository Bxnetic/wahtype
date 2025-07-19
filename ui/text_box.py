import pygame # imports pygame modules
from config import *
from data.stats_tracker import *
from data.sentence_manager import *

class Text():
    def __init__(self, screen):
        pygame.init()
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types
        self.target_text = sentence.get_easy_sentence() # grabs the constructed target sentence in the sentence class
        self.timer = Stats()

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
        self.font_underline = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_underline.set_underline(True)
    
    def text_handle(self, event):
        if self.done:
            return # ignore input if typing is done

        if not self.done and self.timer.start_time == 0 and event.unicode and event.unicode.isprintable(): # if the sentence hasn't been completed
            # and the timer hasn't started (and the user types a key)
            self.timer.start() # start the timer

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


    def draw_text(self, currentWidth, currentHeight):
        # timer
        elapsed_time = self.timer.get_elapsed_time()
        
        # draw the timer
        if elapsed_time != 0:
            timer_text = self.font.render(f"{round(elapsed_time)}", True, self.maincolour)
            self.screen.blit(timer_text, (100, currentHeight / 2 - 135))

        underline_char = self.font.render("_", True, self.white)

        """ rendering characters """
        max_width = currentWidth - 200 # add 20px padding to edge
        y_offset =  (currentHeight / 2) - 100 # height of the line
        
        target_text_lines = self.wrap_text(self.target_text, self.font, max_width)

        # break words down into each character
        user_chars = list(self.usertext)

        char_index = 0 # index of current character across all lines
        
        for line in target_text_lines: # loop through each line in the target sentence
            x_offset = 100 # left padding for each line
            for char in line: # go through each character in the line
                if char_index < len(user_chars): # checks if the user has typed the amount of characters
                    
                    user_char = user_chars[char_index] # gets current character typed at same position as target character, to compare them

                    if user_char == char: # if user's character matches target char then print character in white
                        color = self.maintextcolour
                    else:
                        color = self.errorcolour # if not, print character in red
                else:
                    color = self.subtextcolour # if neither, then display grey

                # display rendered character
                rendered_char = self.font.render(char, True, color)
                # draw the character at the (x, y) positions of the screen
                rendered_char_rect = rendered_char.get_rect(topleft=(x_offset, y_offset))
                self.screen.blit(rendered_char, rendered_char_rect)

                # move x pos to the right, by the width of the character just drawn, so the characters dont overlap themselves
                x_offset += self.font.size(char)[0] # gets x pos of the character just rendered

                # increase the character index, so it goes to the next character
                char_index += 1

            # once line finishes, move the next line down vertically
            y_offset += self.font.get_linesize() + 10 # add 10px of vertical spacing
        
        if len(self.usertext) == len(self.target_text) and not self.done: # checks if user's sentence fully matches target sentence
            # and the condition to check if the target sentence hasn't been completed
                self.timer.stop() # stop the time
                self.done = True # stop the user from typing
        elif len(self.usertext) == len(self.target_text) and self.done: # if the sentences match, and the user can't type anymore
            # temporarily display well done (will be replaced with WPM)
                test = self.font.render("well done", True, self.maintextcolour)
                self.screen.blit(test, (currentWidth / 2 - 75, currentHeight / 2 + 50))
