############################################################################################

#TITLE:  THE BEES AND THE HIKER

#PURPOSE:  A SAMPLE VIDEO GAME THAT SHOWS HOW TO COMBINE GRAPHICS, USER INTERACTIONS, AND SCORE-KEEPING IN A PYTHON PROGRAM

#DATE LAST MODIFIED: 12/27/2013

#PROGRAMMER:  J. SCHATTMAN

############################################################################################

from tkinter import *
from time import *
from math import *
from random import *

root = Tk()
screen = Canvas( root, width = 800, height = 800, background = "white" )

def contin():
    global cont, numBees, beeDumbness

    numBees = int(numBeesE.get())
    beeDumbness = int(numBeesE.get()) #THE BIGGER beeDumbness IS, THE LONGER THE BEES TAKE TO ADJUST THEIR DIRECTION TOWARDS THE HIKER'S CURRENT POSITION
    
    popup.destroy()
    screen.focus_set()
    cont = True

def startPopup():
    global popup, cont, numBeesE, beeDumbnessE

    popup = Toplevel()

    title = Label(popup, text = "Please set the initial values:")
    title.grid(columnspan = 2)

    q1 = Label(popup, text = "Number of bees:")
    q1.grid(row = 1)
    
    numBeesE = Entry(popup)
    numBeesE.insert(0, "25")
    numBeesE.grid(row = 1, column = 1)

    q2 = Label(popup, text = "Bee dumbness:")
    q2.grid(row = 2)
    
    beeDumbnessE = Entry(popup)
    beeDumbnessE.insert(0, "5")
    beeDumbnessE.grid(row = 2, column = 1)

    done = Button(popup, text = "Done", command = contin, width = 8)
    done.grid(columnspan = 2)

    q1.focus_set()

    cont = False


#GETS CALLED ONCE AT THE START OF THE GAME
#SETS THE HIKER'S AND MOUSE'S STARTING POSITIONS AND THE GAME OPTIONS
def setInitialValues():
    global hikerImageFile, beeImageFile, xHiker, yHiker, xMouse, yMouse, hikersMaximumSpeed, speedBees, beeDumbness, numBees
    global stickLength, stingsLeft, statisticsDisplay, userQuit, gameRunning, gamePaused
    global numBeesE, beeDumbnessE
    
    hikerImageFile = PhotoImage(file = "hikerGIF.gif")
    beeImageFile = PhotoImage(file = "beeGIF.gif")

    #CURRENT POSITION OF THE HIKER. STARTS AT (400, 600)
    xHiker = 400
    yHiker = 600

    #CURRENT POSITION OF THE MOUSE
    xMouse = 400
    yMouse = 750

    #GAME OPTIONS
    stingsLeft = int( numBees/2 )
    hikersMaximumSpeed = 18
    speedBees = 5
    stickLength = 30

    statisticsDisplay = 0

    userQuit = False    #BECOMES TRUE IF THE USER PRESSES 'Q' OR 'q'
    gameRunning = True  #BECOMES FALSE (i.e. THE GAME ENDS) IF THE USER QUITS OR GETS STUNG TOO MANY TIMES
    gamePaused = False
    

#GETS CALLED EVERYTIME THE USER MOVES THE MOUSE. SETS xMouse AND yMouse TO THE CURRENT MOUSE POSITION
def getMousePosition( event ):
    global xMouse, yMouse
    
    xMouse = event.x
    yMouse = event.y



#GETS CALLED EVERYTIME THE USER PRESSES A KEY.
#USED FOR CHECKING WHETHER THE USER QUIT, BUT COULD BE EXPANDED TO MAKE OTHER THINGS HAPPEN, LIKE MAKE THE HIKER FIRE BULLETS
def getKeyStroke( event ):
    global userQuit, gameRunning, gamePaused

    if event.keysym == "q" or event.keysym == "Q": #TESTS WHETHER THE USER PUSHED Q OR q
        userQuit = True
        gameRunning = False

    if event.keysym == "p" or event.keysym == "P": #TESTS WHETHER THE USER PUSHED P OR p
        if gamePaused == False:
            gamePaused = True

        else:
            gamePaused = False

    elif event.keysym == "f":
        print("Hiker just fired a bullet, but nothing really happens on screen yet.")
        #how could you make the hiker fire a bullet?

    else:
        print("You just pushed the " + event.keysym + " key, but that doesn't do anything.")



#GETS CALLED BY updateBeePositions AND updateHikerPosition BELOW
#CALCULATES THE DISTANCE BETWEEN POINTS (X1, Y1) AND (X2, Y2).  EXAMPLE: BETWEEN THE HIKER AND A BEE
def getDistance(x1, y1, x2, y2):
    return sqrt( (x2 - x1)**2 + (y2-y1)**2 )



