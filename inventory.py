import pygame
import level
import random
import button
import datetime


#let me know if I fix anything c:
#Loop to see how much space is available
# Credit to [Kam]
def spaceAvailable():
    itemSpace = 4
    #for i in range(level.getLevel()):
    if level.getLevel() > 4 & level.getLevel() < 8 :
        itemSpace += 1
    elif level.getLevel() >= 8:
        itemSpace = 7
    return itemSpace

#inventory function to print out the inventory
def inventory():
    listOfItems = []
    #opens file with items
    randomItems = open("randomItems.txt", "r")

    #adds each item to the list
    for x in randomItems:
        listOfItems.append(x.strip('\n'))
       
    #shuffles the list
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
class Inventory:
    def __init__(self):
        self.itemList = inventory()
        self.color = (51, 140, 48)
        self.main_color = (88, 243, 100, 180)
        self.x_r = 10
        self.y = 55
        self.x_l = 230
        self.menu_width = 200
        self.height = 45
        self.item_button = button.Button((0, 0, 0, 0), self.x_r, self.y, self.menu_width, 30, "")
        self.item_button_2 = button.Button((0, 0, 0, 0), self.x_r, self.y + 30, self.menu_width, 30, "")
        self.item_button_3 = button.Button((0, 0, 0, 0), self.x_r, self.y + 60, self.menu_width, 30, "")
        self.item_button_4 = button.Button((0, 0, 0, 0), self.x_r, self.y + 90, self.menu_width, 30, "")
        self.item_button_5 = button.Button((0, 0, 0, 0), self.x_r, self.y + 120, self.menu_width, 30, "")

        #Cam Variables
        self.space_available = spaceAvailable()
        print(self.space_available)

        #setup initial itemlist
        for i in range(0, len(self.itemList) - self.space_available):
            self.itemList.pop()

    def draw(self, surf):
        rect = (self.x_r, self.y), (200, 235)
        draw_rect_alpha(surf, self.color, rect)

        rect = (self.x_l, self.y), (235, 235)
        draw_rect_alpha(surf, self.color, rect)

    def read_file(self, surf, filename='', item=''):
        f = open(filename, "r")

        x = 235
        y = 55
        for line in f:
            lines = line.split(',')
            if lines[0] == item:
                rect = (self.x_l, y), (x, 30)
                draw_rect_alpha(surf, (51, 140, 48, 100), rect)
                # =text = line
                display_text(surf, self.x_l + 5, y, (100, 252, 127), lines[1].strip('\n'))
                y += 33
        f.close()

    def use_item(self, text):
        for item in self.itemList:
            # Use below if statements to call status function of the virtual pet
            # whenever it gets made and stuff
            #if item[-1] == 'f':
            #if item[-1] == 'g':
            #if item[-1] == 't':

            if item[0:len(item) - 2] == text:
                self.itemList.remove(item)

    def tab(self, surf, y_increase, in_button, filename='', text=''):
        # Steps
        if in_button.is_pressed(surf):
            rect = (self.x_r, self.y + y_increase), (200, 30)
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
        total_day = (hour * 60) + minute

        # Set health based on current time
        # Check with group about how they want the time to be split up :)
        if total_day % 30 == 0:
            self.itemList = inventory()
            for i in range(0, len(self.itemList) - self.space_available):
                self.itemList.pop()

    def menu(self, surf):
        sep = 0
        index = 0

        button_array = [self.item_button, self.item_button_2, self.item_button_3, self.item_button_4, self.item_button_5]

        for item in self.itemList:
                if item[-1] == 'f':
                    self.tab(surf, sep, button_array[index], "food.txt", item[0:len(item)-2])
                    sep += 30
                    index += 1

                if item[-1] == 'g':
                    self.tab(surf, sep, button_array[index], "grooming.txt", item[0:len(item) - 2])
                    sep += 30
                    index += 1

                if item[-1] == 't':
                    self.tab(surf, sep, button_array[index], "fun.txt", item[0:len(item) - 2])
                    sep += 30
                    index += 1

