from tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "blue" )
screen.pack()


boxSize = 40

yUL = 200
yLR = yUL + boxSize

for columnNumber in range(1, 11):

    xUL = boxSize * columnNumber
    xLR = xUL + boxSize

    screen.create_rectangle( xUL, yUL, xLR, yLR, fill="yellow", outline="red")
    screen.update()

yUL = 240
yLR = yUL + boxSize

for columnNumber in range(1, 11):

    xUL = boxSize * columnNumber
    xLR = xUL + boxSize


    screen.create_rectangle( xUL, yUL, xLR, yLR, fill="yellow", outline="red")
    screen.update()

yUL = 280
yLR = yUL + boxSize

for columnNumber in range(1, 11):

    xUL = boxSize * columnNumber
    xLR = xUL + boxSize


    screen.create_rectangle( xUL, yUL, xLR, yLR, fill="yellow", outline="red")
    screen.update()

