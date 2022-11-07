import pygame
import Level
import random

#cycle randomly (4 objects at first 4 levels)
#after level 8, 8 objects are maxed out

int itemSpace = 4
Level level
listOfItems =[]

#let me know if I fix anything c:
#Loop to see how much space is available
def spaceAvailable():
    for i in level:
        if getLevel() > 4 & getLevel() < 8 :
            itemSpace += 1
        elif getLevel >= 8:
            itemSpace = 8

#inventory function to print out the inventory
def inventory():

    #run spaceAvailable
    spaceAvailable()

    #opens file with items
    randomItems= open("randomItems.txt", "r")

    #adds each item to the list
    for x in randomItems:
        listOfItems.add(x)
       
    #shuffles the list
    random.shuffle(listOfItems)

    #prints the inventory
    print("My Inventory: ")
    for i in range(1, itemSpace):
        print(i": " + listOfItems[i]) 
