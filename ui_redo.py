import pygame
import pygame_gui
import button
import health, inventory, level, mish_time, data, radio, map

# Credit to [MISH]
'''
The UI for the PipBoy
    Basically the main for the PipBoy, will call most classes and functions in here
    Handles mainly the display and inputs from the user.
    NOTES:
        Need to Implement STAT, INV, DATA, MAP, RADIO Classes
        Currently set to running on Desktop, be-sure to check fonts 
        before transferring to Raspberry Pi
        - Reconfigure Text to display correctly on the data 
          screen for the [Pip Boy]
        - Reconfigure the deco lines for the [Pip Boy]
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
exit_button = button.Button((0, 0, 0, 0), 460, 10, 10, 30, "x")

# create level
level_bar = level.Level()

#create health
health_bar = health.Health()

#create time
time_bar = mish_time.Time()

# define background image
overlay = pygame.image.load("overlay.png")
overlay_BIG = pygame.transform.rotozoom(overlay, 0, 2)

#Screen Triggers
stat_flag = False
inv_flag = False
data_flag = False
map_flag = False
radio_flag = False

#create Menus
data_menu = data.Data()
radio_menu = radio.Radio()
inv_menu = inventory.Inventory()
map_menu = map.Map()

#Shape Function [Testing Purpose only] - will later be removed once classes are made for the different screens
def draw_shape(color):
    pygame.draw.rect(window_surface, color, (100, 100, 20, 20))

#Menu Decro function - draws the little lines on the menu
def menu_deco(start, end):
    # First half
    pygame.draw.line(window_surface, BORDER, (start, 23), (start + 5, 23), width=1)
    pygame.draw.line(window_surface, BORDER, (start, 23), (start, 38), width=1)
    pygame.draw.line(window_surface, BORDER, (10, 38), (start, 38), width=1)

    # Second half
    pygame.draw.line(window_surface, BORDER, (end - 5, 23), (end, 23), width=1)
    pygame.draw.line(window_surface, BORDER, (end, 23), (end, 38), width=1)
    pygame.draw.line(window_surface, BORDER, (end, 38), (470, 38), width=1)


# game time!!
running = True

while running:

    window_surface.blit(overlay_BIG, (0, 0))

    # check menu state
    if menu_state == "main":
        # draw pause screen buttons
        if stat_button.is_pressed(window_surface):
            stat_flag = True
            inv_flag = False
            data_flag = False
            map_flag = False
            radio_flag = False

        if inv_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = True
            data_flag = False
            map_flag = False
            radio_flag = False

        if data_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = True
            map_flag = False
            radio_flag = False

        if map_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = True
            radio_flag = False

        if radio_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = False
            radio_flag = True

        if exit_button.is_pressed(window_surface):
            running = False

        level_bar.update_level(window_surface)
        health_bar.update_health(window_surface)
        time_bar.update_time(window_surface)

        # [For Testing Purposes Only]
        # if level_bar.is_pressed(window_surface):
        #     print("EXP")

    #Execute screens
    if stat_flag:
        draw_shape(RED)
        menu_deco(30, 90)
        map_menu.draw_map(window_surface, False)

    if inv_flag:
        draw_shape(ORANGE)
        menu_deco(125, 173)
        inv_menu.menu(window_surface)
        map_menu.draw_map(window_surface, False)
    if data_flag:
        draw_shape((15, 190, 20))
        menu_deco(210, 268)
        data_menu.menu(window_surface)
        map_menu.draw_map(window_surface, False)
    if radio_flag:
        draw_shape((0, 100, 150))
        menu_deco(380, 455)
        radio_menu.menu(window_surface)
        map_menu.draw_map(window_surface, False)
    if map_flag:
        draw_shape((255, 255, 255))
        menu_deco(300, 357)
        map_menu.draw_map(window_surface, True)

    # print out the buttons!!
    # we can change this to detect like- a button push or the I/O Button input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
