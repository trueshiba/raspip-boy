import pygame
import pygame_gui
import button
import health, inventory, level, mish_time, data, radio, map, virtual_pet

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

# create health
health_bar = health.Health()

# create time
time_bar = mish_time.Time()

# define background image
overlay = pygame.image.load("overlay.png")
overlay_BIG = pygame.transform.rotozoom(overlay, 0, 2)

# Screen Triggers
stat_flag = False
inv_flag = False
data_flag = False
map_flag = False
radio_flag = False

# create Menus
data_menu = data.Data()
radio_menu = radio.Radio()
pet_menu = virtual_pet.Virtual_Pet()
inv_menu = inventory.Inventory(pet_menu)
map_menu = map.Map()

# frames
image_sprite = [pygame.image.load('pip-animation/pip-0.png'),
                pygame.image.load('pip-animation/pip-1.png'),
                pygame.image.load('pip-animation/pip-2.png'),
                pygame.image.load('pip-animation/pip-3.png'),
                pygame.image.load('pip-animation/pip-4.png'),
                pygame.image.load('pip-animation/pip-5.png'),
                pygame.image.load('pip-animation/pip-6.png'),
                pygame.image.load('pip-animation/pip-7.png'),
                pygame.image.load('pip-animation/pip-8.png'),
                pygame.image.load('pip-animation/pip-9.png'),
                pygame.image.load('pip-animation/pip-10.png'),
                pygame.image.load('pip-animation/pip-11.png'),
                pygame.image.load('pip-animation/pip-12.png'),
                pygame.image.load('pip-animation/pip-13.png'),
                pygame.image.load('pip-animation/pip-14.png'),
                pygame.image.load('pip-animation/pip-15.png'),
                pygame.image.load('pip-animation/pip-16.png'),
                pygame.image.load('pip-animation/pip-17.png'),
                pygame.image.load('pip-animation/pip-18.png'),
                pygame.image.load('pip-animation/pip-19.png'),
                pygame.image.load('pip-animation/pip-20.png')
                ]

#Draw Rectangle Background
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)

# Menu Decor function - draws the little lines on the menu
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
clock = pygame.time.Clock()
value = 0
walk_flag = False

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
            walk_flag = False

        if data_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = True
            map_flag = False
            radio_flag = False
            walk_flag = False

        if map_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = True
            radio_flag = False
            walk_flag = False

        if radio_button.is_pressed(window_surface):
            stat_flag = False
            inv_flag = False
            data_flag = False
            map_flag = False
            radio_flag = True
            walk_flag = False

        if exit_button.is_pressed_promise(window_surface):
            running = False

        level_bar.update_level(window_surface, walk_flag)
        health_bar.update_health(window_surface)
        time_bar.update_time(window_surface)
        pet_menu.update_radiation()
        pet_menu.update_hunger()
        pet_menu.update_fun()

        # [For Testing Purposes Only]
        # if level_bar.is_pressed(window_surface):
        #     print("EXP")

    # Execute screens
    if stat_flag:
        menu_deco(30, 90)
        pet_menu.menu(window_surface)

        clock.tick(10)

        if value >= len(image_sprite):
            value = 0

        image = image_sprite[value]

        window_surface.blit(image, (180, 50))

        value += 1

        # Walk Button
        walk_button = button.Button((0, 0, 0, 0), 10, 250, 90, 30, "Walk")
        rect = (10, 250), (90, 30)
        draw_rect_alpha(window_surface, (51, 109, 48, 200), rect)
        if walk_button.is_pressed_promise(window_surface):
            walk_flag = True

    if inv_flag:
        menu_deco(125, 173)
        inv_menu.menu(window_surface)
    if data_flag:
        menu_deco(210, 268)
        data_menu.menu(window_surface)
    if radio_flag:
        menu_deco(380, 455)
        radio_menu.menu(window_surface)
    if map_flag:
        menu_deco(300, 357)
        map_menu.menu(window_surface)

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
