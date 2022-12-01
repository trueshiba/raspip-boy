'''
The Virtual Pet System for the PipBoy
NOTES:
    Needs to write to a file to save stats! Look at what others did in their code
    Save hunger, radiation, and fun amounts
'''
import datetime
import random

# Credit to [Alison]
class Virtual_Pet:
    def __init__(self):
        # Current stats
        self.hunger = 115
        self.radiation = 0
        self.fun = 5
        self.mood = "null"

        # Max Stats (Increases with level ups, can change values)
        self.maxHunger = 115
        self.maxRadiation = 115
        self.maxFun = 115

        self.time_increase_hung = 0
        self.time_increase_rad = 0
        self.time_increase_fun = 0
        self.stat_increase = 0
        self.rand_stat_range = 10

        #CONSTANT
        self.DIVIDER = 12.5217
        self.HUNGPERCENT = 0.55
        self.RADSPERCENT = 0.30
        self.FUNPERCENT = 0.65

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
                self.hunger = self.maxHunger - int((total_day // self.DIVIDER))
                self.time_increase_hung = total_day
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
                self.radiation = self.radiation + int((total_day // self.DIVIDER))
                self.time_increase_rad = total_day
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
                self.fun = self.maxFun - int((total_day // self.DIVIDER))
                self.time_increase_fun = total_day
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
    def find_mood(self):
        # Calculate radiation value (Reversed from the others)
        self.radiation = self.maxRadiation - self.radiation

        currentTotal = self.hunger + self.radiation + self.fun
        maxTotal = self.maxHunger + self.maxRadiation + self.maxFun
        percent = currentTotal / maxTotal

        if percent >= .75:
            self.mood = "good"
        elif percent <= .25:
            self.mood = "bad"
        else:
            self.mood = "meh"

