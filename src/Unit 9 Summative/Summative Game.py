'''
Created on Jan 11, 2015

@author: Jacob
'''
#Imports
from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from random import *
from time import sleep, clock
from datetime import *
from math import *
from threading import Timer

#Set up the tkinter window
root = Tk()
root.title("ICS3UI Summative Game by Jacob Sawatzky")
root.resizable(FALSE, FALSE)

#Set up the canvas
s = Canvas(root, height = 800, width = 600, bg = "black")
s.grid(row = 0, column = 0)

#Initialize all variables for global use
def initializeVariables():
    global player, asteroidImgs, enemyShipImg, enemies, background, explosions
    global lives, difficulty, score
    global menu, paused, exiting
    global buttons
    global scoreText, pausedText, gameOverText, finalScoreText, gameTitleText, livesText, helpControlsText, helpText, controlsText

    #Game difficulty. 1 = Easy, 2 = Medium, 3 = Hard
    difficulty = 1

    #Current score
    score = 0

    #Booleans for the users current menu
    menu = True
    paused = False
    exiting = False

    #The scrolling stars
    background = Background(600, 800)

    #The players ship
    player = Player()

    #Asteroids and enemy ships
    asteroidImgs = [PhotoImage(file = "asteroid1.gif"), PhotoImage(file = "asteroid2.gif"), PhotoImage(file = "asteroid3.gif"), PhotoImage(file = "asteroid4.gif")]
    enemyShipImg = PhotoImage(file = "enemy.gif")
    enemies = Enemies()

    #Explosion handler
    explosions = Explosion()

    #All text that appears in the game
    gameTitleText = s.create_text(-1000, -1000, text = "ICS3UI Summative", font = "Arial 50", fill = "white")
    scoreText = s.create_text(-1000, -1000, text = "Score: 0", font = "Arial 15", fill = "white", anchor = NE)
    livesText = s.create_text(-1000, -1000, text = "Lives left: 2", font = "Arial 15", fill = "white", anchor = SW)
    finalScoreText = s.create_text(-1000, -1000, text = "Score: ", font = "Arial 30", fill = "white")
    pausedText = s.create_text(-1000, -1000, text = "Paused", font = "Arial 60", fill = "white")
    gameOverText = s.create_text(-1000, -1000, text = "Game Over", font = "Arial 40", fill = "white")
    helpControlsText = s.create_text(-1000, -1000, text = "Help / Controls", font = "Arial 40", fill = "white")
    
    helpText = s.create_text(-1000, -1000,
                                      text = "HELP\n\nWhen you start the game you have 3 lives\nEverytime you die you have 3 seconds to move\naway from danger before the game resumes\nYou may shoot a bullet every 0.1s\nYou may shoot a rocket every 1s\nBullets can only destroy enemy ships\nRockets can destroy both enemy ships and asteroids",
                                      font = "Arial 15", fill = "white", anchor = S, justify = CENTER)
    controlsText = s.create_text(-1000, -1000,
                                 text = "CONTROLS\n\n- W or UP to move forward\n- S or DOWN to move backwards\n- A or RIGHT to move right\n- D or LEFT to move left\n- Left click or E to shoot a bullet\n- Right click or Q to fire a rocket\n- Escape to pause",
                                 font = "Arial 15", fill = "white", anchor = N, justify = CENTER)

    #All buttons that appear
    buttons = {}
    buttons['start'] = Button(300, 400, 200, 100, startGame, text = "Start Game")
    buttons['easy'] = Button(175, 500, 75, 50, lambda: setDifficulty(1), text = "Easy")
    s.itemconfig(buttons['easy'].content1, fill = "green")
    buttons['medium'] = Button(300, 500, 125, 50, lambda: setDifficulty(2), text = "Medium")
    buttons['hard'] = Button(425, 500, 75, 50, lambda: setDifficulty(3), text = "Hard")
    buttons['pause'] = Button(25, 25, 20, 20, pauseGame, image = "pause.gif")
    buttons['resume'] = Button(300, 400, 200, 100, unpauseGame, text = "Resume")
    buttons['quit'] = Button(300, 700, 200, 100, windowClose, text = "Quit Game")
    buttons['menu'] = Button(300, 500, 200, 100, mainMenu, text = "Main Menu")
    buttons['playagain'] = Button(300, 400, 200, 100, startGame, text = "Play Again")
    buttons['helpcontrols'] = Button(300, 600, 200, 100, helpControls, text = "Help/Controls")
    buttons['back'] = Button(300, 750, 200, 50, helpControls, text = "Back")
    

