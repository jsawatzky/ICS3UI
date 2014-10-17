'''
Created on Oct 15, 2014

@author: Jacob 
'''

from tkinter import *
from threading import Timer

WIDTH = 400
HEIGHT = 800

#Pause
paused = False

def unpause():
    global paused
    paused = False

def pause(s, time):
    global s, paused
    paused = True
    timer = Timer(time, unpause)
    timer.start()
    while paused == True:
        s.update()

def drawRipple(s, x, y):
    
    radius = 0
    
    ripple = None
    
    while x-radius > 0 or y-radius > 0 or x+radius < WIDTH or y+radius < HEIGHT:
        
        s.delete(ripple)
        
        s.create_oval(x-radius, y-radius, x+radius, y+radius, fill = None, outline = "black")
        s.update()
        
        radius += 2
        
        pause(0.05)

def run():
    
    tk = Tk()
    s = Canvas(tk, width = WIDTH, height = HEIGHT, bg = "blue")
    s.pack()
    
    while True:
        
        x = int(input("X: "))
        x = int(input("Y: "))
        
        drawRipple(s, x, y)

if __name__ == "__main__":
    run()