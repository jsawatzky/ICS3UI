'''
Created on Oct 20, 2014

@author: Jacob Sawatzky
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
    global s, WIDTH, HEIGHT, x, y, running, text
    
    running = True
    s.delete(ALL)
    
    maxRadius = 400
    
    for i in range(0, 50):
        
        ripple = s.create_oval(x, y, x, y, fill = None, outline = "blue")
    
        radius = 0
        
        while x-radius > 0 and y-radius > 0 and x+radius < WIDTH and y+radius < HEIGHT and radius <= maxRadius:
            
            s.coords(ripple, x-radius, y-radius, x+radius, y+radius)
            s.update()
            
            radius += 5
            
            pause(0.02)
            
        maxRadius = radius-10
        if maxRadius <= 0:
            break
            
    text = s.create_text(400, 400, text = "Click anywhere on the screen", font = "Times 30")
            
    running = False

def run():
    global s, x, y, text
    
    tk = Tk()
    s = Canvas(tk, width = WIDTH, height = HEIGHT, bg = "Light Blue")
    s.bind("<Button-1>", click)
    text = s.create_text(400, 400, text = "Click anywhere on the screen", font = "Times 30")
    s.pack()
    
    while True:
        
        try:
            s.update()
        except:
            return

if __name__ == "__main__":
    run()