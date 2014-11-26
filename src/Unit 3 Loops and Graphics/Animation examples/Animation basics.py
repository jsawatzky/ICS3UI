from tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=600, height=600, background = "white" )
screen.pack()


#STARTING VALUES FOR THE VARIABLES THAT WILL CHANGE
xUL = 400
yUL = 400
xLR = xUL + 50
yLR = yUL + 50


#PARAMETERS WE CAN CHANGE TO CHANGE THE APPEARANCE OF THE ANIMATION

numberOfFrames = 100
myBox = 0


#ANIMATION LOOP

for frameCounter in range(0, numberOfFrames):

    screen.delete( myBox )

    #UPDATE THE POSITION VARIABLES
    xUL = xUL - 5
    yUL = yUL - 5
    
    xLR = xLR + 5
    yLR = yLR + 5
    

    #DRAW THE NEW FRAME
    myBox = screen.create_oval( xUL, yUL, xLR, yLR, fill="blue" )
    screen.update()

    #DELAY A SHORT TIME BETWEEN FRAMES SO THAT IT DOESN'T GO BY TOO FAST
    sleep(0.05)

    #DELETE THE PREVIOUS BOX
    

    
    
    
        
