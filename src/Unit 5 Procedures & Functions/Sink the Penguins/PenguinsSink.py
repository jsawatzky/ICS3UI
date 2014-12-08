from tkinter import *
from time import sleep
from random import randint
from math import sin

def drawSunset():
    
    startRed = 111
    endRed = 255
    startGreen = 193
    endGreen = 91
    startBlue = 213
    endBlue = 15
    
    #Cross fade colors
    for y in range(0, 401, 10):
        
        red = (startRed * (400 - y) + endRed * y) / (400)
        green = (startGreen * (400 - y) + endGreen * y) / 400
        blue = (startBlue * (400 - y) + endBlue * y) / 400
        
        color = "#%02x%02x%02x" % (red, green, blue)
        
        s.create_rectangle(0, y, 800, y+10, fill = color, outline = color)
        
    sun=s.create_oval(200,300,600,500,fill="yellow", outline="yellow")
    
def createPenguins(numPenguins):
    
    penguins = []
    
    for i in range(numPenguins):
        x = randint(150, 650)
        if x <= 400:
            direction = 1
        else: 
            direction = 0
        penguins.append([s.create_image(x, 313, image = penguinImages[direction]), x, direction])
        
    return penguins

def updateBackground(frame, yChange):
    
    s.coords(wave1, 400+frame%800, 400)
    s.coords(wave2, -400+frame%800, 400)
    
    s.coords(iceberg, 100, 350+yChange, 700, 450+yChange)

def hasCollided(penguin1, penguin2):
        
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
    global iceberg, wave1, wave2

    drawSunset()

    #Draw the iceberg
    iceberg = s.create_rectangle(100, 350, 700, 450, fill = "white", outline = "white")
    
    penguins = createPenguins(numPenguins)
    fallingPenguins = []
    toRemove = []
            
    #Draw the waves 
    wave1 = s.create_image(400, 400, image = wave)
    wave2 = s.create_image(-400, 400, image = wave)
    water = s.create_rectangle(0, 400, 800, 800, fill = "#0196D9", outline = "#0196D9")
    
    frame = 0

    while len(penguins) > 0 or len(fallingPenguins) > 0:

        yChange = sin(frame/3)*3
        
        updateBackground(frame, yChange)

        for i in range(len(penguins)):
            
            #Check collisions
            for i2 in range(i, len(penguins)):
                if hasCollided(penguins[i], penguins[i2]) == True:
                    #Reverse directions if collided
                    penguins[i][2] = (penguins[i][2]-1) % 2
                    penguins[i2][2] = (penguins[i2][2]-1) % 2
                    
            #Move the penguins
            if penguins[i][2] == 1:
                penguins[i][1] += 2
            else:
                penguins[i][1] -= 2
                
            #Update the penguins
            s.coords(penguins[i][0], penguins[i][1], 313+yChange)
            s.itemconfig(penguins[i][0], image = penguinImages[penguins[i][2]])
            
            #Check if penguin has fallen off the iceberg and if so move it to the falling penguins array
            if penguins[i][1] < 84 or penguins[i][1] > 716:
                fallingPenguins.append(penguins[i])
                toRemove.append(penguins[i])
                penguins[i].append(313+yChange)

        #Delete penguins from main array that have fallen off iceberg
        for i in toRemove:
            penguins.remove(i)
        toRemove = []

        #Get all penguins in water
        for penguin in fallingPenguins:
            penguin[3] += 5
            s.coords(penguin[0], penguin[1], penguin[3])
            if penguin[3] > 450:
                toRemove.append(penguin)
                
        #Delete penguins in water
        for i in toRemove:
            fallingPenguins.remove(i)
        toRemove = []
        
        s.update()
        sleep(0.05)
        frame += 1

numPenguins = int(input("Please enter the number of penguins you would like: "))

tk = Tk()
s = Canvas(tk, width = 800, height = 800, bg = "black")
s.pack()

#Get wave image file
wave = PhotoImage(file = "wave.gif")

#Get penguin image files
penguinImages = []
penguinImages.append(PhotoImage(file = "penguinLeft.gif"))
penguinImages.append(PhotoImage(file = "penguinRight.gif"))

tk.focus_force()

run(numPenguins)
