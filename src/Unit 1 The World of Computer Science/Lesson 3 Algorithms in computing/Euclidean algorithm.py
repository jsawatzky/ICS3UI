from math import *

a = int( input("Enter a positive integer: ") )
b = int( input("Enter another positive integer: ") )
print()

Max = max( a, b )
Min = min( a, b )

rem = Max % Min

while rem != 0:
    Max = Min
    Min = rem
    rem = Max % Min

GCD = Min

print ("The GCD of", a, "and", b, "is", GCD)
