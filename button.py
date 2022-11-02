import pygame

# button class
class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

    def draw(self, surf, outline=None):
        if outline:
            pygame.draw.rect(surf, outline, self.x-2, self.y-2, self.width+4, self.height+4)

        pygame.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            surf.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_pressed(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                action = True

        #send result
        return action
