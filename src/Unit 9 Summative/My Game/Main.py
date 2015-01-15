'''
Created on Jan 11, 2015

@author: Jacob
'''
from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from random import *
from time import sleep
from datetime import *

root = Tk()
root.title("Unnamed Game")

s = Canvas(root, height = 800, width = 600, bg = "black")
s.pack()

#INITIALIZERS
def initializeVariables():
    global player, background, lives, difficulty, score, menu, paused, mouse, keys, exiting
    global buttons
    
    difficulty = 1
    score = 0
    menu = True
    paused = False
    exiting = False
    
    background = Background()
    player = Player()
    
    buttons = {}
    buttons['start'] = Button(300, 400, 200, 100, startGame, text = "Start Game")
    buttons['easy'] = Button(175, 500, 75, 50, lambda: setDifficulty(1), text = "Easy")
    s.itemconfig(buttons['easy'].content1, fill = "green")
    buttons['medium'] = Button(300, 500, 125, 50, lambda: setDifficulty(2), text = "Medium")
    buttons['hard'] = Button(425, 500, 75, 50, lambda: setDifficulty(3), text = "Hard")
    buttons['pause'] = Button(25, 25, 20, 20, pauseGame, image = "pause.gif")
    buttons['resume'] = Button(300, 400, 200, 100, unpauseGame, text = "Resume")
    buttons['quit'] = Button(300, 600, 200, 100, windowClose, text = "Quit Game")
    
    
    
def setDifficulty(diff):
    global difficulty
    
    difficultly = diff
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
    
    menu = False
    buttons['start'].deactivate()
    buttons['easy'].deactivate()
    buttons['medium'].deactivate()
    buttons['hard'].deactivate()
    buttons['quit'].deactivate()
    buttons['pause'].activate()
    
def pauseGame():
    global paused 
    
    paused = True
    buttons['pause'].deactivate()
    buttons['resume'].activate()
    buttons['quit'].activate()
    
def unpauseGame():
    global paused
    
    paused = False
    buttons['resume'].deactivate()
    buttons['quit'].deactivate()
    buttons['pause'].activate()
        
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
    global mouse
    
    player.fireRocket()
    
def rightMouseUp(event):
    global mouse
    
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
    if event.keysym == "a":
        player.right = True
    if event.keysym == "s":
        player.backward = True
    if event.keysym == "d":
        player.left = True
        
    if event.keysym == "Escape":
        if menu == False:
            if paused == True:
                unpauseGame()
            else:
                pauseGame()
    
def keyUp(event):
    global paused
    
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
            
        if paused != True and menu != True:
            self.bgSpeed += 0.00027777777777
        
class Player():
    
    def __init__(self):
        
        self.img = PhotoImage(file = "ship.gif")
    
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
    global score
    
    initializeVariables()
    
    buttons['start'].activate()
    buttons['easy'].activate()
    buttons['medium'].activate()
    buttons['hard'].activate()
    buttons['quit'].activate()
    
    scoreO = s.create_text(590, 10, text = "Score: " + str(score), font = "Arial 15", fill = "white", anchor = NE)
    
    while exiting == False:
        
        startTime = int(str(datetime.now().time())[9:])
        
        if paused == True or menu == True:
            
            background.update()
            
        else:
        
            if player.lives > 0:
                
                background.update()
                player.update()
                
                score += 0.3333333333
                s.itemconfig(scoreO, text = "Score: " + str(round(score)))
                
            else:
                
                pass
        
        root.update()
        
        endTime = int(str(datetime.now().time())[9:])
        runTime = endTime - startTime
        if runTime < 0:
            runTime += 1000000
        sleepTime = (33333 - runTime) / 1000000
        
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