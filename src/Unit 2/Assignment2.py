'''
Created on Sep 15, 2014

@author: Jacob Sawatzky
'''

##Gets the integer version of a string
def getInt(numStr):
    valid = False
    while valid == False:
        try:
            numInt = int(numStr)
            valid = True
        except ValueError:
            try:
                numFloat = float(numStr)
                numStr = input("You must enter an integer value! (No decimals) Please try again: ")
            except ValueError:
                numStr = input("You must enter a number! Please try again: ")
    return numInt

##Gets the float version of a string
def getNum(numStr):
    valid = False
    while valid == False:
        try:
            num = float(numStr)
            valid = True
        except ValueError:
            numStr = input("You must enter a number! Please try again: ")
    return num

again = True
while again == True: 
    ##Asks which part the user wants to do
    print("Assignment 2:")
    print("Part 1: Trinomials")
    print("Part 2: Ordinal Numbers")
    print("Part 3: Quadrilateral")
    part = input("Which part would you like to do? (1/2/3): ")
    while part != "1" and part != "2" and part != "3":
        part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
        
    if part == "1": ##Part 1
        
        squared = u"\u00B2"
        
        a = getNum(input("Please enter the A value: "))
        b = getNum(input("Please enter the B value: "))
        c = getNum(input("Please enter the C value: "))
        
        if a % 1 == 0:
            a = int(a)
        if b % 1 == 0:
            b = int(b)
        if c % 1 == 0:
            c = int(c)
        
        exp = "The formated expression is: "
        
        ##Gets the A part
        if a == -1:
            exp += "-x" + squared
        elif a == 1:
            exp += "x" + squared
        elif a < -1 or a > 1:
            exp += str(a) + "x" + squared
        else:
            pass
        ##Gets the B part
        if b == -1:
            exp += "-x"
        elif b == 1:
            exp += "+x"
        elif b < -1:
            exp += str(b) + "x"
        elif b > 1:
            exp += "+" + str(b) + "x"
        else:
            pass
        ##Gets the C part
        if c < -1:
            exp += str(c)
        elif c > 1:
            exp += "+" + str(c)
        else:
            pass
        
        print(exp)
    
    elif part == "2": ##Part 2
        
        numInt = getInt(input("Please enter a number: "))
        while numInt < 1 or numInt > 100:
            numInt = getInt(input("Invalid! Please enter a number in between 1 and 100: "))
        num = str(numInt)
                
        numChar = len(num)
        lastChar = num[numChar - 1]
           
        if lastChar == "1":
            if num[numChar - 2] != "1":
                ending = "st"
        elif lastChar == "2":
            if num[numChar - 2] != "1":
                ending = "nd"
        elif lastChar == "3":
            if num[numChar - 2] != "1":
                ending = "rd"
        else:
            ending = "th"
            
        print(num + ending)
        
    else: ##Part 3
        
        points = {'A': 0, 'B': 0, 'C'}
        
        for i in ("A", "B", "C", "D"):
            x = getNum(input("Please enter the x for point " + i + ": "))
            y = getNum(input("Please enter the y for point " + i + ": "))
            points[i] = {}
    
    ##Asks if user wants do do another one
    again = input("Would you like to do another? (y/n): ")
    while again != "y" and again != "n":
        again = input("Invalid! Please enter a y or an n: ")
    if again == "y":
        again = True
    else:
        again = False