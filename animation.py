import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super(Animation, self).__init__()

        self.images = []
        ##self.images.append(pygame.image.load("wave-C.png"))
        self.images.append(pygame.image.load("wave-A.png"))
        self.images.append(pygame.image.load("wave-B.png"))
        self.images.append(pygame.image.load("wave-C.png"))
        self.images.append(pygame.image.load("wave-B.png"))
        #self.images.append(pygame.image.load("wave-A.png"))
        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(235, 55, 235, 55)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    def dance(self, surf, flag):
        my_sprite = self
        my_group = pygame.sprite.Group(my_sprite)
        clock = pygame.time.Clock()

        while flag:
            my_group.update()
            my_group.draw(surf)
            pygame.display.update()
            clock.tick(7)
