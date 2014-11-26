from time import *

#GOAL:  Given the current time, determine what time it will be h hours from now.


#STEP 1:  USE A LOOP AND THE .append() FUNCTION TO MAKE AN ARRAY OF CLOCK TIMES
hoursOfTheDay = ["1:00", "2:00", "3:00", "4:00","5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00"]


##for i in range(1,13):
##    nextHour = str(i) + ":00"
##
##    hoursOfTheDay.append( nextHour )
##
##    print( hoursOfTheDay )
##
##    sleep(0.4)


#STEP 2:  INPUT THE CURRENT TIME AND h
startTime = "3:00"

elapsedTime = 15


#STEP 3:  GET THE INDEX OF THE CURRENT TIME
startIndex = hoursOfTheDay.index( startTime )

print( "The index of " + startTime + " is " + str(startIndex) )


#STEP 4:  USE MODULAR ARITHMETIC TO CALCULATE THE INDEX OF THE ENDING TIME
finalIndex = (startIndex + elapsedTime) % 12
print( "The final index is " + str(startIndex) )

finalTime = hoursOfTheDay[ finalIndex ]

print (finalTime)
