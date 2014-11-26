########################################
# Title: Animation Examples
# Purpose: To show how to separate your animation parameters from the for-loop
#           so that it's easier to change the appearance of the movie
# Programmer:  Mr. Schattman
# Last modified:  May 6, 2010
########################################

from tkinter import *
from time import *
from math import *

tk = Tk()
me = Canvas(tk, width=800,height=800, background="yellow")
me.pack()

xStart = 100
yStart = 400
xSpeed = 30
ySpeed = -20

Width = 40
time = 0

for frameCount in range(0,1000): #200 frames in the animation

    #The variable time goes up by 1 in each frame, just like frameCount, except that it gets reset to 0
    #at every collision
    
    time = time + 1
    
    #Calculate the position of the  ball
    x1 = xSpeed * time + xStart
    y1 = ySpeed * time + yStart
    
    x2 = x1 + Width
    y2 = y1 + Width

    if y2 > 800: #if the ball hits the floor
       time = 0
       xStart = x1
       yStart = y1
       ySpeed = -1*ySpeed #reverse the y-speed


    if x1 < 0: #if the ball hits the left wall
       time = 0
       xStart = x1
       yStart = y1
       xSpeed = -1*xSpeed #reverse the x-speed


    if y1 < 0: #if the ball hits the ceiling
       time = 0
       xStart = x1
       yStart = y1
       ySpeed = -1*ySpeed #reverse the y-speed


    if x2 > 800: #if the ball hits the right wall
       time = 0
       xStart = x1
       yStart = y1
       xSpeed = -1*xSpeed #reverse the x-speed
        
    Ball = me.create_oval(  x1,  y1,  x2,  y2,  fill="blue", outline="black")
    
    me.update()
    sleep(0.05)
    me.delete(Ball)

