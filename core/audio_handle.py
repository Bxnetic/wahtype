import pygame

class Audio:
    def __init__(self):
        # audio
        self.last_music = None # tracks last music that was played
        self.music_paused = False # checks if the music has been paused or not
        self.settings_file = "data\\settings.txt" # settings file

        # key sfx
        self.key_fx = {
            pygame.K_a: pygame.mixer.Sound("audio\\typing\\a.wav"), # a sfx
            pygame.K_b: pygame.mixer.Sound("audio\\typing\\b.wav"), # b sfx
            pygame.K_c: pygame.mixer.Sound("audio\\typing\\c.wav"), # c sfx
            pygame.K_d: pygame.mixer.Sound("audio\\typing\\d.wav"), # d sfx
            pygame.K_e: pygame.mixer.Sound("audio\\typing\\e.wav"), # e sfx
            pygame.K_f: pygame.mixer.Sound("audio\\typing\\f.wav"), # f sfx
            pygame.K_g: pygame.mixer.Sound("audio\\typing\\g.wav"), # g sfx
            pygame.K_h: pygame.mixer.Sound("audio\\typing\\h.wav"), # h sfx
            pygame.K_i: pygame.mixer.Sound("audio\\typing\\i.wav"), # i sfx
            pygame.K_j: pygame.mixer.Sound("audio\\typing\\j.wav"), # j sfx
            pygame.K_k: pygame.mixer.Sound("audio\\typing\\k.wav"), # k sfx
            pygame.K_l: pygame.mixer.Sound("audio\\typing\\l.wav"), # l sfx
            pygame.K_m: pygame.mixer.Sound("audio\\typing\\m.wav"), # m sfx
            pygame.K_n: pygame.mixer.Sound("audio\\typing\\n.wav"), # n sfx
            pygame.K_o: pygame.mixer.Sound("audio\\typing\\o.wav"), # o sfx
            pygame.K_p: pygame.mixer.Sound("audio\\typing\\p.wav"), # p sfx
            pygame.K_q: pygame.mixer.Sound("audio\\typing\\q.wav"), # q sfx
            pygame.K_r: pygame.mixer.Sound("audio\\typing\\r.wav"), # r sfx
            pygame.K_s: pygame.mixer.Sound("audio\\typing\\s.wav"), # s sfx
            pygame.K_t: pygame.mixer.Sound("audio\\typing\\t.wav"), # t sfx
            pygame.K_u: pygame.mixer.Sound("audio\\typing\\u.wav"), # u sfx
            pygame.K_v: pygame.mixer.Sound("audio\\typing\\v.wav"), # v sfx
            pygame.K_w: pygame.mixer.Sound("audio\\typing\\w.wav"), # w sfx
            pygame.K_x: pygame.mixer.Sound("audio\\typing\\x.wav"), # x sfx
            pygame.K_y: pygame.mixer.Sound("audio\\typing\\y.wav"), # y sfx
            pygame.K_z: pygame.mixer.Sound("audio\\typing\\z.wav"), # z sfx
            pygame.K_SPACE: pygame.mixer.Sound("audio\\typing\\space.wav"), # space sfx
            pygame.K_BACKSPACE: pygame.mixer.Sound("audio\\typing\\backspace.wav") # backspace sfx
        }
    
    # load settings from settings.txt
    def load_settings(self):
        settings = {} # settings dictionary
        with open(self.settings_file, "r") as file: # open scores.txt
            for line in file: # go through each line in file
                music, sound_fx = line.strip().split() # split each setting value into its
                # own variable
                settings = { # create list of dictionaries
                    "music": str(music),
                    "sound_fx": str(sound_fx),
                }

        file.close() # close scores.txt
        return settings # return settings
    
    # update user's settings
    def update_settings(self, music, sound_fx):
        if music == "On":
            music = 0
        else:
            music = 1

        if sound_fx == "On":
            sound_fx = 0
        else:
            sound_fx = 1

        with open(self.settings_file, "w") as file: # open file, create new one if not exisitng
            file.write(f"{music} {sound_fx}") # update settings
            file.close() # close settings.txt
    
    # get user's settings
    def get_settings(self, setting):
        settings = self.load_settings() # load settings

        return settings[setting]
    
    def play_music(self, path, volume=0.2, loop=-1): # plays bgm
        if self.last_music == path:
            return # if last music equals to current music then don't restart music

        pygame.mixer.music.stop() # stops bgm
        pygame.mixer.music.load(path) # loads music
        pygame.mixer.music.set_volume(volume) # set volume
        pygame.mixer.music.play(loop, fade_ms=2000) # play bgm and loop it

        self.last_music = path

    def pause_music(self):
        if not self.music_paused:
            pygame.mixer.music.pause()
            self.music_paused = True

    def resume_music(self):
        if self.music_paused:
            pygame.mixer.music.unpause()
            self.music_paused = False