#############################
#TITLE:  Candy Cane Snow Fall
#This program draws a snow fall with candy cane flavours
#Programmer:  Mr. Schattman
#Last modified:  Jan 5, 2011
###############################

from tkinter import *
from time import *
from math import *
from random import *

tk = Tk()
me = Canvas(tk, width=800,height=800,background="black")
me.pack()


#Set number of snow flakes, ground level and wind speed
numFlakes = 500
groundLevel = 500
windSpeed = 2
colors = ["white", "red", "purple","blue", "yellow"]
#colors = ["white", "white", "white", "white", "white"]


#Draw the ground
ground = me.create_rectangle(0,groundLevel-5, 800, 800, fill="white",outline="white")


#Set up arrays 
flakes = []
xSpeeds = []
ySpeeds = []
xPos = []
yPos = []
xStart = []
yStart = []
sizes = []
t = []
colorChoice = []


#Set random initial values for each snow flake's speed, starting point, and size
for n in range(0,numFlakes):
    xPos.append(0)
    yPos.append(0)
    xSpeeds.append( windSpeed )
    ySpeeds.append( randint(8,11))
    xStart.append( randint(-200*windSpeed,800))
    yStart.append( randint(-800,0))
    sizes.append( randint(2,4) )
    flakes.append(0)
    t.append(0)
    colorChoice.append(0)



#For each frame, do all this
    
for frameCount in range(0,1000):

    #For each individual flake in the current frame, do all this

    for n in range(0, numFlakes):

        #Update the flake's position using its own private time-value (t)
        xPos[n] = xSpeeds[n] * t[n] + xStart[n]
        yPos[n] = ySpeeds[n] * t[n] + yStart[n]

        #Draw the current flake in the current frame using its own position, size, and current color choice
        flakes[n] = me.create_oval(xPos[n],yPos[n],xPos[n]+sizes[n],yPos[n]+sizes[n], fill=colors[colorChoice[n]], outline=colors[colorChoice[n]])

        #Update this flake's internal clock
        t[n] = t[n] + 1

        if yPos[n] >= groundLevel:
            # As soon as a flake hits the ground, reset its internal clock to 0, reset its yStart to 0, and change its color
            t[n] = 0
            yStart[n] = 0
            colorChoice[n] = (colorChoice[n] + 1) % 5

    me.update()

    sleep(0.005)

    #Delete all flakes before going on to the next frame
    for n in range(0, numFlakes):

        if yPos[n] < groundLevel: #DON'T delete flakes that have reached the ground.  This creates the accumulation effect.
            me.delete( flakes[n])
