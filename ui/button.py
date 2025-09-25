import pygame

class Button:
    def __init__(self, x, y, image, hover_image, scale, text_input, text_size, text_color, text_hover_color):
        width = image.get_width() # current width of image
        height = image.get_height() # current height of image
        # image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # change size normal img
        self.image_hover = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale))) # change size of hover img
        self.rect = self.image.get_rect() # get rectangular area of the image
        self.rect.topleft = (x, y) # get the coords of the top left of the rect around image
        # text
        self.font = pygame.font.Font("fonts\\RobotoMono-Medium.ttf", text_size) # font
        self.text_color = text_color
        self.text_hover_color = text_hover_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.clicked = False # value that is held whether the user has clicked the button or not

    def setText(self, new_text): # update the text on the button
        self.text_input = new_text # set the current text to the new text
        self.text = self.font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # update the text to be in the center of the button
        self.text_rect = self.text.get_rect(center=self.rect.center)

        # check if the mouse is over button and has been clicked
        if self.rect.collidepoint(pos): # if the mouse hovering the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # checks if left click has been clicked
                # but self.clicked is currently false
                self.clicked = True # user has clicked the button
                action = True # perform action
   
            if pygame.mouse.get_pressed()[0] == 0: # if left click hasn't been clicked
                self.clicked = False # set back to false

            screen.blit(self.image_hover, (self.rect.x, self.rect.y)) # display hover button
            self.text = self.font.render(self.text_input, True, self.text_hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.text_color)
            screen.blit(self.image, (self.rect.x, self.rect.y)) # display button
            
        screen.blit(self.text, self.text_rect) # display text
        return action
        

