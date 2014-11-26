#THIS PYTHON PROGRAM SHOWS HOW TO MANIPULATE STRINGS AND NUMBERS
#SO THAT YOU CAN PICK OUT CERTAIN PARTS OF IT THAT YOU NEED TO WORK WITH


###EXAMPLE WITH A PHRASE
##myPhrase = "What's up?"
##firstLetter = myPhrase[0]  #The first letter on the left. Start counting from 0
##secondLetter = myPhrase[1]  
##thirdLetter = myPhrase[2]  
##fourthLetter = myPhrase[4]  #Use 3 to get the 4th letter because Python starts counting from 0
##
##print("The 1st letter of " + myPhrase + " is " + firstLetter)
##print("The 2nd letter of " + myPhrase + " is " + secondLetter)
##print("The 3rd letter of " + myPhrase + " is " + thirdLetter)
##print("The 4th letter of " + myPhrase + " is " + fourthLetter)
##
##

#EXAMPLE WITH A NUMBER
myNumber = "37834985703284502234231433849"
numDigits = len( myNumber ) #The number of digits in myNumber
print("The number " + myNumber + " has " + str( numDigits ) + " digits")


firstDigit = myNumber[0] #Gets the 3
onesDigit = myNumber[ numDigits - 1 ]  #Gets the 9. Since numDigits is 4, numDigits-1 is 3
print("The thousands digit of " + myNumber + " is " + firstDigit)
print("The ones digit of " + myNumber + " is " + onesDigit)