#Resets game for another round
def resetGame():
    global paused, score

    #Reset score and unpause
    score = 0
    paused = False

    #Move all text off screen
    s.coords(pausedText, -1000, -1000)
    s.coords(scoreText, -1000, -1000)
    s.coords(livesText, -1000, -1000)
    s.coords(finalScoreText, -1000, -1000)
    s.coords(gameOverText, -1000, -1000)
    s.coords(gameTitleText, -1000, -1000)
    s.coords(helpControlsText, -1000, -1000)
    s.coords(helpText, -1000, -1000)
    s.coords(controlsText, -1000, -1000)

    #Reset game objects to default values
    background.reset()
    player.reset()
    enemies.reset()

#Set the difficulty of the game
#Used by the difficulty buttons
def setDifficulty(diff):
    global difficulty

    #Set the difficulty
    difficulty = diff

    s.itemconfig(buttons['easy'].content1, fill = "white")
    s.itemconfig(buttons['medium'].content1, fill = "white")
    s.itemconfig(buttons['hard'].content1, fill = "white")
    
    #Easy
    if diff == 1:
        s.itemconfig(buttons['easy'].content1, fill = "green")
    #Medium
    elif diff == 2:
        s.itemconfig(buttons['medium'].content1, fill = "green")
    #Hard
    elif diff == 3:
        s.itemconfig(buttons['hard'].content1, fill = "green")

#Starts the game 
def startGame():
    global menu

    #Prep the game
    resetGame()

    #Exit the menu
    menu = False

    #Move required text on screen
    s.coords(scoreText, 590, 10)
    s.coords(livesText, 10, 790)

    #Deactive all buttons
    buttons['start'].deactivate()
    buttons['easy'].deactivate()
    buttons['medium'].deactivate()
    buttons['hard'].deactivate()
    buttons['quit'].deactivate()
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['playagain'].deactivate()
    buttons['helpcontrols'].deactivate()

    #Activate the pause button
    buttons['pause'].activate()

#Open the main menu
def mainMenu():
    global menu

    #Clear screen
    resetGame()

    #Enter the menu
    menu = True

    #Put the game title on screen
    s.coords(gameTitleText, 300, 200)

    #Deactive all buttons that won't be used
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['playagain'].deactivate()
    buttons['back'].deactivate()

    #Activate required buttons
    buttons['start'].activate()
    buttons['easy'].activate()
    buttons['medium'].activate()
    buttons['hard'].activate()
    buttons['quit'].activate()
    buttons['helpcontrols'].activate()

#Open the help/controls menu
def helpControls():

    #Deactivate all buttons
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['quit'].deactivate()
    buttons['helpcontrols'].deactivate()
    buttons['start'].deactivate()
    buttons['easy'].deactivate()
    buttons['medium'].deactivate()
    buttons['hard'].deactivate()
    buttons['playagain'].deactivate()

    #Hide text
    s.coords(pausedText, -1000, -1000)
    s.coords(gameOverText, -1000 , -1000)
    s.coords(finalScoreText, -1000, -1000)
    s.coords(gameTitleText, -1000, -1000)

    #Activate the back button
    buttons['back'].activate()

    #Move on help text
    s.coords(helpControlsText, 300, 100)
    s.coords(helpText, 300, 425)
    s.coords(controlsText, 300, 475)

    #Set where the back button leads
    if paused == True:
        buttons['back'].command = pauseGame
    elif menu == True:
        buttons['back'].command = mainMenu
    else:
        buttons['back'].command = gameOver
    
def pauseGame():
    global paused 

    #Enter pause menu
    paused = True

    #Move text
    s.coords(pausedText, 300, 200)
    s.coords(helpControlsText, -1000, -1000)
    s.coords(helpText, -1000, -1000)
    s.coords(controlsText, -1000, -1000)

    #Deactivate buttons
    buttons['pause'].deactivate()
    buttons['back'].deactivate()

    #Activate pause menu buttons
    buttons['resume'].activate()
    buttons['menu'].activate()
    buttons['quit'].activate()
    buttons['helpcontrols'].activate()
    
