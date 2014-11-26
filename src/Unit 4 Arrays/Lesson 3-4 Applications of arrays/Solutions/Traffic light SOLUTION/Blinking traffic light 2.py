from tkinter import *
from random import *
from time import *


root = Tk()
screen = Canvas( root, width=800, height=800, background = "light green" )
screen.pack()

#SKY
sky = screen.create_rectangle(0, 0, 800, 400, fill = "black", outline="black")


#STARS
for starNum in range(0, 200):
    
    xStar = randint(0, 800)
    yStar = randint(0, 380)
    starSize = randint(1,5)
    
    screen.create_oval(xStar, yStar, xStar+starSize, yStar+starSize, fill="white")


#ROAD   
road = screen.create_polygon(0, 800,  200, 400,  250, 400,  600, 800, fill="grey")
medianStripe = screen.create_polygon( 220, 400,  223, 400,  300, 800, 265, 800, fill="yellow")


#TRAFFIC LIGHT BOX
lamp = screen.create_rectangle(400, 200, 600, 650, fill = "orange")
post = screen.create_rectangle(475, 650, 525, 800, fill = "orange")


#BLINKING LIGHTS ANIMATION
diameter = 100
numFrames = 200

colors = [ "green", "yellow", "red" ]
lightHeights = [ 500, 375, 250 ]

xLights1 = 450
xLights2 = xLights1 + diameter

for i in range(0, numFrames):

    #PAINT 3 BLACK DISKS ALL AT ONCE
    for diskNum in range(0,3):
        
        yLights1 = lightHeights[ diskNum ]
        yLights2 = yLights1 + diameter
        
        screen.create_oval( xLights1, yLights1, xLights2, yLights2, fill ="black")
        screen.update()


    #PAINT THE COLORED LIGHT ON TOP OF ONE OF THOSE BLACK DISKS
    #BOTH THE HEIGHT AND THE COLOR MUST CHANGE WITH EVERY FRAME (i)
        
    screen.create_oval(xLights1, lightHeights[ i % 3 ], xLights2, lightHeights[i%3]+diameter, fill = colors[i % 3])


    screen.update()
    sleep(1)
    
    
    
