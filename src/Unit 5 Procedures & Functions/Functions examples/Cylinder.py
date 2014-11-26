from math import *

def cylinderVolume( radius, height ):
      vol = pi*radius**2*height
      return vol


myVol = cylinderVolume( 10, 40 )

print("The volume is " + str( myVol))
