from tkinter import *
from random import *
from time import *

root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

xUL = 0
xLimit = 800
yMiddle = 400
numCircles = 10
xSpeed = 10
ball=0

for i in range(1,numCircles+1):
    
    diameter = randint(50,150)
    xUL = 0
    xLR = diameter
    
    yUL = yMiddle - diameter/2
    yLR = yMiddle + diameter/2
    
    while xLR < xLimit:
        
        xUL = xUL + xSpeed
        xLR = xUL + diameter

        ball = screen.create_oval(xUL, yUL, xLR, yLR, fill="blue")
        screen.update()
        sleep(0.05)
        if xLR < xLimit:
            screen.delete(ball)

    xLimit = xLimit - diameter
