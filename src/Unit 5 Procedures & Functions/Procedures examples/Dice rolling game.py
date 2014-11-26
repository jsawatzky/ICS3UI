from random import *

def rollTwoDice():
    rollOne = randint(1,6)
    rollTwo = randint(1,6)
    print("The dice were a " + str( rollOne ) + " and a " + str(rollTwo) ) #No return statement --> procedure



print("Here's your first die roll...")
rollTwoDice() #we can tell it's a procedure because there's no LHS and no equals sign

print("Here's a second roll...")
rollTwoDice()

print("And a third roll...")
rollTwoDice()

##for i in range(0,100):
##    rollTwoDice()
