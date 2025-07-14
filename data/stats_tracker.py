import time

class Stats():
    def __init__(self):
        self.start_time = False
        self.end_time = False
        self.final_time = False
    
    def start(self):
        # starts timer
        self.start_time = time.time()

    def stop(self):
        # ends timer
        if self.start_time != False:
            self.final_time = time.time() - self.start_time

    def get_elapsed_time(self):
        if self.start_time == False: # if the timer hasn't started then display 0
            return 0
        if self.final_time != False: # if the user hasn't completed the sentence
            # and the time the final time doesn't have a value then
            return self.final_time # get the current time
          
        return time.time() - self.start_time # if the user has finished typing and the final time has a value
        # then display the final time