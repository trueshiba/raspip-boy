'''
The Virtual Pet System for the PipBoy
NOTES:
    Change level up so that when you get a level up, you increase a stat? (Random)
    percent chance for each to go up, some are harder to level than others?
'''
import datetime

# Global Variables
# Current stats
hunger = 5
radiation = 0
fun = 5
mood = "null"

# Max Stats (Increases with level ups)
maxHunger = 10
maxRadiation = 10
maxFun = 10

# maybe

'''
The Virtual Pet System for the PipBoy
NOTES:
    Needs to write to a file to save stats! Look at what others did in their code
    Save hunger, radiation, and fun amounts
'''
import datetime
import random
import pygame
import level


# Credit to [Mish]
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


# Credit to [Alison]
class Virtual_Pet:
    def __init__(self):
        # Current stats
        # Read Previous Stats from File
        r = open("pet-rad.txt", "r")
        h = open("pet-hunger.txt", "r")
        f = open("pet-fun.txt", "r")

        # Credit to 'AskPython'
        self.hunger = int(h.readline())
        self.radiation = int(r.readline())
        self.fun = int(f.readline())

        # Max Stats (Increases with level ups, can change values)
        self.maxHunger = 60
        self.maxRadiation = 60
        self.maxFun = 60

        self.time_increase_hung = 0
        self.time_increase_rad = 0
        self.time_increase_fun = 0
        self.stat_increase = 0
        self.rand_stat_range = 10

        # CONSTANT
        self.DIVIDER_HUNGER = (1140 / maxHunger)
        self.DIVIDER_FUN = (1140 / maxFun)
        self.DIVIDER_RADIATION = (1140 / maxRadiation)

        self.HUNGPERCENT = 0.55
        self.RADSPERCENT = 0.30
        self.FUNPERCENT = 0.65

        # Menu Stuff
        self.pip = pygame.transform.scale(pygame.image.load('pipboy.png'), (120, 180))
        self.rad_img = pygame.transform.scale(pygame.image.load('Stat/radiate-green.png'), (25, 25))
        self.hunger_img = pygame.transform.scale(pygame.image.load('Stat/hunger-green.png'), (22, 22))
        self.fun_img = pygame.transform.scale(pygame.image.load('Stat/fun-green.png'), (25, 25))

        self.happy = pygame.transform.scale(pygame.image.load('Stat/happy.png'), (30, 30))
        self.sad = pygame.transform.scale(pygame.image.load('Stat/sad.png'), (30, 30))
        self.meh = pygame.transform.scale(pygame.image.load('Stat/meh.png'), (30, 30))

        self.color = (51, 109, 48, 200)

    # Getters
    def getHunger(self):
        return self.hunger

    def getRadiation(self):
        return self.radiation

    def getFun(self):
        return self.fun

    def getMood(self):
        return self.mood

    # Setters
    def setMaxHunger(self, hung):
        self.maxHunger = hung

    def setMaxRadiation(self, rads):
        self.maxRadiation = rads

    def setMaxFun(self, f):
        self.maxFun = f

    def setMood(self, m):
        self.mood = m

    # Temporary! Don't know how this stuff works :/
    # Lower stats over time, same as Mish's health.py? (hunger, radiation, fun)
    def update_hunger(self):
        update = False
        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        total_day = (hour * 60) + minute  # in minutes

        # Set hunger based on current time
        if total_day > (self.time_increase_hung + 10):
            if total_day % 30 >= 1:
                self.hunger = self.maxHunger - int((total_day // self.DIVIDER_HUNGER))
                self.time_increase_hung = total_day

                f = open("pet-hunger.txt", "w")
                f.write(str(self.hunger))
        update = True
        return update

    def update_radiation(self):
        update = False
        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        total_day = (hour * 60) + minute  # in minutes

        # Set radiation based on current time (More rather than less)
        if total_day > (self.time_increase_rad + 10):
            if total_day % 30 >= 1:
                self.radiation = self.radiation + int((total_day // self.DIVIDER_RADIATION))
                self.time_increase_rad = total_day

                f = open("pet-rad.txt", "w")
                f.write(str(self.radiation))

        update = True
        return update

    def update_fun(self):
        update = False
        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        total_day = (hour * 60) + minute  # in minutes

        # Set fun based on current time
        if total_day > (self.time_increase_fun + 10):
            if total_day % 30 >= 1:
                self.fun = self.maxFun - int((total_day // self.DIVIDER_FUN))
                self.time_increase_fun = total_day

                f = open("pet-fun.txt", "w")
                f.write(str(self.fun))
        update = True
        return update

    # Increase max stats through level ups (Called in level.py)
    # Also increases how much items increase your stats
    def increase_cap(self):
        if random.random() < self.HUNGPERCENT:
            self.maxHunger = self.maxHunger + 1
        if random.random() < self.RADSPERCENT:
            self.maxRadiation = self.maxRadiation + 1
        if random.random() < self.FUNPERCENT:
            self.maxFun = self.maxFun + 1
        self.DIVIDER_HUNGER = (1140 / maxHunger)
        self.DIVIDER_FUN = (1140 / maxFun)
        self.DIVIDER_RADIATION = (1140 / maxRadiation)
        self.rand_stat_range += 4

    # Increase current stats through items (in a random range that increases as you level, see above function)
    # use_item() is in the inventory class, this should be called by that?
    # One for health, food, and toy
    def item_h_increase(self):
        # Randomly determine an amount for the stat to increase
        self.radiation += random.randrange(1, self.rand_stat_range)

    def item_f_increase(self):
        self.hunger += random.randrange(1, self.rand_stat_range)

    def item_t_increase(self):
        self.fun += random.randrange(1, self.rand_stat_range)

    # Determine overall moods (Add stats together and divide by max)
    def find_mood(self, surf):
        # Calculate radiation value (Reversed from the others)
        rad = self.maxRadiation - self.radiation

        currentTotal = self.hunger + rad + self.fun
        maxTotal = self.maxHunger + self.maxRadiation + self.maxFun
        percent = currentTotal / maxTotal

        if percent >= .75:
            self.mood = "good"
            surf.blit(self.happy, (175, 254))
        elif percent <= .25:
            self.mood = "bad"
            surf.blit(self.sad, (175, 254))
        else:
            self.mood = "meh"
            surf.blit(self.meh, (175, 254))

    # Credit to [Mish]
    def draw_pip(self, surf, running):
        if running:
            # self.screen.fill((self.white))
            # (x , y)
            surf.blit(self.pip, (180, 50))
            # pygame.display.flip()

    def draw_stats(self, surf, running):
        if running:
            surf.blit(self.hunger_img, (228, 235))
            surf.blit(self.fun_img, (262, 233))
            surf.blit(self.rad_img, (297, 233))

    def draw_bar(self, surf):
        rect = (160, 230), (60, 60)
        draw_rect_alpha(surf, self.color, rect)
        rect = (225, 230), (30, 60)
        draw_rect_alpha(surf, self.color, rect)
        rect = (260, 230), (30, 60)
        draw_rect_alpha(surf, self.color, rect)
        rect = (295, 230), (30, 60)
        draw_rect_alpha(surf, self.color, rect)


    def menu(self, surf):
        #self.draw_pip(surf, True)
        #self.draw_pipwalk(surf, True)
        self.draw_bar(surf)
        self.draw_stats(surf, True)

        TEXT_COL = (100, 252, 127, 255)
        font = pygame.font.SysFont('arial', 16)
        text = font.render("MOOD", False, TEXT_COL)
        surf.blit(text, (170, 233))

        stat_font = pygame.font.SysFont('arial', 18)

        surf.blit(stat_font.render(str(self.getHunger()), False, TEXT_COL), (229, 265))
        surf.blit(stat_font.render(str(self.getFun()), False, TEXT_COL), (265, 265))
        surf.blit(stat_font.render(str(self.getRadiation()), False, TEXT_COL), (300, 265))

        self.find_mood(surf)
        level.Level().update_level(surf, False)



    # surf.blit("MOOD", (self.x + 5, self.y))
