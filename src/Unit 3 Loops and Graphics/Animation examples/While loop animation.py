from tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "yellow" )
screen.pack()


#STARTING VALUES FOR THE VARIABLES THAT WILL CHANGE
xUL = 0
yUL = 200
xLR = xUL + 50
yLR = yUL + 50


#PARAMETERS WE CAN CHANGE TO CHANGE THE APPEARANCE OF THE ANIMATION

numberOfFrames = 200

xSpeed = 2
ySpeed = 1
diameter = 20

wall = 400

myBall = 0

#DRAW THE WALL
wallLine = screen.create_line( wall, 0, wall, 800, fill="red", width = 5 )


#ANIMATION LOOP

while xLR < wall:
    screen.delete( myBall )

    #UPDATE THE POSITION VARIABLES
    xUL = xUL + xSpeed
    yUL = yUL + ySpeed
    
    xLR = xUL + diameter
    yLR = yUL + diameter


    #DRAW THE NEW FRAME
    myBall = screen.create_oval( xUL, yUL, xLR, yLR, fill="blue" )
    screen.update()

    #DELAY A SHORT TIME BETWEEN FRAMES SO THAT IT DOESN'T GO BY TOO FAST
    sleep(0.02)

    #DELETE THE PREVIOUS FRAME


###########
#NEXT CHALLENGE: CAN YOU GET THE WALL TO MOVE, TOO?
###########   
    
    
        
