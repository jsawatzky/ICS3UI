'''
Created on Feb 25, 2014

@author: JONATHAN SCHUMACHER
'''

#====================================================
#                Imports
#====================================================
from math import *

#====================================================
#                Variables
#====================================================
shape = ""

x1 = float(input("Please input a value for X1:\n"))
y1 = float(input("Please input a value for Y1:\n"))
x2 = float(input("Please input a value for X2:\n"))
y2 = float(input("Please input a value for Y2:\n"))
x3 = float(input("Please input a value for X3:\n"))
y3 = float(input("Please input a value for Y3:\n"))
x4 = float(input("Please input a value for X4:\n"))
y4 = float(input("Please input a value for Y4:\n"))

slope1 = None
slope2 = None
slope3 = None
slope4 = None

length1 = sqrt((x2 - x1)**2)+((y2 - y1)**2)
length2 = sqrt((x3 - x2)**2)+((y3 - y2)**2)
length3 = sqrt((x4 - x3)**2)+((y4 - y3)**2)
length4 = sqrt((x1 - x4)**2)+((y1 - y4)**2)

#====================================================
#    Special cases for Zero and Undefined slopes
#====================================================
if y2 - y1 == 0:
      slope1 = "undefined"
elif x2 - x1 == 0:
      slope1 = "zero"
else:
    slope1 = (y2 - y1)/(x2 - x1)

if y3 - y2 == 0:
      slope2 = "undefined"
elif x3 - x2 == 0:
      slope2 = "zero"
else:
    slope2 = (y3 - y2)/(x3 - x2)

if y4 - y3 == 0:
      slope3 = "undefined"
elif x4 - x3 == 0:
      slope3 = "zero"
else:
    slope3 = (y4 - y3)/(x4 - x3)

if y1 - y4 == 0:
      slope4 = "undefined"
elif x1 - x4 == 0:
      slope4 = "zero"
else:
    slope4 = (y1 - y4)/(x1 - x4)

#=========================================================================================================
#                                                Logic
#=========================================================================================================     
if (slope1 == slope3 and slope2 == slope4):      

    if (slope1 == "undefined" and slope2 == "zero") and (slope3 == "undefined" and slope4 == "zero"):     
        if length1 == length3 and length2 == length4:       
            if length1 == length2 == length3 == length4:        
                shape = "Square"
            else:
                shape = "Rectangle"

    elif (slope1 == "zero" and slope2 == "undefined") and (slope3 == "zero" and slope4 == "undefined"):     
        if length1 == length3 and length2 == length4:       
            if length1 == length2 == length3 == length4:        
                shape = "Square"
            else:
                shape = "Rectangle"
    
    elif ((((float(slope1))**-1)*-1) == float(slope2)) and ((((float(slope3))**-1)*-1) == float(slope4)):     
        if length1 == length3 and length2 == length4:       
            if length1 == length2 == length3 == length4:        
                shape = "Square"
            else:
                shape = "Rectangle"           

    elif length1 == length3 and length2 == length4:
        if length1 == length2 == length3 == length4:      
            shape = "Rhombus"
        else:    
            shape = "Parallelogram"
        
elif (slope1 == slope3 and slope2 != slope4):
    shape = "Trapezoid"

elif (slope1 != slope3 and slope2 == slope4):
    shape = "Trapezoid"
    
elif (slope1 != slope3 and slope2 != slope4):
    if length1 == length2 and length3 == length4:
        shape = "Kite"
    
    else:
        shape = "Quadrilateral"
     
#====================================================
#                    Output
#====================================================
print("The Shape is a:\n" +shape)