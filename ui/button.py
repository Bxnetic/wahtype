import pygame

class Button:
    def __init__(self, x, y, image, hover_image, scale):
        width = image.get_width() # current width of image
        height = image.get_height() # current height of image

        self.image_hover = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale))) # change size of hover img
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # change size normal img
    
        self.rect = self.image.get_rect() # get rectangular area of the image
        self.rect.topleft = (x, y) # get the coords of the top left of the rect around image
        self.clicked = False # value that is held whether the user has clicked the button or not

    def draw(self, screen):
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if the mouse is over button and has been clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                print("Clicked")
            screen.blit(self.image_hover, (self.rect.x, self.rect.y)) # display button
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y)) # display button
        

