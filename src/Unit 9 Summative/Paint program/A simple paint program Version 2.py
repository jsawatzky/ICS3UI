from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xBrush, yBrush, brushWidth, xMouse, yMouse, mouseDown, Qpressed, paintColour
    global xBlackMin,xBlackMax,yBlackMin,yBlackMax,xBlueMin,xBlueMax,yBlueMin,yBlueMax,xRedMin,xRedMax,yRedMin,yRedMax
    
    xBrush = 300
    yBrush = 300

    xBlackMin = 1
    xBlackMax = 50
    yBlackMin = 1
    yBlackMax = 50

    xBlueMin = 1
    xBlueMax = 50
    yBlueMin = 51
    yBlueMax = 100

    xRedMin = 1
    xRedMax = 50
    yRedMin = 101
    yRedMax = 150

    blackPalette = screen.create_rectangle(xBlackMin,yBlackMin,xBlackMax,yBlackMax,fill="black")
    bluePalette = screen.create_rectangle(xBlueMin,yBlueMin,xBlueMax,yBlueMax,fill="blue")
    redPalette = screen.create_rectangle(xRedMin,yRedMin,xRedMax,yRedMax,fill="red")

    paintColour = "white"
    brushWidth = 10

    mouseDown = False

    Qpressed = False


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
    if xMouse <= 50 and yMouse <= 150:
        return True
    else:
        return False


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, paintColour, mouseDown
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True

    if mouseInsidePalette() == True:
        paintColour = getNewColour()

    else:
        xBrush = xMouse
        yBrush = yMouse
        #paintOneStroke()


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
        Qpressed = True



#DRAWS THE BALL AT ITS CURRENT LOCATION AND SIZE
def drawBrush():
    global brush
    
#    brush = screen.create_oval(xBrush-brushWidth, yBrush-brushWidth, xBrush + brushWidth, yBrush+brushWidth, fill= paintColour)
    screen.update()


def startPaintProgram():
    setInitialValues()

root.after(0, startPaintProgram)

#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<Motion>", mouseMotionHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)

screen.pack()
screen.focus_set()
root.mainloop()