def unpauseGame():
    global paused

    #Exit pause menu
    paused = False

    #Move text
    s.coords(pausedText, -1000, -1000)

    #Deactivate pause menu buttons
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['quit'].deactivate()
    buttons['helpcontrols'].deactivate()

    #Activate pause button
    buttons['pause'].activate()
    
def gameOver():

    #Get rid of text
    s.coords(scoreText, -1000, -1000)
    s.coords(livesText, -1000, -1000)
    s.coords(helpControlsText, -1000, -1000)
    s.coords(helpText, -1000, -1000)
    s.coords(controlsText, -1000, -1000)

    #Add gameover text and info
    s.coords(gameOverText, 300 , 200)
    s.coords(finalScoreText, 300, 250)
    s.itemconfig(finalScoreText, text = "Score: " + str(round(score)))

    #Deactivate buttons
    buttons['pause'].deactivate()
    buttons['back'].deactivate()

    #Activate buttons
    buttons['menu'].activate()
    buttons['quit'].activate()
    buttons['playagain'].activate()
    buttons['helpcontrols'].activate()
        
#EVENT HANDLERS

#Left click
def leftMouseDown(event):

    #Check if the user clicked on a button and if the did call its function
    for button in buttons.values():
        if button.active:
            if button.isOver(event.x, event.y):
                button.click()
                return

    #Fire a bullet if the game is running
    if paused == False and menu == False:
        player.fireBullet()

#Right click
def rightMouseDown(event):

    #Fire a rocket if the game is running
    if paused == False and menu == False:
        player.fireRocket()

#Move moved
def mouseMove(event):

    #Check if the mouse is over a button and if it is change the cursor
    for button in buttons.values():
        if button.active:
            if button.isOver(event.x, event.y):
                root.config(cursor = button.cursor)
                break
            else:
                root.config(cursor = "")

#Key pressed
def keyDown(event):
    global paused

    #Player movement
    if event.keysym == "w" or event.keysym == "Up":
        player.forward = True
    elif event.keysym == "a" or event.keysym == "Left":
        player.right = True
    elif event.keysym == "s" or event.keysym == "Down":
        player.backward = True
    elif event.keysym == "d" or event.keysym == "Right":
        player.left = True

    #Player shooting
    elif event.keysym == "e":
        if paused == False and menu == False:
            player.fireBullet()
    elif event.keysym == "q":
        if paused == False and menu == False:
            player.fireRocket()

    #Pausing
    elif event.keysym == "Escape":
        if menu == False:
            if paused == True:
                unpauseGame()
            else:
                pauseGame()

#Key released
def keyUp(event):
    global paused

    #Player movement
    if event.keysym == "w" or event.keysym == "Up":
        player.forward = False
    elif event.keysym == "a" or event.keysym == "Left":
        player.right = False
    elif event.keysym == "s" or event.keysym == "Down":
        player.backward = False
    elif event.keysym == "d" or event.keysym == "Right":
        player.left = False

#Window closed
def windowClose():
    global exiting

    #Check if the user really wants to quit
    if askyesno("Quit", "Are you sure you want to quit?"):
        
        exiting = True

#CLASSES

