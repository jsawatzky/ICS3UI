from Tkinter import *
from math import *
from time import *
from random import *
myInterface = Tk()
me = Canvas(myInterface, width=700, height=700, background="black")
me.pack()
yarnColors = ["red", "purple", "blue"]
deltaTheta = 6
radius = 340
xCenter = 350
yCenter = 350
theta1 = 0
thetaSkip = 90
tinyRadius = 0
starsOn = True
runInnerCircle = True
innerCircleColor = "orange"
k = pi/180
numLines = 360 / deltaTheta
numWeaves = len(yarnColors)
minimumInnerRadius = radius * cos(thetaSkip/2 * k)**numWeaves
deltaTinyRadius = minimumInnerRadius / (numWeaves*numLines)
if starsOn: 
    for i in range (0,400):
        x = randint(0,1000)
        y = randint(0,800)
        starRadius = randint(1,4)
        star = me.create_oval(x,y,x+starRadius,y+starRadius,fill="white",outline="white")
        me.update()
circle = me.create_oval(xCenter-radius, yCenter-radius, xCenter+radius, yCenter+radius, outline="white")
sleep(1)
me.update()
for weaveNum in range(0, numWeaves):
    for lineNum in range(0, numLines):
        theta1 = theta1 + deltaTheta
        theta2 = theta1 + thetaSkip        
        xStart = xCenter + radius*cos(theta1 * k)
        yStart = yCenter - radius*sin(theta1 * k)       
        xEnd = xCenter + radius*cos(theta2 * k)
        yEnd = yCenter - radius*sin(theta2 * k)
        line = me.create_line(xStart, yStart, xEnd, yEnd, fill=yarnColors[ weaveNum ])
        if runInnerCircle:
            tinyRadius = tinyRadius + deltaTinyRadius
            innerCircle = me.create_oval(xCenter-tinyRadius, yCenter-tinyRadius, xCenter+tinyRadius, yCenter+tinyRadius, fill=innerCircleColor, outline=innerCircleColor)
        me.update()
        sleep(0.05)
    theta1 = theta2
    radius = radius * cos(thetaSkip/2 * k)

   
