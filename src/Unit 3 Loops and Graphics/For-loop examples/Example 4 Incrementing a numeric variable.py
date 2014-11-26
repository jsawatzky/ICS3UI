#Try changing the monthly salary
#Try changing the starting value of totalEarnedSoFar to 20000 and also
#  change the plus sign in the formula to a minus sign

total = 0

monthlySalary = 4300

for monthCount in range(1, 13):

    print("This is month #" + str( monthCount) )

    total = total + monthlySalary
    
    print( "You just earned another $" + str( monthlySalary ))
    print( "SO FAR THIS YEAR YOU HAVE EARNED $" + str( total ))
    
    print( "##################" )
    print( "" )



    
