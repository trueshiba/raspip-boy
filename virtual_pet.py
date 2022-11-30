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

# Temporary! Don't know how this stuff works :/
# Lower stats over time, same as Mish's health.py?

# Increase max stats through level ups
# (HAPPEN in level.py? See above notes.)
    
    
    
# Increase stats through items



# Determine overall moods (Add stats together and divide by max)
    # Good Mood - If added together and have >=75%
    # Meh Mood - If added together and have >=25%
    # Bad Mood - If added together and have <25%
def mood(hung, rads, enjoyment):
    # Calculate radiation value (Reversed from the others)
    rads = maxRadiation - rads

    currentTotal = hung + rads + enjoyment
    maxTotal = maxHunger + maxRadiation + maxFun
    percent = currentTotal / maxTotal

    if percent >= .75:
        setMood("good")
    elif percent <= .25:
        setMood("bad")
    else:
        setMood("meh")

# Getters
def getHunger():
    return hunger

def getRadiation():
    return radiation

def getFun():
    return fun

def getMood():
    return mood

# Setters
def setHunger(hung):
    global hunger
    hunger = hung

def setRadiation(rads):
    global radiation
    radiation = rads

def setFun(enjoyment):
    global fun
    fun = enjoyment

def setMood(m):
    global mood
    mood = m


class Virtual_Pet:
    def __init__():
        self.hunger = 115
        self.maxHunger = 115
        self.text = f'HP {self.health_max} / {self.health_current}'
        self.time_increase =  0 #so program doesn't constantly open health.txt
        #CONSTANT
        self.DIVIDER = 12.5217


    def update_hunger():
        update = False

        # Define the time
        time = datetime.datetime.now()
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        total_day = (hour * 60) + minute

        # Set hunger based on current time
        if total_day > (self.time_increase + 10):
            if total_day % 30 >= 1:
                self.hunger = self.maxHunger - int((total_day // self.DIVIDER))
                self.time_increase = total_day
                print(self.time_increase)

        update = True

        return update


print(Virtual_Pet.update_hunger())
    


    
