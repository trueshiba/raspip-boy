import pygame


# draw rect but with transparency
# SRCALPHA - basically saves each pixel and its
# transparency level for late application or something
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


# draw level bar
def draw_shield_bar(surf, x, y, xp, xp_total):
    #GREEN = (5, 69, 8)  no longer used
    BORDER = (88, 243, 100)

    # Size of the bar
    BAR_LENGTH = 200
    BAR_HEIGHT = 12

    # the actual bar itself
    fill = (xp / xp_total) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)

    # Check what color the bar should be based on the points given
    #color = GREEN no longer used

    # draws the bar :D
    pygame.draw.rect(surf, BORDER, fill_rect)
    pygame.draw.rect(surf, BORDER, outline_rect, 2)


# Credit to [GLOOSES]
'''
The Leveling System for the PipBoy
NOTES:
    Current this relies on the Pedometer code calling the gainExp() function
    to give the user exp (Can do it for every step or add code to do it for a
    certain amount of steps).
    exp = # of steps
    needed exp= # of steps needed for a level up
'''

# Global Variables
exp = 0
level = 1
neededExp = 10
NEXTLEVEL = 2


# Experience Function
# When you walk a certain amount the pedometer calls this function.
# If you have enough exp to level up that function is called.
def gainExp():
    global exp

    exp += 1
    print("---gainExp: Test---")
    print("Exp: ")
    print(exp)
    if exp == neededExp:
        levelUp()


# Level up
# Reset the experience and level up
# Increase needed exp by the set amount (NEXTLEVEL)
def levelUp():
    global exp, level, neededExp, NEXTLEVEL

    exp = 0
    level += 1
    neededExp *= NEXTLEVEL
    print("---levelUp: Test---")
    print("Exp: ")
    print(exp)
    print("Level: ")
    print(level)
    print("Needed Exp: ")
    print(neededExp)


# Get Functions
def getLevel():
    return level


def getExp():
    return exp


def getNeededExp():
    return neededExp

#Set Functions
def setLevel(lvl):
    global level
    level = lvl

def setExp(xp):
    global exp
    exp = xp


def setNeededExp(ndxp):
    global neededExp
    neededExp = ndxp


# Credit to [MISH]
'''
The Level Class for the PipBoy
    Since there is currently no Pedometer it is permanently turned off
    Future edits will be made to take in GPIO PIN Reading 
    NOTES:
        Need to Update Green Color for Level Fill
        Config to Accelerometer 
'''


# level class
class Level:
    def __init__(self):
        self.color = (51, 109, 48, 200)
        self.x = 110
        self.y = 300
        self.width = 265
        self.height = 35

        #Read Previous Stats from File
        f = open("level.txt", "r")

        #Credit to 'AskPython'
        # Use of isdigit() function to extract digits from a Python string
        num = [int(x) for x in f.readline().split() if x.isdigit()]
        self.level = num[0]

        num = [int(x) for x in f.readline().split() if x.isdigit()]
        self.exp = num[0]

        num = [int(x) for x in f.readline().split() if x.isdigit()]
        self.exp_total = num[0]

        #Set Global Variables
        setNeededExp(self.exp_total)
        setExp(self.exp)
        setLevel(self.level)

        self.text = f'LEVEL {self.level}'

    def draw(self, surf):
        rect = (self.x, self.y), (self.width, self.height)
        draw_rect_alpha(surf, self.color, rect)

    def update_level(self, surf):
        self.draw(surf)
        update = False
        Pedometer_Status = False

        # get Accelerometer Info - replace True with accelerometer check
        while update:
            if Pedometer_Status:
                gainExp()

                # Update Data in Level File
                f = open("level.txt", "w")
                f.write(f'Current Level {self.level:>23}\n')
                f.write(f"Current XP {self.exp:>26}\n")
                f.write(f"XP Needed {self.exp_total:>25}\n")
                f.close()

        self.level = getLevel()
        self.exp = getExp()
        self.exp_total = getNeededExp()

        self.text = f'LEVEL {self.level}'

        # Print Level Amount
        TEXT_COL = (100, 252, 127, 255)

        font = pygame.font.SysFont('arial', 15)
        text = font.render(self.text, False, TEXT_COL)
        surf.blit(text, (self.x + 5, self.y))

        # Print Level Bar
        draw_shield_bar(surf, 170, 304, self.exp, self.exp_total)

        update = True

        return update

    # [For Testing Purposes Only]
    def is_pressed(self, surf):
        action = False

        # get mouse position

        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                action = True

        gainExp()

        #send result
        return action