#Buttons
class Button():

    #Initialization
    def __init__(self, x, y, maxWidth, maxHeight, command, text = "", image = "", cursor = "hand2"):

        #Set base variables
        self.x = x
        self.y = y
        self.width = maxWidth
        self.height = maxHeight
        self.command = command
        self.cursor = cursor
        self.active = False
        self.text = text

        #Get the right font to fit in box
        if text != "":
            fontsize, self.width, self.height = self.getFontSize(text, maxWidth, maxHeight)
            self.font = "Arial " + str(fontsize)
        else:
            self.font = "Arial 10"

        #Get the image
        if image != "":
            self.image = PhotoImage(file = image)
        else:
            self.image = None

        #Create the text and image
        self.content1 = s.create_text(-100, -100, text = self.text, font = self.font, fill = "white")
        self.content2 = s.create_image(-100, -100, image = self.image)

    #Activate the button
    def activate(self):
        
        self.active = True
        #Move objects to their location
        s.coords(self.content1, self.x, self.y)
        s.coords(self.content2, self.x, self.y)

    #Deactivate the button
    def deactivate(self):
        
        self.active = False
        #Move the objects off screen
        s.coords(self.content1, -100, -100)
        s.coords(self.content2, -100, -100)

    #Check if the given coordinate are over the button
    def isOver(self, x, y):
        
        if x > self.x - self.width/2 and x < self.x + self.width/2 and y > self.y - self.height/2 and y < self.y + self.height/2:
            return True
        else:
            return False

    #Click the button
    def click(self):
        self.command()

    #Get the right font size to fit in the bounding box
    def getFontSize(self, string, maxWidth, maxHeight):
        
        size = 10
        com = ""
        while True:
            font = Font(s, family = "Arial", size = size)
            width, height = font.measure(string), font.metrics("linespace")
            if width > maxWidth or height > maxHeight:
                size -= 1
                com = "big"
            elif width < maxWidth:
                if com == "big":
                    return (size, width, height)
                size += 1
                com = "small"
            else:
                return (size, width, height)

#Explosion handler
class Explosion():

    #Initialization
    def __init__(self):
        
        self.numActiveExplosions = 0

        #Create an explosion object
        self.explosions = []
        self.explosions.append([[], -100, -100, 0, 0])
        for i in range(50):
            self.explosions[0][0].append([s.create_oval(-100, -100, -100, -100, fill = choice(["yellow", "orange", "red"])), randint(5, 10), randint(0, 360), 0])

    #Start an new explosion at x, y
    def new(self, x, y, r):

        #Update active explosions
        self.numActiveExplosions += 1

        #Create a new explosion object if necessary 
        if self.numActiveExplosions > len(self.explosions):
            self.explosions.append([[], x, y, r, r])
            for i in range(50):
                self.explosions[len(self.explosions)-1][0].append([s.create_oval(-100, -100, -100, -100, fill = choice(["yellow", "orange", "red"])), randint(5, 10), randint(0, 360), randint(0, r)])
        #Update an existing object if not
        else:
            self.explosions[self.numActiveExplosions-1][1] = x
            self.explosions[self.numActiveExplosions-1][2] = y
            self.explosions[self.numActiveExplosions-1][3] = r
            self.explosions[self.numActiveExplosions-1][4] = r
            for i in range(50):
                self.explosions[self.numActiveExplosions-1][0][i][1] = randint(5, 10)
                self.explosions[self.numActiveExplosions-1][0][i][2] = randint(0, 360)
                self.explosions[self.numActiveExplosions-1][0][i][3] = randint(0, r)

    #Update for next frame
    def update(self):

        #Go through every active explosion
        for explosion in range(self.numActiveExplosions):
            
            if explosion == self.numActiveExplosions:
                break
            
            repeat = True
            while repeat == True and self.numActiveExplosions > 0:

                #Move the explosion parts to animate explosion
                for i in range(len(self.explosions[explosion][0])):
                
                    size = self.explosions[explosion][0][i][1]
                    xMove = self.explosions[explosion][0][i][3]*cos(radians(self.explosions[explosion][0][i][2]))
                    yMove = self.explosions[explosion][0][i][3]*sin(radians(self.explosions[explosion][0][i][2]))
                    s.coords(self.explosions[explosion][0][i][0], self.explosions[explosion][1]+xMove-size, self.explosions[explosion][2]+yMove-size, self.explosions[explosion][1]+xMove+size, self.explosions[explosion][2]+yMove+size)
                    self.explosions[explosion][0][i][3] += 1

                self.explosions[explosion][4] += 1
                #Check if the explosion is a certain size and if it is, end it
                if self.explosions[explosion][4] - self.explosions[explosion][3] > 30:
                    self.numActiveExplosions -= 1
                    for i in range(50):
                        s.coords(self.explosions[explosion][0][i][0], -100, -100, -100, -100)
                    self.explosions.append(self.explosions.pop(explosion))
                else:
                    repeat = False
                
    
