from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xMouse, yMouse, mouseDown, Qpressed

    xMouse = 400
    yMouse = 400

    mouseDown = False
    Qpressed = False



#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, mouseDown
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True
    drawBox()


def drawBox():
    box = screen.create_rectangle( xMouse, yMouse, xMouse+10, yMouse+10, fill="red", outline="red")


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseMotionHandler( event ):
    global xMouse, yMouse
    
    xMouse = event.x
    yMouse = event.y

    if mouseDown == True :
        print("The mouse is DOWN and has been dragged to " + str(xMouse) + ", " + str(yMouse))
        drawBox()


    else:
        print("The mouse is UP and has been moved to " + str(xMouse) + ", " + str(yMouse))
        

#GETS CALLED WHENEVER THE MOUSE IS RELEASED
def mouseReleaseHandler( event ):
    global mouseDown
    
    mouseDown = False
    print("The mouse has just been released at" + str(xMouse) + ", " + str(yMouse))



#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    if event.keysym == "q" or event.keysym == "Q":
        root.destroy()
        

def startMyProgram():
    setInitialValues()


#PASSES CONTROL TO THE PROCEDURE NAMED startMyProgram() AFTER 0 MILLISECONDS
root.after(0, startMyProgram)

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
