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
r = 380
n = 200
s = 1
#must be less than numNails

deltaTheta = 360/n  #when n was 24, this should be 15 degrees

xValues = []
yValues = []

for i in range( 0, n ):
    
    angle = deltaTheta * i
    angleRad = radians( angle )

    #The (x,y) coordinates of the current nail.
    x = r * cos( angleRad ) + xC 
    y = r * sin( angleRad ) + yC

    xValues.append( x )
    yValues.append( y )


    #DRAW THE NEXT NAIL
    screen.create_oval( x, y, x+4, y+4, fill = "black" )


#YOUR JOB:  Draw the lines using s and the arrays xValues and yValues

for i in range(0, n):
    xStart = xValues[i]
    yStart = yValues[i]

    i2 = (i + s) % n
    
    xEnd = xValues[ i2 ]
    yEnd = yValues[ i2 ]

    screen.create_line(xStart, yStart, xEnd, yEnd, fill="blue")
    screen.update()

    s = s + 12

    

    















