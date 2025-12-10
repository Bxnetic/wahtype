import pygame # imports pygame modules
from config import* # import config attributes, classes
from ui.text_box import * # import text_box attributes, classes
from ui.button import * # import button attributes, classes
from ui.surface_handle import * # import commonly used procedures for surface
from ui.results_screen import * # import results_screen attributes, classes
from core.menu import * # import menu attributes, classes
from core.selection import Selection # import selection class
from core.stats import StatsMenu # import statsmenu class
from core.settings import Settings # import settings class
from core.audio_handle import Audio # import audio class
from core.about import About # import about class

class Game:
    def __init__(self): # game constructor
        pygame.init() # initialises pygame
        pygame.key.set_repeat(300, 30) # allows user to hold key
        pygame.display.set_caption("wahtype") # sets name of window
        self.width = WIDTH # width of window
        self.height = HEIGHT # height of window
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) # sets size of the window

        # RUNTIME #
        self.clock = pygame.time.Clock() # creates time using time pygame clock module
        self.running = True # tracks if program is running
        self.mouse_released = True # check if user has stopped holding left click

        # CONDITIONS #
        self.game_started = False # tracks if game has started
        self.test_failed = False # checks if user has failed test
        self.current_screen = "menu" # tracks the current screen
        self.last_screen = None # tracks last screen it was on
    
        # THEME #
        self.bgcolour = pygame.Color(BACKGROUND) # theme colours
        self.maintext = pygame.Color(MAINTEXT) # theme colours

        # IMAGES #
        self.reset_img = pygame.image.load("images\\reset_button.png").convert_alpha()
        self.reset_img_hover = pygame.image.load("images\\reset_button_hover.png").convert_alpha()
        self.home_img = pygame.image.load("images\\home_button.png").convert_alpha()
        self.home_img_hover = pygame.image.load("images\\home_button_hover.png").convert_alpha()
        self.game_icon = pygame.image.load("images\\game_icon.png").convert_alpha()

        # BUTTONS #
        self.reset_button = Button(0, 0, self.reset_img, 
            self.reset_img_hover, 0.2, "", 0, self.maintext, self.maintext)
        self.home_button = Button(0, 0, self.home_img,
            self.home_img_hover, 0.2, "", 0, self.maintext, self.maintext)
        
        # ICON #
        pygame.display.set_icon(self.game_icon) # set window icon
        
        # CLASSES #
        self.menu = Menu(self.screen) # create menu object and passes screen to menu

        self.game_selection = Selection(self.screen, self.current_screen) # create selection object
        self.number_of_words = self.game_selection.getNumberOfWords() # get number of words from selection class
        self.time_selection = self.game_selection.getSeconds() # get user's selected seconds from selection class
        self.game_mode = self.game_selection.getGameMode() # get game mode from selection class
        
        # audio
        self.audio = Audio() # create audio object
        self.music_index = self.audio.get_settings("music")
        self.sound_fx_index = self.audio.get_settings("sound_fx")

        self.stats_menu = StatsMenu(self.screen, self.current_screen) # create statsmenu object
        self.settings_menu = Settings(self.screen, self.current_screen, self.music_index, self.sound_fx_index) # create settingsmenu object
        self.about_menu = About(self.screen, self.current_screen)
        self.text = Text(self.screen, self.number_of_words, self.time_selection) # create text object
        self.results_screen = Results(self.screen) # create results screen object

    # DEBUG
    def debug(self):
        print(self.number_of_words)
        print(self.current_screen)
        print(f"width: {self.width} height: {self.height}")
        print(self.game_mode)
        print(f"lives: {self.text.game_lives}")
        print(self.time_selection)
        print(self.text.stats.count_time)
        print(self.music)
        print(f"music: {self.audio.get_settings("music")} sound fx: {self.audio.get_settings("sound_fx")}")
    
    # RESET TEST
    def reset(self):
        self.text.usertext = "" # set usertext back to normal state
        self.text.full_usertext = "" # set full_usertext back to normal state
        self.text.game_lives = 3 # reset number of lives
        self.text.incorrect_chars = 0 # reset incorrect characters
        self.text.target_text = sentence.get_easy_sentence(self.text.number_of_words) # set target_text back to normal state
        self.text.stats.reset() # set timer back to normal state
        self.text.done = False # set done back to false state
        self.test_failed = False # set failed state back to false
        self.game_started = False # game / test is still running

    # RESIZE WINDOW
    def resizable_window(self): # get current width & height of window
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

    # CHECK IF USER IS CLICKING BUTTONS
    def clicking_buttons(self):
        if self.reset_button.draw(self.screen, self.mouse_released): # if the reset button is clicked
            self.current_screen = "game" # display test
            self.reset() # call the reset method in the Text class (resets all attributes)
            self.mouse_released = False # user is holding down left click
        if self.home_button.draw(self.screen, self.mouse_released): # if the home button is clicked
            self.current_screen = "menu" # display menu
            self.mouse_released = False # user is holding down left click 
    
    # ELEMENTS FOR THE TEST
    def test_elements(self):
        if self.current_screen == "game": # if the test is running
            self.screen.fill(self.bgcolour) # sets the display background to selected background colour
            self.text.draw_text(self.width, self.height, self.game_mode) # draws to screen and passes current width to draw_text

            # set the the buttons to its default positions
            self.reset_button.rect.topleft = centre(self.reset_button.image, self.width, self.height, 30, 250) # reset button
            self.home_button.rect.topleft = centre(self.home_button.image, self.width, self.height, -30, 250) # home button

            if len(self.text.usertext) == len(self.text.target_text) and not self.text.done:
            # checks if user's sentence fully matches target sentence
            # and the condition to check if the target sentence hasn't been completed
                if self.game_mode == "Normal" or self.game_mode == "Survival":
                    self.text.stats.stop() # stop the time
                    self.text.done = True # stop the user from typing
                elif self.game_mode == "Timed":
                    self.text.usertext = ""
                    self.text.create_sentence(self.number_of_words) # create another target sentence
                      
            # survival mode
            if self.game_mode == "Survival" and self.text.game_lives <= 0: # if user loses all lifes
                self.text.stats.stop() # stop the time
                self.text.done = True # end test
                self.test_failed = True # user has failed test

            # timed mode
            if self.game_mode == "Timed":
                self.text.stats.countdown() # setup countdown
                if self.text.countdown_time == 0: # once countdown reaches 0
                    self.text.done = True # end test

            if self.text.done: # once test has been completed
                self.current_screen = "results" # go to results screen
                if self.test_failed != True: # if user hasn't failed test
                    self.text.stats.save_score(
                        self.game_mode, self.text.current_wpm, self.text.final_accuracy, self.text.time_selection,
                        self.text.typed_characters, self.text.incorrect_chars, self.text.number_of_words, self.text.game_lives
                    ) # save score
                self.stats_menu.update_stats() # update stats
                return self.current_screen
            
            self.clicking_buttons() # check if buttons are being clicked
        else:
            self.reset() # reset the test
        
    def check_audio(self):
        self.music = self.settings_menu.music_selection # get music selection
        self.sound_fx = self.settings_menu.sound_fx_selection # get sound fx selection

        if self.current_screen != self.last_screen: # if current screen is different to last screen
            if self.music == "On": # music is on
                if self.current_screen in ("menu", "selection"): # in menu and selection menu
                    self.audio.play_music("audio\\main_menu.mp3") # play bgm

                if self.current_screen == "stats": # in stats menu
                    self.audio.play_music("audio\\stats_menu.mp3") # play bgm

                if self.current_screen == "settings": # in settings menu
                    self.audio.play_music("audio\\settings_menu.mp3") # play bgm

        if self.current_screen == "game": # test / game 
                self.audio.pause_music() # pause music
        else:
            if self.music == "On": # music is on
                self.audio.resume_music() # resume music
            
        self.last_screen = self.current_screen # set last screen to current screen
    
    def check_screen(self):
        # menu
        if self.current_screen == "menu":
            game_state = self.menu.draw(self.width, self.height, self.mouse_released) # display the menu
            if game_state:
                self.current_screen = game_state # set current screen as current game state
                self.mouse_released = False # user is holding down left click
                self.game_started = False # don't start the game
                self.reset() # reset the attributes for the test itself

        # game selection
        elif self.current_screen == "selection":
            game_state = self.game_selection.draw(self.width, self.height, self.mouse_released) # display the selection screen
            if game_state:
                self.current_screen = game_state # set current screen as current game state
                self.mouse_released = False # user is holding down left click

        # game
        elif self.current_screen == "game": # if the current screen is the game
            if not self.game_started: # and the game start condition is false
                self.text.stats.count_time = -1 # make the countdown timer decrement by one until game starts
                self.time_selection = self.game_selection.getSeconds() # get user's selected time
                self.text.update_time(self.time_selection) # update user's selected time
                self.number_of_words = self.game_selection.getNumberOfWords() # get number of words
                self.game_mode = self.game_selection.getGameMode() # get game mode
                self.text.create_sentence(self.number_of_words) # create target sentence
                self.game_started = True # game has started - so sentence stops being created
            self.test_elements() # test elements to be displayed on screen

        # results
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

            self.clicking_buttons() # check if buttons are being clicked
            
        # stats
        elif self.current_screen == "stats":
            game_state = self.stats_menu.draw(self.width, self.height, self.mouse_released) # display the stats screen
            if game_state:
                self.current_screen = game_state # set current screen as current game state
                self.mouse_released = False # user is holding down left click

        # settings
        elif self.current_screen == "settings":
            self.settings_menu.check_buttons() # checks if user presses buttons
            game_state = self.settings_menu.draw(self.width, self.height, self.mouse_released) # display the settings screen
            if game_state:
                self.current_screen = game_state # set current screen as current game state
                self.mouse_released = False # user is holding down left click

        # about
        elif self.current_screen == "about":
            game_state = self.about_menu.draw(self.width, self.height, self.mouse_released) # display the settings screen
            if game_state:
                self.current_screen = game_state # set current screen as current game state
                self.mouse_released = False # user is holding down left click

        # quit   
        elif self.current_screen == "quit":
            self.running = False # end program
    
    def run(self):
        while self.running:
            self.clock.tick(FPS) # set to 60fps
            self.resizable_window() # enables user to resize window
            self.check_audio() # checks music & sound fx conditions
            self.check_screen() # checks current screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if user quits program,
                    self.running = False # end program
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouse_released = True
                if self.current_screen == "game": # if the test is running
                    if event.type == pygame.KEYDOWN: # if presses any key, then add character to string
                        self.text.text_handle(event, self.game_mode, self.sound_fx) # call text_handle method

        pygame.quit() # closes program