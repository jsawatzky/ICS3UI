#FULL SOLUTION OF THE NUMBER SPELLER THAT HAS 1 BUG:  IT SPELLS "200,000,000,000" AS "TWO HUNDRED BILLION MILLION THOUSAND"
#CHALLENGE: FIX THE BUG

from math import *

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



#TAKES A 2-DIGIT NUMBER AND RETURNS THE ENGLISH SPELLING OF THAT NUMBER.
#MAKES USE OF THE FUNCTIONS tensSpeller AND spellTeens ABOVE.
def twoDigitSpeller( twoDigitNumber ):
    
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

        elif d1 == "0" and d2 == "0": #"00"
            return ""

        elif d1 == "0": #01-09
            return onesSpeller( d2 )

        elif d2 == "0": #20, 30, 40, etc.
            return tensSpeller( d1 )
        
        else:  #21-99 
            spelling = tensSpeller( d1 ) + " " + onesSpeller( d2 )
            return spelling




#TAKES A 3-DIGIT NUMBER AND RETURNS THE ENGLISH SPELLING OF THAT NUMBER
#MAKES USE OF THE FUNCTIONS spellOnes AND spellTwoDigits ABOVE.
def threeDigitSpeller( threeDigitNumber ):
    length = len(threeDigitNumber)
    
    if length != 3:
        return "Error in spell three digits - received " + threeDigitNumber
    
    else:
        hundredsDigit = threeDigitNumber[0]
        lastTwoDigits = threeDigitNumber[1:3]

        if hundredsDigit == "0":
            return twoDigitSpeller( lastTwoDigits )
        
        else:
            hundredsWords = onesSpeller( hundredsDigit )
            
        twoDigitWords = twoDigitSpeller( lastTwoDigits )

        return hundredsWords + " hundred " + twoDigitWords



def speller( num ):
    endings = ["THOUSAND", "MILLION", "BILLION", "TRILLION", "QUADRILLION", "QUINTILLION", "SEXTILLION", "SEPTILLION", "OCTILLION",
               "NONILLION", "DECTILLION"]

    L = len(num)

    if L <= 3:
        return spellThreeDigits( num )

    if L > 36: #num is bigger than 999 dectillion
        return "NUMBER TOO LARGE"

    else:
        numBlocks = round( L/3 + 0.5 )
        
        endingsIndex = numBlocks - 2

        numLeadingDigits = L % 3

        spelling = ""
        
        if numLeadingDigits == 1:   #example: 3,444,555
            spelling = onesSpeller( num[0] ) + " " + endings[ endingsIndex ]
            endingsIndex = endingsIndex - 1
            numBlocks = numBlocks - 1
            iStart = 1
            
        elif numLeadingDigits == 2: #example: 33,444,555
            spelling = twoDigitSpeller( num[0:2] ) + " " + endings[ endingsIndex ]
            endingsIndex = endingsIndex - 1
            numBlocks = numBlocks - 1
            iStart = 2

        else:                       #example: 333,444,555
            spelling = ""
            iStart = 0
            
        #Spells each 3-digit block and tacks the spelling onto the 
        for b in range(1, numBlocks+1 ):
            
            currentBlock = num[ iStart : iStart+3 ]

            if b < numBlocks:  #all blocks except the last one get a suffix
                spelling = spelling + " " + threeDigitSpeller( currentBlock ) + " " + endings[ endingsIndex ]

            else:  #the last block does not get a suffix
                spelling = spelling + " " + threeDigitSpeller( currentBlock )
                
            endingsIndex = endingsIndex - 1
            
            iStart = iStart + 3
            
        return spelling

    

    
#############
#TEST CASES
#############

numbersToTry_A = [ "1", "6", "9", "0" ]

for num in numbersToTry_A :
    print(str(num) + ": " + onesSpeller( num ))



numbersToTry_B = [ "26", "15", "99", "76", "70", "11", "08", "00" ]

for num in numbersToTry_B :
    print(str(num) + ": " + twoDigitSpeller( num ))



numbersToTry_C = [ "194", "310", "909", "500", "819", "067", "007" ]

for num in numbersToTry_C :
    print(str(num) + ": " + threeDigitSpeller( num ))


numbersToTry_D = [ "1940", "12310", "503909", "1503909", "200000000000", "200000300000"]

for num in numbersToTry_D :
    print(str(num) + ": " + speller( num ))



    

    


