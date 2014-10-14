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

#Command and button to close window
def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

#Start x and y of the blue lines
x = 0
y = 0

#Length of the blue lines
length = 0

#The blue lines
xAxis = None
yAxis = None

#Array to keep track of lines
lines = []

#Function to draw the lines on the screen based on the selected user input
def drawLines():
    global length, x, y, numLines, mirroring, lines
    spacing = int(length / numLines.get())
    for line in lines:
        s.delete(line)
    lines.clear()
    for i in range(0, numLines.get()):
        x1 = x
        y1 = (y - length) + spacing * i
        x2 = x + spacing * (i+1)
        y2 = y
        lines.append(s.create_line(x1, y1, x2, y2, fill = "yellow"))
        if mirroring.get() == "On the y-axis" or mirroring.get() == "Both":
            lines.append(s.create_line(x1, y1, WIDTH-x2, y2, fill = "yellow"))
        if mirroring.get() == "On the x-axis" or mirroring.get() == "Both":
            lines.append(s.create_line(x1, HEIGHT-y1, x2, y2, fill = "yellow"))
        if mirroring.get() == "Both":
            lines.append(s.create_line(x1, HEIGHT-y1, WIDTH-x2, y2, fill = "yellow"))
        
def updateMirroring():
    global s, x, xAxis, y, yAxis, length, mirroring, menu, menuW
    
    s.delete(xAxis, yAxis)
    
    if mirroring.get() == "None":
        x = 100
        y = HEIGHT-100
        length = min(WIDTH, HEIGHT)-200
        xAxis = s.create_line(x, y, x + length, y, fill = "blue")
        yAxis = s.create_line(x, y, x, y - length, fill = "blue")
    elif mirroring.get() == "On the y-axis":
        x = int(WIDTH/2)
        y = int((HEIGHT/4)+(HEIGHT/2))
        length = int((HEIGHT-200)/2)
        xAxis = s.create_line(x - length, y, x + length, y, fill = "blue")
        yAxis = s.create_line(x, y, x, y - length, fill = "blue")
    elif mirroring.get() == "On the x-axis":
        x = int(WIDTH/4)
        y = int(HEIGHT/2)
        length = int((WIDTH-200)/2)
        xAxis = s.create_line(x, y, x + length, y, fill = "blue")
        yAxis = s.create_line(x, y - length, x, y + length, fill = "blue")
    else:
        x = int(WIDTH/2)
        y = int(HEIGHT/2)
        length = int((min(WIDTH, HEIGHT)-200) / 2)
        xAxis = s.create_line(x - length, y, x + length, y, fill = "blue")
        yAxis = s.create_line(x, y - length, x, y + length, fill = "blue")
        
    numLines.set(int(length/40))
    menu = OptionMenu(s, numLines, int(length/40), int(length/35), int(length/30), int(length/25), int(length/20))
    menu.configure(width = 7)
    menuW = s.create_window((WIDTH/2)+15, 45, window = menu, anchor = E)
    drawLines()
    
#Question at top of screen
text = s.create_text(WIDTH/2, 7, text = "How many lines would you like?", fill = "white", anchor = N, font = "Times 14")

#Drop down menu
numLines = IntVar(s)
numLines.set(int(length/40))
menu = OptionMenu(s, numLines, 0)
menu.configure(width = 7)
menuW = s.create_window((WIDTH/2)+15, 45, window = menu, anchor = E)

#Enter button
button = Button(s, text="Enter", command = drawLines)
button.configure(width = 5, activebackground = "green")
buttonW = s.create_window((WIDTH/2)+25, 45, window = button, anchor = W)

text = s.create_text(WIDTH-75, 7, text = "Mirroring", fill = "white", anchor = N, font = "Times 14")

#Drop down menu
mirroring = StringVar(s)
mirroring.set("None")
menu2 = OptionMenu(s, mirroring, "None", "On the y-axis", "On the x-axis", "Both")
menu2.configure(width = 10)
menu2W = s.create_window(WIDTH-60, 45, window = menu2, anchor = E)

#Enter button
button2 = Button(s, text="Enter", command = updateMirroring)
button2.configure(width = 5, activebackground = "green")
button2W = s.create_window(WIDTH-50, 45, window = button2, anchor = W)

updateMirroring()

def run():
    global running
    s.pack()
    #Update loop
    while running == True:
        try:
            s.update()
        except:
            running = False

if __name__ == "__main__":
    run()
