'''
Created on Jan 11, 2015

@author: Jacob
'''
from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from random import *
from time import sleep, clock
from datetime import *
from math import *
from threading import Timer

root = Tk()
root.title("Unnamed Game")
root.resizable(FALSE, FALSE)

s = Canvas(root, height = 800, width = 600, bg = "black")
s.grid(row = 0, column = 0)

#INITIALIZERS
def initializeVariables():
    global player, asteroidImgs, enemies, background, explosions
    global lives, difficulty, score
    global menu, paused, exiting
    global buttons
    global scoreText, pausedText, gameOverText, finalScoreText, gameTitleText, livesText
    
    difficulty = 1
    
    score = 0
    
    menu = True
    paused = False
    exiting = False
    
    background = Background(600, 800)
    
    player = Player()
    
    asteroidImgs = [PhotoImage(file = "asteroid1.gif"), PhotoImage(file = "asteroid2.gif"), PhotoImage(file = "asteroid3.gif"), PhotoImage(file = "asteroid4.gif")]
    enemies = Enemies()
    
    explosions = Explosion()
    
    gameTitleText = s.create_text(-1000, -1000, text = "Unnamed Game", font = "Arial 55", fill = "white")
    scoreText = s.create_text(-1000, -1000, text = "Score: 0", font = "Arial 15", fill = "white", anchor = NE)
    livesText = s.create_text(-1000, -1000, text = "Lives left: 2", font = "Arial 15", fill = "white", anchor = SW)
    finalScoreText = s.create_text(-1000, -1000, text = "Score: ", font = "Arial 30", fill = "white")
    pausedText = s.create_text(-1000, -1000, text = "Paused", font = "Arial 60", fill = "white")
    gameOverText = s.create_text(-1000, -1000, text = "Game Over", font = "Arial 40", fill = "white")
    
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
    
    
def resetGame():
    global paused, score
    
    score = 0
    paused = False
    
    s.coords(pausedText, -1000, -1000)
    s.coords(scoreText, -1000, -1000)
    s.coords(livesText, -1000, -1000)
    s.coords(finalScoreText, -1000, -1000)
    s.coords(gameOverText, -1000, -1000)
    s.coords(gameTitleText, -1000, -1000)
    
    background.reset()
    player.reset()
    enemies.reset()
    
def setDifficulty(diff):
    global difficulty
    
    difficulty = diff
    if diff == 1:
        s.itemconfig(buttons['easy'].content1, fill = "green")
        s.itemconfig(buttons['medium'].content1, fill = "white")
        s.itemconfig(buttons['hard'].content1, fill = "white")
    elif diff == 2:
        s.itemconfig(buttons['easy'].content1, fill = "white")
        s.itemconfig(buttons['medium'].content1, fill = "green")
        s.itemconfig(buttons['hard'].content1, fill = "white")
    elif diff == 3:
        s.itemconfig(buttons['easy'].content1, fill = "white")
        s.itemconfig(buttons['medium'].content1, fill = "white")
        s.itemconfig(buttons['hard'].content1, fill = "green")
    
def startGame():
    global menu
    
    resetGame()
    
    menu = False
    
    s.coords(scoreText, 590, 10)
    s.coords(livesText, 10, 790)
    
    buttons['start'].deactivate()
    buttons['easy'].deactivate()
    buttons['medium'].deactivate()
    buttons['hard'].deactivate()
    buttons['quit'].deactivate()
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['playagain'].deactivate()
    buttons['helpcontrols'].deactivate()
    
    buttons['pause'].activate()
    
def mainMenu():
    global menu
    
    resetGame()
    
    menu = True
    
    s.coords(gameTitleText, 300, 200)
    
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['playagain'].deactivate()
    
    buttons['start'].activate()
    buttons['easy'].activate()
    buttons['medium'].activate()
    buttons['hard'].activate()
    buttons['quit'].activate()
    buttons['helpcontrols'].activate()
    
def helpControls():
    
    pass
    
