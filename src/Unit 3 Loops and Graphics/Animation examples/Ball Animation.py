########################################
# Title: Animation Examples
# Purpose: To show how to separate your animation parameters from the for-loop
#           so that it's easier to change the appearance of the movie
# Programmer:  Mr. Schattman
# Last modified:  May 6, 2014
########################################

from tkinter import *
from time import *
from math import *

tk = Tk()
me = Canvas(tk, width=800,height=800, background="yellow")
me.pack()

redStartX = 600
redStartY = 400
blueStartX = 0
blueStartY = 100

redSpeedX = -8
redSpeedY = -20
blueSpeedX = 5
blueSpeedY = 5

redWidth = 120
blueWidth = 20

for frameCount in range(0,200): #200 frames in the animation
    
    #Calculate the position of the RED ball
    x1red = redSpeedX * frameCount + redStartX
    y1red = .5*frameCount**2 + redSpeedY * frameCount + redStartY
    
    x2red = x1red + redWidth
    y2red = y1red + redWidth


    #Calculate the position of the BLUE ball    
    x1blue = blueSpeedX * frameCount + blueStartX
    y1blue = blueSpeedY * frameCount + blueStartY
    
    x2blue = x1blue + blueWidth
    y2blue = y1blue + blueWidth
    
    #Create the objects 
    blueBall = me.create_oval( x1blue, y1blue, x2blue, y2blue, fill="blue", outline="black")
    redBall = me.create_oval(  x1red,  y1red,  x2red,  y2red,  fill="red",  outline="black") 

    #Draw the balls in their current position
    me.update()

    #Slow down the camera so the human eye can see it.
    sleep(0.05)

    #Delete old object
    me.delete(redBall, blueBall)

