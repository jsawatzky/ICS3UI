from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xBrush, yBrush, brushWidth, xMouse, yMouse, mouseDown, Qpressed, paintColour, numColours
    global xBlackMin,xBlackMax,yBlackMin,yBlackMax,xBlueMin,xBlueMax,yBlueMin,yBlueMax,xRedMin,xRedMax,yRedMin,yRedMax
    global xPaletteMax,yPaletteMax
    
    xBrush = 300
    yBrush = 300

    numColours = 3

    xPaletteMax = 50
    yPaletteMax = xPaletteMax*(numColours+1)

    xBlackMin = 1
    xBlackMax = xPaletteMax
    yBlackMin = 1
    yBlackMax = xPaletteMax

    xBlueMin = 1
    xBlueMax = xPaletteMax
    yBlueMin = 51
    yBlueMax = 100

    xRedMin = 1
    xRedMax = xPaletteMax
    yRedMin = 101
    yRedMax = 150

    newScreen()

    paintColour = "white"
    brushWidth = 5

    mouseDown = False

    Qpressed = False


def newScreen():
    background = screen.create_rectangle(0,0,600,600,fill="white")
    blackPalette = screen.create_rectangle(xBlackMin,yBlackMin,xBlackMax,yBlackMax,fill="black")
    bluePalette = screen.create_rectangle(xBlueMin,yBlueMin,xBlueMax,yBlueMax,fill="blue")
    redPalette = screen.create_rectangle(xRedMin,yRedMin,xRedMax,yRedMax,fill="red")

    
#RETURNS TRUE IF THE MOUSE WAS CLICKED INSIDE THE BALL
def getNewColour():
    
    if xMouse <= xBlackMax and xMouse >= xBlackMin and yMouse <= yBlackMax and yMouse >= yBlackMin:
        return "black"
    
    elif xMouse <= xBlueMax and xMouse >= xBlueMin and yMouse <= yBlueMax and yMouse >= yBlueMin:
        return "blue"

    elif xMouse <= xRedMax and xMouse >= xRedMin and yMouse <= yRedMax and yMouse >= yRedMin:
        return "red"

    else:
        return "white"


def mouseInsidePalette():
    if xMouse <= xPaletteMax and yMouse <= yPaletteMax:
        return True
    else:
        return False


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, xBrush, yBrush, paintColour, mouseDown
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True

    if mouseInsidePalette() == True:
        paintColour = getNewColour()

    else:
        xBrush = xMouse
        yBrush = yMouse
        paintOneStroke()


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseMotionHandler( event ):
    global xMouse, yMouse, xBrush, yBrush
    
    xMouse = event.x
    yMouse = event.y

    if mouseInsidePalette() == False and mouseDown == True:
        xBrush = xMouse
        yBrush = yMouse
        paintOneStroke()
        

def paintOneStroke():
    screen.create_oval( xBrush-brushWidth, yBrush-brushWidth, xBrush+brushWidth, yBrush+brushWidth, fill=paintColour, outline=paintColour )
    screen.update()
    

#GETS CALLED WHENEVER THE MOUSE IS RELEASED
def mouseReleaseHandler( event ):
    global mouseDown
    
    mouseDown = False


#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    global Qpressed

    if event.keysym == "q" or event.keysym == "Q":
        root.destroy()
        

def startPaintProgram():
    setInitialValues()


root.after(0, startPaintProgram)

#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-MOTION EVENTS
screen.bind("<Motion>", mouseMotionHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)


clearButton = Button( root, text = "Click on me to clear the screen", command = newScreen, anchor = W)

screen.pack()
clearButton.pack()

screen.focus_set()
root.mainloop()
