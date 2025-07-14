import pygame # imports pygame modules
from config import *
from wonderwords import RandomWord
import time

class Text():
    def __init__(self, screen):
        pygame.init()
        self.done = False # turns into true once user finishes typing
        self.usertext = "" # variable which stores what the user types
        self.randomword = RandomWord() # creates instance of RandomWord class
        self.target_text = self.get_sentence() # get the sentence in the target text
        self.start_time = None
        self.final_time = None

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

    def get_wpm(self, start_time, end_time):
        return
    
    def text_handle(self, event):
        if self.done:
            return # ignore input if typing is done

        if self.start_time is None and event.unicode.isprintable():
            self.start_time = time.time()

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
        words = [] # words are stored in the array
        sentence = "" # to construct the sentence
        for _ in range(15): # loop 15 times to create sentence with 15 words
            words.append(self.randomword.word(include_parts_of_speech=["nouns", "verbs", "adjectives"],
             word_max_length=5, word_min_length=2))
            sentence = " ".join(words) # adds a blank character 

        return sentence

    def get_timer(self):
        return

    def draw_text(self):
        # timer
        if self.start_time is not None: # if the timer has started, 
            # and the user hasnt completed the sentence
            if self.done and self.final_time is not None:
                elapsed_time = self.final_time # get the current time
            else:
                elapsed_time = time.time() - self.start_time # if the user has finished typing and the final time has a value
                # then display the final time
        else:
            elapsed_time = 0 # if none are true then set timer to 0
        
        # draw the timer
        timer_text = self.font.render(f"{elapsed_time}", True, self.subtextcolour)
        self.screen.blit(timer_text, (200, 200))

        max_width = WIDTH - 20 # add 20px padding to edge
        y_offset = 20 # height of the line

        target_text_lines = self.wrap_text(self.target_text, self.font, max_width)

        # break words down into each character
        user_chars = list(self.usertext)

        char_index = 0 # index of current character across all lines
        
        for line in target_text_lines: # loop through each line in the target sentence
            x_offset = 20 # left padding for each line
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
        
        if self.usertext == self.target_text and not self.done: # checks if user's sentence fully matches target sentence
            # and the condition to check if the sentence isn't done is false then
                self.done = True

                # calculate the final time
                if self.start_time is not None: # checks that self.start_time always has a value
                    self.final_time = time.time() - self.start_time  # store final time
                
                test = self.font.render("well done", True, self.maintextcolour)
                self.screen.blit(test, (200, 200))
