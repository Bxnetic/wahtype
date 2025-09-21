import pygame # imports pygame modules
from config import *
from ui.text_box import *
from ui.button import *
from ui.results_screen import *
from core.menu import *
from core.selection import *

class Game:
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30) # allows user to hold key
        # screen, fps and run
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # sets size of the window
        self.current_screen = "menu"
        self.clock = pygame.time.Clock() # creates time using time pygame clock module
        self.running = True
        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND)
        self.white = pygame.Color(WHITE) 
        # images for all the buttons
        self.reset_img = pygame.image.load("images\\reset_button.png").convert_alpha()
        self.reset_img_hover = pygame.image.load("images\\reset_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()
        # initiate buttons
        self.reset_button = Button(0, 0, self.reset_img, 
            self.reset_img_hover, 0.2, "test", 0, self.white, self.white)
        self.home_button = Button(0, 0, self.home_img,
            self.home_img_hover, 0.2, "", 0, self.white, self.white)
        # pygame window
        pygame.display.set_caption("Another Type Racing Game") # sets name of window (new)
        # classes
        self.text = Text(self.screen) # create text object and passes screen to Text
        self.menu = Menu(self.screen) # create menu object and passes screen to Menu
        self.results_screen = Results(self.screen) # create results screen object and passes screen to Results
        self.gameSelection = gameSelection(self.screen) # create game selection object and passes screen to gameSelection

    def reset(self):
        self.text.usertext = "" # set usertext back to normal state
        self.text.target_text = sentence.get_easy_sentence(self.text.number_of_words) # set target_text back to normal state
        self.text.stats.reset() # set timer back to normal state
        self.text.done = False # set done back to false state

    def resizableWindow(self): # get current width & height of window
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()

            # prevents user from resizing window under 800x600
            if self.width < 800: # if width is less than 800 (min width)
                self.screen = pygame.display.set_mode((WIDTH, self.height), pygame.RESIZABLE) # set width back to 800 and
                # keep current height
            elif self.height < 600: # if height is less than 600 (min height)
                self.screen = pygame.display.set_mode((self.width, HEIGHT), pygame.RESIZABLE)
                # set height back to 600, keep current width

            pygame.display.flip() # continuously updates the screen

    def testElements(self):
        def centre(button, widthPadding, heightPadding): # function that centers buttons on the middle of the screen
            return (
                int((self.width / 2)) - int(button.rect.width / 2) + widthPadding,
                    int((self.height / 2)) + heightPadding
            )
        
        if self.current_screen == "game": # if the test is running
            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text(self.width, self.height) # draws to screen and passes current width to draw_text

            if len(self.text.usertext) == len(self.text.target_text) and not self.text.done:
            # checks if user's sentence fully matches target sentence
            # and the condition to check if the target sentence hasn't been completed
                self.text.stats.stop() # stop the time
                self.text.done = True # stop the user from typing
                
            # once the test is over
            if self.text.done: # once test has been completed
                self.results_screen.end_stats(
                    round(self.text.current_wpm), 
                    round(self.text.elapsed_time),
                    round(self.text.final_accuracy),
                    self.width, self.height
                ) # call the results_screen method
                # move the buttons further down the screen
                self.reset_button.rect.topleft = (centre(self.reset_button, 30, 150)) # reset button
                self.home_button.rect.topleft = (centre(self.home_button, -30, 150)) # home button
            else:
                # set the the buttons to its default positions
                self.reset_button.rect.topleft = (centre(self.reset_button, 30, 50)) # reset button
                self.home_button.rect.topleft = (centre(self.home_button, -30, 50)) # home button
                
            # clicking buttons
            if self.reset_button.draw(self.screen): # if the reset button is clicked
                self.reset() # call the reset method in the Text class (resets all variables)
            if self.home_button.draw(self.screen): # if the home button is clicked
                self.current_screen == "menu"
  
        else:
            self.reset() # reset the test

    def run(self):
        while self.running: # gets current status of game
            self.clock.tick(FPS) # sets the frames to 60
            self.resizableWindow() # calls function so user can resize window
            print(self.current_screen)
            if self.current_screen == "menu":
                game_state = self.menu.draw(self.width, self.height) # display the menu
                if game_state:
                    self.current_screen = game_state
            elif self.current_screen == "selection":
                game_state = self.gameSelection.draw(self.width, self.height) # display the menu
                if game_state:
                    self.current_screen = game_state
            elif self.current_screen == "game":
                self.testElements() # test elements to be displayed on screen
            elif self.current_screen == "quit":
                self.running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if self.current_screen == "game": # if the test is running
                    if event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                        self.text.text_handle(event) # call text_handle method
        pygame.quit() # closes program
