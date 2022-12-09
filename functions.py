import pygame

class Function:
    """
    A class with functions used for making modifications to the display,
    including text and printing rectangles.
    """
    @staticmethod
    def draw_rect_alpha(surf, color, rect):
        """
        Draws a rectangle with modifiable alpha level on the surface.
        :param surf: Surface
        :param color: tuple
        :param rect: tuple[tuple(int x_coord, int y_coord), tuple(int width, height)]
        """
        shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape, color, shape.get_rect())
        surf.blit(shape, rect)

    @staticmethod
    def display_text(surf, x_coord, y_coord, color, text=''):
        """
        Displays text, size 20, onto the surface at (x_coord, y_coord) using the color given.
        :param surf: Surface
        :param x_coord: int
        :param y_coord: int
        :param color: tuple
        :param text: String
        """
        TEXT_COL = color

        font = pygame.font.SysFont('arial', 20)
        text = font.render(text, False, TEXT_COL)
        surf.blit(text, (x_coord, y_coord))

    @staticmethod
    def display_text_small(surf, x_coord, y_coord, color, text=''):
        """
        Displays text, size 15, onto the surface at (x_coord, y_coord) using the color given.
        :param surf: Surface
        :param x_coord: int
        :param y_coord: int
        :param color: tuple
        :param text: String
        """
        TEXT_COL = color

        font = pygame.font.SysFont('arial', 15)
        text = font.render(text, False, TEXT_COL)
        surf.blit(text, (x_coord, y_coord))
