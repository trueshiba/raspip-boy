import pygame
import button


# draw rect but with transparency
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


def display_text(surf, x_coord, y_coord, color, text=''):
    """
    :param color: tuple
    :type x_coord: int
    :type y_coord: int
    :type text: String
    :type surf: Surface
    """
    TEXT_COL = color

    font = pygame.font.SysFont('arial', 20)
    text = font.render(text, False, TEXT_COL)
    surf.blit(text, (x_coord, y_coord))


# Credit to [MISH]
'''
The Data Class for the PipBoy
    This will display the data screen and all its wonderful functionalities
    It wil display the users 
    Health Info
    Level Info
    Steps Info
    And some other information stuff for fun
    NOTES:
        Need to Update Green Color for Level Fill
        Config to Accelerometer 
'''


class Data:
    def __init__(self):
        self.color = (51, 140, 48)
        self.main_color = (88, 243, 100, 180)
        self.x_r = 10
        self.y = 55
        self.x_l = 230
        self.menu_width = 200
        self.height = 45
        self.health_button = button.Button((0, 0, 0, 0), self.x_r, self.y, self.menu_width, 30, "")
        self.level_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 30, self.menu_width, 30, "")
        self.steps_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 60, self.menu_width, 30, "")
        self.random_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 90, self.menu_width, 30, "")
        self.random_button_2 = button.Button((0, 0, 0, 0), self.x_r, self.y + 120, self.menu_width, 30, "")
        # CONSTANT
        self.DIVIDER = 12.5217

    def draw(self, surf):
        rect = (self.x_r, self.y), (200, 235)
        draw_rect_alpha(surf, self.color, rect)

        rect = (self.x_l, self.y), (235, 235)
        draw_rect_alpha(surf, self.color, rect)

    def read_file(self, surf, filename=''):
        f = open(filename, "r")

        x = 235
        y = 55
        for line in f:
            rect = (self.x_l, y), (x, 30)
            draw_rect_alpha(surf, (51, 140, 48, 100), rect)
            #=text = line
            display_text(surf, self.x_l + 5, y, (100, 252, 127), line.strip('\n'))
            y += 33
        f.close()

    def tab(self, surf, y_increase, in_button, filename='', text=''):
        # Steps
        if in_button.is_pressed(surf):
            rect = (self.x_r, self.y + y_increase), (200, 30)
            draw_rect_alpha(surf, self.main_color, rect)

            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (52, 68, 52), text)

            self.read_file(surf, filename)
            # rect = (self.x_l, self.y), (235, 235)
            # draw_rect_alpha(surf, self.color, rect)
        else:
            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (100, 252, 127), text)


    def menu(self, surf):
        self.tab(surf, 0, self.health_button, "health.txt", "Health")
        self.tab(surf, 30, self.level_button, "level.txt", "Levels")
        #self.tab(surf, 60, self.steps_button, "Steps")
        self.tab(surf, 90, self.random_button, "random.txt", "General")
        # create buttons
        # self.health_button.draw(surf)
        # self.level_button.draw(surf)
        # self.steps_button.draw(surf)
        # self.random_button.draw(surf)
        # self.random_button_2.draw(surf)

        # while running:
        #     if self.health_button.is_pressed(surf):
        #         rect = (self.x_r, self.y), (200, 30)
        #         draw_rect_alpha(surf, self.color, rect)
        #
        #         #display_text(surf, self.x_r + 5, self.y, 'Health')
        #
        #         rect = (self.x_l, self.y), (235, 235)
        #         draw_rect_alpha(surf, self.color, rect)
        #     else:
        #         display_text(surf, self.x_r + 5, self.y, 'Health')

        # display_text(surf, self.x_r + 5, self.y + 30, 'Level')
        # display_text(surf, self.x_r + 5, self.y + 60, 'Steps')
        # display_text(surf, self.x_r + 5, self.y + 90, "Random")
        # display_text(surf, self.x_r + 5, self.y + 120, 'Random 2')
