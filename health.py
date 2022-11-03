import pygame
import level
import time

# draw rect but with transparency
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


# Credit to [MISH]
'''
The Health Class for the PipBoy
    I think the original idea was that the Health on the PipBoy would lessen 
    as the day goes on
    NOTES:
        Plan is to have health tied to level as well as time.
'''


class Health:
    def __init__(self):
        self.color = (51, 109, 48, 200)
        self.x = 110
        self.y = 300
        self.width = 260
        self.height = 30
        self.level = 1
        self.text = f'Level {self.level}'