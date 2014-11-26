####################################################################
# Title:  Equation of a Line
# Programmer:  Mr. Schattman
# Last modified:  10/19/2009
# Purpose: This program takes as input the x and y coordinates of 2 points
#           and determines the equation of the line between those points
#           in slope-intercept form
#####################################################################


#Input coordinates from the user
x1 = input("Enter x1: ")
y1 = input("Enter y1: ")
x2 = input("Enter x2: ")
y2 = input("Enter y2: ")


#Check for horizontal or vertical lines
if x1 == x2 and y == y2:
    print("This is a single point. The line does not exist. Go away.")

elif x1 == x2:
    print("The line is vertical.  Its equation is x = " + str(x1))

elif y1 == y2:
    print("The line is horizontal.  Its equation is y = " + str(y1))


#If not horizontal or vertical, then do all this
else:
    
    #Calculate the slope
    deltaY = float(y2 - y1)
    deltaX = float(x2 - x1)
    m = deltaY / deltaX


    #Format the printing of the x-term based on what the slope is
    if m == 1:
        xTerm = "x"
        
    elif m == -1:
        xTerm = "-x"
        
    else:
        xTerm = str(m) + "x"


    #Calculate the y-intercept
    b = y1 - m * x1


    #Format the printing of the y-intercept
    if b > 0:
        bTerm = "+ " + str(b)
        
    elif b < 0:
        bTerm = str(b)
        
    else:
        bTerm = ""
        
    print("The equation of the line is y = " + xTerm + bTerm)

#END OF PROGRAM
