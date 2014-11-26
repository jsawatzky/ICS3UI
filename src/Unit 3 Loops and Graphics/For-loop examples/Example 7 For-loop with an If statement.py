#What is the if-statement inside the for-loop doing?

for myCounter in range( 1, 9 ):

    if myCounter == 1:
        ending = "st"
        
    elif myCounter == 2:
        ending = "nd"
        
    elif myCounter == 3:
        ending = "rd"
        
    else:
        ending = "th"


    descriptor = str( myCounter ) + ending
    
    print( "Hello for the " + descriptor + " time today." )
    

