#Purpose:  This program creates beautiful string-art patterns inside a circle
#Prerequisites: Arrays, modular indexing, and Grade 11 trigonometry
#Programmer:  J. Schattman
#Last modified:  July 30, 2013


#IMPORTS
from tkinter import *
from math import *
from time import *


#SET UP THE DRAWING CANVAS
screenHeight = 800
screenWidth = 800
root = Tk()
screen = Canvas( root, width=screenWidth, height=screenHeight, background = "yellow" )
screen.pack()


#SET PARAMETERS
xC = 400
yC = 400
r = 300
n = 25
s = 7 #must be less than numNails

deltaTheta = 360/n  #when n was 25, this should be about 14 degrees

xValues = []
yValues = []

for i in range( 0, n ):
    
    theta = deltaTheta * i
    thetaRadians = radians( theta )

    #The (x,y) coordinates of the current nail.
    x= r * cos( thetaRadians ) + 400 
    y = r * sin( thetaRadians ) + 400

    xValues.append( x )
    yValues.append( y )


    #DRAW THE NEXT NAIL
    screen.create_oval( x, y, x+4, y+4, fill = "black" )

#Draw the lines
for i in range(0, n):

    screen.create_line(xValues[i], yValues[i], xValues[(i+s)%n], yValues[(i+s)%n], fill = "red")
    
while True:
    screen.update()
















#DRAW THE STRINGS   
##for i in range(0, numNails):
##
##    iEnd = (i + 60) % numNails
##
##    xStart = xNails[ i ]
##    xEnd = xNails[ iEnd ]
##    
##    yStart = yNails[ i ]
##    yEnd = yNails[ iEnd ]
##
##    screen.create_line( xStart, yStart, xEnd, yEnd, fill = colors[ i % numColors ] )
##
##    screen.update()
##       
##    sleep(0.05)

