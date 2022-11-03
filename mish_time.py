import pygame
import datetime


# draw rect but with transparency
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


# Credit to [MISH]
'''
The Time Class for the PipBoy
    Instead of displaying AP, the Pip boy will display the current time in the corner
    Since we dont have any interesting way of using AP in our Raspberry Po
    NOTES:
'''


class Time:
    def __init__(self):
        self.color = (51, 109, 48, 200)
        self.x = 380
        self.y = 300
        self.width = 95
        self.height = 35
        self.hour = "00"
        self.minute = "00"
        self.meridiem = "AM"
        self.text = f'{self.hour} : {self.minute} {self.meridiem}'

    def draw(self, surf):
        rect = (self.x, self.y), (self.width, self.height)
        draw_rect_alpha(surf, self.color, rect)

    def update_time(self, surf):
        self.draw(surf)
        update = False

        # Define the time
        time = datetime.datetime.now()
        self.hour = (time.strftime("%H"))
        self.minute = (time.strftime("%M"))
        self.meridiem = (time.strftime("%p"))
        self.text = f'     {self.hour} : {self.minute} {self.meridiem}'

        # Print Health Amount
        TEXT_COL = (100, 252, 127, 255)

        font = pygame.font.SysFont('arial', 16)
        text = font.render(self.text, False, TEXT_COL)
        surf.blit(text, (self.x + 5, self.y))

        update = True

        return update
