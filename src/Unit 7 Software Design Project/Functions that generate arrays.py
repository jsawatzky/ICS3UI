#THIS PROGRAM SHOWS HOW TO
#  1)  DEFINE A FUNCTION THAT RETURNS AN ARRAY
#  2)  USE THAT FUNCTION TO CREATE AN ARRAY
#  3)  WRITE A PROCEDURE THAT TAKES AN ARRAY AS AN ARGUMENT AND DOES
#        SOMETHING WITH IT


from time import *
from Tkinter import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()





def getOrderedPairs( numPairs ):
    pairList = []

    for i in range(0, numPairs+1):

        
        xValue = i*100
        yValue = i*100

        nextPair = [xValue, yValue]
        pairList.append( nextPair )

    
    return pairList


def plotOrderedPairs( orderedPairs ):

    for i in range(0, len(orderedPairs) ):
        currentPair = orderedPairs[i]  # [200,200]
        xVal = currentPair[0]  #200
        yVal = currentPair[1]
        s.create_oval( xVal , yVal, xVal + 5, yVal+5, fill="yellow" )

    s.update()
        


myPairs = getOrderedPairs( 8 )

plotOrderedPairs( myPairs )



        


    
