'''
Created on Sep 29, 2014

@author: Jacob
'''

from tkinter import *

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

def grid(s, spacing, width, height):
    for x in range(0, width, spacing): 
        s.create_line(x, 10, x, height, fill="magenta")
        s.create_text(x, 0, text=str(x), font="Times 8", anchor = N)
    for y in range(0, height, spacing):
        s.create_line(20, y, width, y, fill="magenta")
        s.create_text(0, y, text=str(y), font="Times 8", anchor = W)