class Background():

    #Initialization
    def __init__(self, width, height):

        #Set base variables
        self.stars = []
        self.bgSpeed = 4
        self.width = width
        self.height = height

        #Create the stars
        for i in range(int(width/12)):
            
            x = randint(0, width)
            y = randint(0, height)
            size = randint(2, 3)
            self.stars.append((s.create_oval(x-size, y-size, x+size, y+size, fill = "white", outline = "white"), (x, y, size)))

    #Update for next frame
    def update(self):

        #Update every star
        for i in range(len(self.stars)):
        
            star, (x, y, size) = self.stars[i]

            #Move the star and if its off screen move it back to the top
            y += self.bgSpeed
            if y > self.height+size:
                x = randint(0, self.width)
                size = randint(2, 3)
                y = 0 - size
                
            s.coords(star, x-size, y-size, x+size, y+size)
                
            self.stars[i] = (star, (x, y, size))

        #Increase the background speed if the game is running
        if paused != True and menu != True and player.lives > 0 and player.isDead == False:
            self.bgSpeed += 0.0001388888888888

    #Reset the background speed for new game
    def reset(self):
        
        self.bgSpeed = 4
        
class Player():

    #Initialization
    def __init__(self):

        #Set base variables
        self.img = PhotoImage(file = "player.gif")
    
        self.object = s.create_image(-100, -100, image = self.img)
        
        self.x = 300
        self.y = 700
        
        self.forward = False
        self.backward = False
        self.right = False
        self.left = False
        
        self.xSpeed = 0
        self.ySpeed = 0
        
        self.lives = 3
        self.isDead = False
        self.canDie = True
        self.lastDeath = 0

        self.countdown = s.create_text(-1000, -1000, text = "3", font = "Arial 50", fill = "white")

        #Create bullets
        self.currentBullets = []
        self.availibleBullets = []
        for i in range(100):
            self.availibleBullets.append(Bullet())
        self.lastBulletFire = 0

        #Create rockets
        self.currentRockets = []
        self.availibleRockets = []
        for i in range(50):
            self.availibleRockets.append(Rocket())
        self.lastRocketFire = 0

    #Update for next frame
    def update(self):

        #Update if player is alive
        if self.isDead != True:

            #Reset speeds
            self.xSpeed = 0
            self.ySpeed = 0

            #Set speed based of directions
            if self.forward == True:
                self.ySpeed -= 5
            if self.backward == True:
                self.ySpeed += 5
            if self.right == True:
                self.xSpeed -= 5
            if self.left == True:
                self.xSpeed += 5

            #Move player
            self.x += self.xSpeed
            self.y += self.ySpeed

            #Keep player on screen
            if self.x - 24 < 0:
                self.x = 24
            elif self.x + 24 > 600:
                self.x = 576
            if self.y - 50 < 0:
                self.y = 0
            elif self.y + 50 > 800:
                self.y = 750

            #Check if the player hit an asteroid
            for asteroid in enemies.spawnedAsteroids:
                if asteroid.hasHit(self.x - 24, self.y - 50) or asteroid.hasHit(self.x + 24, self.y - 50) or asteroid.hasHit(self.x - 24, self.y + 50) or asteroid.hasHit(self.x + 24, self.y + 50):
                    self.die()

            #Check if the player hit an enemy ship
            for ship in enemies.spawnedShips:
                if ship.hasHit(self.x - 24, self.y - 50) or ship.hasHit(self.x + 24, self.y - 50) or ship.hasHit(self.x - 24, self.y + 50) or ship.hasHit(self.x + 24, self.y + 50):
                    self.die()
                    ship.destroy()

        #If the player is dead respawn them after 2 seconds
        else:
            if clock() - self.lastDeath > 2 and self.lives > 0:
                self.revive()

        #If the player is currently invincible after respawning, give them a countdown.
        if self.canDie == False and self.lives > 0:
            if clock() - self.lastDeath > 5:
                s.coords(self.countdown, -1000, -1000)
                self.canDie = True
            elif clock() - self.lastDeath > 2:
                s.tag_raise(self.countdown)
                s.coords(self.countdown, 300, 400)
                s.itemconfig(self.countdown, text = int(4 - (clock() - (self.lastDeath+2))))

        #Move player object
        s.coords(self.object, self.x, self.y)

        #Update bullets
        for bullet in self.currentBullets:
            if bullet.update() == True:
                self.availibleBullets.append(bullet)
                self.currentBullets.remove(bullet)

        #Update rockets
        for rocket in self.currentRockets:
            if rocket.update() == True:
                self.availibleRockets.append(rocket)
                self.currentRockets.remove(rocket)

    #Kill the player
    def die(self):

        #Kills player if the can die
        if self.canDie == True:
            self.lives -= 1
            s.itemconfig(livesText, text = "Lives left: " + str(self.lives - 1))
            self.isDead = True
            explosions.new(self.x, self.y, 50)
            self.x = -100
            self.y = -100
            self.canDie = False
            self.lastDeath = clock()

            #Ends game if out of lives
            if self.lives == 0:
                gameOver()

    #Make the playe respawn
    def revive(self):
        
        self.isDead = False
        self.x = 300
        self.y = 700

    #Shoot a bullet
    def fireBullet(self):

        #Shoots bullet if last bullet was shot more than 0.1 seconds ago and the player is alive
        if clock() - self.lastBulletFire > 0.1 and self.isDead == False and self.canDie == True:
        
            bullet = self.availibleBullets.pop()
            bullet.fire(self.x, self.y)
            self.currentBullets.append(bullet)
            
            self.lastBulletFire = clock()

    #Shoot rocket
    def fireRocket(self):

        #Shoots rocket if last rocket was shot more than 1 second ago and the player is alive
        if clock() - self.lastRocketFire > 1 and self.isDead == False and self.canDie == True:
        
            rocket = self.availibleRockets.pop()
            rocket.fire(self.x, self.y)
            self.currentRockets.append(rocket)
            
            self.lastRocketFire = clock()

    #Reset player lives and location for new game
    def reset(self):
        
        self.lives = 3
        self.isDead = False
        self.x = 300
        self.y = 700
        s.coords(self.object, -1000, -1000)
        s.itemconfig(livesText, text = "Lives left: 2")
    
