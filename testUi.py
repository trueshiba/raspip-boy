import pygame
import pygame_gui
import time

pygame.init()

# create game window
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

pygame.display.set_caption('Pip Boy')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

image = pygame.image.load('maps.jpg')

# UI Manager
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    # self.screen.fill((self.white))
    window_surface.blit(image, (10, 10))
    pygame.display.flip()

    time.sleep(.2)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()