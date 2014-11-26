##############
# Title:  Tornado Animation
# Purpose:  Illustrate useful techniques for drawing and changing animations
# Programmer:  Mr. Schattman
# Last modified:  May 5, 2010
################

#Import Python functions
from tkinter import *
from math import *
from time import *
from random import *

#Set up the drawing canvas
myInterface = Tk()
me = Canvas(myInterface, width=600, height=600, background="#999fff")
me.pack()

#Animation settings.  Experiment with these values to make the scene appear differently each time you run it
numFrames = 570
maxTornadoWidth = 300
slimFactor = 0.4
wiggleFactor = 60
tornadoSpeed = 2
numWiggles = 6
wiggleSpeed = 2 * 3.14159 * numWiggles / numFrames
groundLevel = 300
dustWidth = 30
dustHeight = 20
numClouds = 10
houseX1 = 300
houseY1 = groundLevel - 80
houseWidth = 200
houseHeight = 100

#Placing the roof relative to the house
roofX1 = houseX1
roofY1 = houseY1
roofX2 = houseX1 + houseWidth/2
roofY2 = houseY1 - 50
roofX3 = houseX1 + houseWidth
roofY3 = roofY1
wallX1 = houseX1 - 40
wallX2 = houseX1 + houseWidth - 40
wallX3 = wallX2 + 40
wallX4 = wallX1 + 40
wallY1 = roofY1
wallY2 = wallY1
wallY3 = houseY1 + houseHeight
wallY4 = wallY3
                    

#How quickly the tornado narrows from top to bottom
widthA = maxTornadoWidth
widthC = slimFactor * widthA
widthE = slimFactor * widthC
widthG = slimFactor * widthE
widthI = slimFactor * widthG

#y-values on the tornado polygon
Ay = 0
By = Ay

Cy = 0.33 * groundLevel
Dy = Cy

Ey = 0.6 * groundLevel 
Fy = Ey

Gy = 0.8 * groundLevel
Hy = Gy

Iy = groundLevel
Jy = Iy


#Draw the grass and house
grass = me.create_rectangle(0, groundLevel-50, 600, 600, fill = "green")
house = me.create_rectangle(houseX1, houseY1, houseX1 + houseWidth, houseY1 + houseHeight, fill = "red", outline = "black", width = 2)
roof = me.create_polygon(roofX1, roofY1, roofX2, roofY2, roofX3, roofY3,  fill="purple", outline = "black", width = 2)

#Draw the clouds
for cloud in range( 0, numClouds ):
    cloudX = cloud * 600 / numClouds
    me.create_oval( cloudX, -50, cloudX + 100, 60, fill="#555555", outline="#555555")
    me.update()


##################################
#MAIN LOOP: Animate the tornado
##################################

for frame in range(0, numFrames):

    #Move the top of the tornado 
    xFunnel = tornadoSpeed * frame
    
    Ax = xFunnel - widthA
    Bx = Ax + 2*widthA
    
    Cx = xFunnel - widthC
    Dx = Cx + 2*widthC

    #Use the sine function from trigonometry to model the wiggling of the tornado's midsection
    middleMovement1 = wiggleFactor * sin( wiggleSpeed * frame )
    middleMovement2 = wiggleFactor * cos( wiggleSpeed * frame )

    Ex = xFunnel - widthE + middleMovement1
    Fx = Ex + 2*widthE

    Gx = xFunnel - widthG + middleMovement2
    Hx = Gx + 2*widthG

    Ix = xFunnel - widthI
    Jx = Ix + 2*widthI

    #The coordinates of the base of the tornado
    xBase = (Ix+Jx)/2
    yBase = groundLevel

                    
    #Draw "damage lines" on the ground
    for damageLine in range(0,10):
        xEnd = xBase + randint(-dustWidth,dustWidth)
        yEnd = yBase - randint(-dustHeight,dustHeight)
        me.create_line(xBase,yBase,xEnd, yEnd, fill="blue")

    #################
    #DRAW THE TORNADO as a smoothed polygon
    #################
    tornado = me.create_polygon(Ax,Ay,Cx,Cy,Ex,Ey,Gx,Gy,Ix,Iy,Jx,Jy,Hx,Hy,Fx,Fy,Dx,Dy,Bx,By,fill="grey",smooth=True)

    #Draw a cloud bulge to cover the top of the tornado so that the top looks like it's inside the clouds
    cloudBulge = me.create_oval(Ax-50,0,Bx+50,70, fill="#555555", outline="#555555")


    #Destroy the house when the tornado comes close to it
    if xFunnel >= houseX1-40 and xFunnel <= houseX1 + houseWidth/2:

        me.delete( roof )
        me.delete( house )

        #Make the roof fly off to the northeast
        roofX1 = roofX1 + 15
        roofY1 = roofY1 - 13
        roofX2 = roofX2 + 15
        roofY2 = roofY2 - 13
        roofX3 = roofX3 + 15
        roofY3 = roofY3 - 13

        #Make the front wall fly off to the southwest
        wallX1 = wallX1 - 12
        wallY1 = wallY1 + 15
        
        wallX2 = wallX2 - 12
        wallY2 = wallY2 + 15
        
        wallX3 = wallX3 - 12
        wallY3 = wallY3 + 15

        wallX4 = wallX4 - 12
        wallY4 = wallY4 + 15

        house = me.create_polygon(wallX1, wallY1, wallX2, wallY2, wallX3, wallY3, wallX4, wallY4, fill = "red", outline="black", width = 2)
        roof = me.create_polygon(roofX1, roofY1, roofX2, roofY2, roofX3, roofY3,  fill="purple", width = 2)

        me.update()
        sleep(0.02)


    #Delete the previous frame
    me.update()
    sleep(0.02)
    me.delete( tornado, cloudBulge)
    


