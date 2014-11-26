####################################################################
# Title: Circular Weave Animation
# Programmer:  Mr. Schattman
# Last modified:  Oct. 19, 2010
# Purpose: This program draws lines in a mathematical pattern that seem to
#           form a circle
#####################################################################


#Import Python packages needed for graphics and mathematical calculations
from Tkinter import *
from math import *
from time import *
from random import *


#Make a canvas to draw on
myInterface = Tk()
me = Canvas(myInterface, width=700, height=700, background="black")
me.pack()


#DRAWING OPTIONS.  Change these values to see different artistic patterns
yarnColors = ["red", "purple", "blue"]
deltaTheta = 6
radius = 340
xCenter = 350
yCenter = 350
theta1 = 0
thetaSkip = 90
tinyRadius = 0


#Starry background? Set to True if yes.
starsOn = False


#Put a growing sun in the middle?  Set to True if yes.
runInnerCircle = True
innerCircleColor = "orange"


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


    #Calculating the radius of the next weave
    theta1 = theta2
    radius = radius * cos(thetaSkip/2 * k)

   
