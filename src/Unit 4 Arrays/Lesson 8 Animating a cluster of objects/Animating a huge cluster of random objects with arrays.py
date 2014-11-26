#Purpose:  This program shows how to use arrays to animate several objects simultaneously
#Prerequisites: Arrays
#Programmer:  J. Schattman
#Last modified:  Sept. 30, 2013

from tkinter import *
from math import *
from time import *
from random import *

master = Tk()
screen = Canvas( master, width = 800, height = 800, background = "yellow")
screen.pack()


numFrames = 200

numBoxes = 100

size = []
x = []
y = []
xSpeed = []
ySpeed = []
box = []

for i in range( 0, numBoxes ):
    
    newSize = randint(10,60)
    newX = randint(100,600)
    newY = randint(100,600)
    newXspeed = randint(-8,8)
    newYspeed = randint(1,10)

    size.append( newSize )
    x.append( newX )
    y.append( newY )
    xSpeed.append( 3 )
    ySpeed.append( newYspeed )
    box.append ( 0 )
    

#Draw background scenery here
####



#Animate 6 boxes moving on top of the background

for frameCount in range( 1, numFrames + 1 ):
    
    for i in range(0,numBoxes):
        x[i] = x[i] + xSpeed[i]
        y[i] = y[i] + ySpeed[i]
        box[i] = screen.create_oval( x[i], y[i], x[i] +size[i], y[i] +size[i], fill="blue")

    screen.update()  #why isn’t this in the nested loop? 
    sleep(0.05)  #why isn’t this in the nested loop?

    #Delete all 6 boxes, one by one
    for i in range(0,numBoxes):
        screen.delete( box[i] )