#GETS CALLED ONCE AT THE START OF THE GAME
#GENERATES A SWARM OF BEES WITH RANDOM STARTING POSITIONS AND DIRECTIONS
def createRandomBees():
    global xBee, yBee, xBeeDir, yBeeDir, xBeeSpeed, yBeeSpeed, beeImage, dieRoll, beeAlive

    xBee = []
    yBee = []
    xBeeDir = []
    yBeeDir = []
    xBeeSpeed = []
    yBeeSpeed = []
    beeAlive = [] #TRUE BY DEFAULT.  BECOMES FALSE (THE BEE DIES) AS SOON AS IT STINGS THE HIKER
    beeImage = []
    dieRoll = [] #USED FOR RANDOMLY DETERMINING IF THE BEE WILL CHANGE ITS CURRENT DIRECTION AND FLY TOWARDS THE HIKER IN THE CURRENT FRAME
    
    for i in range( 0, numBees ):
        xRandom = randint( 1, 800 )
        yRandom = randint( 1, 200 )
        
        xBee.append(xRandom)
        yBee.append(yRandom)

        xBeeDir.append(1) #A DIRECTION OF (1, 1) MEANS THAT THE BEES HEAD SOUTHEAST IN THE 1ST FRAME.  IN LATER FRAMES, THEY CAN TRACK THE HIKER
        yBeeDir.append(1)
        
        xBeeSpeed.append(1)
        yBeeSpeed.append(1)
        
        beeAlive.append( True )

        beeImage.append(0)

        dieRoll.append(0)



#GETS CALLED IN EVERY FRAME.
#MAKES THE HIKER RUN TOWARDS THE MOUSE.  THAT IS, THE PLAYER USES THE MOUSE TO "SHOW" THE HIKER WHICH WAY TO RUN
#THE FARTHER AWAY THE MOUSE IS, THE FASTER THE HIKER MOVES, UP TO A CERTAIN MAXIMUM SPEED.
def updateHikerPosition():
    global xDir, yDir, speedHiker, xSpeed, ySpeed, xHiker, yHiker

    #SETS THE HIKER'S DIRECTION TOWARDS WHEREVER THE MOUSE IS
    xDir = xMouse - xHiker
    yDir = yMouse - yHiker
    
    distFromMouseToHiker = getDistance( xHiker, yHiker, xMouse, yMouse )

    speedHiker = min( hikersMaximumSpeed, distFromMouseToHiker / 20 ) #FORMULA FOR SETTING THE HIKER'S SPEED BASED ON THE DISTANCE TO THE MOUSE
    
    xSpeed = speedHiker * xDir / distFromMouseToHiker  #FORMULA FOR SPLITTING THE HIKER'S SPEED INTO AN X-COMPONENT AND A Y-COMPONENT
    ySpeed = speedHiker * yDir / distFromMouseToHiker

    xHiker = xHiker + xSpeed  #UPDATES THE HIKER'S POSITION BASED ON HIS X- AND Y-SPEEDS, WHICH WERE CALCULATED ABOVE
    yHiker = yHiker + ySpeed



#GETS CALLED IN EVERY FRAME.
#UPDATES THE BEES' DIRECTIONS, SPEEDS AND POSITIONS, BASED ON WHERE THE HIKER IS
#IN EACH FRAME, EACH BEE EITHER CHANGES ITS DIRECTION TOWARDS THE HIKER, OR KEEPS FLYING IN ITS PREVIOUS DIRECTION
#THIS IS DETERMINED RANDOMLY.  THE DUMBER THE BEES, THE LOWER THE CHANCE THAT THEY CHANGE DIRECTION
def updateBeePositions():
    global dieRoll, xBee, yBee, xBeeDir, yBeeDir, xBeeSpeed, yBeeSpeed

    for i in range( 0, numBees ):
        dieRoll[i] = randint( 1, beeDumbness ) #EXAMPLE:  IF THE BEES HAVE DUMBNESS 50, DIE ROLL CAN BE ANYWHERE BETWEEN 1 AND 50

    for i in range( 0, numBees ):
        
        if beeAlive[i] == True: #ONLY LIVING BEES HAVE A CHANCE TO CHANGE THEIR DIRECTION. (DEAD BEES ARE ALWAYS FALLING STRAIGHT DOWN)
            
            if dieRoll[i] == 1:   #IF THE DIE-ROLL TURNS UP "1", THE BEE CHANGES ITS DIRECTION. OTHERWISE, IT KEEPS ITS OLD DIRECTION, EVEN IF THE HIKER HAS MOVED
                xBeeDir[i] = xHiker - xBee[i] 
                yBeeDir[i] = yHiker - yBee[i] 
        
                distFromHiker = getDistance( xHiker, yHiker, xBee[i], yBee[i] )
        
                xBeeSpeed[i] = speedBees * xBeeDir[i] / distFromHiker
                yBeeSpeed[i] = speedBees * yBeeDir[i] / distFromHiker


        xBee[i] = xBee[i] + xBeeSpeed[i] #UPDATES ALL BEES' POSITIONS (EVEN DEAD ONES), REGARDLESS OF HOW THEIR CURRENT SPEED WAS CALCULATED
        yBee[i] = yBee[i] + yBeeSpeed[i]
    


