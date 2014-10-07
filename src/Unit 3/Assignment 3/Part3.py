'''
Created on Oct 2, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

#Boolean for update loops
running = True

#Constants for reference
WIDTH = 800
HEIGHT = 800

#Creates the screen
myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
s.pack()

#Command and button to close window
def buttonCmd(name):
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)


cardImg = PhotoImage(file = "cards.gif")
cards = {}
y = 0
for type in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
    x = 0
    for suit in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
        x1 = (x*72)+1
        y1 = (y*97)+1
        img = PhotoImage()
        cards[type+suit] = img.tk.call(img, 'copy', cardImg, '-from', x1, y1, x1+70, y1+70, '-to', 0, 0, 0, 0)
        x += 1
    y += 1
    
index = 0
for card in cards.values():
    s.create_image(index*70, 0, file = card)


#Update loop
while running == True:
    try:
        s.update()
    except:
        running = False