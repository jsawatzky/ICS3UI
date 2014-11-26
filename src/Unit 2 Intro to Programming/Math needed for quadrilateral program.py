from math import *


###SQUARE ROOTS
##x = 144
##L = sqrt(x)
##print("The square root of " + str(x) + " is " + str(L))
##
##a = 3
##b = 4
##hypotenuse = sqrt(a**2 + b**2)
##print("The length of the hypotenuse is " + str(hypotenuse))
##
##x1 = 5
##y1 = 3
##x2 = 10
##y2 = 6
##length = sqrt( (x2-x1)**2 + (y2-y1)**2 )
##print("The length of the line segment is " + str(length))


#TESTING FOR MULTIPLE WAYS TO GET THE SAME RESULT
#gotLitTest = input("Have you passed the Lit Test? ")


####### WAY 1: JOIN ALL THE POSSIBILITIES USING THE WORD or IN ONE LONG IF-CONDITION

##if gotLitTest == "yes" or gotLitTest == "YES" or gotLitTest == "y" or gotLitTest == "Yeah":  
##    print("Can graduate")
##
##else:
##    print("Can't graduate")
##

######### WAY 2: PUT EACH POSSIBILITY IN ITS OWN ELIF-CONDITION, EACH ONE HAVING THE SAME OUTCOME
##    
##if gotLitTest == "yes":
##    print("Can graduate")
##    
##elif gotLitTest == "YES":
##    print("Can graduate")
##    
##elif gotLitTest == "y":
##    print("Can graduate")
##
##else:
##    print("Can't")
##
##

#TESTING FOR PERPENDICULAR SLOPES

slope12 = 5         #in your program, this value will be set by an if-statement using (x1,y1) and (x2,y2)
slope23 =-1/5  #in your program, this value will be set by an if-statement using (x2,y2) and (x3,y3)

if slope12 == 0 and slope23 == "undefined":
    print("Perpendicular")

elif slope12 == "undefined" and slope23 == 0:
    print("Perpendicular")

elif slope12 == "undefined" or slope23 == "undefined" :
    print("Not perpendicular")

elif slope12*slope23 == -1:
    print("Perpendicular")

else:
    print("NOT perpendicular")