def pauseGame():
    global paused 
    
    paused = True
    
    s.coords(pausedText, 300, 200)
    
    buttons['pause'].deactivate()
    
    buttons['resume'].activate()
    buttons['menu'].activate()
    buttons['quit'].activate()
    buttons['helpcontrols'].activate()
    
def unpauseGame():
    global paused
    
    paused = False
    
    s.coords(pausedText, -1000, -1000)
    
    buttons['resume'].deactivate()
    buttons['menu'].deactivate()
    buttons['quit'].deactivate()
    buttons['helpcontrols'].deactivate()
    
    buttons['pause'].activate()
    
def gameOver():
    
    s.coords(scoreText, -1000, -1000)
    s.coords(livesText, -1000, -1000)
    
    s.coords(gameOverText, 300 , 200)
    s.coords(finalScoreText, 300, 250)
    s.itemconfig(finalScoreText, text = "Score: " + str(round(score)))
    
    buttons['pause'].deactivate()
    
    buttons['menu'].activate()
    buttons['quit'].activate()
    buttons['playagain'].activate()
    buttons['helpcontrols'].activate()
        
#HANDLERS
def leftMouseDown(event):
    
    for button in buttons.values():
        if button.active:
            if button.isOver(event.x, event.y):
                button.click()
                return
            
    if paused == False and menu == False:
        player.fireBullet()
    
def leftMouseUp(event):
    
    pass
    
def rightMouseDown(event):
    
    if paused == False and menu == False:
        player.fireRocket()
    
def rightMouseUp(event):
    
    pass
    
def mouseMove(event):
    
    for button in buttons.values():
        if button.active:
            if button.isOver(event.x, event.y):
                root.config(cursor = button.cursor)
                break
            else:
                root.config(cursor = "")
    
def keyDown(event):
    global paused
    
    if event.keysym == "w":
        player.forward = True
    elif event.keysym == "a":
        player.right = True
    elif event.keysym == "s":
        player.backward = True
    elif event.keysym == "d":
        player.left = True
        
    elif event.keysym == "e":
        if paused == False and menu == False:
            player.fireBullet()
    elif event.keysym == "q":
        if paused == False and menu == False:
            player.fireRocket()
        
    elif event.keysym == "Escape":
        if menu == False:
            if paused == True:
                unpauseGame()
            else:
                pauseGame()
    
def keyUp(event):
    global paused
    
    if event.keysym == "w":
        player.forward = False
    elif event.keysym == "a":
        player.right = False
    elif event.keysym == "s":
        player.backward = False
    elif event.keysym == "d":
        player.left = False
    
def windowClose():
    global exiting
    
    if askyesno("Quit", "Are you sure you want to quit?"):
        
        exiting = True
        
class Button():
    
    def __init__(self, x, y, maxWidth, maxHeight, command, text = "", image = "", cursor = "hand2"):
        
        self.x = x
        self.y = y
        self.width = maxWidth
        self.height = maxHeight
        
        self.command = command
        
        self.text = text
        if text != "":
            fontsize, self.width, self.height = self.getFontSize(text, maxWidth, maxHeight)
            self.font = "Arial " + str(fontsize)
        else:
            self.font = "Arial 10"
            
        if image != "":
            self.image = PhotoImage(file = image)
        else:
            self.image = None
            
        self.cursor = cursor
        
        self.active = False
        
        self.content1 = s.create_text(-100, -100, text = self.text, font = self.font, fill = "white")
        self.content2 = s.create_image(-100, -100, image = self.image)
        
    def activate(self):
        
        self.active = True
        s.coords(self.content1, self.x, self.y)
        s.coords(self.content2, self.x, self.y)
        
    def deactivate(self):
        
        self.active = False
        s.coords(self.content1, -100, -100)
        s.coords(self.content2, -100, -100)
        
    def isOver(self, x, y):
        
        if x > self.x - self.width/2 and x < self.x + self.width/2 and y > self.y - self.height/2 and y < self.y + self.height/2:
            return True
        else:
            return False
        
    def click(self):
        self.command()
            
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
            
