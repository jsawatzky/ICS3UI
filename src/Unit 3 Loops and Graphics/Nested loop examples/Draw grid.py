from tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "blue" )
screen.pack()


boxSize = 40

for rowNumber in range( 1, 4) :
    
    yUL = boxSize * rowNumber
    yLR = yUL + boxSize

    print( "\nRow  " + str(rowNumber) + " is now starting")

    for columnNumber in range( 1, 11 ):

        xUL = boxSize * columnNumber

        xLR = xUL + boxSize

        screen.create_rectangle( xUL, yUL, xLR, yLR, fill="yellow", outline="red")
        screen.update()

        print( "Column  " + str(columnNumber) + " is now done")


    print( "Row  " + str(rowNumber) + " is now done")

