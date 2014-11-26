######################
#TITLE:  numberSpellingTools.py
#DESCRIPTION:  A package of functions for converting numbers into their English spelling
#PROGRAMMERS:  J. Schattman
#LAST MODIFIED:  11/26/2013
######################


#RETURNS THE SPELLING OF A ONE-DIGIT NUMBER
def spellOneDigitNumber( oneDigitNumber ):
    
    if oneDigitNumber=="1":
        return "one"

    elif oneDigitNumber=="2":
        return "two"

    elif oneDigitNumber=="3":
        return "three"

    elif oneDigitNumber=="4":
        return "four"

    elif oneDigitNumber=="5":
        return "five"

    elif oneDigitNumber=="6":
        return "six"

    elif oneDigitNumber=="7":
        return "seven"

    elif oneDigitNumber=="8":
        return "eight"

    elif oneDigitNumber=="9":
        return "nine"

    else:
        return "Error in SpellOnes - received " + oneDigitNumber


#RETURNS THE SPELLING OF THE TENS DIGIT OF A NUMBER
def spellTensDigit( tensDigit ):
    
    if tensDigit == "0":
        return ""

    elif tensDigit=="2":
        return "twenty"

    elif tensDigit=="3":
        return "thirty"

    elif tensDigit=="4":
        return "forty"

    elif tensDigit=="5":
        return "fifty"

    elif tensDigit=="6":
        return "sixty"

    elif tensDigit=="7":
        return "seventy"

    elif tensDigit=="8":
        return "eighty"

    elif tensDigit=="9":
        return "ninety"

    else:
        return "Error in SpellTens - received " + tensDigit


#INPUTS THE ONES-DIGIT OF A NUMBER BETWEEN 10 AND 19 AND RETURNS THE SPELLING OF THE TEENS-NUMBER
#IT ASSUMES THAT onesDigit CAME FROM A NUMBER BETWEEN 10 AND 19
def spellTeensNumber( onesDigit ):
    
    if onesDigit=="0":
        return "ten"

    elif onesDigit=="1":
        return "eleven"

    elif onesDigit=="2":
        return "twelve"

    elif onesDigit=="3":
        return "thirteen"

    elif onesDigit=="4":
        return "fourteen"

    elif onesDigit=="5":
        return "fifteen"

    elif onesDigit=="6":
        return "sixteen"

    elif onesDigit=="7":
        return "seventeen"

    elif onesDigit=="8":
        return "eighteen"

    elif onesDigit=="9":
        return "nineteen"

    else:
        return "Error in SpellTeens - received " + onesDigit


#RETURNS THE SPELLING OF ANY 2-DIGIT NUMBER
def spellTwoDigitNumber( twoDigitNumber ):
    
    length = len( twoDigitNumber )
    
    if length != 2:
        return "Error in spell two digits - received " + twoDigitNumber
    
    else:
        onesDigit = twoDigitNumber[1]
        tensDigit = twoDigitNumber[0]

        if tensDigit == "1":
            return spellTeensNumber(onesDigit)
        else:
            return spellTensDigit( tensDigit ) + " " + spellOneDigitNumber( onesDigit )


#RETURNS THE SPELLING OF ANY 3-DIGIT NUMBER
def spellThreeDigitNumber( threeDigitNumber ):
    
    length = len( threeDigitNumber )
    
    if length != 3:
        return "Wrong number of digits in spellThreeDigitNumber - received " + threeDigitNumber
    
    else:
        hundredsDigit = threeDigitNumber[0]
        firstTwoDigits = threeDigitNumber[1:3]

        if hundredsDigit == "0":
            hundredsWords = ""
            
        else:
            hundredsWords = spellOneDigitNumber( hundredsDigit )
            
        twoDigitWords = spellTwoDigitNumber( firstTwoDigits )

        return hundredsWords + " hundred " + twoDigitWords


#RETURNS THE SPELLING OF NUMBER THAT HAS MORE THAN 3 DIGITS
#NOT YET FINISHED
def spellFourOrMoreDigitNumber( longNumber ):
    return "SPELLING NUMBERS BIGGER THAN 999 IS NOT YET IMPLEMENTED -- BE PATIENT"


#RETURNS THE SPELLING OF ANY NUMBER
def spellAnyNumber( anyNumber ):

    numDigits = len( anyNumber )

    if numDigits == 1:
        return spellOneDigitNumber (anyNumber )

    elif numDigits == 2:
        return spellTwoDigitNumber (anyNumber )
    
    elif numDigits == 3:
        return spellThreeDigitNumber (anyNumber )

    else:
        return spellFourOrMoreDigitNumber (anyNumber )
