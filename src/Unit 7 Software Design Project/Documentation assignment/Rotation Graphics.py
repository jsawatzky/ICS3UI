#DOCUMENT THIS PROGRAM AS WELL AS YOU CAN.
#DON'T WORRY TOO MUCH ABOUT THE MATH BEHIND THE FORMULAS.
#JUST DESCRIBE THE BASIC IDEAS

from Tkinter import *
from time import *
from math import *
from random import *

master = Tk()
screen = Canvas( master, width = 1000, height = 1000, background = "black")
screen.pack()

def rotatePoint( point, centre, thetaDegrees):
    deltaX = point[0] - centre[0]
    deltaY = point[1] - centre[1]
    
    thetaRadians = radians( thetaDegrees )
    
    s = -sin(thetaRadians)
    c = cos(thetaRadians)
    
    newDeltaX = c*deltaX - s*deltaY
    newDeltaY = s*deltaX + c*deltaY
    
    newX = centre[0] + newDeltaX
    newY = centre[1] + newDeltaY
    
    return [newX, newY]


def getCentre( polygon ):
    xSum = 0
    ySum = 0
    n = len(polygon)
    for i in range(0,n):
        xSum += polygon[i][0]
        ySum += polygon[i][1]

    return [xSum/n, ySum/n]



def rotatePolygon( polygon, centre, angleDegrees ):

    for i in range(0,len(polygon)):
        polygon[i] = rotatePoint( polygon[i], centre, angleDegrees)

    return polygon


def translatePolygon( polygon, v ):

    for i in range(0,len(polygon)):
        polygon[i] = [polygon[i][0]+v[0], polygon[i][1]+v[1]]

    return polygon


def randomPolygon(maxRadius):
    radius = uniform(-1.2*maxRadius, 1.2*maxRadius)
    theta = uniform(0,2*pi)
    x1 = 400 + radius * cos(theta)
    y1 = 400 + radius * sin(theta)
    x2 = x1 + randint(0, 20)
    y2 = y1 + uniform(-5,5)
    x3 = x2 + uniform(-5,5)
    y3 = y2 + uniform(0,20)
    x4 = x1 + uniform(-5,5)
    y4 = y3 + uniform(-5,5)

    return [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]


def getVelocity( poly, vMax ):

    x1 = poly[0][0]
    y1 = poly[0][1]

    vMin = -2

    if x1 <= 400:
        xVelocity = uniform(-vMax, -vMin )
    else:
        xVelocity = uniform(vMin, vMax )
        
    if y1 <= 400:
        yVelocity = uniform(-vMax, -vMin )
    else:
        yVelocity = uniform(vMin, vMax )

    return [xVelocity,yVelocity]
        



def animateRotatingPolygon( initPolygon, rotationSpeed, velocity, numFrames ):

    poly = initPolygon
    centre = getCentre( poly )
    theta = 0
    
    for frame in range( 0, numFrames ):

        polygonDrawing = screen.create_polygon( poly, fill="white", outline="red")

        poly = translatePolygon( poly, velocity )

        centre = getCentre( poly )
        
        poly = rotatePolygon( poly, centre, rotationSpeed )

        screen.update()
        sleep(0.05)
        screen.delete( polygonDrawing )


def drawPlanet( planetRadius, col ):
    return screen.create_oval(400-planetRadius,400-planetRadius,400+planetRadius,400+planetRadius,fill=col)


def drawStars( numStars ):
    for i in range(0, numStars):
        x = randint(0,1000)
        y = randint(0,1000)
        size = randint(1,3)
        screen.create_oval(x, y, x+size, y+size, fill= "white")
        screen.update()


def animateAsteroidField( numAsteroids, vMax, omega, decayFactor1, decayFactor2, planetRadius, col ):

    drawStars(200)
    planet = drawPlanet( planetRadius, col )
    
    polygons = []
    centres = []
    velocities = []
    rotationSpeeds = []
    polygonDrawings = []

    for i in range(0, numAsteroids ):
        poly = randomPolygon( planetRadius )
        centre = getCentre( poly )
        velocity = getVelocity( poly, vMax )
        rotationSpeed = uniform(-omega, omega)

        polygons.append(poly)
        centres.append( centre )
        velocities.append( velocity )
        rotationSpeeds.append( rotationSpeed )
        polygonDrawings.append( 0 )

    screen.update() 
    sleep(3)
                   
    for frame in range( 0, 300 ):

        if frame == 1:
            screen.delete(planet)
            planet2 = drawPlanet( planetRadius*1.8, "red" )

        if frame == 2:
            screen.delete(planet2)

        for i in range(0, numAsteroids ):
            polygonDrawings[i] = screen.create_polygon( polygons[i], fill=col)

            polygons[i] = translatePolygon( polygons[i], velocities[i] )

            centres[i] = getCentre( polygons[i] )
            
            polygons[i] = rotatePolygon( polygons[i], centres[i], rotationSpeeds[i] )

            velocities[i][0] = decayFactor1 * velocities[i][0]
            velocities[i][1] = decayFactor1 * velocities[i][1]

            rotationSpeeds[i] = decayFactor2 * rotationSpeeds[i]

        screen.update()
        sleep(0.00)

        for i in range(0, numAsteroids ):
            screen.delete( polygonDrawings[i] )


animateAsteroidField( 1000, 50, 30, 0.98, 1.02, 50, "yellow" )       

#animateRotatingPolygon( poly, omega, v, 200)
    
    
