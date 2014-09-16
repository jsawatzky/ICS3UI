#TITLE:  Cylinder Volume Calculator
#PROGRAMMER: Mr. Schattman
#DATE LAST MODIFIED: Sept 12, 2014
#PURPOSE: Inputs the height and radius of a cylinder, and the units of
#         measurement.  It outputs the volume of the cylinder in cubic units.


#LOAD MATHEMATICAL FUNCTIONS AND CONSTANTS (SINCE WE'LL BE USING PI BELOW)
from math import *


#WELCOME THE USER TO THE PROGRAM
print("Welcome to my cylinder volume program!")


#INPUT VALUES FROM THE USER
units = input("First tell me what units of distance you're using: ")
radius = float( input("Enter the radius of the cylinder (without the units): ") )
height = float( input("Enter the height of the cylinder (without the units): ") )


#CALCULATE THE VOLUME AND STORE THE ANSWER IN A VARIABLE CALLED "volume"
#A SINGLE * MEANS MULTIPLY.  A DOUBLE ** MEANS EXPONENT
volume = pi * radius**2 * height
volumeRounded = round( volume, 3 )


#OUTPUT THE ANSWER, INCLUDING THE UNITS
print("The volume of the cylinder is " + str( volumeRounded ) + " cubic " + units)



