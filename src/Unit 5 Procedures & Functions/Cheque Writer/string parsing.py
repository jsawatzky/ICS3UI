###How to pick out individual characters in a string

###Example 1
##myString = "Aug 05, 2013"
##
###print( myString[6] )
##
##monthName = myString[4:6]
##print(monthName)

#Example 2:  A two digit number
##dollarAmount = "67"
##
##onesDigit = dollarAmount[1]
##tensDigit = dollarAmount[0]
##
##print (onesDigit, tensDigit)


#Example 3:  A three digit number
##dollarAmount2 = "367"
##
##hundredsDigit = dollarAmount2[0]
##otherTwoDigits = dollarAmount2[1:3]
##
##print (hundredsDigit, otherTwoDigits)


##Example 4:  A dollar amount with cents
##dollarAmount3 = "2367.50"
##
##dollarPart = dollarAmount3[0:4]
##centsPart = dollarAmount3[:5]
##print ( centsPart )
##

#Example 5:  A dollar amount with cents and unknown number of dollar-digits
dollarAmount4 = "123293749271423974194745.67"  #input("Enter a dollar amount")

L = len( dollarAmount4 )

dollarPart = dollarAmount4[:L-3]
centsPart = dollarAmount4[L-2:]
print(centsPart)


