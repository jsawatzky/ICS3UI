#TAKES A 1-DIGIT NUMBER (REPRESENTED AS A STRING) AS A PARAMETER AND RETURNS THE ENGLISH SPELLING OF THAT NUMBER
def onesSpeller( d ):
    if d == "0":
        return "zero"
    
    elif d == "1":
        return "one"
    
    elif d == "2":
        return "two"
    
    elif d == "3":
        return "three"
    
    elif d == "4":
        return "four"
    
    elif d == "5":
        return "five"
    
    elif d == "6":
        return "six"
    
    elif d == "7":
        return "seven"
    
    elif d == "8":
        return "eight"
    
    elif d == "9":
        return "nine"
    
    else:
        return "Error in onesSpeller - received " + d


#TAKES THE TENS DIGIT OF A NUMBER (REPRESENTED AS A STRING) AS A PARAMETER AND RETURNS THE ENGLISH SPELLING OF THE TENS PLACE FOR THAT DIGIT
def tensSpeller( d ):
    if d == "0":
        return ""
    
    if d == "2":
        return "twenty"
    
    elif d == "3":
        return "thirty"
    
    elif d == "4":
        return "forty"
    
    elif d == "5":
        return "fifty"
    
    elif d == "6":
        return "sixty"
    
    elif d == "7":
        return "seventy"
    
    elif d == "8":
        return "eighty"
    
    elif d == "9":
        return "ninety"
    
    else:
        return "Error in tensSpeller - received " + d



#TAKES A 2-DIGIT NUMBER (REPRESENTED AS A STRING) AS A PARAMETER AND RETURNS THE ENGLISH SPELLING OF THAT NUMBER.
#MAKES USE OF THE FUNCTIONS tensSpeller AND spellTeens ABOVE.
def spellTwoDigits( twoDigitNumber ):
    
    numDigits = len(twoDigitNumber)
    
    if numDigits != 2:
        return "Error in spellTwoDigits - received " + twoDigitNumber
    
    else:
        d1 = twoDigitNumber[0] #tens digit
        d2 = twoDigitNumber[1] #ones digit

        if d1 == "1": #11-19
            
            if d2 == "0":
                return "ten"
            elif d2 == "1":
                return "eleven"
            elif d2 == "2":
                return "twelve"
            elif d2 == "3":
                return "thirteen"
            elif d2 == "4":
                return "fourteen"
            elif d2 == "5":
                return "fifteen"
            elif d2 == "6":
                return "sixteen"
            elif d2 == "7":
                return "seventeen"
            elif d2 == "8":
                return "eighteen"
            elif d2 == "9":
                return "nineteen"
        
        else:  #20-99
            spelling = tensSpeller( d1 ) + " " + onesSpeller( d2 )
            return spelling



#TAKES A 3-DIGIT NUMBER AS A PARAMETER AND RETURNS THE ENGLISH SPELLING OF THAT NUMBER.
#MAKES USE OF THE FUNCTIONS onesSpeller AND spellTwoDigits ABOVE.
def spellThreeDigits( threeDigitNumber ):
    
    numDigits = len( threeDigitNumber )
    
    #YOU FILL THIS IN

    return "This program can't yet spell " + threeDigitNumber   #GIVE THIS RETURN STATEMENT THE RIGHT VALUE



#############
#TEST CASES
#############

numbersToTry_A = [ "1", "6", "9", "0" ]

for num in numbersToTry_A :
    print(str(num) + ": " + onesSpeller( num ))



numbersToTry_B = [ "26", "15", "99", "08", "76", "70", "11" ]

for num in numbersToTry_B :
    print(str(num) + ": " + spellTwoDigits( num ))



numbersToTry_C = [ "194", "310", "909", "500", "819" ]

for num in numbersToTry_C :
    print(str(num) + ": " + spellThreeDigits( num ))




    