class Explosion():
    
    def __init__(self):
        
        self.numActiveExplosions = 0
        
        self.explosions = []
        self.explosions.append([[], -100, -100, 0, 0])
        for i in range(50):
            self.explosions[0][0].append([s.create_oval(-100, -100, -100, -100, fill = choice(["yellow", "orange", "red"])), randint(5, 10), randint(0, 360), 0])
            
    def new(self, x, y, r):
        
        self.numActiveExplosions += 1
        
        if self.numActiveExplosions > len(self.explosions):
            self.explosions.append([[], x, y, r, r])
            for i in range(50):
                self.explosions[len(self.explosions)-1][0].append([s.create_oval(-100, -100, -100, -100, fill = choice(["yellow", "orange", "red"])), randint(5, 10), randint(0, 360), 0])
        else:
            self.explosions[self.numActiveExplosions-1][1] = x
            self.explosions[self.numActiveExplosions-1][2] = y
            self.explosions[self.numActiveExplosions-1][3] = r
            self.explosions[self.numActiveExplosions-1][4] = r
            for i in range(50):
                self.explosions[self.numActiveExplosions-1][0][i][3] = randint(0, r)
            
    def update(self):
        
        for explosion in range(self.numActiveExplosions):
            
            if explosion == self.numActiveExplosions:
                break
            
            repeat = True
            while repeat == True and self.numActiveExplosions > 0:
            
                for i in range(len(self.explosions[explosion][0])):
                
                    size = self.explosions[explosion][0][i][1]
                    xMove = self.explosions[explosion][0][i][3]*cos(radians(self.explosions[explosion][0][i][2]))
                    yMove = self.explosions[explosion][0][i][3]*sin(radians(self.explosions[explosion][0][i][2]))
                    s.coords(self.explosions[explosion][0][i][0], self.explosions[explosion][1]+xMove-size, self.explosions[explosion][2]+yMove-size, self.explosions[explosion][1]+xMove+size, self.explosions[explosion][2]+yMove+size)
                    self.explosions[explosion][0][i][3] += 1
                    
                self.explosions[explosion][4] += 1
                if self.explosions[explosion][4] - self.explosions[explosion][3] > 30:
                    self.numActiveExplosions -= 1
                    for i in range(50):
                        s.coords(self.explosions[explosion][0][i][0], -100, -100, -100, -100)
                    self.explosions.append(self.explosions.pop(explosion))
                else:
                    repeat = False
                
    
class Background():
    
    def __init__(self, width, height):
        
        self.stars = []
        self.bgSpeed = 4
        
        self.width = width
        self.height = height
        
        for i in range(int(width/12)):
            
            x = randint(0, width)
            y = randint(0, height)
            size = randint(2, 3)
            self.stars.append((s.create_oval(x-size, y-size, x+size, y+size, fill = "white", outline = "white"), (x, y, size)))
            
    def update(self):
        
        for i in range(len(self.stars)):
        
            star, (x, y, size) = self.stars[i]
            
            y += self.bgSpeed
            if y > self.height+size:
                x = randint(0, self.width)
                size = randint(2, 3)
                y = 0 - size
                
            s.coords(star, x-size, y-size, x+size, y+size)
                
            self.stars[i] = (star, (x, y, size))
            
        if paused != True and menu != True and player.lives > 0 and player.isDead == False:
            self.bgSpeed += 0.0001388888888888
            
    def reset(self):
        
        self.bgSpeed = 4
        
