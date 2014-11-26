#ARRAY QUIZ SOLUTIONS

#Write a line of code that makes an array called days that contains the names of the days of the week.
days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

print("")



#Write a line of code that uses the days array to print out “Wednesday”.
print( days[3] )

print("")



##Write a for-loop that uses the days array to print out on four separate lines:
  ##Tuesday
  ##Wednesday
  ##Thursday
  ##Friday
for i in range( 2, 6 ):
    print(days[i])

print("")



#Write a for-loop that uses the % operator and the days array
#to print the 7 days of the week over and over. 
for i in range(0, 28):
    print(days[i % 7])

print("")



##Write a line of code that makes an array of marks named NikolasMarks with values 
##80, 60, 30, 40, 20.
NikolasMarks = [80, 60, 30, 40, 20]

print("")



##Write a line of code that adds a new mark with value 90 to the end of the array.  
##This will make Nikola happy.

NikolasMarks.append( 90 )
print( NikolasMarks )

print("")



#Write some code that adds 15 to each mark in the array and then prints the new array.
#This will make Nikola happy.

for i in range(0, len(NikolasMarks) ):
    NikolasMarks[i] = NikolasMarks[i] + 15

print( NikolasMarks )

print("")



#Write a for-loop that finds the lowest mark in the array.
#Then add a line below that loop that prints the lowest value.
#This will make Nikola sad.

lowestSoFar = NikolasMarks[0]

for i in range(0, len(NikolasMarks) ):
    if NikolasMarks[i] < lowestSoFar:
        lowestSoFar = NikolasMarks[i]

print("The lowest mark is " + str(lowestSoFar))

print("\n")


        
#Write a line of code that removes that lowest value from the array, and then prints the new array.  This will make Nikola happy.
NikolasMarks.remove( lowestSoFar )
print(NikolasMarks)


