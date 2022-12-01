import pygame
from pygameZoom import PygameZoom
img = pygame.image.load('maps.jpg')

class Map:
    def __init__(self):

        self.color = (51, 109, 48, 200)
        self.x = 15
        self.y = 50
        self.width = 450
        self.height = 240
        self.white = (255, 64, 64)
        self.image = pygame.transform.scale(img, (self.width, self.height))

        #self.screen = pygame.display.set_mode((self.width, self.height))
        #screen.fill((self.white))
        running = 1

    def draw_map(self, surf, running):
        if running:
            #self.screen.fill((self.white))
            surf.blit(self.image, (self.x, self.y))
            pygame.display.flip()

    def menu(self, surf):
        self.draw_map(surf, True)


