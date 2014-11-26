from tkinter import *
root = Tk()
screen = Canvas(root, width=800, height=800, background = "black" )
screen.pack()


#INPUTS
wallWidth = 400.0
wallHeight = 50.0
xMin = 100
yMin = 150

howManyNumbers = 25

spacing = int(wallWidth/howManyNumbers)
fontSize = int(0.7*spacing)
fontString = "Times " + str(fontSize) + " bold"


#DRAW THE WALL
screen.create_rectangle( xMin, yMin, xMin + wallWidth, yMin + wallHeight, fill="yellow", outline="blue" )

#DRAW THE NUMBERS
for i in range( 1, howManyNumbers + 1 ):
    
    numberString = str( i )
    
    xTextPosition = xMin + spacing * i
    
    screen.create_text( xTextPosition, yMin+25, text = numberString, font=fontString, fill="blue")


