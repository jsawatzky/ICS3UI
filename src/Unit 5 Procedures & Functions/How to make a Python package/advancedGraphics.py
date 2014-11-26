from random import *


def drawCircle(xCentre, yCentre, r, someScreen):
    someScreen.create_oval(xCentre-r, yCentre-r, xCentre+r, yCentre+r)


def drawStarCluster( starColor, numStars, someScreen ):
    for i in range(0, numStars):
        x = randint(0,600)
        y = randint(0,600)
        size = randint(1,5)
        someScreen.create_oval(x, y, x+size, y+size, fill= starColor)
        someScreen.update()
