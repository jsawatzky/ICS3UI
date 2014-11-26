def evenOrOdd( x ):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


for i in range(0,21):
    print( str(i) + " is " + evenOrOdd( i ) )
