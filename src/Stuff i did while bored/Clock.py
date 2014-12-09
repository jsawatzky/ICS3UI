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
    if int(hour) > 12: hour = str(int(hour)-12)
    elif hour == "0": hour = "12"
    minute = time[3:5]
    second = time[6:8]
    millis = time[9:]
    
    secondAngle = radians(6*int(second))+radians(0.000006*int(millis))
    minuteAngle = radians(6*int(minute))+radians(0.1*int(second))+radians(0.0000001*int(millis))
    hourAngle = radians(30*(int(hour)%12))+radians(0.5*int(minute))+radians(0.0083333333*int(second))+radians(0.0000000083333333*int(millis))
    
    secondX = (340*sin(secondAngle))+400
    secondY = -(340*cos(secondAngle))+400
    minuteX = (340*sin(minuteAngle))+400
    minuteY = -(340*cos(minuteAngle))+400
    hourX = (240*sin(hourAngle))+400
    hourY = -(240*cos(hourAngle))+400
    
    s.itemconfig(text, text = hour + time[2:8])
    
    s.coords(secondHand, 400, 400, secondX, secondY)
    s.coords(minuteHand, 400, 400, minuteX, minuteY)
    s.coords(hourHand, 400, 400, hourX, hourY)
    
    sleep(0.05)
    
    s.update()