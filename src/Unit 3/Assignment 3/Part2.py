'''
Created on Sep 30, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

running = True

WIDTH = 800
HEIGHT = 800

myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
s.pack()

def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

x = 100
y = HEIGHT-100

length = min(WIDTH, HEIGHT)-200

s.create_line(x, y, x + length, y, fill = "blue")
s.create_line(x, y, x, y - length, fill = "blue")



text = s.create_text(WIDTH/2, (HEIGHT/2)-30, text = "How many lines would you like?", fill = "white", anchor = N)

numLines = 0

entry = StringVar(s)
entry.set(int(length/40))
menu = OptionMenu(s, entry, int(length/20), int(length/25), int(length/30), int(length/35), int(length/40))
menu.configure(width = 7)
menuW = s.create_window((WIDTH/2)+15, HEIGHT/2, window = menu, anchor = E)

def drawLines(numLines):
    global length, x, y, entry
    spacing = int(length / int(entry.get()))
    for i in range(x+spacing, x+length, spacing):
        s.create_line(i, y, x, i, fill = "yellow")

button = Button(s, text="Enter", command = drawLines)
button.configure(width = 5, activebackground = "green")
buttonW = s.create_window((WIDTH/2)+25, HEIGHT/2, window = button, anchor = W)

while numLines == 0:
    s.update()
    
s.delete(text, menuW, buttonW)
    
text = s.create_text(WIDTH/2, HEIGHT+30, text = "How many lines would you like?", fill = "white", anchor = N)

menu = OptionMenu(s, entry, int(length/20), int(length/25), int(length/30), int(length/35), int(length/40))
menu.configure(width = 7)
menuW = s.create_window((WIDTH/2)+15, HEIGHT+45, window = menu, anchor = E)

button = Button(s, text="Enter", command = drawLines)
button.configure(width = 5, activebackground = "green")
buttonW = s.create_window((WIDTH/2)+25, HEIGHT+45, window = button, anchor = W)

# spacing = 25
# for x in range(0, 800, spacing): 
#     s.create_line(x, 10, x, 800, fill="blue")
#     s.create_text(x, 0, text=str(x), font="Times 8", anchor = N)
# 
# for y in range(0, 800, spacing):
#     s.create_line(20, y, 800, y, fill="blue")
#     s.create_text(0, y, text=str(y), font="Times 8", anchor = W)

while running == True:
    try:
        s.update()
    except:
        running = False