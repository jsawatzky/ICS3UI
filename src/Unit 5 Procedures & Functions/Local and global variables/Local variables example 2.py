def getAverage( a, b ) :
	total = a + b 	#total is a local variable!
	average = total/2
	return average

#x, y, and avg are global variables
x = 10
y = 20
avg = getAverage( x, y )

print( avg  ) 		#Prints 15 because avg is a global variable
print( average )	#ERROR!  The variable "average" is not known anywhere outside getAverage()
print( total )		#ERROR!  The variable "total" is not known anywhere outside getAverage()
print( a + b )		#ERROR!  The variables a and b are not known anywhere outside getAverage()
