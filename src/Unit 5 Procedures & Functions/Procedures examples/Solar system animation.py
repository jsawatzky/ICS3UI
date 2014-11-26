
################################################################################
# PURPOSE:  THIS PROGRAM ANIMATES OUR SOLAR SYSTEM USING PROCEDURES & FUNCTIONS
# PROGRAMMER:  IAN FOX
# DATE:  NOVEMBER 2013
###############################################################################

from tkinter import *
from random import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=900,height=900,background="black")
screen.pack()


#CONVERTS AN ANGLE IN DEGREES TO AN ANGLE IN RADIANS.  NEEDED BECAUSE sin() AND cos() IN PYTHON TAKE RADIAN ANGLES
def toRadians( degreeAngle ):
    return pi * degreeAngle / 180


#DRAWS A STARRY BACKGROUND
def drawStars( numStars ):
    for i in range(0,numStars):
        x = randint(0,900)
        y = randint(0,900)
        size = randint(1,3)
        screen.create_oval(x,y, x+size, y+size, fill="white")
        screen.update()


#DRAWS THE SUN GIVEN ITS CENTRE AND RADIUS
def drawSun( xCentre, yCentre, sunRadius ):
    sunx1 = xCentre - sunRadius
    suny1 = yCentre - sunRadius
    sunx2 = xCentre + sunRadius
    suny2 = yCentre + sunRadius

    screen.create_oval(sunx1, suny1, sunx2, suny2, fill = "yellow" ) #we don't need to return this value because the sun won't ever be deleted


#DRAWS A PLANET GIVEN THE CENTRE OF ITS ORBIT, ITS ANGLE ALONG THAT ORBIT, ITS RADIUS AND COLOUR.
def drawPlanet( xSunCentre, ySunCentre, angle, orbitalRadius, planetRadius, color ):

    xPlanetCentre = xSunCentre + orbitalRadius * cos(angle)
    yPlanetCentre = ySunCentre - orbitalRadius * sin(angle)
        
    x1 = xPlanetCentre - planetRadius
    y1 = yPlanetCentre - planetRadius
    x2 = xPlanetCentre + planetRadius
    y2 = yPlanetCentre + planetRadius
        
    return screen.create_oval(x1, y1, x2, y2, fill = color ) #We have to return this graphic, because it has to be deleted and redrawn in the loop


#RUNS THE ANIMATION USING THE ABOVE PROCEDURES AND FUNCTIONS
def animateSolarSystem( ):

    orbitalRadii = [100, 150, 200, 300, 400]
    planetaryRadii = [8, 8, 9, 7 , 30 ]
    startingAngles = [0, 45, 90, 180, 20]
    orbitingSpeeds = [3, 2, 5, 1, -4]
    colors = ["white", "orange", "blue", "red", "orange"]
    planetGraphic = [0,0,0,0,0]

    numPlanets = len(colors)
    
    drawStars( 200 )
    drawSun( 450, 450, 50 )

    frameCount = 0

    #keep the animation going forever instead of for a fixed number of frames
    while True:
        
        #draw all the planets for the current frame
        for i in range(0,numPlanets): 
            degreeAngle = startingAngles[i] + frameCount * orbitingSpeeds[i]
            radianAngle = toRadians( degreeAngle ) 
            planetGraphic[i] = drawPlanet(450, 450, radianAngle, orbitalRadii[i], planetaryRadii[i], colors[i] )

        #update the screen and sleep after all the planets have been drawn  
        screen.update()  
        sleep(0.01)

        #Delete all the planets
        for i in range(0,numPlanets):
            screen.delete( planetGraphic[i] )
            
        #We have to increase the frameCount manually because we're not using a for-loop
        frameCount = frameCount + 1


#CALLS THE PROCEDURE
animateSolarSystem()


        





        
