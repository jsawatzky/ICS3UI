from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xMouse, yMouse, mouseDown, Qpressed
    global xCat, yCat, catWidth, catHeight, catImage, cat, catBeingMoved
    global xFood, yFood, foodWidth, foodHeight, foodImage, food, foodStillThere

    xCat = 300
    yCat = 300

    xFood = 200
    yFood = 200

    xMouse = 400
    yMouse = 400

    catWidth = 100
    catHeight = 50

    foodWidth = 80
    foodHeight = 40

    catBeingMoved = False
    foodStillThere = True
    mouseDown = False
    Qpressed = False

    catImage = PhotoImage( file="simons-cat.gif" )
    foodImage = PhotoImage( file="cat food.gif" )
    
    cat = 0
    food = 0
    
    drawCat()
    drawFood()



def drawCat():
    global cat

    screen.delete(cat)
    cat = screen.create_image(xCat, yCat, image=catImage, anchor=CENTER)
    screen.update()


def drawFood():
    global food, foodStillThere

    screen.delete(food)
    food = screen.create_image(xFood, yFood, image=foodImage, anchor=CENTER)
    screen.update()

    foodStillThere = True


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
    global xMouse, yMouse, xCat, yCat, foodStillThere
    
    xMouse = event.x
    yMouse = event.y

    if mouseDown == True and catBeingMoved == True:
        xCat = xMouse
        yCat = yMouse
        drawCat()

        if foodStillThere == False:           
            drawRandomFoodBowl()
        
        if catHasCaughtFoodBowl() == True:
            screen.delete( food )
            foodStillThere = False


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


def drawRandomFoodBowl():
    global xFood, yFood

    while getDist( xCat, yCat, xFood, yFood ) < 50:
        xFood = randint(50,550)
        yFood = randint(50,550)

    drawFood()


def getDist( x1, y1, x2, y2 ):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )


def catHasCaughtFoodBowl():
    distBetweenCatAndFood = getDist( xCat, yCat, xFood, yFood )

    if distBetweenCatAndFood <= 20:
        return True

    else:
        return False


def startCatProgram():
    global foodStillThere
    
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
