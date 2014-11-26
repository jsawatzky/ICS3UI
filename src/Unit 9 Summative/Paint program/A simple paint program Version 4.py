from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
root.title("My Painting Program")
screen = Canvas(root,width=800, height=800, background="white")

def setInitialValues():
    global xBrush, yBrush, brushWidth, xMouse, yMouse, mouseDown, Qpressed, paintColour, numButtons
    global xBlackMin,xBlackMax,yBlackMin,yBlackMax,xBlueMin,xBlueMax,yBlueMin,yBlueMax,xRedMin,xRedMax,yRedMin,yRedMax
    global xGreenMin,xGreenMax,yGreenMin,yGreenMax,xYellowMin, yYellowMin, xYellowMax, yYellowMax
    global xWhiteMin, yWhiteMin, xWhiteMax, yWhiteMax
    global colourBoxSize, xPaletteMin, xPaletteMax, yPaletteMin, yPaletteMax
    global artMode, currentShape, xStart, yStart, xEnd, yEnd
    
    xBrush = 300
    yBrush = 300

    numColours = 6
    colourBoxSize = 50
    spacing = 5
    
    xPaletteMin = 10
    xPaletteMax = xPaletteMin + colourBoxSize
    yPaletteMin = 40
    yPaletteMax = yPaletteMin + (spacing + colourBoxSize)*numColours

    xBlackMin = xPaletteMin
    xBlackMax = xPaletteMin + colourBoxSize
    yBlackMin = yPaletteMin
    yBlackMax = yBlackMin + colourBoxSize

    xBlueMin = xPaletteMin
    xBlueMax = xPaletteMin + colourBoxSize
    yBlueMin = yBlackMax + spacing
    yBlueMax = yBlueMin+colourBoxSize

    xRedMin = xPaletteMin
    xRedMax = xPaletteMin + colourBoxSize
    yRedMin = yBlueMax + spacing
    yRedMax = yRedMin+colourBoxSize

    xGreenMin = xPaletteMin
    xGreenMax = xPaletteMin + colourBoxSize
    yGreenMin = yRedMax + spacing
    yGreenMax = yGreenMin+colourBoxSize

    xYellowMin = xPaletteMin
    xYellowMax = xPaletteMin + colourBoxSize
    yYellowMin = yGreenMax + spacing
    yYellowMax = yYellowMin+colourBoxSize

    xWhiteMin = xPaletteMin
    xWhiteMax = xPaletteMin + colourBoxSize
    yWhiteMin = yYellowMax + spacing
    yWhiteMax = yWhiteMin+colourBoxSize

    newScreen()

    paintColour = "black"
    brushWidth = 8

    mouseDown = False
    Qpressed = False

    artMode = "paint brush"  
    currentShape = 0
    currentShape = 0


def newScreen():
    background = screen.create_rectangle(0,0,800,800,fill="white")
    paintBox = screen.create_rectangle(xPaletteMin-5, yPaletteMin-5, xPaletteMax+5, yPaletteMax+5, fill = "white", outline="black",width=4)
    blackPalette = screen.create_oval(xBlackMin,yBlackMin,xBlackMax,yBlackMax,fill="black")
    bluePalette = screen.create_oval(xBlueMin,yBlueMin,xBlueMax,yBlueMax,fill="blue")
    redPalette = screen.create_oval(xRedMin,yRedMin,xRedMax,yRedMax,fill="red")
    greenPalette = screen.create_oval(xGreenMin,yGreenMin,xGreenMax,yGreenMax,fill="green")
    yellowPalette = screen.create_oval(xYellowMin,yYellowMin,xYellowMax,yYellowMax,fill="yellow")
    whitePalette = screen.create_oval(xWhiteMin,yWhiteMin,xWhiteMax,yWhiteMax,fill="white")

def setLineMode():
    global artMode

    artMode = "draw line"


def setRectangleMode():
    global artMode

    artMode = "draw rectangle"


def setOvalMode():
    global artMode

    artMode = "draw oval"


def setPaintBrushMode():
    global artMode

    artMode = "paint brush"


def setColour():
    global paintColour

    if yMouse <= yBlackMax and yMouse >= yBlackMin:
        paintColour = "black"
    
    elif yMouse <= yBlueMax and yMouse >= yBlueMin:
        paintColour = "blue"

    elif  yMouse <= yRedMax and yMouse >= yRedMin:
        paintColour = "red"

    elif  yMouse <= yGreenMax and yMouse >= yGreenMin:
        paintColour = "green"

    elif  yMouse <= yYellowMax and yMouse >= yYellowMin:
        paintColour = "yellow"

    elif  yMouse <= yWhiteMax and yMouse >= yWhiteMin:
        paintColour = "white"



def mouseInsidePalette():
    if xMouse <= colourBoxSize and yMouse <= yPaletteMax:
        return True
    else:
        return False


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, xBrush, yBrush, mouseDown, currentShape, currentShape, xStart, yStart
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True

    if mouseInsidePalette() == True:
        setColour()

    else:
        xBrush = xMouse
        yBrush = yMouse

        if artMode == "paint brush":
            paintOneStroke()

        elif artMode == "draw line":
            xStart = xBrush
            yStart = yBrush
            currentShape = 0

        elif artMode == "draw rectangle":
            xStart = xBrush
            yStart = yBrush
            currentShape = 0

        elif artMode == "draw oval":
            xStart = xBrush
            yStart = yBrush
            currentShape = 0




#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseMotionHandler( event ):
    global xMouse, yMouse, xBrush, yBrush, xEnd, yEnd, currentShape, currentShape
    
    xMouse = event.x
    yMouse = event.y

    if mouseInsidePalette() == False and mouseDown == True:
        xBrush = xMouse
        yBrush = yMouse
        
        if artMode == "paint brush":
            paintOneStroke()

        elif artMode == "draw line":
            xEnd = xBrush
            yEnd = yBrush
            screen.delete( currentShape )
            currentShape = screen.create_line( xStart, yStart, xEnd, yEnd, fill=paintColour, width=3)

        elif artMode == "draw rectangle":
            xEnd = xBrush
            yEnd = yBrush
            screen.delete( currentShape )
            currentShape = screen.create_rectangle( xStart, yStart, xEnd, yEnd, fill=paintColour, outline=paintColour)
       
        elif artMode == "draw oval":
            xEnd = xBrush
            yEnd = yBrush
            screen.delete( currentShape )
            currentShape = screen.create_oval( xStart, yStart, xEnd, yEnd, fill=paintColour, outline=paintColour)
       

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

#CLEAR BUTTON
clearButton = Button( root, text = "Clear", command = newScreen, anchor = W)
clearButton.pack()
clearButton.place(x=0,y=0, width=100)

#DRAW LINE BUTTON
drawLineButton = Button( root, text = "Lines", command = setLineMode, anchor = CENTER)
drawLineButton.pack()
drawLineButton.place(x=100, y=0,width=100)

#DRAW RECTANGLE BUTTON
drawRectangleButton = Button( root, text = "Rectangles", command = setRectangleMode, anchor = E)
drawRectangleButton.pack()
drawRectangleButton.place(x=200, y=0,width=100)

#DRAW OVAL BUTTON
drawOvalButton = Button( root, text = "Ovals", command = setOvalMode, anchor = E)
drawOvalButton.pack()
drawOvalButton.place(x=300, y=0,width=100)

#PAINT BRUSH BUTTON
paintBrushButton = Button( root, text = "Paint brush", command = setPaintBrushMode, anchor = E)
paintBrushButton.pack()
paintBrushButton.place(x=400, y=0,width=100)

screen.pack()

screen.focus_set()
root.mainloop()
