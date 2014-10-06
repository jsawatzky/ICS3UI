'''
Created on Sep 29, 2014

@author: Jacob
'''
from utilities import *

#Gets the dollar amount to calculate for
dollar = round(getNum(input("Please enter a dollar amount: $"), "$"), 2)

while dollar < 0:
    dollar = round(getNum(input("You cannot enter a negative dollar amount! Please try again: $"), "$"), 2)

#Prints the correctly formatted statement
if str(dollar)[len(str(dollar))-2] == ".":
     print("To get $" + str(dollar) + "0 in cash you need:")
else:
     print("To get $" + str(dollar) + " in cash you need:")
    
#Creates a dictionary of each type of bill or coin and its value
types = {100: "$100 bill", 50: "$50 bill", 20: "$20 bill", 10: "$10 bill", 5: "$5 bill", 2: "toonie", 1: "loonie", 0.25: "quarter", 0.1: "dime", 0.05: "nickel"}
#Runs once for each type of bill or coin
for amount in [100, 50, 20, 10, 5, 2, 1, 0.25, 0.1, 0.05]:
    num = 0
    while dollar - amount >= 0:
        num += 1
        dollar -= amount
    if amount == 0.05 and 0.02 < dollar < 0.05:
        num += 1
        dollar = 0
    if num > 0:
        #Prints the number of the type of bill or coin if its more than 0
        message = "    - " + str(num) + " " + types[amount]
        if num > 1:
            message += "s"
        print(message)
        
#Prints how many cents are left over due to pennies being removed
if dollar > 0:
    print("This is " + str(int(round(dollar*100, 0))) + " cents short but pennies don't exist anymore!")