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
size = [ 60, 60, 60, 60, 60, 200]
x = [200, 300, 100, 50, 400, 450]
y = [300, 300, 400, 425, 560, 300]
xSpeed = [-5, -6, 2, -10, -8, 5]
ySpeed = [-4, -5, -5, -3, -3, 0]
box = [0,0,0,0,0,0]
colors = ["blue","green","yellow","white","black","red"]


####
#DRAW BACKGROUND SCENERY HERE
#...
####


######################################
#ANIMATE 6 BOXES ON TOP OF THE BACKGROUND
######################################

for frameCount in range( 1, numFrames + 1 ):

      #UPDATE THE POSITIONS OF THE BOXES, THEN DRAW THEM
     for i in range(0,6):
          x[i] = x[i] + xSpeed[i]
          y[i] = y[i] + ySpeed[i]

          box[i] = screen.create_rectangle( x[i], y[i], x[i]+size[i], y[i]+size[i], fill=colors[i])


     screen.update() #why isn’t this in the nested loop?
     sleep(0.05)     #why isn’t this in the nested loop?

      #DELETE ALL OBJECTS IN THE CLUSTER
     for i in range(0,6):
          screen.delete( box[i] )
