import pygame # imports pygame modules
from config import* # import config variables, classes
from ui.text_box import * # import text_box variables, classes
from ui.button import * # import button variables, classes
from ui.results_screen import * # import results_screen variables, classes
from core.menu import * # import menu variables, classes
from core.selection import Selection # import selection class
from core.stats import StatsMenu # import statsmenu class

class Game:
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30) # allows user to hold key
        pygame.display.set_caption("wahtype") # sets name of window
        self.width = WIDTH # width of window
        self.height = HEIGHT # height of window
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) # sets size of the window

        # runtime
        self.clock = pygame.time.Clock() # creates time using time pygame clock module
        self.running = True # tracks if program is running
        self.mouse_released = True # check if user has stopped holding left click

        # game conditions
        self.game_started = False # tracks if game has started
        self.test_failed = False # checks if user has failed test
        self.current_screen = "menu" # tracks the current screen
    
        # theme colours
        self.bgcolour = pygame.Color(BACKGROUND) # theme colours
        self.white = pygame.Color(WHITE) # theme colours

        # images
        self.reset_img = pygame.image.load("images\\reset_button.png").convert_alpha()
        self.reset_img_hover = pygame.image.load("images\\reset_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()
        self.game_icon = pygame.image.load("images\\game_icon.png").convert_alpha() # game icon
        
        # initiate buttons
        self.reset_button = Button(0, 0, self.reset_img, 
            self.reset_img_hover, 0.2, "test", 0, self.white, self.white)
        self.home_button = Button(0, 0, self.home_img,
            self.home_img_hover, 0.2, "", 0, self.white, self.white)
        
        pygame.display.set_icon(self.game_icon) # set window icon
        
        # classes
        self.game_selection = Selection(self.screen, self.current_screen) # create selection object
        self.statsmenu = StatsMenu(self.screen, self.current_screen) # create statsmenu object
        self.number_of_words = self.game_selection.getNumberOfWords() # get number of words from selection class
        self.game_mode = self.game_selection.getGameMode() # get game mode from selection class
        self.time_selection = self.game_selection.getSeconds() # get user's selected seconds from selection class
        self.text = Text(self.screen, self.number_of_words, self.time_selection) # create text object
        self.menu = Menu(self.screen) # create menu object and passes screen to menu
        self.results_screen = Results(self.screen) # create results screen object
            
    def reset(self):
        self.text.usertext = "" # set usertext back to normal state
        self.text.full_usertext = "" # set full_usertext back to normal state
        self.text.game_lives = 3 # reset number of lives
        self.text.incorrect_chars = 0 # reset incorrect characters
        self.text.target_text = sentence.get_easy_sentence(self.text.number_of_words) # set target_text back to normal state
        self.text.stats.reset() # set timer back to normal state
        self.text.done = False # set done back to false state
        self.test_failed = False # set failed state back to false
        self.game_started = False

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

    def centre(self, surface, widthPadding, heightPadding): # function that centres surface
        rect = surface.get_rect()
        return (
            int((self.width / 2)) - int(rect.width / 2) + widthPadding,
        int((self.height / 2)) - int(rect.height / 2) + heightPadding
        ) # centre surface
        
    def testElements(self):
        if self.current_screen == "game": # if the test is running
            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text(self.width, self.height, self.game_mode) # draws to screen and passes current width to draw_text

            # set the the buttons to its default positions
            self.reset_button.rect.topleft = (self.centre(self.reset_button.image, 30, 250)) # reset button
            self.home_button.rect.topleft = (self.centre(self.home_button.image, -30, 250)) # home button

            if len(self.text.usertext) == len(self.text.target_text) and not self.text.done:
            # checks if user's sentence fully matches target sentence
            # and the condition to check if the target sentence hasn't been completed
                if self.game_mode == "Normal" or self.game_mode == "Survival":
                    self.text.stats.stop() # stop the time
                    self.text.done = True # stop the user from typing
                elif self.game_mode == "Timed":
                    self.text.usertext = ""
                    self.text.create_sentence(self.number_of_words) # create another target sentence
                    print("new sentence generated")
                      
            # survival mode
            if self.game_mode == "Survival" and self.text.game_lives <= 0:
                self.text.stats.stop() # stop the time
                self.text.done = True
                self.test_failed = True

            if self.game_mode == "Timed":
                self.text.stats.countdown() # call countdown method
                if self.text.countdown_time == 0:
                    self.text.done = True

            # once the test is over
            if self.text.done: # once test has been completed
                self.current_screen = "results"
                if self.test_failed != True:
                    self.text.stats.save_score(
                        self.game_mode, self.text.current_wpm, self.text.final_accuracy, self.text.time_selection,
                        self.text.typed_characters, self.text.incorrect_chars, self.text.number_of_words, self.text.game_lives
                    )
                    print("Saved score")
                self.statsmenu.update_stats() # update stats
                return self.current_screen
            
            # clicking buttons
            if self.reset_button.draw(self.screen, self.mouse_released): # if the reset button is clicked
                self.reset() # call the reset method in the Text class (resets all variables)
                self.mouse_released = False
            if self.home_button.draw(self.screen, self.mouse_released): # if the home button is clicked
                self.current_screen = "menu" # display menu
                self.mouse_released = False
        else:
            self.reset() # reset the test
        
    def run(self):
        while self.running: # gets current status of game
            """ debug """
            # print(self.number_of_words)
            # print(self.current_screen)
            # print(self.height)
            # print(self.game_mode)
            # print(f"lives: {self.text.game_lives}")
            # print(self.time_selection)
            # print(self.text.stats.count_time)

            """ methods """
            self.clock.tick(FPS) # sets the frames to 60
            self.resizableWindow() # calls function so user can resize window
            
            """ screen states """
            if self.current_screen == "menu":
                game_state = self.menu.draw(self.width, self.height, self.mouse_released) # display the menu
                if game_state:
                    self.current_screen = game_state # set current screen as current game state
                    self.mouse_released = False # left click has been clicked
                    self.game_started = False # don't start the game
                    self.reset() # reset the attributes for the test itself

            elif self.current_screen == "selection":
                game_state = self.game_selection.draw(self.width, self.height, self.mouse_released) # display the selection screen
                if game_state:
                    self.current_screen = game_state # set current screen as current game state
                    self.mouse_released = False # left click has been clicked

            elif self.current_screen == "game": # if the current screen is the game
                if not self.game_started: # and the game start condition is false
                    self.text.stats.count_time = -1 # make the countdown timer decrement by one until game starts
                    self.time_selection = self.game_selection.getSeconds() # get user's selected time
                    self.text.update_time(self.time_selection) # update user's selected time
                    self.number_of_words = self.game_selection.getNumberOfWords() # get number of words
                    self.game_mode = self.game_selection.getGameMode() # get game mode
                    self.text.create_sentence(self.number_of_words) # create target sentence
                    self.game_started = True # game has started - so sentence stops being created
                self.testElements() # test elements to be displayed on screen

            elif self.current_screen == "results": # if the current screen is the result screen
                self.displayed_time = 0 # either display elapsed_time or the time_selection
                if self.game_mode == "Normal" or self.game_mode == "Survival":
                    self.displayed_time = self.text.elapsed_time # display elapsed time
                if self.game_mode == "Timed":
                    self.displayed_time = self.text.time_selection # display time selection
                self.results_screen.end_stats (
                    round(self.text.current_wpm), 
                    round(self.displayed_time),
                    round(self.text.final_accuracy),
                    self.width, self.height,
                    self.game_mode, self.test_failed, self.text.game_lives,
                    self.text.typed_characters, self.text.incorrect_chars
                ) # call the results_screen method

                # set the the buttons to its default positions
                self.reset_button.rect.topleft = (self.centre(self.reset_button.image, 30, 250)) # reset button
                self.home_button.rect.topleft = (self.centre(self.home_button.image, -30, 250)) # home button

                # clicking buttons
                if self.reset_button.draw(self.screen, self.mouse_released): # if the reset button is clicked
                    self.reset() # call the reset method in the Text class (set values to default)
                    self.current_screen = "game" # start game
                    self.mouse_released = False
                if self.home_button.draw(self.screen, self.mouse_released): # if the home button is clicked
                    self.current_screen = "menu" # display menu
                    self.reset() # reset the test
                    self.mouse_released = False

            elif self.current_screen == "stats":
                game_state = self.statsmenu.draw(self.width, self.height, self.mouse_released) # display the stats screen
                if game_state:
                    self.current_screen = game_state # set current screen as current game state
                    self.mouse_released = False # left click has been clicked
                
            elif self.current_screen == "quit":
                self.running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if user quits progra,
                    self.running = False # end program
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouse_released = True
                if self.current_screen == "game": # if the test is running
                    if event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                        self.text.text_handle(event, self.game_mode) # call text_handle method
        pygame.quit() # closes program