'''
Created on Oct 15, 2014

@author: Jacob 
'''

from tkinter import *
from threading import Timer
from math import sqrt

WIDTH = 800
HEIGHT = 800

s = None

text = None

x = -1
y = -1

running = False

ripple = None

#Pause
paused = False

def unpause():
    global paused
    paused = False

def pause(time):
    global s, paused
    paused = True
    timer = Timer(time, unpause)
    timer.start()
    while paused == True:
        s.update()
        
def click(event):
    global x, y, running
    if running == False:
        x = event.x
        y = event.y
        drawRipple()

def drawRipple():
    global s, WIDTH, HEIGHT, x, y, running, text, ripple
    
    running = True
    s.delete(text)
    
    radius = 0
    
    lUL = sqrt((x**2)+(y**2))
    lUR = sqrt(((WIDTH-x)**2)+(y**2))
    lLL = sqrt((x**2)+((HEIGHT-y)**2))
    lLR = sqrt(((WIDTH-x)**2)+((HEIGHT-y)**2))
    
    while radius <= lUL or radius <= lUR or radius <= lLL or radius <= lLR:
        
        s.coords(ripple, x-radius, y-radius, x+radius, y+radius)
        s.update()
        
        radius += 4
        
        pause(0.02)
        
    running = False

def run():
    global s, x, y, text, ripple
    
    tk = Tk()
    s = Canvas(tk, width = WIDTH, height = HEIGHT, bg = "Light Blue")
    s.bind("<Button-1>", click)
    ripple = s.create_oval(-5000,-5000, -5000, -5000, fill = None, outline = "blue")
    s.pack()
    
    text = s.create_text(400, 400, text = "Click anywhere on the screen", font = "Times 30")
    
    while True:
        
        try:
            s.update()
        except:
            return

if __name__ == "__main__":
    run()