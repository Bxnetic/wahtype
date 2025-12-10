import time
import pygame
import os

class Stats:
    def __init__(self):
        self.start_time = 0 # start time of timer
        self.end_time = 0 # end time of timer
        self.final_time = 0 # final time of timer
        self.current_tick = 0 # current count down timer
        self.last_tick = 0 # previous number of count down
        self.count_time = 0 # count down timer
        self.wpm = 0 # current wpm
        self.last_wpm_time = 0 # last time the wpm was calculated
        self.accuracy = 0 # end accuracy
        # SCORES
        self.scores_file = "data\\databases\\scores.txt"

    def reset(self):
        # resets all instance attributes
        self.start_time = 0
        self.end_time = 0
        self.final_time = 0
        self.current_tick = 0
        self.last_tick = 0
        self.count_time = 0
        self.wpm = 0
        self.last_wpm_time = 0
        self.accuracy = 0
    
   # timer
    def start(self):
        # starts timer
        self.start_time = time.time()

    def stop(self):
        # ends timer
        if self.start_time != 0: # if the timer has already started 
            self.final_time = time.time() - self.start_time # final

    def get_elapsed_time(self):
        if self.start_time == 0: # if the timer hasn't started then display 0
            return 0
        if self.final_time != 0: # if the user hasn't completed the sentence
            # and the time the final time doesn't have a value then
            return self.final_time # get the current time
          
        return time.time() - self.start_time # if the user has finished typing and the final time has a value
        # then display the final time

    # countdown timer
    def start_countdown(self, user_time):
        self.count_time = user_time # user's selected time
        self.last_tick = pygame.time.get_ticks() # get starting tick

    def countdown(self):
        self.current_tick = pygame.time.get_ticks() # get current tick
        if self.current_tick - self.last_tick >= 1000: # 1000ms = 1s
            self.count_time -= 1 # decrease timer by 1
            self.last_tick = self.current_tick # update last tick to current tick
            # print(self.count_time) # debug
    
    def get_countdown_timer(self):
        return self.count_time # return countdown time

    # wpm
    def get_wpm(self, text, elapsed_time):
        if int(elapsed_time) != self.last_wpm_time: # if the current time doesnt match the last wpm time
            self.last_wpm_time = int(elapsed_time) # update the last wpm time
            self.wpm = (len(text)/5)/(elapsed_time / 60) # get wpm

        return self.wpm # return wpm

    # accuracy
    def get_accuracy(self, target_text, user_text, incorrect_chars):
        correct_chars = 0 # number of correct characters
        total_chars = len(user_text) # get total number of characters

        for i, char in enumerate(user_text): # go through each character, and get the index and character typed
            if i < len(target_text) and char == target_text[i]: # check the length is in range, and the character
                # equals the target character
                correct_chars += 1 # add 1 to correct characters
        if total_chars == 0: # if the user hasn't typed anything yet
            return 0
        else:
            self.accuracy = (correct_chars / (total_chars + incorrect_chars)) * 100 # calculate accuracy
            return self.accuracy # return accuracy value

    def load_scores(self):
        scores = [] # list where the dictionaries will be stored
        if not os.path.exists(self.scores_file):
            with open(self.scores_file, "a") as file:
                file.write("")
            file.close
        else:
            with open(self.scores_file, "r") as file: # open scores.txt
                for line in file: # go through each line in file
                    mode, wpm, accuracy, time_taken, chars, incorrect, words, lives = line.strip().split() # split each stat into its
                    # own value
                    scores.append ( # create list of dictionaries
                    {
                        "mode": str(mode),
                        "wpm": float(wpm),
                        "accuracy": float(accuracy),
                        "time": float(time_taken),
                        "chars": int(chars),
                        "incorrect": int(incorrect),
                        "words": int(words),
                        "lives": int(lives)
                    }
                    )
            file.close() # close scores.txt
        return scores # return list of stats

    def save_score(self, mode, wpm, accuracy, time_taken, chars, incorrect, words, lives):
        with open(self.scores_file, "a") as file: # open file, create new one if not exisitng
            file.write(f"{mode} {round(wpm)} {round(accuracy)} {round(time_taken)} {chars} {incorrect} {words} {lives}\n") # add new stats to file
            file.close() # close scores.txt

    def delete_scores(self):
        with open(self.scores_file, "w") as file: # open file in "write" mode
            file.write(f"") # clear everything
            file.close() # close file

    def get_personal_best(self, mode, words):
        scores = self.load_scores()
        mode_scores = [] # list of scores for depending on mode

        # filter only by matching game mode
        for s in scores: # go through each score in scores
            if s["mode"] == mode and s["words"] == words: # if score matches game mode
                mode_scores.append(s) # add to mode_scores list
        
        if not mode_scores: # if there is nothing in the list
            return None

        best_score = mode_scores[0] # start with first score
        for score in mode_scores[1:]: # go through rest of scores
            if score["wpm"] > best_score["wpm"]: # if current score is bigger than the current best score
                best_score = score # set that as the best score
        return best_score

    def get_timed_personal_best(self, time_taken):
        scores = self.load_scores()
        timed_scores = [] # list of scores for depending on mode

        # filter only by matching time
        for s in scores: # go through each score in scores
            if s["mode"] == "Timed" and s["time"] == time_taken: # if score matches time
                timed_scores.append(s) # add to timed_scores list
        
        if not timed_scores: # if there is nothing in the list
            return None

        best_score = timed_scores[0] # start with first score
        for score in timed_scores[1:]: # go through rest of scores
            if score["wpm"] > best_score["wpm"]: # if current score is bigger than the current best score
                best_score = score # set that as the best score
        return best_score