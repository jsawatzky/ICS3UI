def getAverage( num1, num2 ):
      Sum = num1 + num2
      avg = Sum/2
      return avg

def isEvenOrNot( num ):
      if num % 2 == 0:
            y = True
      else:
            y = False

      return y

      

x = 500
y = 100

z = getAverage( x, y )

print( z )

print( getAverage(6, 7) )

z2 = isEvenOrNot( 21 )
print(z2)


for i in range(0,100):
      if isEvenOrNot( i ):
            print("Even teams")

      else:
            print("Need an extra player")