class Bullet():

    #Initialization
    def __init__(self):
        
        self.object1 = s.create_line(0 , 0,0, 0, fill = "yellow")
        self.object2 = s.create_line(0, 0, 0, 0, fill = "yellow")

    #Shoot the bullet from x, y
    def fire(self, x, y):
        
        self.x = x
        self.y = y

    #Update for next frame
    def update(self):
        global score

        #Move bullet
        self.y -= 12
        
        s.coords(self.object1, self.x - 14, self.y - 6, self.x - 14, self.y + 6)
        s.coords(self.object2, self.x + 14, self.y - 6, self.x + 14, self.y + 6)

        #Checks if the bullet has hit an asteroid
        for asteroid in enemies.spawnedAsteroids:
            if asteroid.hasHit(self.x - 14, self.y + 8) or asteroid.hasHit(self.x + 14, self.y + 8):
                s.coords(self.object1, -100, -100, -100, -100)
                s.coords(self.object2, -100, -100, -100, -100)
                return True

        #Checks if the bullet has hit an enemy ship and destroy it if it has
        for ship in enemies.spawnedShips:
            if ship.hasHit(self.x - 14, self.y + 8) or ship.hasHit(self.x + 14, self.y + 8):
                s.coords(self.object1, -100, -100, -100, -100)
                s.coords(self.object2, -100, -100, -100, -100)
                ship.destroy()
                score += 100
                return True

        #Checks if the bullet is off screen
        if self.y + 6 < 0:
            return True
        else:
            return False
        
class Rocket():

    #Initialization
    def __init__(self):
        
        self.object = s.create_line(0 , 0, 0, 0, fill = "red", width = 4)

    #Shoot the rocket
    def fire(self, x, y):
        
        self.x = x
        self.y = y

    #Update for next frame
    def update(self):
        global score

        #Move the rocket
        self.y -= 12
        
        s.coords(self.object, self.x, self.y - 8, self.x, self.y + 8)

        #Checks if the rockets hit an asteroid and destroy it if it has
        for asteroid in enemies.spawnedAsteroids:
            if asteroid.hasHit(self.x, self.y + 8):
                asteroid.destroy()
                s.coords(self.object, -100, -100, -100, -100)
                score += 50
                return True
        #Checks if the rockets hit an enemy ship and destroy it if it has
        for ship in enemies.spawnedShips:
            if ship.hasHit(self.x, self.y + 8):
                s.coords(self.object, -100, -100, -100, -100)
                ship.destroy()
                score += 100
                return True

        #Checks if the rocket if off screen
        if self.y + 8 < 0:
            return True
        else:
            return False
        
