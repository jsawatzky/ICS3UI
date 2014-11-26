from math import *

a = int(input("Enter a positive integer: "))
b = int(input("Enter another positive integer: "))

MAX = max(a,b)
MIN = min(a,b)
remainder = MAX % MIN

while remainder != 0:
    MAX = MIN
    MIN = remainder
    remainder = MAX % MIN

gcd = MIN

print ("The GCD of " + str(a) + " and " + str(b) + " is " + str(gcd))
