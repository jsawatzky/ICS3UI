'''
Created on Oct 15, 2014

@author: Jacob 
'''

from tkinter import *
from threading import Timer
from math import sqrt

done = False

def doneF():
    global done
    done = True

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
    s.coords(text, -5000, -5000)
    
    radius = 0
    
    while x-radius > 0 and y-radius > 0 and x+radius < WIDTH and y+radius < HEIGHT:
        
        s.coords(ripple, x-radius, y-radius, x+radius, y+radius)
        s.update()
        
        if done == True:
            return
        
        radius += 5
        
        pause(0.02)
        
    s.coords(text, 400, 400)
        
    running = False

def run():
    global s, x, y, text, ripple, done
    
    tk = Tk()
    
    label = Label(tk, text = "Single Ripple", font = "Times 20 bold")
    label.grid(row = 0, sticky = W)
    doneB = Button(tk, text = "Done", command = doneF, width = 10)
    doneB.grid(row = 0, column = 1, sticky = E)
    
    s = Canvas(tk, width = WIDTH, height = HEIGHT, bg = "Light Blue")
    s.bind("<Button-1>", click)
    ripple = s.create_oval(-5000,-5000, -5000, -5000, fill = None, outline = "blue")
    text = s.create_text(400, 400, text = "Click anywhere on the screen", font = "Times 30")
    s.grid(column = 0, columnspan = 2)
    
    while done == False:
        
        try:
            s.update()
        except:
            break
    tk.destroy()

if __name__ == "__main__":
    run(Tk())