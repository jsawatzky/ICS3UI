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
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="white")
s.pack()

#Draws grid
grid(s, 25)

#Command and button to close window
def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

def update():
    global s
    #Main animation
    
    s.update()

#Update loop
while running == True:
    try:
        update()
    except:
        running = False