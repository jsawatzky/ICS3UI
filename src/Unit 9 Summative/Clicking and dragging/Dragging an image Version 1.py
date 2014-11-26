from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xCat, yCat, catWidth, catHeight, catImage, catBeingMoved, xMouse, yMouse, mouseDown, Qpressed

    xCat = 300
    yCat = 300

    xMouse = 400
    yMouse = 400

    catWidth = 100
    catHeight = 50

    catImage = PhotoImage( file="simons-cat.gif" )
    drawCat()

    catBeingMoved = False
    
    mouseDown = False

    Qpressed = False


def drawCat():
    global cat

    cat = screen.create_image(xCat, yCat, image=catImage, anchor=CENTER)
    screen.update()


def mouseInsideCatImage():
    if xMouse >= xCat - catWidth/2 and xMouse <= xCat + catWidth/2  and yMouse >= yCat - catHeight/2 and  yMouse <= yCat + catHeight/2:
        return True
    else:
        return False


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, catBeingMoved, mouseDown
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True

    if mouseInsideCatImage() == True:
        catBeingMoved = True


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseMotionHandler( event ):
    global xMouse, yMouse, xCat, yCat
    
    xMouse = event.x
    yMouse = event.y

    if mouseDown == True and catBeingMoved == True:
        xCat = xMouse
        yCat = yMouse
        drawCat()
        

#GETS CALLED WHENEVER THE MOUSE IS RELEASED
def mouseReleaseHandler( event ):
    global mouseDown, catBeingMoved
    
    mouseDown = False
    catBeingMoved = False


#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    global Qpressed

    if event.keysym == "q" or event.keysym == "Q":
        root.destroy()
        

def startCatProgram():
    setInitialValues()


root.after(0, startCatProgram)

#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-MOTION EVENTS
screen.bind("<Motion>", mouseMotionHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)

screen.pack()
screen.focus_set()
root.mainloop()
