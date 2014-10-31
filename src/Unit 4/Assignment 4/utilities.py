'''
Created on Sep 29, 2014

@author: Jacob
'''

from tkinter import *
from threading import Timer
        
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