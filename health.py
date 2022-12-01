import pygame
import level
import datetime
import os

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
        Plan is to have health tied to time...some how
'''



class Health:
    def __init__(self):
        self.color = (51, 109, 48, 200)
        self.x = 10
        self.y = 300
        self.width = 95
        self.height = 35
        self.health_max = 115
        self.health_current = 115
        self.text = f'HP {self.health_max} / {self.health_current}'
        self.time_increase =  0 #so program doesn't constantly open health.txt
        #CONSTANT
        self.DIVIDER = 12.5217

    def draw(self, surf):
        rect = (self.x, self.y), (self.width, self.height)
        draw_rect_alpha(surf, self.color, rect)

    def update_health(self, surf):
        self.draw(surf)
        update = False

        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        total_day = (hour * 60) + minute

        # Set health based on current time
        # Check with group about how they want the time to be split up :)
        if total_day > (self.time_increase + 10):
            if total_day % 30 >= 1:
                self.health_current = self.health_max - int((total_day // self.DIVIDER))
                self.text = f'HP {self.health_current} / {self.health_max}'
                self.time_increase = total_day

                with open("healths.txt", "w", encoding='utf-8') as f:
                    f.write(f'Current Health{self.health_current:>21}\n')
                    f.write(f"Maximum Health{self.health_max:>17}\n")
                f.close()
                print("file closed")

        # Print Health Amount
        TEXT_COL = (100, 252, 127, 255)

        font = pygame.font.SysFont('arial', 16)
        text = font.render(self.text, False, TEXT_COL)
        surf.blit(text, (self.x + 5, self.y))

        #Update Data in Health File
        #assert os.path.isfile("health.txt")

        update = True

        return update
