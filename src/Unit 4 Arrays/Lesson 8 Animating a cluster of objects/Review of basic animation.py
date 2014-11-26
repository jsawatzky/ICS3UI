#Purpose:  This program shows how to animate a cluster of related objects using arrays
#Prerequisites: Arrays, modular indexing, and Grade 11 trigonometry
#Programmer:  J. Schattman
#Last modified:  Sept. 30, 2014


#IMPORTS
from tkinter import *
from math import *
from time import *
master = Tk()
screen = Canvas( master, width = 800, height = 800, background = "white")
screen.pack()


#PARAMETERS
numFrames = 200
size = 60
x = 500
y = 400
x2 = 600
y2 = 100
xSpeed = -5
ySpeed = -4
x2Speed = 3
y2Speed = 2
color = "blue"


###########################
#DRAW BACKGROUND SCENERY HERE
#...
##########################


######################################
#ANIMATE 1 BOX
######################################

for frameCount in range( 1, numFrames + 1 ):

     #UPDATE THE POSITIONS OF THE BOX, THEN DRAW THEM
     
     x = x + xSpeed
     y = y + ySpeed

     box = screen.create_rectangle( x, y, x+size, y+size, fill=color)

     screen.update() 
     sleep(0.05)
     screen.delete( box )
