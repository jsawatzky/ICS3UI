def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0


def NAND(a,b):
    if AND(a,b) == 1:
        return 0
    else:
        return 1


def OR(a,b):
#WRITE THIS
    return ""


def NOR(a,b):
#WRITE THIS
    return ""


def XOR(a,b):
#WRITE THIS
    return ""


def halfAdder( a, b ):
    sumBit = "" #provide formula
    carryBit = "" #provide formula
    return "" #provide the array to be returned


def fullAdder( a, b, c0 ):
    #We'll do this one together in the next lesson
    return "" 

print( "AND" )
print( AND(0,0) )
print( AND(0,1) )
print( AND(1,0) )
print( AND(1,1) )

print( "NAND" )
print( NAND(0,0) )
print( NAND(0,1) )
print( NAND(1,0) )
print( NAND(1,1) )

print( "OR" )

print( "NOR" )

print( "XOR" )
