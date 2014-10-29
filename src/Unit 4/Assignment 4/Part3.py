'''
Created on Oct 29, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from math import sqrt
from utilities import *

class Sun():
    
    def __init__(self, startY, peak):
        self.k = peak
        self.h = 400
        self.a = sqrt(startY + self.k)/(-self.h)
        self.object = None
        
    def update(self, time):
        self.x = time
        self.y = self.a*((self.x-self.h)**2) + self.k
        
    def draw(self, s):
        if self.object == None:
            self.object = s.create_oval(self.x-75, self.y-75, self.x+75, self.x+75, fill = "yellow", outline = "yellow")
        else:
            s.coords(self.object, self.x-75, self.y-75, self.x+75, self.x+75)

##Functions go here

def run(tk):
    
    s = Canvas(tk, width =  800, height = 800, background = "blue")
    s.grid(row = 0, column = 0)
    
    sun = Sun(300, 100)
    
    time = 0
    while True:
        sun.update(time)
        sun.draw(s)
        s.update()
        time += 1
        pause(0.05, tk)
    
    clearScreen(tk)
        
#Runs the program if not from menu
if __name__ == "__main__":
    run(Tk())