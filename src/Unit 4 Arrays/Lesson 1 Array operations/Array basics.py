
#A STRING ARRAY.  AN ARRAY IS AN INDEXED LIST OF VALUES
movieList = ["Frozen", "Hobbit", "22 Jump Steet", "Hunger Games 3"] 
print( movieList )


#ACCESSING ELEMENTS OF AN ARRAY
print(movieList[2])
print(movieList[0])


#HOW BIG IS AN ARRAY? USE THE len() FUNCTION
numMovies = len( movieList )
print(numMovies)


#CAN YOU CHANGE THE VALUES OF AN ARRAY?
movieList[2] = "Twilight 6: They All Die"
print( movieList )


#CAN YOU ADD NEW ITEMS TO AN ARRAY? YES! USE THE .append() FUNCTION
movieList.append( "Dora Goes To The Dentist" )
print( movieList )


#TO PROCESS AN ARRY, USE A FOR-LOOP.  THE LOOPING VARIABLE WILL BE THE INDEX
ratings = [ "***", "**", "****", "*", "NO STARS" ]

for i in range(0, 5):
      print( movieList[i] + " was rated " + ratings[i])


#AN INTEGER ARRAY
marks = [90, 77, 40, 91, 77, 65, 100]
print(marks)


###RAISE ALL THE  MARKS BY 10 POINTS
for i in range(0, len(marks) ):
      marks[i] = marks[i] + 10

print(marks)



#WHICH INDEX IS "STAR WARS"?
myIndex = marks.index( 40 )
print("The kid who got the 40 and who likes Dairy Queen is index " + str( myIndex ))


#HOW TO ENTER AN ARRAY FROM THE KEYBOARD (needed for Challenge C)
coolTeachers = []

coolTeachers.append( "Mr. Schattman" )
print(coolTeachers)

coolTeachers.append( "Mr. Da Silva" )
print(coolTeachers)


