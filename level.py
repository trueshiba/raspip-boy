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
level = 0
neededExp = 10
NEXTLEVEL = 2


# Main Function (Mostly just for testing)
def main():    
    i = 0
    while i < 11:
        i += 1
        gainExp()


# Experience Function
    # When you walk a certain amount the pedometer calls this function.
    # If you have enough exp to level up that function is called.
def gainExp():
    global exp
    
    exp += 1
    print("---gainExp: Test---")
    print("Exp: "); print(exp)
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
    print("Exp: "); print(exp)
    print("Level: "); print(level)
    print("Needed Exp: "); print(neededExp)
    

# Get Functions
def getLevel():
    return level

def getExp():
    return exp;



# Call Main Function
if __name__ == '__main__':
    main()
