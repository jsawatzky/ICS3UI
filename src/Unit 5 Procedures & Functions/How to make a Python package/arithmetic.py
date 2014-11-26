#A PACKAGE OF HANDY MATH FUNCTIONS I WROTE FOR USE IN OTHER PROGRAMS


#RETURNS TRUE IF X IS EVEN
def isEven( x ):
    if x % 2 == 0:
        return True
    else:
        return False


#RETURNS THE DISTANCE BETWEEN THE POINTS (x1, y1) AND (x2, y2)
def distance(x1, y1, x2, y2):
    d = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
    return d


#RETURNS THE GCD OF a AND b
def gcd( a, b ):
    if a >= b:
        MAX = a
        MIN = b
    else:
        MAX = b
        MIN = a

    REM = MAX % MIN

    while REM != 0:
        MAX = MIN
        MIN = REM
        REM = MAX % MIN

    return MIN



