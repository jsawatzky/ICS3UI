'''
Created on Nov 27, 2014

@author: Jacob
'''
from tkinter import *
from datetime import datetime
from time import sleep
from math import radians, sin, cos

tk = Tk()
s = Canvas(tk, width = 800, height = 800, bg = "white")
s.pack()

for i in range(1, 13):
    angle = radians(30*i)
    x = (375*sin(angle))+400
    y = -(375*cos(angle))+400
    s.create_text(x, y, text = str(i), font = "Times 15")
     
for i in range(0, 361, 6):
    angle = radians(i)
    x1 = (350*sin(angle))+400
    y1 = (350*cos(angle))+400
    x2 = (355*sin(angle))+400
    y2 = (355*cos(angle))+400
    s.create_line(x1, y1, x2, y2, fill = "black", width = 3)
    
text = s.create_text(400, 600, text = "", font = "Times 25")
    
hourHand = s.create_line(0,0,0,0, fill = "black", width = 6)
minuteHand = s.create_line(0,0,0,0, fill = "black", width = 3)
secondHand = s.create_line(0,0,0,0, fill = "black", width = 1)
    
while True:
    
    time = str(datetime.now().time())
    
    hour = time[:2]
    minute = time[3:5]
    second = time[6:8]
    
    secondAngle = radians(6*float(second))
    minuteAngle = radians(6*float(minute))
    hourAngle = radians(30*(float(hour)%12))+radians(float(minute)/2)
    
    secondX = (340*sin(secondAngle))+400
    secondY = -(340*cos(secondAngle))+400
    minuteX = (340*sin(minuteAngle))+400
    minuteY = -(340*cos(minuteAngle))+400
    hourX = (240*sin(hourAngle))+400
    hourY = -(240*cos(hourAngle))+400
    
    s.itemconfig(text, text = time[:8])
    
    s.coords(secondHand, 400, 400, secondX, secondY)
    s.coords(minuteHand, 400, 400, minuteX, minuteY)
    s.coords(hourHand, 400, 400, hourX, hourY)
    
    sleep(0.05)
    
    s.update()