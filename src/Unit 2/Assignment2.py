'''
Created on Sep 15, 2014

@author: Jacob Sawatzky
'''

part = input("Which part would you like to do? (1/2/3): ")
while part != "1" and part != "2" and part != "3":
    part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
    
if part == "1":
    
    num = input("Please enter a number between 1 and 100: ")
    valid = False
    while vaild == False:
        try:
            numInt = int(num)
            if 1 > numInt or numInt > 100:
                num = input("The number must be in between 1 and 100. Please try again: ")
            else:
                vaild = True
        except ValueError:
            num = input("You must enter a number! Please try again: ")
            
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

elif part == "2":
    
    pass
    
else:
    
    pass