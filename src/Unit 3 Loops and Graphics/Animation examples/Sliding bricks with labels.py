from tkinter import *
from time import *
from random import *

tk = Tk()
screen = Canvas(tk, width=1000,height=450,background="black")
screen.pack()

y1 = 200
y2 = 280
yText = (y1+y2)/2

xLimit = 800 #The x-position at which the current brick will stop.
             #This value will be reduced every time a new brick begins

widthOfBrick = 30

speed = 4

brick = 0

brickCount = 0

while xLimit > 0: #Keep shooting bricks for as long as this limit is at least 0.
    
    # Reset the starting position of the next brick
    xUL = 0
    xLR = widthOfBrick

    brickCount = brickCount + 1

    # Nested loop! Animate the next brick
    while xLR < xLimit:
        
        xUL = min( xUL + speed, xLimit - widthOfBrick )
        xLR = xUL + widthOfBrick

        brick = screen.create_rectangle( xUL, y1, xLR, y2, outline = "white", fill="red", width=1 ) #This draws the current brick
        xText = (xUL + xLR)/2
        label = screen.create_text( xText, yText, text = str( brickCount ), fill = "blue", font = "Times 12 bold") #This draws the number label on the current brick
        
        screen.update()
        sleep(0.01)

        #For each box, delete all but the last frame, so that the brick will stay on screen when the next brick begins
        if xLR < xLimit:  
            screen.delete( brick, label
                           )

    #Reduce xLimit by widthOfBrick so that the next brick stops sooner than the current one
    xLimit = xLimit - widthOfBrick  


