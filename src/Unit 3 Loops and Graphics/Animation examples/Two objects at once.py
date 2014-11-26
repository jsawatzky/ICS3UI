from tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=600, height=600, background = "white" )
screen.pack()


#STARTING VALUES FOR THE VARIABLES THAT WILL CHANGE
xUL = 0
yUL = 0

xULblue = 700
yULblue = 700


#PARAMETERS WE CAN CHANGE TO CHANGE THE APPEARANCE OF THE ANIMATION
boxSize = 75
numberOfFrames = 100


#ANIMATION LOOP

for frameCounter in range(0, numberOfFrames):

    #UPDATE THE POSITION VARIABLES
    xUL = xUL + 5  #How far will the box slide to the right in total?
    yUL = yUL + 5 

    xLR = xUL + boxSize
    yLR = yUL + boxSize

    xULblue = xULblue - 5  #How far will the box slide to the right in total?
    yULblue = yULblue -5 

    xLRblue = xULblue + boxSize
    yLRblue = yULblue + boxSize


    #DRAW THE NEW FRAME
    myBox = screen.create_rectangle( xUL, yUL, xLR, yLR, fill="red" )
    myBoxBlue = screen.create_rectangle( xULblue, yULblue, xLRblue, yLRblue, fill="blue" )
    screen.update()

    #DELAY A SHORT TIME BETWEEN FRAMES SO THAT IT DOESN'T GO BY TOO FAST
    sleep(0.1)

    #DELETE THE PREVIOUS BOX
    screen.delete( myBox, myBoxBlue )

    
    
    
        
