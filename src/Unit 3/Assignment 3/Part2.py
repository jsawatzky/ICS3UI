'''
Created on Sep 30, 2014

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
def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

#Start x and y of the blue lines
x = 100
y = HEIGHT-100

#Length of the blue lines
length = min(WIDTH, HEIGHT)-200

#Draws blue lines
s.create_line(x, y, x + length, y, fill = "blue")
s.create_line(x, y, x, y - length, fill = "blue")

#Array to keep track of lines
lines = []

#Function to draw the lines on the screen based on the selected user input
def drawLines():
    global length, x, y, entry, lines
    spacing = int(length / int(entry.get()))
    for line in lines:
        s.delete(line)
    for i in range(x+spacing, x+length, spacing):
        lines.append(s.create_line(i, y, x, i, fill = "yellow"))
    
#Question at top of screen
text = s.create_text(WIDTH/2, 7, text = "How many lines would you like?", fill = "white", anchor = N, font = "Times 14")

#Drop down menu
entry = StringVar(s)
entry.set(int(length/40))
menu = OptionMenu(s, entry, int(length/40), int(length/35), int(length/30), int(length/25), int(length/20))
menu.configure(width = 7)
menuW = s.create_window((WIDTH/2)+15, 45, window = menu, anchor = E)

#Enter button
button = Button(s, text="Enter", command = drawLines)
button.configure(width = 5, activebackground = "green")
buttonW = s.create_window((WIDTH/2)+25, 45, window = button, anchor = W)

#Update loop
while running == True:
    try:
        s.update()
    except:
        running = False