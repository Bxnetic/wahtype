from config import *
from core.menu import Menu
from data.stats_tracker import Stats
from ui.surface_handle import *

class StatsMenu(Menu): # inherit from menu class
    def __init__(self, screen):
        super().__init__(screen) # inherit screen from menu class

        # CLASSES
        self.stats = Stats()
        
        # SCORES
        self.normal_best = self.stats.get_personal_best("Normal", 15)
        self.survival_best = self.stats.get_personal_best("Survival", 15)

        self.normal_best_25 = self.stats.get_personal_best("Normal", 25)
        self.survival_best_25 = self.stats.get_personal_best("Survival", 25)

        self.timed_best_15 = self.stats.get_timed_personal_best(15) 
        self.timed_best_30 = self.stats.get_timed_personal_best(30)
        self.timed_best_60 = self.stats.get_timed_personal_best(60)

    # update the stats when score has been submitted
    def update_stats(self):
        self.normal_best = self.stats.get_personal_best("Normal", 15)
        self.survival_best = self.stats.get_personal_best("Survival", 15)
        self.normal_best_25 = self.stats.get_personal_best("Normal", 25)
        self.survival_best_25 = self.stats.get_personal_best("Survival", 25)
        self.timed_best_15 = self.stats.get_timed_personal_best(15)
        self.timed_best_30 = self.stats.get_timed_personal_best(30)
        self.timed_best_60 = self.stats.get_timed_personal_best(60)
    
    def draw(self, width, height, mouse_released):
        self.update_stats() # update stats when loaded
        self.screen.fill(self.bgcolour) # clear all the entities on screen
        
        # normal
        draw_text_centre(self.screen, "Normal", width, height, -200, -250, self.maintext, 30) # display "normal"
        draw_text_centre(self.screen, "15 words", width, height, -300, -200, self.subtextcolour, 24) # display "15 words"
        draw_text_centre(self.screen, "25 words", width, height, -100, -200, self.subtextcolour, 24) # display "25 words"

        # 15 words
        if self.normal_best is None:
            draw_text_centre(self.screen, f"0", width, height, -300, -150, self.maincolour, 70) # display 0 wpm
            draw_text_centre(self.screen, f"0%", width, height, -300, -100, self.maintext, 24) # display 0 accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.normal_best["wpm"])}", width, height, -300, -150, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"{round(self.normal_best["accuracy"])}%", width, height, -300, -100, self.maintext, 24) # display accuracy
        
        # 25 words
        if self.normal_best_25 is None:
            draw_text_centre(self.screen, f"0", width, height, -100, -150, self.maincolour, 70) # display 0 wpm
            draw_text_centre(self.screen, f"0%", width, height, -100, -100, self.maintext, 24) # display 0 accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.normal_best_25["wpm"])}", width, height, -100, -150, self.maincolour, 70) # display 0 wpm
            draw_text_centre(self.screen, f"{round(self.normal_best_25["accuracy"])}%", width, height, -100, -100, self.maintext, 24) # display 0 accuracy
        
        # survival
        draw_text_centre(self.screen, "Survival", width, height, 200, -250, self.maintext, 30) # display "normal"
        draw_text_centre(self.screen, "15 words", width, height, 100, -200, self.subtextcolour, 24) # display "15 words"
        draw_text_centre(self.screen, "25 words", width, height, 300, -200, self.subtextcolour, 24) # display "25 words"

        # 15 words
        if self.survival_best is None:
            draw_text_centre(self.screen, f"0", width, height, 100, -150, self.maincolour, 70) # display 0 wpm
            draw_text_centre(self.screen, f"0%", width, height, 100, -100, self.maintext, 24) # display 0 accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.survival_best["wpm"])}", width, height, 100, -150, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"{round(self.survival_best["lives"])} lives", width, height, 100, -100, self.maintext, 24) # display characters
            draw_text_centre(self.screen, f"{round(self.survival_best["accuracy"])}%", width, height, 100, -70, self.maintext, 24) # display accuracy

        # 25 words
        if self.survival_best_25 is None:
            draw_text_centre(self.screen, f"0", width, height, 300, -150, self.maincolour, 70) # display 0 wpm
            draw_text_centre(self.screen, f"0%", width, height, 300, -100, self.maintext, 24) # display 0 accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.survival_best_25["wpm"])}", width, height, 300, -150, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"{round(self.survival_best_25["lives"])} lives", width, height, 300, -100, self.maintext, 24) # display characters
            draw_text_centre(self.screen, f"{round(self.survival_best_25["accuracy"])}%", width, height, 300, -70, self.maintext, 24) # display accuracy

        # timed
        draw_text_centre(self.screen, "Timed", width, height, 0, 0, self.maintext, 30) # display "wpm"
        draw_text_centre(self.screen, "15s", width, height, -200, 50, self.subtextcolour, 24) # display "15s"
        draw_text_centre(self.screen, "30s", width, height, 0, 50, self.subtextcolour, 24) # display "30s"
        draw_text_centre(self.screen, "60s", width, height, 200, 50, self.subtextcolour, 24) # display "60s"
        
        # 15s
        if self.timed_best_15 is None:
            draw_text_centre(self.screen, f"0", width, height, -200, 100, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"0%", width, height, -200, 150, self.maintext, 24) # display accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.timed_best_15["wpm"])}", width, height, -200, 100, self.maincolour, 70) # display wpm 
            draw_text_centre(self.screen, f"{round(self.timed_best_15["chars"])} chars", width, height, -200, 150, self.maintext, 24) # display characters
            draw_text_centre(self.screen, f"{round(self.timed_best_15["accuracy"])}%", width, height, -200, 180, self.maintext, 24) # display accuracy
        
        # 30s
        if self.timed_best_30 is None:
            draw_text_centre(self.screen, f"0", width, height, 0, 100, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"0%", width, height, 0, 150, self.maintext, 24) # display accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.timed_best_30["wpm"])}", width, height, 0, 100, self.maincolour, 70) # display accuracy
            draw_text_centre(self.screen, f"{round(self.timed_best_30["chars"])} chars", width, height, 0, 150, self.maintext, 24) # display characters
            draw_text_centre(self.screen, f"{round(self.timed_best_30["accuracy"])}%", width, height, 0, 180, self.maintext, 24) # display wpm
            
        # 60s
        if self.timed_best_60 is None:
            draw_text_centre(self.screen, f"0", width, height, 200, 100, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"0%", width, height, 200, 150, self.maintext, 24) # display accuracy
        else:
            draw_text_centre(self.screen, f"{round(self.timed_best_60["wpm"])}", width, height, 200, 100, self.maincolour, 70) # display wpm
            draw_text_centre(self.screen, f"{round(self.timed_best_60["chars"])} chars", width, height, 200, 150, self.maintext, 24) # display characters
            draw_text_centre(self.screen, f"{round(self.timed_best_60["accuracy"])}%", width, height, 200, 180, self.maintext, 24) # display accuracy

        # home button
        self.home_button.rect.topleft = centre(self.home_button.image, width, height, 0, 250) # home button
        if self.home_button.draw(self.screen, mouse_released): # display button on screen, checks if it has been clicked
            self.current_screen = "menu" # set current screen to menu
            return self.current_screen # return current screen state