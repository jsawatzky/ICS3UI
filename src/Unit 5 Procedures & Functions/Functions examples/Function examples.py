def getAverage( num1, num2 ):
      myAnswer = (num1+num2)/2
      return myAnswer


def getArrayAverage( someArray ):
      total = 0
      for i in range(0, len(someArray)):
            total = total + someArray[i]
      myAnswer = total/len(someArray)
      return myAnswer

def isItEven( x ):
      if x % 2 == 0:
            return "Even"
      else:
            return "Odd"
      

z = getAverage(4, 10)
print("The average of 4 and 10 is " + str(z))

print("The average of 9 and 100 is " + str(getAverage(9,100)))

salmansMarks = [100, 99, 100, 98, 90, 100, 90, 5]
salmansAverage = getArrayAverage( salmansMarks )
print( "Salman has a " + str( salmansAverage ) + " in Underwater Basket Weaving TCJ3MI")

parityOfMyAge = isItEven(31)
print(parityOfMyAge)
