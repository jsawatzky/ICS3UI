#Purpose:  This program creates beautiful string-art patterns inside a circle
#Prerequisites: Arrays, modular indexing, and Grade 11 trigonometry
#Programmer:  J. Schattman
#Last modified:  October 30, 2014


#IMPORTS
from tkinter import *
from math import *


#SET UP THE DRAWING CANVAS
root = Tk()
screen = Canvas( root, width=800, height=800, background = "yellow" )
screen.pack()


#SET PARAMETERS
xC = 400
yC = 400
r = 300
n = 150
s = 7

deltaTheta = ???

for i in range( 0, n ):
    
    angle = ???
    angleRad = radians( angle )

    #The (x,y) coordinates of the current nail.
    x = ???
    y = ???

    #DRAW THE NEXT NAIL
    screen.create_oval( ?,?,?,?, fill = "black" )


#YOUR JOB:  Draw the lines using s and the arrays xValues and yValues

#for i in range(0, n):