class Enemies():

    #Initialization
    def __init__(self):

        #Create asteroids
        self.spawnedAsteroids = []
        self.availibleAsteroids = []
        for i in range(20):
            self.availibleAsteroids.append(Asteroid())

        #Create enemy ships
        self.spawnedShips = []
        self.availibleShips = []
        for i in range(20):
            self.availibleShips.append(EnemyShip())

        #Create bullet for enemy ships
        self.currentBullets = []
        self.availibleBullets = []
        for i in range(50):
            self.availibleBullets.append(EnemyBullet())

        self.lastSpawn = 0
        self.lastUpdate = 0

    #Update for next frame
    def update(self):

        #Checks if the last enemy was spawned more than a certain number of seconds ago based on the difficulty
        if clock() - self.lastUpdate > 0.5:
            self.lastSpawn = clock() - (self.lastUpdate - self.lastSpawn)
        if clock() - self.lastSpawn > difficulty/-2 + 2:
            #Spawn a new enemy
            self.spawn()
            self.lastSpawn = clock()

        #Update asteroids
        for asteroid in self.spawnedAsteroids:
            asteroid.update()
            if asteroid.y > 900:
                self.availibleAsteroids.append(asteroid)
                self.spawnedAsteroids.remove(asteroid)

        #Update enemy ships
        for ship in self.spawnedShips:
            ship.update()
            if ship.y > 900:
                self.availibleShips.append(ship)
                self.spawnedShips.remove(ship)

        #Update bullets
        for bullet in self.currentBullets:
            if bullet.update() == True:
                self.availibleBullets.append(bullet)
                self.currentBullets.remove(bullet)
                
        self.lastUpdate = clock()

    #Spawn a new enemy
    def spawn(self):

        #Randomly pick between an asteroid and a ship to spawn
        if randint(0, 1) == 0:
            #Spawn asteroid
            asteroid = self.availibleAsteroids.pop(0)
            asteroid.spawn()
            self.spawnedAsteroids.append(asteroid)
        else:
            #Spawn ship
            ship = self.availibleShips.pop()
            ship.spawn()
            self.spawnedShips.append(ship)
                
    def reset(self):

        #Move asteroids off screen
        for asteroid in self.spawnedAsteroids:
            
            s.coords(asteroid.object, -1000, -1000)
            
            self.availibleAsteroids.append(asteroid)
            self.spawnedAsteroids.remove(asteroid)

        #Move ships off screen
        for ship in self.spawnedShips:
            
            s.coords(ship.object, -1000, -1000)
            
            self.availibleShips.append(ship)
            self.spawnedShips.remove(ship)
        
class Asteroid():

    #Initialization
    def __init__(self):
        
        self.image = asteroidImgs[randint(0, 3)]
        self.object = s.create_image(-300, -300, image = self.image)

    #Spawn asteroid
    def spawn(self):

        #Set speed based on difficulty
        self.speed = difficulty*2

        #Set starting values
        self.x = randint(int(self.image.width()/2), int(600-self.image.width()/2))
        self.y = -self.image.height()/2

    #Update for next frame
    def update(self):

        #Checks if the asteroid is off screen
        if self.y > 900:
            return

        #Move asteroid based of speed and background speed
        self.y += self.speed + background.bgSpeed
        
        s.coords(self.object, self.x, self.y)

    #Checks if x, y is inside the asteroid
    def hasHit(self, x, y):
        
        xDiff = abs(self.x - x)
        yDiff = abs(self.y - y)
        
        if xDiff < self.image.width()/2 - 5 and yDiff < self.image.height()/2 - 5:
            return True
        else:
            return False

    #Destory the asteroid
    def destroy(self):

        #Create an explosion
        explosions.new(self.x, self.y, int(self.image.width()/2))

        #Move asteroid off screen
        self.y = 901
        s.coords(self.object, self.x, self.y)
        
