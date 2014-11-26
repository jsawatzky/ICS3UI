from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

def setInitialValues():
    global xBall, yBall, ballRadius, ballColour, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, ball, Qpressed
    
    xBall = 300
    yBall = 300

    ballRadius = 20
    ballColour = "black"

    xMouse = 0
    yMouse = 0

    xSpeed = 0
    ySpeed = 0

    maxSpeed = 1

    ball = 0

    Qpressed = False


#RETURNS TRUE IF THE MOUSE WAS CLICKED INSIDE THE BALL
def mouseInsideBall():
    global xBall, yBall, xMouse, yMouse
    
    dist = sqrt( (yMouse-yBall)**2 + (xMouse-xBall)**2 )

    if dist < ballRadius:
        return True
    
    else:
        return False


#GETS CALLED WHENEVER THE MOUSE IS CLICKED DOWN
def mouseClickHandler( event ):
    global xMouse, yMouse, ballColour
    
    screen.focus_set()
    
    xMouse = event.x
    yMouse = event.y

    if mouseInsideBall() == True: 
        ballColour = choice( ["red", "blue", "green", "black", "hot pink", "purple", "yellow", "white"] )
    

#GETS CALLED WHENEVER THE MOUSE IS RELEASED
def mouseReleaseHandler( event ):
    print ("Mouse released at", event.x, event.y )


#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    global xSpeed, ySpeed, Qpressed

    print( "Key down")
    
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


#GETS CALLED IN EVERY FRAME.  DRAWS THE BALL AT ITS CURRENT LOCATION AND SIZE
def drawBall():
    global ball
    
    ball = screen.create_oval(xBall-ballRadius, yBall-ballRadius, xBall + ballRadius, yBall+ballRadius, fill= ballColour)


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

    while Qpressed == False:
        updateBallPosition()
        drawBall()
        screen.update()
        sleep(0.01)
        screen.delete(ball)

    stopGame()

   
#STARTS THE GAME BY PASSING CONTROL TO THE PROCEDURE runGame() 1000 MILLISECONDS AFTER PUSHING F5
root.after(1000, runGame)

#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)

#BINDS THE PROCEDURE keyUPHandler TO ALL KEY-UP EVENTS
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
root.mainloop()
