import pygame
import time

# button class
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


# Credit to [MISH]
'''
The Button Class for the PipBoy
    Simple Button class that allows for menu like button screen
    Each button will return a true or false bool if the user presses it
    NOTES:
        None so Far
'''


class Button:
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
            pygame.draw.rect(surf, outline, self.x - 2, self.y - 2, self.width + 4, self.height + 4)
        # rect = pygame.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height), 0)
        rect = (self.x, self.y), (self.width, self.height)
        draw_rect_alpha(surf, self.color, rect)
        if self.text != '':
            TEXT_COL = (100, 252, 127, 255)

            font = pygame.font.SysFont('arial', 20)
            text = font.render(self.text, False, TEXT_COL)
            surf.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_pressed(self, surf):

        self.draw(surf)

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                action = True

        return action

    def is_pressed_promise(self, surf):

        self.draw(surf)

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                if pygame.mouse.get_pressed()[0]:
                    time.sleep(.2)
                    action = True

        # send result
        return action

