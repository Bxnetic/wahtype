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

    def get_wpm(self, text, elapsed_time):
        if int(elapsed_time) != self.last_wpm_time:
            self.last_wpm_time = int(elapsed_time)
            self.wpm = (len(text)/5)/(elapsed_time / 60) # get wpm

        return self.wpm