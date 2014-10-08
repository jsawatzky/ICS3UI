'''
Created on Oct 2, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

from random import *

#Boolean for update loops
playing = True

#Constants for reference
WIDTH = 800
HEIGHT = 800

#Creates the screen
myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="#27462c")
s.pack()

#Gets images off a sprite sheet (Source: http://tkinter.unpythonic.net/wiki/PhotoImage)
def subimage(src, l, t, r, b):
    dst = PhotoImage()
    dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
    return dst


#Create Deck
cardSprite = PhotoImage(file = "cards.gif")
cardBack = subimage(cardSprite, 0, 400, 71, 499)
cards = []
cardTracker = {}
y = 0
for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
    x = 0
    for type in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]:
        x1 = x*72
        y1 = y*100
        img = subimage(cardSprite, x1, y1, x1+71, y1+99)
        cardTracker[img] = {}
        cardTracker[img]['holder'] = "deck"
        cardTracker[img]['value'] = type
        cardTracker[img]['suit'] = suit
        cards.append(img)
        x += 1
    y += 1
    
shuffle(cards)