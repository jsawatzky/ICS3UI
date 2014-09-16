'''
Created on Sep 15, 2014

@author: Jacob Sawatzky
'''

part = input("Which part would you like to do? (1/2/3): ")
while part != "1" and part != "2" and part != "3":
    part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
    
if part == "1":
    
    num = getInt(input("Please enter a number between 1 and 100: "))
    while 1 > num < 101:
        num = getInt(input("You must enter a number in between 1 and 100! Please try again: "))
            
    numChar = len(num)
    lastChar = num[numChar - 1]
       
    if lastChar == "1":
        if num != "11":
            ending = "st"
    elif lastChar == "2":
        if num != "12":
            ending = "nd"
    elif lastChar == "3":
        if num != "13":
            ending = "rd"
    else:
        ending = "th"
        
    print(num + ending)

elif part == "2":
    
    squared = u"\u00B2"
    
    a = getInt(input("Please enter the A value: "))
    b = getInt(input("Please enter the B value: "))
    c = getInt(input("Please enter the C value: "))
    
    exp = ""
    
    if a == -1:
        exp += "-"
    elif a == 1:
        exp += "x" + squared
    elif a < -1 or a > 1:
        exp += str(a) + "x" + squared
    else:
        pass
    if b == -1:
        exp += "-"
    elif b == 1:
        exp += "x"
    elif b < -1:
        exp += str(b) + "x"
    elif b > 1:
        exp += "+" + str(b) + "x"
    else:
        pass
    if b < -1:
        exp += str(b)
    elif b > 1:
        exp += "+" + str(b)
    else:
        pass
    
    print(exp)
    
else:
    
    pass

##Gets the integer version of a string
def getInt(numStr):
    valid = False
    while valid == False:
        try:
            numInt = int(numStr)
            valid = True
        except ValueError:
            try:
                numFloat = float(num)
                numStr = input("You must enter an integer value! (No decimals) Please try again: ")
            except ValueError:
                numStr = input("You must enter a number! Please try again: ")
    return numInt