from tkinter import *
from time import sleep
from random import randint
from math import sin

tk = Tk()
s = Canvas(tk, width = 800, height = 800, bg = "blue")
s.pack()

wave = PhotoImage(file = "wave.gif")

penguinImages = []
penguinImages.append(PhotoImage(file = "penguinLeft.gif"))
penguinImages.append(PhotoImage(file = "penguinRight.gif"))

def hasHit(penguin1, penguin2):
    
    if penguin1[2] != penguin2[2]:
        if penguin1[1] == penguin2[1]:
            return True
        elif penguin1[1]+16 in range(penguin2[1]-16, penguin2[1]) and penguin1[2] == 1:
            return True
        elif penguin2[1]+16 in range(penguin1[1]-16, penguin1[1]) and penguin2[2] == 1:
            return True
        else:
            return False

def run(numPenguins):
    
    iceberg = s.create_rectangle(100, 350, 700, 450, fill = "white", outline = "white")
    
    penguins = []
    fallingPenguins = []
    toRemove = []
    
    for i in range(numPenguins):
        x = randint(150, 650)
        if x <= 400:
            direction = 1
        else: 
            direction = 0
        penguins.append([s.create_image(x, 313, image = penguinImages[direction]), x, direction])
        
    wave1 = s.create_image(400, 400, image = wave)
    wave2 = s.create_image(-400, 400, image = wave)
    water = s.create_rectangle(0, 400, 800, 800, fill = "#0196D9", outline = "#0196D9")
    
    frame = 0

    while len(penguins) > 0 or len(fallingPenguins) > 0:
        
        s.coords(wave1, 400+frame%800, 400)
        s.coords(wave2, -400+frame%800, 400)
        
        yChange = sin(frame/3)*3
        
        s.coords(iceberg, 100, 350+yChange, 700, 450+yChange)
        
        for i in range(len(penguins)):
            for i2 in range(i, len(penguins)):
                if hasHit(penguins[i], penguins[i2]) == True:
                    penguins[i][2] = (penguins[i][2]-1) % 2
                    penguins[i2][2] = (penguins[i2][2]-1) % 2
                    
            if penguins[i][2] == 1:
                penguins[i][1] += 2
            else:
                penguins[i][1] -= 2
            s.coords(penguins[i][0], penguins[i][1], 313+yChange)
            s.itemconfig(penguins[i][0], image = penguinImages[penguins[i][2]])
            if penguins[i][1] < 84 or penguins[i][1] > 716:
                fallingPenguins.append(penguins[i])
                toRemove.append(penguins[i])
                penguins[i].append(313+yChange)
                
        for i in toRemove:
            penguins.remove(i)
        toRemove = []
        
        for penguin in fallingPenguins:
            penguin[3] += 5
            s.coords(penguin[0], penguin[1], penguin[3])
            if penguin[3] > 450:
                toRemove.append(penguin)
                
        for i in toRemove:
            fallingPenguins.remove(i)
        toRemove = []
        
        s.update()
        sleep(0.05)
        frame += 1
    
run(15)