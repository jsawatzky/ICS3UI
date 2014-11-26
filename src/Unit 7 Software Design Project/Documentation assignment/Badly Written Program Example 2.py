x1 = input("Enter x1: ")
y1 = input("Enter y1: ")
x2 = input("Enter x2: ")
y2 = input("Enter y2: ")
if x1 == x2 and y == y2:
    print("This is a single point. The line does not exist. Go away.")
elif x1 == x2:
    print("The line is vertical.  Its equation is x = " + str(x1))
elif y1 == y2:
    print("The line is horizontal.  Its equation is y = " + str(y1))
else:
    deltaY = float(y2 - y1)
    deltaX = float(x2 - x1)
    m = deltaY / deltaX
    if m == 1:
        xTerm = "x"     
    elif m == -1:
        xTerm = "-x"        
    else:
        xTerm = str(m) + "x"
    b = y1 - m * x1
    if b > 0:
        bTerm = "+ " + str(b)        
    elif b < 0:
        bTerm = str(b)        
    else:
        bTerm = ""        
    print("The equation of the line is y = " + xTerm + bTerm)
