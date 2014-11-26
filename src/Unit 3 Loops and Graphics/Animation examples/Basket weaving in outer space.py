####################################################################
# Title: Circular Weave Animation
# Programmer:  Mr. Schattman
# Last modified:  Oct. 19, 2014
# Purpose: This program draws lines in a mathematical pattern that seem to
#           form a circle
#####################################################################


#Import Python packages needed for graphics and mathematical calculations
from tkinter import *
from math import *
from time import *
from random import *


#Make a canvas to draw on
myInterface = Tk()
me = Canvas(myInterface, width=700, height=700, background="white")
me.pack()


#DRAWING OPTIONS.  Change these values to see different artistic patterns
yarnColors = ["red", "pink", "blue"]
deltaTheta = 4
radius = 340
xCenter = 350
yCenter = 350
theta1 = 0
thetaSkip = 90
tinyRadius = 0
me.create_rectangle(0,0,700,700,fill="black")


#Starry background?
starsOn = False


#Put a growing sun in the middle?
runInnerCircle = True
innerCircleColor = "white"


#Formulas needed to draw the lines in the correct places
k = pi/180
numLines = 360 / deltaTheta
numWeaves = len(yarnColors)
minimumInnerRadius = radius * cos(thetaSkip/2 * k)**numWeaves
deltaTinyRadius = minimumInnerRadius / (numWeaves*numLines)


#Draw the starry background if requested
if starsOn: 
    for i in range (0,400):
        x = randint(0,1000)
        y = randint(0,800)
        starRadius = randint(1,4)
        star = me.create_oval(x,y,x+starRadius,y+starRadius,fill="white",outline="white")
        me.update()


#Draw the main, large circle
circle = me.create_oval(xCenter-radius, yCenter-radius, xCenter+radius, yCenter+radius, outline="white")
sleep(1)
me.update()


#Draw all the weave layers
for weaveNum in range(0, numWeaves):

    #Draw all the lines within a given weave layer
    for lineNum in range(0, numLines):

        #Calculate the start and end points of the current line being drawn
        theta1 = theta1 + deltaTheta
        theta2 = theta1 + thetaSkip
        
        xStart = xCenter + radius*cos(theta1 * k)
        yStart = yCenter - radius*sin(theta1 * k)
        
        xEnd = xCenter + radius*cos(theta2 * k)
        yEnd = yCenter - radius*sin(theta2 * k)

        #Draw the current line
        line = me.create_line(xStart, yStart, xEnd, yEnd, fill=yarnColors[ weaveNum ])

        #Make the inner circle grow a little bit after each line is drawn
        if runInnerCircle:

            tinyRadius = tinyRadius + deltaTinyRadius
            innerCircle = me.create_oval(xCenter-tinyRadius, yCenter-tinyRadius, xCenter+tinyRadius, yCenter+tinyRadius, fill=innerCircleColor, outline=innerCircleColor)

        me.update()

        #Pause to prevent the animation from going by too quickly to see
        sleep(0.05)


    #Calculate the radius of the next weave
    theta1 = theta2
    radius = radius * cos(thetaSkip/2 * k)

me.postscript(file="/Users/Jason/Dropbox/AAA Teaching/Math Dept projects/weave 1.eps")

   