class Player():
    
    def __init__(self):
        
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
        
        self.currentBullets = []
        self.availibleBullets = []
        for i in range(100):
            self.availibleBullets.append(Bullet())
        self.lastBulletFire = 0
            
        self.currentRockets = []
        self.availibleRockets = []
        for i in range(50):
            self.availibleRockets.append(Rocket())
        self.lastRocketFire = 0
        
        self.countdown = s.create_text(-1000, -1000, text = "3", font = "Arial 50", fill = "white")
        
    def update(self):
        
        if self.isDead != True:
        
            self.xSpeed = 0
            self.ySpeed = 0
            
            if self.forward == True:
                self.ySpeed -= 5
            if self.backward == True:
                self.ySpeed += 5
            if self.right == True:
                self.xSpeed -= 5
            if self.left == True:
                self.xSpeed += 5
            
            self.x += self.xSpeed
            self.y += self.ySpeed
            
            if self.x - 24 < 0:
                self.x = 24
            elif self.x + 24 > 600:
                self.x = 576
            if self.y - 50 < 0:
                self.y = 0
            elif self.y + 50 > 800:
                self.y = 750
            
            for asteroid in enemies.spawnedAsteroids:
                if asteroid.hasHit(self.x - 24, self.y - 50) or asteroid.hasHit(self.x + 24, self.y - 50) or asteroid.hasHit(self.x - 24, self.y + 50) or asteroid.hasHit(self.x + 24, self.y + 50):
                    self.die()
        
        else:
            if clock() - self.lastDeath > 2 and self.lives > 0:
                self.revive()
                
        if self.canDie == False and self.lives > 0:
            if clock() - self.lastDeath > 5:
                s.coords(self.countdown, -1000, -1000)
                self.canDie = True
            elif clock() - self.lastDeath > 2:
                s.tag_raise(self.countdown)
                s.coords(self.countdown, 300, 400)
                s.itemconfig(self.countdown, text = int(4 - (clock() - (self.lastDeath+2))))
                    
        s.coords(self.object, self.x, self.y)
        
        for bullet in self.currentBullets:
            if bullet.update() == True:
                self.availibleBullets.append(bullet)
                self.currentBullets.remove(bullet)
                
        for rocket in self.currentRockets:
            if rocket.update() == True:
                self.availibleRockets.append(rocket)
                self.currentRockets.remove(rocket)
                
    def die(self):
        
        if self.canDie == True:
            self.lives -= 1
            s.itemconfig(livesText, text = "Lives left: " + str(self.lives - 1))
            self.isDead = True
            explosions.new(self.x, self.y, 50)
            self.x = -100
            self.y = -100
            self.canDie = False
            self.lastDeath = clock()
            
            if self.lives == 0:
                gameOver()
        
    def revive(self):
        
        self.isDead = False
        self.x = 300
        self.y = 700
        
    def fireBullet(self):
        
        if clock() - self.lastBulletFire > 0.1 and self.isDead == False and self.canDie == True:
        
            bullet = self.availibleBullets.pop()
            bullet.fire(self.x, self.y)
            self.currentBullets.append(bullet)
            
            self.lastBulletFire = clock()
    
    def fireRocket(self):
        
        if clock() - self.lastRocketFire > 1 and self.isDead == False and self.canDie == True:
        
            rocket = self.availibleRockets.pop()
            rocket.fire(self.x, self.y)
            self.currentRockets.append(rocket)
            
            self.lastRocketFire = clock()
            
    def reset(self):
        
        self.lives = 3
        self.isDead = False
        self.x = 300
        self.y = 700
        s.coords(self.object, -1000, -1000)
        s.itemconfig(livesText, text = "Lives left: 2")
    
class Bullet():
    
    def __init__(self):
        
        self.object1 = s.create_line(0 , 0,0, 0, fill = "yellow")
        self.object2 = s.create_line(0, 0, 0, 0, fill = "yellow")
        
    def fire(self, x, y):
        
        self.x = x
        self.y = y
        
    def update(self):
        
        self.y -= 12
        
        s.coords(self.object1, self.x - 14, self.y - 6, self.x - 14, self.y + 6)
        s.coords(self.object2, self.x + 14, self.y - 6, self.x + 14, self.y + 6)
        
        for asteroid in enemies.spawnedAsteroids:
            if asteroid.hasHit(self.x - 14, self.y + 8) or asteroid.hasHit(self.x + 14, self.y + 8):
                s.coords(self.object1, -100, -100, -100, -100)
                s.coords(self.object2, -100, -100, -100, -100)
                return True

        if self.y + 6 < 0:
            return True
        else:
            return False
        
