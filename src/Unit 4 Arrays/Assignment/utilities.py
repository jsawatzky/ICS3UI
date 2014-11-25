'''
Created on Sep 29, 2014

@author: Jacob
'''

from tkinter import *
from threading import Timer
from ctypes.wintypes import RGB
from multiprocessing import Pipe
        
class Boolean():
    
    def __init__(self, state):
        self.state = state
        
    def set(self, newState):
        self.state = newState
        
    def flip(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True
            
    def get(self):
        return self.state
    
def grid(s, spacing):
    for x in range(0, 800, spacing): 
        s.create_line(x, 10, x, 800, fill="magenta")
        s.create_text(x, 0, text=str(x), font="Times 8", anchor = N)
    for y in range(0, 800, spacing):
        s.create_line(20, y, 800, y, fill="magenta")
        s.create_text(0, y, text=str(y), font="Times 8", anchor = W)
        
def pause(time, tk):
    
    paused = Boolean(True)
    Timer(time, lambda: paused.set(False)).start()
    while paused.get() == True:
        tk.update()
        
def clearScreen(tk):
    
    for widget in tk.children.values():
        widget.grid_forget()
        
class QueueItem():
    
    def __init__(self, oper, object = None, *coords, **kw):
        
        self.oper = oper
        self.object = object
        self.pipeSend, self.pipeRecv = Pipe()
        self.coords = coords
        self.kw = kw
        
NUMERALS = '0123456789abcdefABCDEF'
HEXDEC = {v: int(v, 16) for v in (x+y for x in NUMERALS for y in NUMERALS)}

def getRGB(hex):
    
    hex = hex[1:7]
    return HEXDEC[hex[0:2]], HEXDEC[hex[2:4]], HEXDEC[hex[4:6]]

def getHex(rgb):
    
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06x')
        
def getColor(startColor, endColor, startTime, endTime, time):
        
    startRed, startGreen, startBlue = getRGB(startColor)
    endRed, endGreen, endBlue = getRGB(endColor)
        
    red = (startRed * (endTime - time) + endRed * (time - startTime)) / (endTime - startTime)
    green = (startGreen * (endTime - time) + endGreen * (time - startTime)) / (endTime - startTime)
    blue = (startBlue * (endTime - time) + endBlue * (time - startTime)) / (endTime - startTime)
        
    color = "#%02x%02x%02x" % (red, green, blue)
        
    return color
    
def darken(hex, time):
    
    nightColor = getColor(hex, "#000000", 0, 20, 14)
    
    if time in range(0, 76):
        color = getColor(getColor(nightColor, hex, 0, 2, 1), hex, 0, 75, time)
    elif time in range(726, 876):
        color = getColor(hex, nightColor, 726, 875, time)
    elif time in range(876, 1526):
        color = nightColor
    elif time in range(1526, 1601):
        color = getColor(nightColor, getColor(nightColor, hex, 0, 2, 1), 1526, 1600, time)
    else:
        color = hex
    
    return color