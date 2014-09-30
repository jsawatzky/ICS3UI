'''
Created on Sep 29, 2014

@author: Jacob
'''

##Gets the integer version of a string
def getInt(numStr, suffix=""):
    valid = False
    while valid == False:
        try:
            numInt = int(numStr)
            valid = True
        except ValueError:
            try:
                numFloat = float(numStr)
                numStr = input("You must enter an integer value! (No decimals) Please try again: " + suffix)
            except ValueError:
                numStr = input("You must enter a number! Please try again: " + suffix)
    return numInt

##Gets the float version of a string
def getNum(numStr, suffix=""):
    valid = False
    while valid == False:
        try:
            num = float(numStr)
            valid = True
        except ValueError:
            numStr = input("You must enter a number! Please try again: " + suffix)
    return num