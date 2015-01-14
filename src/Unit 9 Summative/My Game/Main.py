'''
Created on Jan 11, 2015

@author: Jacob
'''
from tkinter import *
from tkinter.messagebox import *
from random import *
from time import sleep
from datetime import *

root = Tk()
root.title("Unnamed Game")

s = Canvas(root, height = 800, width = 600, bg = "black")
s.pack()

#INITIALIZERS
def initializeVariables():
    global lives, difficulty, score, paused, mouse, keys, exiting
    global bullets, rockets
    
    lives = 3
    difficulty = "easy"
    score = 0
    paused = False
    exiting = False
    
    availibleBullets = []
    for i in range(100):
        availibleBullets.append((s.create_line(-100, -100, -100, -100, fill = "yellow"),
                        s.create_line(-100, -100, -100, -100, fill = "yellow"),
                        -100, -100))
    bullets = []
    rockets = []
    
    keys = {}
    mouse = {'loc': (0, 0), 'left': False, 'right': False}
        
#HANDLERS
def leftMouseDown(event):
    
    player.fireBullet()
    
def leftMouseUp(event):
    
    pass
    
def rightMouseDown(event):
    global mouse
    
    player.fireRocket()
    
def rightMouseUp(event):
    global mouse
    
    pass
    
def mouseMove(event):
    global mouse
    
    mouse['loc'] = (event.x, event.y)
    
def keyDown(event):
    global keys
    
    if event.keysym == "w":
        player.forward = True
    if event.keysym == "a":
        player.right = True
    if event.keysym == "s":
        player.backward = True
    if event.keysym == "d":
        player.left = True
    
def keyUp(event):
    global keys
    
    if event.keysym == "w":
        player.forward = False
    if event.keysym == "a":
        player.right = False
    if event.keysym == "s":
        player.backward = False
    if event.keysym == "d":
        player.left = False
    
def windowClose():
    global exiting
    
    if askyesno("Quit", "Are you sure you want to quit?"):
        
        exiting = True
    
class Background():
    
    def __init__(self):
        
        self.stars = []
        self.bgSpeed = 4
        
        for i in range(50):
            
            x = randint(0, 600)
            y = randint(0, 800)
            size = randint(2, 3)
            self.stars.append((s.create_oval(x-size, y-size, x+size, y+size, fill = "white", outline = "white"), (x, y, size)))
            
    def update(self):
        
        for i in range(len(self.stars)):
        
            star, (x, y, size) = self.stars[i]
            
            y += self.bgSpeed
            if y > 800+size:
                x = randint(0, 600)
                size = randint(2, 3)
                y = 0 - size
                
            s.coords(star, x-size, y-size, x+size, y+size)
                
            self.stars[i] = (star, (x, y, size))
            
        self.bgSpeed += 0.00027777777777
        
class Player():
    
    def __init__(self):
        
        self.img = PhotoImage(file = "ship.gif")
    
        self.object = s.create_image(300, 700, image = self.img)
        
        self.x = 300
        self.y = 700
        
        self.forward = False
        self.backward = False
        self.right = False
        self.left = False
        
        self.xSpeed = 0
        self.ySpeed = 0
        
        self.currentBullets = []
        self.availibleBullets = []
        for i in range(100):
            self.availibleBullets.append(Bullet())
        self.currentRockets = []
        
        self.availibleRockets = []
        for i in range(50):
            self.availibleRockets.append(Rocket())
        
    def update(self):
        
        self.xSpeed = 0
        self.ySpeed = 0
        
        if self.forward == True:
            self.ySpeed -= 8
        if self.backward == True:
            self.ySpeed += 8
        if self.right == True:
            self.xSpeed -= 8
        if self.left == True:
            self.xSpeed += 8
        
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
        
        s.coords(self.object, self.x, self.y)
        
        for bullet in self.currentBullets:
            if bullet.update() == True:
                self.availibleBullets.append(bullet)
                self.currentBullets.remove(bullet)
                
        for rocket in self.currentRockets:
            if rocket.update() == True:
                self.availibleRockets.append(rocket)
                self.currentRockets.remove(rocket)
        
    def fireBullet(self):
        
        bullet = self.availibleBullets.pop()
        
        bullet.fire(self.x, self.y)
        
        self.currentBullets.append(bullet)
    
    def fireRocket(self):
        
        rocket = self.availibleRockets.pop()
        
        rocket.fire(self.x, self.y)
        
        self.currentRockets.append(rocket)
    
class Bullet():
    
    def __init__(self):
        
        self.object1 = s.create_line(0 , 0,0, 0, fill = "yellow")
        self.object2 = s.create_line(0, 0, 0, 0, fill = "yellow")
        
    def fire(self, x, y):
        
        self.x = x
        self.y = y
        
    def update(self):
        
        self.y -= 12
        
        s.coords(self.object1, self.x - 14, self.y - 4, self.x - 14, self.y + 4)
        s.coords(self.object2, self.x + 14, self.y - 4, self.x + 14, self.y + 4)

        if self.y + 4 < 0:
            return True
        else:
            return False
        
class Rocket():
    
    def __init__(self):
        
        self.object1 = s.create_line(0 , 0,0, 0, fill = "yellow")
        
    def fire(self, x, y):
        
        self.x = x
        self.y = y
        
    def update(self):
        
        self.y -= 12
        
        s.coords(self.object1, self.x, self.y - 4, self.x, self.y + 4)

        if self.y + 4 < 0:
            return True
        else:
            return False
    
#MAIN FUNCTION
def runGame():
    global lives, score, paused, player
    
    initializeVariables()
    background = Background()
    
    #DO MENU STUFF HERE
    
    player = Player()
    scoreO = s.create_text(590, 10, text = "Score: " + str(score), font = "Times 15", fill = "white", anchor = NE)
    
    while lives > 0:
        
        startTime = int(str(datetime.now().time())[9:])
        
        if paused == False:
        
            background.update()
            player.update()
            
            score += 0.3333333333
            s.itemconfig(scoreO, text = "Score: " + str(round(score)))
        
        root.update()
        
        if exiting == True:
            root.destroy()
            break
        
        endTime = int(str(datetime.now().time())[9:])
        runTime = endTime - startTime
        if runTime < 0:
            runTime += 1000000
        sleepTime = (33333 - runTime) / 1000000
        
        if sleepTime > 0:
            sleep(sleepTime)
    
s.bind("<Button-1>", leftMouseDown)
s.bind("<ButtonRelease-1>", leftMouseUp)
s.bind("<Button-3>", rightMouseDown)
s.bind("<ButtonRelease-3>", rightMouseUp)
s.bind("<Motion>", mouseMove)
root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)
root.protocol("WM_DELETE_WINDOW", windowClose)

root.after(0, runGame)

root.mainloop()