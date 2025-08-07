import pygame # imports pygame modules
from config import *
from data.stats_tracker import *
from data.sentence_manager import *
from ui.results_screen import *

class Text:
    def __init__(self, screen):
        # screen
        self.screen = screen

        # text
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types
        self.target_text = sentence.get_easy_sentence() # grabs the constructed target sentence in the sentence class

        # classes
        self.timer = Timer() # create timer object
        self.wpm = Wpm() # create wpm object
        self.results_screen = Results(self.screen)

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

        # font
        self.font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_underline = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", 24)
        self.font_underline.set_underline(True)
    
    """ text inputs from user """
    def text_handle(self, event):
        if not self.done and self.timer.start_time == 0 and event.unicode and event.unicode.isprintable(): # if the sentence hasn't been completed
            # and the timer hasn't started (and the user types a key)
            self.timer.start() # start the timer

        # split words into own variable
        user_words = self.usertext.split(" ") # put current words into array
        target_words = self.target_text.split(" ") # put target words into array

        current_index = len(user_words) - 1 # get the index of current word
        current_word = user_words[current_index] # get the current word the user is typing

        if current_index < len(target_words): # checks if the current index is less than the length of the no. of words
            target_word = target_words[current_index] # if it is then get the target word
        else:
            target_word = "" # no target word

        if event.key == pygame.K_BACKSPACE: # if user presses backspace, removes last character 
            if len(self.usertext) > 0: 
                self.usertext = self.usertext[:-1]

        # can only press space if the length of the user's word and target word matches, 
        # adds blank space & prevents spamming
        elif event.key == pygame.K_SPACE:
            if len(current_word) == len(target_word):
                self.usertext += " "

        else:
            if event.unicode and event.unicode.isprintable():
                if len(current_word) < len(target_word): # if the length of current word is less than the target word
                    # then let the user type
                    self.usertext += event.unicode # adds user's letter to the usertext string
                
    """ text wrapping """
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
    
    """ cursor """
    def get_cursor(self, char_index, user_chars, x_offset, y_offset):
        cursor = self.font.render("|", True, self.maintextcolour) # create cursor
        cursor_rect = cursor.get_rect(topright=(x_offset + self.font.get_height() // 4, y_offset)) # cursor rect    

        # display cursor
        if (char_index == len(user_chars)) and not self.done: # checks the number of characters the user has inputted
            # matches the current characters
            return self.screen.blit(cursor, cursor_rect) # display the cursor

    def draw_text(self, currentWidth, currentHeight):

        """ timer & wpm"""
        elapsed_time = self.timer.get_elapsed_time()
   
        if elapsed_time != 0: # if the timer hasn't started
            # display timer & wpm
            stats_text = self.font.render(f"{round(elapsed_time)} {round(self.wpm.get_wpm(self.usertext, elapsed_time))}",
            True, self.maincolour)
            self.screen.blit(stats_text, (100, currentHeight / 2 - 135))

        """ rendering characters """
        max_width = currentWidth - 200 # add 200px padding to edge
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
                if color == self.errorcolour: # if user get character incorrect
                    rendered_char = self.font_underline.render(char, True, color) # underline character
                else:
                    rendered_char = self.font.render(char, True, color) # display normally

                # draw the character at the (x, y) positions of the screen
                rendered_char_rect = rendered_char.get_rect(topleft=(x_offset, y_offset))
                self.screen.blit(rendered_char, rendered_char_rect)

                # move x pos to the right, by the width of the character just drawn, so the characters dont overlap themselves
                x_offset += self.font.size(char)[0] # gets x pos of the character just rendered

                # increase the character index, so it goes to the next character
                char_index += 1
                
                # get cursor
                self.get_cursor(char_index, user_chars, x_offset, y_offset)

            # once line finishes, move the next line down vertically
            y_offset += self.font.get_linesize() + 10 # add 10px of vertical spacing
        
        if len(self.usertext) == len(self.target_text) and not self.done: # checks if user's sentence fully matches target sentence
            # and the condition to check if the target sentence hasn't been completed
                self.timer.stop() # stop the time
                self.done = True # stop the user from typing

        # once the test is over
        if self.done:
            return self.results_screen.end_stats(round(self.wpm.get_wpm(self.usertext, elapsed_time)), 
             round(elapsed_time), currentWidth, currentHeight)

    def reset(self):
        self.usertext = "" # set usertext back to normal state
        self.target_text = sentence.get_easy_sentence() # set target_text back to normal state
        self.timer.reset() # set timer back to normal state
        self.wpm.reset() # set wpm back to normal state
        self.done = False # set done back to false state