
##############################################
#HOW TO RESIZE A FONT, BASED ON USER INPUTS ##
##############################################

#SET UP SCREEN
from tkinter import *
root = Tk()
screen = Canvas(root, width=800, height=800, background = "black" )
screen.pack()


#INPUTS
wallWidth = 400.0
wallHeight = 100.0
xMin = 130
yMin = 200
howManyNumbers = 5


#CALCULATIONS
padding = 10
spacing = (wallWidth - 2*padding) / howManyNumbers


#SET FONT SIZE
fontSize = int( spacing/2 ) 
myFavouriteFont = "Times " + str( fontSize ) + " bold"


#DRAW THE WALL
screen.create_rectangle( xMin, yMin, xMin + wallWidth, yMin + wallHeight, fill="yellow", outline="blue" )


#DRAW THE NUMBERS
for i in range( 1, howManyNumbers + 1 ):
    
    numberString = str( i )
    
    xTextPosition = xMin + spacing * (i-1) + padding
    yTextPosition = yMin * 1.2
    
    screen.create_text( xTextPosition, yTextPosition, text = numberString, font = myFavouriteFont, fill = "blue")


