import pygame
import pygame_gui
import button
import level

# Credit to [MISH]
'''
The UI for the PipBoy
    Basically the main for the PipBoy, will call most classes and functions in here
    Handles mainly the display and inputs from the user.
    NOTES:
        Need to Implement STAT, INV, DATA, MAP, RADIO Classes
        Currently set to running on Desktop, be-sure to check fonts 
        before transferring to Raspberry Pi
        Have it so that User Data is written onto a file, this includes:
        Steps
        Levels
        Max Health
        (maybe other stuff)
        Then have this stuff visible on the Data Tab  
'''

pygame.init()

# create game window
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

pygame.display.set_caption('Pip Boy')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# UI Manager
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# game variables
game_paused = True
menu_state = "main"

# define fonts - switch between fonts depending on device
font_pc = pygame.font.SysFont('arial', 20)
# font_py = pygame_menu.font.SysFont('notosansmono', 20)

# define colors - not all needed but are available for testing
TEXT_COL = (100, 252, 127, 255)
GREEN = (5, 69, 8)
BORDER = (88, 243, 100)
ORANGE = (255, 150, 0)
RED = (255, 0, 0)

# create buttons
stat_button = button.Button((0, 0, 0, 0), 15, 10, 90, 30, "STAT")
inv_button = button.Button((0, 0, 0, 0), 105, 10, 90, 30, "INV")
data_button = button.Button((0, 0, 0, 0), 195, 10, 90, 30, "DATA")
map_button = button.Button((0, 0, 0, 0), 285, 10, 90, 30, "MAP")
radio_button = button.Button((0, 0, 0, 0), 375, 10, 90, 30, "RADIO")

# create level
level_bar = level.Level()

# define background image
overlay = pygame.image.load("overlay.png")
overlay_BIG = pygame.transform.rotozoom(overlay, 0, 2)

#Screen Triggers
stat_flag = False
inv_flag = False
data_flag = False
map_flag = False
radio_flag = False


# game time!!
running = True


# ERASE FUNCTION - Note Rect objects store and manipulate rectangular areas
def erase(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)

#Shape Functions - will later be removed once classes are made for the different screens
def draw_shape():
    pygame.draw.rect(window_surface, RED, (100, 100, 20, 20))

def draw_diff_shape():
    pygame.draw.rect(window_surface, ORANGE, (200, 200, 20, 20))


while running:

    window_surface.blit(overlay_BIG, (0, 0))

    # check menu state
    if menu_state == "main":
        # draw pause screen buttons
        if stat_button.is_pressed(window_surface):
            print("STAT")
            stat_flag = True
            inv_flag = False
            data_flag = False
            map_flag = False
            radio_flag = False

        if inv_button.is_pressed(window_surface):
            print("INV")
            stat_flag = False
            inv_flag = True
            data_flag = False
            map_flag = False
            radio_flag = False

        if data_button.is_pressed(window_surface):
            print("DATA")
            stat_flag = False
            inv_flag = False
            data_flag = True
            map_flag = False
            radio_flag = False

        if map_button.is_pressed(window_surface):
            print("MAP")
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = True
            radio_flag = False

        if radio_button.is_pressed(window_surface):
            print("RADIO")
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = False
            radio_flag = True

        level_bar.update_level(window_surface)

        # [For Testing Purposes Only]
        # if level_bar.is_pressed(window_surface):
        #     print("EXP")

    #Execute screens
    if stat_flag:
        draw_shape()

    if inv_flag:
        draw_diff_shape()

    if data_flag:
        draw_shape()

    if map_flag:
        draw_diff_shape()

    if radio_flag:
        draw_shape()

    # print out the buttons!!
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