class Rocket():
    
    def __init__(self):
        
        self.object = s.create_line(0 , 0, 0, 0, fill = "red", width = 4)
        
    def fire(self, x, y):
        
        self.x = x
        self.y = y
        
    def update(self):
        global score
        
        self.y -= 12
        
        s.coords(self.object, self.x, self.y - 8, self.x, self.y + 8)
        
        for asteroid in enemies.spawnedAsteroids:
            if asteroid.hasHit(self.x, self.y + 8):
                asteroid.destroy()
                s.coords(self.object, -100, -100, -100, -100)
                score += 50
                return True

        if self.y + 8 < 0:
            return True
        else:
            return False
        
class Enemies():
    
    def __init__(self):
        
        self.spawnedAsteroids = []
        self.availibleAsteroids = []
        for i in range(20):
            self.availibleAsteroids.append(Asteroid())
        
#         self.spawnedShips = []
#         self.availibleShips = []
#         for i in range(20):
#             self.availibleShips.append(Ship())

        self.lastSpawn = 0
        self.lastUpdate = 0

    def update(self):
        
        if clock() - self.lastUpdate > 0.5:
            self.lastSpawn = clock() - (self.lastUpdate - self.lastSpawn)
        
        if clock() - self.lastSpawn > difficulty/-2 + 2:
            self.spawn()
            self.lastSpawn = clock()
        
        for asteroid in self.spawnedAsteroids:
            asteroid.update()
            if asteroid.y > 900:
                self.availibleAsteroids.append(asteroid)
                self.spawnedAsteroids.remove(asteroid)
                
        self.lastUpdate = clock()
            
    def spawn(self):
        
        if randint(0, 1) < 2:
            asteroid = self.availibleAsteroids.pop(0)
            if asteroid.spawn():
                self.spawnedAsteroids.append(asteroid)
            else:
                self.availibleAsteroids.append(asteroid)
                
    def reset(self):
        
        for asteroid in self.spawnedAsteroids:
            
            s.coords(asteroid.object, -1000, -1000)
            
            self.availibleAsteroids.append(asteroid)
            self.spawnedAsteroids.remove(asteroid)
        
class Asteroid():
    
    def __init__(self):
        
        self.image = asteroidImgs[randint(0, 3)]
        self.object = s.create_image(-300, -300, image = self.image)
        self.speed = difficulty*2
        
    def spawn(self):
        
        self.x = randint(int(self.image.width()/2), int(600-self.image.width()/2))
        self.y = -self.image.height()/2
        return True
        
    def update(self):
        
        if self.y > 900:
            return
        
        self.y += self.speed + background.bgSpeed
        
        s.coords(self.object, self.x, self.y)
        
    def hasHit(self, x, y):
        
        xDiff = abs(self.x - x)
        yDiff = abs(self.y - y)
        
        if xDiff < self.image.width()/2 - 5 and yDiff < self.image.height()/2 - 5:
            
            return True
        
        else:
            
            return False
        
    def destroy(self):
        
        explosions.new(self.x, self.y, 62)
        self.y = 901
        s.coords(self.object, self.x, self.y)
    
#MAIN FUNCTION
def runGame():
    global score
    
    initializeVariables()
    
    mainMenu()
    
    while exiting == False:
        
        startTime = clock()
        
        if paused == True or menu == True:
            
            background.update()
            
        else:
                
            background.update()
            
            player.update()
                
            if player.canDie == True or player.lives == 0:
                enemies.update()
                
            explosions.update()
            
            if player.lives > 0 and player.canDie == True:
                score += 0.166666666666
                s.itemconfig(scoreText, text = "Score: " + str(round(score)))
        
        root.update()
        
        endTime = clock()
        runTime = endTime - startTime
        sleepTime = (0.01666666666 - runTime)
        
        if sleepTime > 0:
            sleep(sleepTime)
            
    root.destroy()
    
root.bind_all("<Button-1>", leftMouseDown)
root.bind_all("<ButtonRelease-1>", leftMouseUp)
root.bind_all("<Button-3>", rightMouseDown)
root.bind_all("<ButtonRelease-3>", rightMouseUp)
root.bind_all("<Motion>", mouseMove)
root.bind_all("<Key>", keyDown)
root.bind_all("<KeyRelease>", keyUp)
root.protocol("WM_DELETE_WINDOW", windowClose)

root.after(0, runGame)

root.mainloop()