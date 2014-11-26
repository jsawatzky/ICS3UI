from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xBall, yBall, ballRadius, ballColour, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, ball, Qpressed
    global balloons, balloonSpeed, xBalloons, yBalloons
    
    xBall = 300
    yBall = 300

    ballRadius = 20
    ballColour = "black"

    xMouse = 0
    yMouse = 0

    xSpeed = 0
    ySpeed = 0

    balloons = []
    xBalloons = []
    yBalloons = []
    balloonSpeed = 10

    maxSpeed = 10

    ball = 0

    Qpressed = False



#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, ballColour
    
    screen.focus_set()
    
    xMouse = event.x
    yMouse = event.y

    



#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    global xSpeed, ySpeed, Qpressed

    
    if event.keysym =="Left":   #LEFT ARROW WAS PRESSED
        xSpeed = -maxSpeed
        
    elif event.keysym == "Right":   #RIGHT ARROW WAS PRESSED
        xSpeed = maxSpeed

    elif event.keysym == "Up":   #UP ARROW WAS PRESSED
        ySpeed = -maxSpeed

    elif event.keysym == "Down":   #DOWN ARROW WAS PRESSED
        ySpeed = maxSpeed

    elif event.keysym == "q" or event.keysym == "Q":    #Q WAS PRESSED
        Qpressed = True

    elif event.keysym == "1":
        spawnNewBalloon()



def spawnNewBalloon():
    global balloons, xBalloons, yBalloons
    xBalloons.append( xBall )
    yBalloons.append( yBall )
    balloons.append(0)
    
    

#GETS CALLED WHENEVER ANY KEY IS RELEASED
def keyUpHandler( event ):
    global xSpeed, ySpeed
    
    xSpeed = 0  #STOP THE BALL
    ySpeed = 0


#GETS CALLED IN EVERY FRAME. UPDATES THE POSITION OF THE BALL, USING THE CURRENT SPEEDS
def updateBallPosition():
    global xBall, yBall
    
    xBall = xBall + xSpeed
    yBall = yBall + ySpeed


def updateBalloonPositions():
    global balloons, xBalloons, yBalloons

    for i in range(0,len(yBalloons)):
        yBalloons[i] = yBalloons[i] - balloonSpeed

    deleteArrayItemsThatAreOffScreen()
            

def deleteArrayItemsThatAreOffScreen():
    i = 0
    
    while i < len(yBalloons)-1:
        if yBalloons[i]<0:
            yBalloons.pop(i)
            xBalloons.pop(i)
            balloons.pop(i)

        else:
            i = i + 1


#GETS CALLED IN EVERY FRAME.  DRAWS THE BALL AT ITS CURRENT LOCATION AND SIZE
def drawBall():
    global ball
    
    ball = screen.create_oval(xBall-ballRadius, yBall-ballRadius, xBall + ballRadius, yBall+ballRadius, fill= ballColour)


def drawBalloons():
    for i in range(0,len(yBalloons)):
        balloons[i] = screen.create_oval( xBalloons[i] - 5, yBalloons[i] - 5,xBalloons[i] + 5,yBalloons[i] + 5,fill="red")

def deleteBalloons():
    for i in range(0,len(yBalloons)):
       screen.delete(balloons[i])


#GETS CALLED IN EVERY FRAME TO CHECK IF THE GAME SHOULD CONTINUE OR NOT
def gameOver():
    if Qpressed == True:
        return True

    else:
        return False


#GETS CALLED ONCE AFTER THE MAIN GAME LOOP HAS STOPPED
def stopGame():
    screen.delete(ball)
    screen.create_text( 300, 300, text="Thanks for playing...good bye", anchor=CENTER, font="Times 40")
    screen.update()
    sleep(2)
    root.destroy()


#GETS CALLED ONCE.  THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME
def runGame():
    global xBall, yBall, ballColour

    setInitialValues()

    screen.create_text(100, 550, text="Press 1 to fire", fill="blue")
    screen.update()

    while Qpressed == False:
        updateBallPosition()
        updateBalloonPositions()
        drawBall()
        drawBalloons()
        screen.update()
        sleep(0.01)
        screen.delete(ball)
        deleteBalloons()

    stopGame()

   
#STARTS THE GAME BY PASSING CONTROL TO THE PROCEDURE runGame() 1000 MILLISECONDS AFTER PUSHING F5
root.after(0, runGame)

#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)

#BINDS THE PROCEDURE keyUPHandler TO ALL KEY-UP EVENTS
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
root.mainloop()
