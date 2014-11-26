from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=600,height=600,background="white")
screen.pack()


def getTableOfValues( m, b, xMin, xMax ):
    TOV = []

    for x in range(xMin, xMax+1):
        y = m*x + b
        orderedPair = [x,y]
        TOV.append( orderedPair )

    return TOV


def printTOV( TOV ):

    numPairs = len( TOV )

    xUL = 100
    yUL = 100

    gap = 40

    width = 100
    height = 30 + gap * numPairs

    xMid = xUL + width/2

    myFont = "Times 30"
    
    xHeader = screen.create_text(xUL + width/4, yUL, text="x", font = myFont, fill="red")
    yHeader = screen.create_text(xUL + 3*width/4, yUL, text="y", font = myFont, fill="red")

    horizontalGridLine = screen.create_line(xUL, yUL + 20, xUL + width, yUL + 20, fill="red")
    verticalGridLine = screen.create_line(xMid, yUL, xMid, yUL + height, fill="red")

    for row in range(0, numPairs):
        yHeight = yUL + (row+1) * gap
        xValue = TOV[row][0]
        yValue = TOV[row][1]
        screen.create_text(xUL+ width/4, yHeight, text = str(xValue), font = myFont )
        screen.create_text(xUL+ 3*width/4, yHeight, text = str(yValue), font = myFont )

    screen.update()
    

myTOV = getTableOfValues( 1, 0, -5, 5)
    
printTOV( myTOV )
    
