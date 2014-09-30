'''
Created on Sep 29, 2014

@author: Jacob
'''
from utilities import *

dollar = getInt(input("Please enter a dollar amount: $"), "$")

print("To get $" + str(dollar) + " in cash you need:")
for type in [100, 50, 20, 10, 5, 2, 1]:
    num = 0
    while dollar - type >= 0:
        num += 1
        dollar -= type
    if num > 0:
        message = ""
        if type == 2:
            message += "    - " + str(num) + " toonie"
        elif type == 1:
            message += "    - " + str(num) + " loonie"
        else:
            message += "    - " + str(num) + " $" + str(type) + " bill"
        if num > 1:
            message += "s"
        print(message)