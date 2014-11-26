from tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=800, height=800, background="turquoise")
myScreen.pack()

from arithmetic import *
from advancedGraphics import *



print("The gcd of 48 and 28 is" + str( gcd(48,28) ))

z = 1000
print( isEven(z) )


drawCircle(400,400,400,myScreen)
drawStarCluster("blue", 500, myScreen )
