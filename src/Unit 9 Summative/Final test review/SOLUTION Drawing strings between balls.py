from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=800, height=800, background="white")
screen.pack()

#INITIAL VALUES
radius = 40
gap = 150
xStart = 100
yRow1 = 300
yRow2 = 500

#DRAW THE TOP ROW OF BALLS
for i in range(0,5):
    x = xStart + i*gap
    screen.create_oval( x-radius, yRow1-radius, x+radius, yRow1+radius,fill="blue")

#DRAW THE BOTTOM ROW OF BALLS
for i in range(0,5):
    x = xStart + i*gap
    screen.create_oval( x-radius, yRow2-radius, x+radius, yRow2+radius,fill="blue")


#DRAW THE STRINGS BETWEEN BALLS
for i in range(0,5):
    x1 = xStart + i*gap

    for j in range(0,5):
        x2 = xStart + j*gap
        screen.create_line(x1,yRow1,x2,yRow2,fill="black")
        
screen.update()


        
        
