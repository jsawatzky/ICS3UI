markTotal = 0

numMarks = int( input( "How many marks would you like to enter? "))

for markCounter in range(0, numMarks):
    currentMark = float( input("Enter a mark: "))

    markTotal = markTotal + currentMark


print("Thank you for entering your marks.")

average = markTotal / numMarks

print("Your average is " + str( average ))

    
                    
