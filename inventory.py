import pygame
import level
import random
import button
import datetime

import virtual_pet
import virtual_pet as pet


# let me know if I fix anything c:
# Loop to see how much space is available
# Credit to [Kam]
def spaceAvailable():
    itemSpace = 4
    # for i in range(level.getLevel()):
    if level.getLevel() > 4 & level.getLevel() < 8:
        itemSpace += 1
    elif level.getLevel() >= 8:
        itemSpace = 7
    return itemSpace


# inventory function to print out the inventory
def inventory():
    listOfItems = []
    # opens file with items
    randomItems = open("InventoryItems.txt", "r")

    # adds each item to the list
    for x in randomItems:
        listOfItems.append(x.strip('\n'))

    # shuffles the list
    random.shuffle(listOfItems)
    return listOfItems


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
The Inventory Class for the PipBoy
    Since there is currently no Pip Boy for the items to interact with
    there is more testing to be done, but for now lets just try to 
    incorporate Cam's stuff into a Inventory class :) 
    
    Inventory Class displays items from the food, fun and groom files, 
    it will pick random amount of items from each category and display the max 
    based on the users level.
    
    If you hover over the item it will display the item description
    If you click the item, it will use the item.
    NOTES:
        Incorporate Virtual Pet stuff
        Test clicking on raspberry Pi
        
'''


def display_image(surf, filename='', running=''):
    img = pygame.image.load(f'PNGs/{filename}')
    image = pygame.transform.scale(img, (100, 110))

    if running:
        # self.screen.fill((self.white))
        surf.blit(image, (340, 60))
        pygame.display.flip()


class Inventory:
    def __init__(self, virtual_Pet):
        self.itemList = inventory()
        self.color = (51, 140, 48)
        self.main_color = (88, 243, 100, 180)
        self.x_r = 10
        self.y = 55
        self.x_l = 300
        self.menu_width = 280
        self.menu_height = 30
        self.height = 45
        self.item_button = button.Button((0, 0, 0, 0), self.x_r, self.y, self.menu_width, self.menu_height, "")
        self.item_button_2 = button.Button((0, 0, 0, 0), self.x_r, self.y + 30, self.menu_width, self.menu_height, "")
        self.item_button_3 = button.Button((0, 0, 0, 0), self.x_r, self.y + 60, self.menu_width, self.menu_height, "")
        self.item_button_4 = button.Button((0, 0, 0, 0), self.x_r, self.y + 90, self.menu_width, self.menu_height, "")
        self.item_button_5 = button.Button((0, 0, 0, 0), self.x_r, self.y + 120, self.menu_width, self.menu_height, "")
        self.vp = virtual_Pet

        # Cam Variables
        self.space_available = spaceAvailable()
        print(self.space_available)

        # setup initial itemlist
        for i in range(0, len(self.itemList) - self.space_available):
            self.itemList.pop()

    def draw(self, surf):
        rect = (self.x_r, self.y), (200, 235)
        draw_rect_alpha(surf, self.color, rect)

        rect = (self.x_l, self.y), (235, 235)
        draw_rect_alpha(surf, self.color, rect)

    def read_file(self, surf, filename='', item=''):
        f = open(filename, "r")

        x = 170
        y = 175
        for line in f:
            lines = line.split(',')
            if lines[0] == item:
                speech = lines[1].split('/')
                for sections in speech:
                    rect = (self.x_l, y), (x, 30)
                    draw_rect_alpha(surf, (51, 140, 48, 100), rect)
                    # =text = line
                    display_text(surf, self.x_l + 5, y, (100, 252, 127), sections)
                    y += 30
                display_image(surf, lines[2].strip('\n'), True)
        f.close()

    def use_item(self, text):
        for item in self.itemList:
            # Use below if statements to call status function of the virtual pet
            # whenever it gets made and stuff
            if item[-1] == 'f':
                self.vp.item_f_increase()
            if item[-1] == 'h':
                self.vp.item_h_increase()
            if item[-1] == 't':
                self.vp.item_t_increase()
            if item[0:len(item) - 2] == text:
                self.itemList.remove(item)

    def tab(self, surf, y_increase, in_button, filename='', text=''):
        # Steps
        if in_button.is_pressed(surf):
            rect = (self.x_r, self.y + y_increase), (self.menu_width, self.menu_height)
            draw_rect_alpha(surf, self.main_color, rect)

            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (52, 68, 52), text)

            self.read_file(surf, filename, text)
            if in_button.is_pressed_promise(surf):
                self.use_item(text)
            # rect = (self.x_l, self.y), (235, 235)
            # draw_rect_alpha(surf, self.color, rect)
        else:
            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (100, 252, 127), text)

    def update_inv(self):
        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        seconds = int(time.strftime("%S"))
        total_day = (hour * 60) + minute + (seconds / 60)

        # Set health based on current time
        # Check with group about how they want the time to be split up :)
        if total_day % 30 == 0:
            self.itemList = inventory()
            for i in range(0, len(self.itemList) - self.space_available):
                self.itemList.pop()

    def menu(self, surf):
        sep = 0
        index = 0

        button_array = [self.item_button, self.item_button_2, self.item_button_3, self.item_button_4,
                        self.item_button_5]

        for item in self.itemList:
            if item[-1] == 'f':
                self.tab(surf, sep, button_array[index], "food.txt", item[0:len(item) - 2])
                sep += 30
                index += 1

            if item[-1] == 'h':
                self.tab(surf, sep, button_array[index], "grooming.txt", item[0:len(item) - 2])
                sep += 30
                index += 1

            if item[-1] == 't':
                self.tab(surf, sep, button_array[index], "fun.txt", item[0:len(item) - 2])
                sep += 30
                index += 1

        self.update_inv()