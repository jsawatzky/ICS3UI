from turtle import *

#RETURNS THE SUM OF THE INTERIOR ANGLES OF A REGULAR POLYGON, GIVEN HOW MANY SIDES IT HAS
def getSumOfInteriorAngles( numSides ):
    return 180*(numSides - 2)


#RETURNS THE MEASURE OF A SINGLE INTERIOR ANGLE OF A REGULAR POLYGON, GIVEN HOW MANY SIDES IT HAS
def getInteriorAngle( numSides ):
    angleSum = getSumOfInteriorAngles( numSides )  #in a square, this is 360
    return angleSum/numSides



#DRAWS A REGULAR POLYGON, GIVEN HOW MANY SIDES IT HAS AND THE LENGTH OF ITS SIDES
def drawRegularPolygon( numSides, sideLength, col ):
    width(4)
    color( col )
    
    interiorAngle = getInteriorAngle( numSides )

    for sideCount in range(1, numSides+1):
        forward( sideLength )
        left( 180 - interiorAngle )


#EQUILATERAL TRIANGLE
drawRegularPolygon( 3, 50, "red" )

#PENTAGON
drawRegularPolygon( 5, 80, "blue" )

#DODECAGON
drawRegularPolygon( 12, 100, "green" )

   