class EnemyShip():

    #Initialization
    def __init__(self):
        
        self.object = s.create_image(-300, -300, image = enemyShipImg)

    #Spawn ship
    def spawn(self):

        #Set speed based on difficulty
        self.xSpeed = 0
        self.ySpeed = difficulty*2

        #Set starting position
        self.x = randint(int(enemyShipImg.width()/2), int(600-enemyShipImg.width()/2))
        self.y = -enemyShipImg.height()/2
        
        self.lastShot = clock()-5

    #Update for next frame
    def update(self):

        #Check if ship is off screen
        if self.y > 900:
            return

        #Make the ship follow the player with it reaction time based on difficulty
        if self.y < player.y and randint(0, (-difficulty + 4)*25) == 0:
            
            if self.x < player.x-15:
                self.xSpeed = difficulty
            elif self.x > player.x+15:
                self.xSpeed = -difficulty

        #Move ship based on speeds
        self.x += self.xSpeed
        self.y += self.ySpeed + background.bgSpeed
        
        s.coords(self.object, self.x, self.y)

        #Shoots a bullet if last bullet was shot more than 0.5 seconds ago
        if clock() - self.lastShot > 0.5:
            self.shoot()

    #Shoots a bullet 
    def shoot(self):
        
        bullet = enemies.availibleBullets.pop()
        bullet.fire(self.x, self.y)
        enemies.currentBullets.append(bullet)
            
        self.lastShot = clock()

    #Checks if x, y if inside the ship
    def hasHit(self, x, y):
        
        xDiff = abs(self.x - x)
        yDiff = abs(self.y - y)
        
        if xDiff < enemyShipImg.width()/2 - 5 and yDiff < enemyShipImg.height()/2 - 5:
            return True
        else:
            return False

    #Destroy the ship
    def destroy(self):

        #Create a new explosion
        explosions.new(self.x, self.y, int(enemyShipImg.width()/2))

        #Move the ship off screen
        self.y = 901
        s.coords(self.object, self.x, self.y)
        
class EnemyBullet():

    #Initialization
    def __init__(self):
        
        self.object = s.create_line(0 , 0, 0, 0, fill = "yellow")

    #Shoot the bullet from x, y
    def fire(self, x, y):
        
        self.x = x
        self.y = y

    #Update for next frame
    def update(self):

        #Move the bullet
        self.y += 12
        
        s.coords(self.object, self.x, self.y - 6, self.x, self.y + 6)

        #Checks if the bullet has hit the player and kill the player if it has
        if abs(self.x - player.x) <= 24 and abs(self.y - player.y) <= 50:
            s.coords(self.object, -100, -100, -100, -100)
            player.die()
            return True

        #Checks if the bullet if off screen
        if self.y - 6 > 800:
            return True
        else:
            return False
    
#MAIN FUNCTION
def runGame():
    global score

    #Set up global variables
    initializeVariables()

    #Open the main menu
    mainMenu()

    #While the player isn't closing the window update the game
    while exiting == False:
        
        startTime = clock()

        #Update the background stars
        background.update()

        #If the game if running update the game
        if paused != True and menu != True:

            #Update the player
            player.update()

            #If the player isn't dead, update the enemies
            if player.canDie == True or player.lives == 0:
                enemies.update()

            #Update the explosions
            explosions.update()

            #Update the score if the player is alive
            if player.lives > 0 and player.canDie == True:
                score += 0.166666666666
                s.itemconfig(scoreText, text = "Score: " + str(round(score)))

        #Update the screen for the user to see
        root.update()

        #Keep the game running at 60 fps
        endTime = clock()
        runTime = endTime - startTime
        sleepTime = (0.01666666666 - runTime)
        if sleepTime > 0:
            sleep(sleepTime)

    #Destroy the applicatin if the user is quiting
    root.destroy()

#Bind events to their respective procedures
root.bind_all("<Button-1>", leftMouseDown)
root.bind_all("<Button-3>", rightMouseDown)
root.bind_all("<Motion>", mouseMove)
root.bind_all("<Key>", keyDown)
root.bind_all("<KeyRelease>", keyUp)
root.protocol("WM_DELETE_WINDOW", windowClose)

#Run the game
root.after(0, runGame)

#Enter the event loop
root.mainloop()
