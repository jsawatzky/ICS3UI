from math import *

def distance(x1, y1, x2, y2):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

def hasCollisionHappened( d, radius ):
    if d < 2* radius :
        return True
    else:
        return False


myDist = int( distance(200, 350, 100, 200) )

if hasCollisionHappened( myDist, 200 ):
    #make the balls bounce and change direction

