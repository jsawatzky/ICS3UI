
#EXAMPLE WITH A PHRASE
myPhrase = "What's up?"
firstLetter = myPhrase[0]  #The first letter on the left
fourthLetter = myPhrase[3]  #Use 3 because Python starts counting from 0

print("The 1st letter of " + myPhrase + " is " + firstLetter)
print("The 4th letter of " + myPhrase + " is " + fourthLetter)


#EXAMPLE WITH A NUMBER
myNumber = "3789"
numDigits = len( myNumber ) #The number of digits in myNumber
firstDigit = myNumber[0]
onesDigit = myNumber[ numDigits - 1 ]  #Since numDigits is 4, numDigits-1 is 3

print("The number " + myNumber + " has " + str( numDigits ) + " digits")
print("The 1st digit of " + myNumber + " is " + firstDigit)
print("The ones digit of " + myNumber + " is " + onesDigit)

