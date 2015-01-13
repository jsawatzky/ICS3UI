'''
Created on Jan 11, 2015

@author: Jacob
'''
from tkinter import *
from random import *
from time import sleep
from datetime import *

root = Tk()
root.title("Unnamed Game")

s = Canvas(root, height = 800, width = 600, bg = "black")
s.pack()

#INITIALIZERS
def initializeVariables():
    global lives, difficulty, score, paused, mouse, keys, quitting
    global bullets, rockets
    
    lives = 3
    difficulty = "easy"
    score = 0
    paused = False
    quitting = False
    
    availibleBullets = []
    for i in range(100):
        bullets.append((s.create_line(-100, -100, -100, -100, fill = "yellow", outline = "yellow"),
                        s.create_line(-100, -100, -100, -100, fill = "yellow", outline = "yellow"),
                        -100, -100))
    bullets = []
    rockets = []
    
    keys = {}
    mouse = {'loc': (0, 0), 'left': False, 'right': False}

def initializeBackground():
    global stars, bgSpeed
    
    stars = []
    bgSpeed = 2
    
    for i in range(50):
        
        x = randint(0, 600)
        y = randint(0, 800)
        size = randint(2, 3)
        stars.append((s.create_oval(x-size, y-size, x+size, y+size, fill = "white", outline = "white"), (x, y, size)))
        
def initializePlayer():
    global player, shipImg
    
    shipImg = PhotoImage(file = "ship.gif")
    
    player = (s.create_image(300, 700, image = shipImg), 300, 700)
        
#HANDLERS
def leftMouseDown(event):
    global mouse
    
    mouse['left'] = True
    
def leftMouseUp(event):
    global mouse
    
    mouse['left'] = False
    
def rightMouseDown(event):
    global mouse
    
    mouse['right'] = True
    
def rightMouseUp(event):
    global mouse
    
    mouse['right'] = False
    
def mouseMove(event):
    global mouse
    
    mouse['loc'] = (event.x, event.y)
    
def keyDown(event):
    global keys
    
    keys[event.keysym] = True
    
def keyUp(event):
    global keys
    
    keys[event.keysym] = False
    
def windowClose():
    global quitting
    
    quitting = True
        
#UPDATERS
def updateBackground():
    global stars, bgSpeed
    
    for i in range(len(stars)):
        
        star, (x, y, size) = stars[i]
        
        y += bgSpeed
        if y > 800+size:
            x = randint(0, 600)
            size = randint(2, 3)
            y = 0 - size
            
        s.coords(star, x-size, y-size, x+size, y+size)
            
        stars[i] = (star, (x, y, size))
        
    bgSpeed += 0.00027777777777
    
def updatePlayer():
    global player, mouse, keys, lastBullet, lastRocket
    
    xSpeed = 0
    ySpeed = 0
    
    if keys.get('a') == True:
        xSpeed -= 8
    if keys.get('d') == True:
        xSpeed += 8
    if keys.get('w') == True:
        ySpeed -= 8
    if keys.get('s') == True:
        ySpeed += 8
        
    playerO, x, y = player
    
    x += xSpeed
    y += ySpeed
    
    if x - 24 < 0:
        x = 24
    elif x + 24 > 600:
        x = 576
    if y - 50 < 0:
        y = 0
    elif y + 50 > 800:
        y = 750
        
    if mouse['left'] == True:
        
    
    s.coords(playerO, x, y)
    
    player = (playerO, x, y)

#MAIN FUNCTION
def runGame():
    global lives, score, paused
    
    initializeVariables()
    initializeBackground()
    
    #DO MENU STUFF HERE
    
    initializePlayer()
    scoreO = s.create_text(590, 10, text = "Score: " + str(score), font = "Times 15", fill = "white", anchor = NE)
    
    while lives > 0:
        
        startTime = int(str(datetime.now().time())[9:])
        
        updateBackground()
        updatePlayer()
        
        score += 0.3333333333
        s.itemconfig(scoreO, text = "Score: " + str(round(score)))
        
        root.update()
        
        if quitting == True:
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
s.bind("<ButtonRelease-3>", rightMouseDown)
s.bind("<Motion>", mouseMove)
root.bind("<Key>", keyDown)
root.bind("<KeyRelease>", keyUp)
root.protocol("WM_DELETE_WINDOW", windowClose)

root.after(0, runGame)

root.mainloop()