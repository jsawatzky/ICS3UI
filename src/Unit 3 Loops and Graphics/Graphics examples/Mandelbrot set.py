from tkinter import *

root = Tk()
screen = Canvas(root, width=700, height=700, background = "white" )
screen.pack()


screenSize = 700
setColor = "black"

def add(z,w):
    return [z[0]+w[0],z[1]+w[1]]


def multiply( z, w ):
    return [z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]]


def magnitude(z):
    return z[0]**2 + z[1]**2


def converges(c, z0, iterationLimit):
    z = z0
    i = 0
    
    while magnitude(z) < 4 and i <= iterationLimit:
        
        zSquared = multiply(z, z)
        
        z = add( zSquared, c )

        i = i + 1

    #print (i, c)

    if i >= iterationLimit:
        return True

    else:
        return False


def drawPoint(w, xMin, xMax, yMin, yMax, scaleX, scaleY):

    x = w[0]
    y = w[1]
    
    xPixel = scaleX * (x - xMin)
    yPixel = screenSize - scaleY * (y - yMin)

    screen.create_rectangle(xPixel, yPixel, xPixel+1, yPixel+1, fill=setColor)
    


def drawMandelbrotSet(z0, xMin, xMax, yMin, yMax, numPoints, iterationLimit):

    scaleX = screenSize / (xMax - xMin)
    scaleY = screenSize / (yMax - yMin)

    deltaX = (xMax-xMin)/numPoints
    deltaY = (yMax-yMin)/numPoints

    x = xMin

    for i in range(0,numPoints):
        y = yMin 

        for j in range(0,numPoints):

            c = [x,y]

            if converges(c, z0, iterationLimit):
                drawPoint(c, xMin, xMax, yMin, yMax, scaleX, scaleY)

            y = y + deltaY


        x = x + deltaX
    print ("Done")


def drawJuliaSet(c, xMin, xMax, yMin, yMax, numPoints, iterationLimit):

    scaleX = screenSize / (xMax - xMin)
    scaleY = screenSize / (yMax - yMin)

    deltaX = (xMax-xMin)/numPoints
    deltaY = (yMax-yMin)/numPoints

    x = xMin

    for i in range(0,numPoints):
        y = yMin 

        for j in range(0,numPoints):

            z0 = [x,y]

            if converges(c, z0, iterationLimit):
                h=1
                #drawPoint(z0, xMin, xMax, yMin, yMax, scaleX, scaleY)

            y = y + deltaY


        x = x + deltaX

    print ("Done")

        
xMin = -1.5
yMin = -1.5
viewRange = 3

drawMandelbrotSet([0,0], xMin, xMin+viewRange, yMin, yMin+viewRange, 400, 50)
#drawJuliaSet([-.74,0.02], xMin, xMin+viewRange, yMin, yMin+viewRange, 400, 100)

