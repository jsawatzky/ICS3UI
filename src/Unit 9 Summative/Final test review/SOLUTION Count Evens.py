def countEvens( someArray ):
    numEvens = 0
    for i in range(0,len(someArray)):
        
        if someArray[i] % 2 == 0:
            numEvens = numEvens + 1

    return numEvens


myDieRolls = [ 4, 11, 7, 8, 12, 6, 5, 9]
print( countEvens( myDieRolls ))  
