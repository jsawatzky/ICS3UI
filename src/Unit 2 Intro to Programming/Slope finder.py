#TITLE:  Slope Calculator
#PROGRAMMER: Mr. Schattman
#DATE LAST MODIFIED: Sept 12, 2014
#PURPOSE: Inputs two ordered pairs and outputs the slope of the line between them as a decimal.


#WELCOME THE USER TO THE PROGRAM
print("This program will help you find the slope between two points (x1, y1) and (x2, y2) \n")


#INPUT VALUES FROM THE USER
x1 = float( input("Enter x1: ") )  #int means whole number, float means decimal
y1 = float( input("Enter y1: ") )
x2 = float( input("Enter x2: ") )
y2 = float( input("Enter y2: ") )


#CALCULATE THE SLOPE AND STORE THE ANSWER IN A VARIABLE CALLED "m"
if x1 == x2:
    m = "undefined"
    
else:
    m = (y2 - y1) / (x2 - x1)  #NOTICE WE NEED BRACKETS AROUND NUMERATOR AND DENOMINATOR


#OUTPUT THE ANSWER
firstPoint = "(" + str(x1) + ", " + str(y1) + ")"
secondPoint = "(" + str(x2) + ", " + str(y2) + ")"

print( "The slope of the line between " + firstPoint + " and " + secondPoint + " is " + str(m) )



