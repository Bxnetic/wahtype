import pygame

def centre(surface, width, height, widthPadding, heightPadding): # function that centres surface
            rect = surface.get_rect()
            return (
                int((width / 2)) - int(rect.width / 2) + widthPadding,
             int((height / 2)) - int(rect.height / 2) + heightPadding
            ) # centre surface

def draw_text(screen, text, width, height, x, y, color, size):
    font = pygame.font.Font("fonts\\RobotoMono-Regular.ttf", size) # font
    current_text = font.render(text, True, color) # render the text
    current_text_rect = current_text.get_rect(
        topleft=centre(current_text, width, height, x, y)) # display text in the centre
    screen.blit(current_text, current_text_rect) # display the text on screen