#GETS CALLED IN EVERY FRAME.
#DRAWS THE HIKER AND HIS WALKING STICK.  THE WALKING STICK POINTS IN THE DIRECTION HE'S MOVING
def drawHiker():
    global hikerImage, hikerStick

    xStickEnd = stickLength * xSpeed / speedHiker #FORMULA FOR THE (X,Y) COORDINATES OF THE END OF THE WALKING STICK
    yStickEnd = stickLength * ySpeed / speedHiker

    hikerImage = screen.create_image( xHiker, yHiker, anchor=CENTER, image=hikerImageFile ) 
    hikerStick = screen.create_line( xHiker, yHiker, xHiker+xStickEnd, yHiker+yStickEnd, fill="red", width=5 )



#GETS CALLED IN EVERY FRAME.
#DRAWS THE BEES IN THEIR CURRENT POSITIONS USING THE .GIF IMAGES REFERENCED ABOVE
def drawBees():
    global beeImage
    
    for i in range(0,numBees):
        beeImage[i] = screen.create_image(xBee[i], yBee[i], anchor=CENTER, image=beeImageFile)


#GETS CALLED IN EVERY FRAME.
#CLEARS THE SCREEN BETWEEN FRAMES
def deleteImages():
    screen.delete( hikerImage, hikerStick, statisticsDisplay ) #DELETES THE HIKER AND THE DISPLAY
        
    for i in range( 0, numBees ): #DELETES THE BEES
        screen.delete( beeImage[i] )


#GETS CALLED IN EVERY FRAME.
#DETERMINES IF ANY OF THE BEES GOT CLOSE ENOUGH TO STING THE HIKER.
#IF A BEE STINGS A HIKER, THE HIKER'S stingsLeft COUNT DROPS BY 1, AND THE BEE THAT STUNG HIM DIES AND FALLS OFF THE SCREEN
def checkForStings():
    global gameRunning, stingsLeft, beeAlive, xBeeSpeed, yBeeSpeed
    
    for i in range( 0, numBees ):
         distFromBeeToHiker = getDistance( xHiker, yHiker, xBee[ i ], yBee[ i ] )
         
         if distFromBeeToHiker < 20: #IF THE BEE IS CLOSE ENOUGH TO THE HIKER...
            stingsLeft = stingsLeft - 1

            if stingsLeft <= 0:
                gameRunning = False    #GAME OVER

            else:
                beeAlive[i] = False    #BEE DIES

                yBee[i] = yBee[i] + 20 #NUDGES THE DEAD BEE AWAY FROM THE HIKER SO THAT IT CAN'T STING HIM MANY TIMES IN A ROW
                xBeeSpeed[i] = 0       #STOPS THE DEAD BEE'S HORIZONTAL MOTION
                yBeeSpeed[i] = 12      #MAKES THE DEAD BEE FALL STRAIGHT DOWN
            

                 
#GETS CALLED IN EVERY FRAME.
#UPDATES THE STATISTICS DISPLAY. IT CHANGES EVERYTIME THE USER GETS STUNG
def updateStatistics():
    global statisticsDisplay

    displayMessage = "Stings left before death: " + str(stingsLeft)

    statisticsDisplay = screen.create_text( 400, 50, text = displayMessage, font = "Times 36", anchor=CENTER, fill="blue" )

    

#GETS CALLED WHEN THE USER QUITS OR GETS STUNG TOO MANY TIMES
def stopGame():

    if userQuit == True:
        gameOverMessage = "You quit the game...game over"

    else:
        gameOverMessage = "You died...game over"

        
    screen.create_text( 400, 100, text = gameOverMessage, font = "Times 30", anchor=CENTER, fill = "red" )
    screen.update()
    
    sleep(2)
    
    root.destroy() #CLOSES THE GAME WINDOW AND ENDS THE PROGRAM
    


#THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME.  IT GETS CALLED ONCE WHEN THE PROGRAM STARTS, AS SEEN BELOW.
def runGame():

    startPopup()

    while cont == False:
        popup.update()
    
    setInitialValues()

    createRandomBees()

    sleep(2)

    while gameRunning == True:
        
        if gamePaused == True:
            drawHiker()
            drawBees()
            screen.update() #ESSENTIALLY DO NOTHING.  TO DO NOTHING, WE JUST CONSTANTLY REFRESH THE SCREEN, EVEN THOUGH NOTHING IS CHANGING

        else:
            updateHikerPosition()
            updateBeePositions()
            updateStatistics()

            checkForStings()

            drawHiker()
            drawBees()
            
            screen.update()
            sleep(0.01)

            deleteImages()

    stopGame()

#BINDS THE USER'S MOUSE-MOVEMENTS TO THE PROCEDURE getMousePosition(), DEFINED ABOVE.
#THAT IS, WHENEVER THE USER MOVES THE MOUSE, getMousePosition() GETS CALLED
screen.bind("<Motion>", getMousePosition )

#BINDS THE USER'S KEY-STROKES TO THE PROCEDURE getKeyStroke(), DEFINED ABOVE.
screen.bind("<Key>", getKeyStroke)

#CREATES THE SCREEN AND SETS THE EVENT LISTENER
screen.pack()

#CALLS THE MAIN PROCEUDRE runGame 1000 MILLISECONDS AFTER THE WINDOW IS CREATED
root.after( 10, runGame )

#STARTS THE PROGRAM
root.mainloop()
