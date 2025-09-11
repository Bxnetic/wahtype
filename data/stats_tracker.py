import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.final_time = 0
    
    """ timer """
    def start(self):
        # starts timer
        self.start_time = time.time()

    def stop(self):
        # ends timer
        if self.start_time != 0: # if the timer has already started 
            self.final_time = time.time() - self.start_time # final

    def reset(self):
        # resets timer
        self.start_time = 0
        self.end_time = 0
        self.final_time = 0

    def get_elapsed_time(self):
        if self.start_time == 0: # if the timer hasn't started then display 0
            return 0
        if self.final_time != 0: # if the user hasn't completed the sentence
            # and the time the final time doesn't have a value then
            return self.final_time # get the current time
          
        return time.time() - self.start_time # if the user has finished typing and the final time has a value
        # then display the final time

class Wpm:
    def __init__(self):
        self.wpm = 0
        self.last_wpm_time = 0
    
    def reset(self):
        self.wpm = 0
        self.last_wpm_time = 0

    def get_wpm(self, text, elapsed_time):
        if int(elapsed_time) != self.last_wpm_time: # if the current time doesnt match the last wpm time
            self.last_wpm_time = int(elapsed_time) # update the last wpm time
            self.wpm = (len(text)/5)/(elapsed_time / 60) # get wpm

        return self.wpm # return wpm

class Accuracy:
    def __init__(self):
        self.accuracy = 0

    def reset(self):
        self.accuracy = 0 # accuracy to go back to 0

    def get_accuracy(self, target_text, user_text):
        correct_chars = 0 # number of correct characters
        total_chars = len(user_text) # get total number of characters

        for i, char in enumerate(user_text): # go through each character, and get the index and character typed
            if i < len(target_text) and char == target_text[i]: # check the length is in range, and the character
                # equals the target character
                correct_chars += 1 # add 1 to correct characters
        if total_chars == 0: # if the user hasn't typed anything yet
            return 0
        else:
            self.accuracy = (correct_chars / total_chars) * 100 # calculate accuracy
            return self.accuracy # return accuracy value