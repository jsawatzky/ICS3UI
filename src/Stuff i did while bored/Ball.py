'''
Created on Nov 27, 2014

@author: Jacob
'''
from tkinter import *
from time import sleep
from math import radians, sin, cos

tk = Tk()
s = Canvas(tk, width = 800, height = 800, bg = "white")
s.pack()

startAngle = Scale(s, from_ = 1, to = 89, orient = HORIZONTAL)
startAngleW = s.create_window(400, 200, window = startAngle)
startVelocity = Entry(tk)
startVelocity.insert(0, 0)
startVelocityW = s.create_window(200, 200, window = startVelocity)

def run():
    global s, startAngle, startVelocity, start, startAngleW, startVelocityW, startW
    
    angle = radians(startAngle.get())
    velocity = startVelocity.get()
    try:
        velocity = float(velocity)
    except:
        return
    
    xVelocity = velocity*cos(angle)
    yVelocity = -velocity*sin(angle)
    print(xVelocity, yVelocity)
    
    s.itemconfig(startAngleW, state = HIDDEN)
    s.itemconfig(startVelocityW, state = HIDDEN)
    s.itemconfig(startW, state = HIDDEN)
    
    ball = s.create_oval(0, 780, 20, 800, fill = "black")
    
    t = 1
    x = 10
    
    while x < 810:
        
        x = 10 + t*xVelocity
        y = 750 + yVelocity*t + 0.5*9.81*t**2
        print (x, y, t)
        
        if y > 790:
            t = 0
            
        s.coords(ball, x-10, y-10, x+10, y+10)
        
        s.update()
        sleep(0.05)
        
        t += 1

start = Button(s, text = "Start", command = run)
startW = s.create_window(600, 200, window = start)

while True:
    s.update()
