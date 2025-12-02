import pygame

def centre(surface, width, height, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
             int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface

def draw_text_centre(screen, text, width, height, x, y, color, size):
    font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font
    current_text = font.render(text, True, color) # render the text
    current_text_rect = current_text.get_rect(
        topleft=centre(current_text, width, height, x, y)) # display text in the centre
    screen.blit(current_text, current_text_rect) # display the text on screen

def draw_text(screen, text, x, y, color, size):
    font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font
    current_text = font.render(text, True, color) # render the text
    current_text_rect = current_text.get_rect(
        topleft=(x, y))# display text in the centre
    screen.blit(current_text, current_text_rect) # display the text on screen

def wrap_text(text, size, max_width):
        words = text.split(" ") # split the words in the sentence
        font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font
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